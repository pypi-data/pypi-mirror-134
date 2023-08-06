import multiprocessing as mp
import tensorflow as tf
import pandas as pd
import numpy as np
import logging
import os

from core.masking import get_masked, set_random, get_padding_mask
from core.utils import standardize
from joblib import Parallel, delayed
from tqdm import tqdm

from time import time
from joblib import wrap_non_picklable_objects

logging.getLogger('tensorflow').setLevel(logging.ERROR)  # suppress warnings

def _bytes_feature(value):
    """Returns a bytes_list from a string / byte."""
    if isinstance(value, type(tf.constant(0))):
        value = value.numpy() # BytesList won't unpack a string from an EagerTensor.
    return tf.train.Feature(bytes_list=tf.train.BytesList(value=[value]))

def _float_feature(list_of_floats):  # float32
    return tf.train.Feature(float_list=tf.train.FloatList(value=list_of_floats))

def _int64_feature(value):
    return tf.train.Feature(int64_list=tf.train.Int64List(value=[value]))

def get_example(lcid, label, lightcurve):
    """
    Create a record example from numpy values.

    Args:
        lcid (string): object id
        label (int): class code
        lightcurve (numpy array): time, magnitudes and observational error

    Returns:
        tensorflow record
    """

    f = dict()

    dict_features={
    'id': tf.train.Feature(bytes_list=tf.train.BytesList(value=[str(lcid).encode()])),
    'label': tf.train.Feature(int64_list=tf.train.Int64List(value=[label])),
    'length': tf.train.Feature(int64_list=tf.train.Int64List(value=[lightcurve.shape[0]])),
    }
    element_context = tf.train.Features(feature = dict_features)

    dict_sequence = {}
    for col in range(lightcurve.shape[1]):
        seqfeat = _float_feature(lightcurve[:, col])
        seqfeat = tf.train.FeatureList(feature = [seqfeat])
        dict_sequence['dim_{}'.format(col)] = seqfeat

    element_lists = tf.train.FeatureLists(feature_list=dict_sequence)
    ex = tf.train.SequenceExample(context = element_context,
                                  feature_lists= element_lists)
    return ex

def divide_training_subset(frame, train, val):
    """
    Divide the dataset into train, validation and test subsets.
    Notice that:
        test = 1 - (train + val)

    Args:
        frame (Dataframe): Dataframe following the astro-standard format
        dest (string): Record destination.
        train (float): train fraction
        val (float): validation fraction
    Returns:
        tuple x3 : (name of subset, subframe with metadata)
    """

    frame = frame.sample(frac=1)
    n_samples = frame.shape[0]
    n_train = int(n_samples*train)
    n_val = int(n_samples*val//2)

    sub_train = frame.iloc[:n_train]
    sub_val   = frame.iloc[n_train:n_train+n_val]
    sub_test  = frame.iloc[n_train+n_val:]

    return ('train', sub_train), ('val', sub_val), ('test', sub_test)

def process_lc(row, source, unique_classes, writer):
    """
    Filter a sample according to our astronomical criteria and write
    example in the corresponding record.

    Args:
        row (Pandas serie): Dataframe row containing information about
                            a particular sample
        source (string):  Lightcurves folder path
        unique_classes (list): list with unique classes
        writer (tf.writer) : record writer

    """

    path  = row['Path'].split('/')[-1]
    label = list(unique_classes).index(row['Class'])
    lc_path = os.path.join(source, path)
    try:
        observations = pd.read_csv(lc_path)

        observations.columns = ['mjd', 'mag', 'errmag']
        observations = observations.dropna()
        observations.sort_values('mjd')
        observations = observations.drop_duplicates(keep='last')
        numpy_lc = observations.values
        ex = get_example(row['ID'], label, numpy_lc)
        writer.write(ex.SerializeToString())
    except:
        print('[ERROR] {} Lightcurve could not be processed.'.format(row['ID']))

@wrap_non_picklable_objects
def process_lc2(row, source, unique_classes, max_obs):
    path  = row['Path'].split('/')[-1]
    label = list(unique_classes).index(row['Class'])
    lc_path = os.path.join(source, path)
    
    observations = pd.read_csv(lc_path, delim_whitespace=True, names=['mjd', 'mag', 'std'])
    
    observations.columns = ['mjd', 'mag', 'errmag']
    observations = observations.dropna()
    observations.sort_values('mjd')
    observations = observations.drop_duplicates(keep='last')

    if max_obs != -1:
        length = observations.shape[0]
        rest = length%max_obs
        filler = max_obs - rest
        observations = observations.reindex(range(length+filler), fill_value=0)
    
    
    numpy_lc = observations.values

    return row['ID'], label, numpy_lc

def process_lc3(lc_index, label, numpy_lc, writer):
    try:
        ex = get_example(lc_index, label, numpy_lc)
        writer.write(ex.SerializeToString())
    except:
        print('[INFO] {} could not be processed'.format(lc_index))

def write_records(frame, dest, max_lcs_per_record, source, unique, n_jobs=None, max_obs=200):
    # Get frames with fixed number of lightcurves
    collection = [frame.iloc[i:i+max_lcs_per_record] \
                  for i in range(0, frame.shape[0], max_lcs_per_record)]

#     if 'test' in dest:
#         max_obs = 200 # For testing we split the entire lc in windows of 200 obs
        
    # Iterate over subset
    # First process and then serialize
    for counter, subframe in enumerate(collection):
        var = Parallel(n_jobs=n_jobs)(delayed(process_lc2)(row, source, unique, max_obs) \
                                    for k, row in subframe.iterrows())

        with tf.io.TFRecordWriter(dest+'/chunk_{}.record'.format(counter)) as writer:
            for counter2, data_lc in enumerate(var):
#                 if 'test' in dest:
                oid, y, x = data_lc
                windows = np.split(x, x.shape[0]/max_obs)
                for w in windows:
                    if np.sum(w) != 0:
                        process_lc3(oid, y, w, writer)
#                 else:
#                     process_lc3(*data_lc, writer)



def create_dataset(meta_df,
                   source='data/raw_data/macho/MACHO/LCs',
                   target='data/records/macho/',
                   n_jobs=None,
                   subsets_frac=(0.5, 0.25),
                   max_lcs_per_record=100):
    os.makedirs(target, exist_ok=True)

    bands = meta_df['Band'].unique()
    if len(bands) > 1:
        b = input('Filters {} were found. Type one to continue'.format(' and'.join(bands)))
        meta_df = meta_df[meta_df['Band'] == b]

    unique, counts = np.unique(meta_df['Class'], return_counts=True)
    info_df = pd.DataFrame()
    info_df['label'] = unique
    info_df['size'] = counts
    info_df.to_csv(os.path.join(target, 'objects.csv'), index=False)

    # Separate by class
    cls_groups = meta_df.groupby('Class')

    for cls_name, cls_meta in tqdm(cls_groups, total=len(cls_groups)):
        subsets = divide_training_subset(cls_meta,
                                         train=subsets_frac[0],
                                         val=subsets_frac[0])

        for subset_name, frame in subsets:
            dest = os.path.join(target, subset_name, cls_name)
            os.makedirs(dest, exist_ok=True)
            write_records(frame, dest, max_lcs_per_record, source, unique, n_jobs)

def get_sample(sample):
    """
    Read a serialized sample and convert it to tensor
    Context and sequence features should match with the name used when writing.
    Args:
        sample (binary): serialized sample

    Returns:
        type: decoded sample
    """
    context_features = {'label': tf.io.FixedLenFeature([],dtype=tf.int64),
                        'length': tf.io.FixedLenFeature([],dtype=tf.int64),
                        'id': tf.io.FixedLenFeature([], dtype=tf.string)}
    sequence_features = dict()
    for i in range(3):
        sequence_features['dim_{}'.format(i)] = tf.io.VarLenFeature(dtype=tf.float32)

    context, sequence = tf.io.parse_single_sequence_example(
                            serialized=sample,
                            context_features=context_features,
                            sequence_features=sequence_features
                            )

    input_dict = dict()
    input_dict['lcid']   = tf.cast(context['id'], tf.string)
    input_dict['length'] = tf.cast(context['length'], tf.int32)
    input_dict['label']  = tf.cast(context['label'], tf.int32)

    casted_inp_parameters = []
    for i in range(3):
        seq_dim = sequence['dim_{}'.format(i)]
        seq_dim = tf.sparse.to_dense(seq_dim)
        seq_dim = tf.cast(seq_dim, tf.float32)
        casted_inp_parameters.append(seq_dim)


    sequence = tf.stack(casted_inp_parameters, axis=2)[0]
    input_dict['input'] = sequence
    return input_dict

def sample_lc(sequence, max_obs):
    '''
    Sample a random window of "max_obs" observations from the input sequence
    '''
    serie_len = tf.shape(sequence)[0]
    curr_max_obs = tf.minimum(serie_len, max_obs)
    
    pivot = 0
    if tf.greater(serie_len, max_obs):
        pivot = tf.random.uniform([],
                                  minval=0,
                                  maxval=serie_len-curr_max_obs,
                                  dtype=tf.int32)

        sequence = tf.slice(sequence, [pivot,0], [curr_max_obs, -1])
    else:
        sequence = tf.slice(sequence, [0,0], [curr_max_obs, -1])

    return sequence

def _parse_pt(sample, msk_prob, rnd_prob, same_prob, max_obs):
    '''
    Pretraining formater
    '''

    input_dict = get_sample(sample)
    input_dict_v2 = {}
    sequence = sample_lc(input_dict['input'], max_obs)
    
    pad_mask = tf.reduce_sum(sequence, 1)
    pad_mask = tf.math.divide_no_nan(pad_mask, pad_mask)
    curr_max_obs = tf.reduce_sum(pad_mask, 0)
    pad_mask = tf.expand_dims(pad_mask, 1)
    
    sequence, mean = standardize(sequence, return_mean=True)

    seq_time = tf.slice(sequence, [0, 0], [max_obs, 1])
    seq_magn = tf.slice(sequence, [0, 1], [max_obs, 1])
    seq_errs = tf.slice(sequence, [0, 2], [max_obs, 1])


    # Save the true values
    orig_magn = seq_magn

    # [MASK] values
    mask_out = get_masked(seq_magn, msk_prob)

    # [MASK] -> Same values
    seq_magn, mask_in = set_random(seq_magn,
                                   mask_out,
                                   seq_magn,
                                   same_prob,
                                   name='set_same')

    # [MASK] -> Random value
    seq_magn, mask_in = set_random(seq_magn,
                                   mask_in,
                                   tf.random.shuffle(seq_magn),
                                   rnd_prob,
                                   name='set_random')

    time_steps = tf.shape(seq_magn)[0]

    mask_out = tf.reshape(mask_out, [max_obs, 1])
    mask_out = tf.multiply(mask_out, pad_mask)
    
    mask_in = tf.reshape(mask_in, [max_obs, 1])
    mask_in = tf.maximum(1.-pad_mask, mask_in)

#     if curr_max_obs < max_obs:
#         print('Masking')
#         filler    = tf.ones([max_obs-curr_max_obs, 1])
#         mask_in   = tf.concat([mask_in, filler], 0)
#         seq_magn  = tf.concat([seq_magn, 1.-filler], 0)
#         seq_time  = tf.concat([seq_time, 1.-filler], 0)
#         mask_out  = tf.concat([mask_out, 1.-filler], 0)
#         orig_magn = tf.concat([orig_magn, 1.-filler], 0)

    input_dict['output']   = orig_magn
    input_dict['input']    = seq_magn
    input_dict['times']    = seq_time
    input_dict['mask_out'] = mask_out
    input_dict['mask_in']  = mask_in
    input_dict['length']   = curr_max_obs
    input_dict['mean']     = mean
    input_dict['obserr']   = seq_errs

    return input_dict

def _parse_normal(sample, max_obs):
    '''
    Specific task formater
    '''
    input_dict = get_sample(sample)
       
    sequence = sample_lc(input_dict['input'], max_obs)
    
    mask = tf.reduce_sum(sequence, 1)
    curr_max_obs = tf.reduce_sum(mask, 0)
    mask = 1.-tf.math.divide_no_nan(mask, mask)
    
    sequence = standardize(sequence)
    seq_time = tf.slice(sequence, [0, 0], [max_obs, 1])
    seq_magn = tf.slice(sequence, [0, 1], [max_obs, 1])
    seq_errs = tf.slice(sequence, [0, 2], [max_obs, 1])

    mask = tf.reshape(mask, [max_obs, 1])

    input_dict['input']    = seq_magn
    input_dict['times']    = seq_time
    input_dict['obserr']   = seq_errs
    input_dict['mask_in']  = mask
    input_dict['length']   = curr_max_obs

    return input_dict

def adjust_fn(func, msk_prob, rnd_prob, same_prob, max_obs):
    def wrap(*args, **kwargs):
        result = func(*args, msk_prob, rnd_prob, same_prob, max_obs)
        return result
    return wrap

def pretraining_records(source, batch_size, shuffle=False, max_obs=100,
                        msk_frac=0.2, rnd_frac=0.1, same_frac=0.1):
    """
    Pretraining data loader.
    This method build the ASTROMER input format.
    ASTROMER format is based on the BERT masking strategy.

    Args:
        source (string): Record folder
        batch_size (int): Batch size
        no_shuffle (bool): Do not shuffle training and validation dataset
        max_obs (int): Max. number of observation per serie
        msk_frac (float): fraction of values to be predicted ([MASK])
        rnd_frac (float): fraction of [MASKED] values to replace with random values
        same_frac (float): fraction of [MASKED] values to replace with true values

    Returns:
        Tensorflow Dataset: Iterator withg preprocessed batches
    """
    fn = adjust_fn(_parse_pt, msk_frac, rnd_frac, same_frac, max_obs)

    rec_paths = [os.path.join(source, folder, x) for folder in os.listdir(source) \
                 for x in os.listdir(os.path.join(source, folder))]

    dataset = tf.data.TFRecordDataset(rec_paths)
    if shuffle:
        print('[INFO] Shuffling')
        dataset = dataset.shuffle(10000)

    dataset = dataset.map(fn)
    dataset = dataset.cache()
    dataset = dataset.padded_batch(batch_size)
    dataset = dataset.prefetch(buffer_size=tf.data.AUTOTUNE)
    return dataset

def adjust_fn_clf(func, max_obs):
    def wrap(*args, **kwargs):
        result = func(*args, max_obs)
        return result
    return wrap

def clf_records(source, batch_size, max_obs=100, take=1):
    """
    Classification data loader.
    It creates ASTROMER-like input but without masking

    Args:
        source (string): Record folder
        batch_size (int): Batch size
        max_obs (int): Max. number of observation per serie
        take (int):  Number of batches.
                     If 'take' is -1 then it returns the whole dataset without
                     shuffle and oversampling (i.e., testing case)
    Returns:
        Tensorflow Dataset: Iterator withg preprocessed batches
    """

    fn = adjust_fn_clf(_parse_normal, max_obs)
    rec_paths = [os.path.join(source, folder, x) for folder in os.listdir(source) \
                 for x in os.listdir(os.path.join(source, folder))]

    if take < 0:
        print('[INFO] No shuffle No Oversampling'.format(take))
        dataset = tf.data.TFRecordDataset(rec_paths)
        dataset = dataset.map(fn).cache()
        dataset = dataset.batch(batch_size)
        dataset = dataset.prefetch(buffer_size=tf.data.AUTOTUNE)
        return dataset
    else:
        print('[INFO] Taking {} balanced batches'.format(take))
        datasets = [tf.data.TFRecordDataset(x) for x in rec_paths]
        datasets = [dataset.repeat() for dataset in datasets]
        dataset = tf.data.experimental.sample_from_datasets(datasets)
        dataset = dataset.map(fn)
        dataset = dataset.batch(batch_size)
        dataset = dataset.take(take)
        # dataset = dataset.cache()
        dataset = dataset.prefetch(buffer_size=tf.data.experimental.AUTOTUNE)
        return dataset

# SINUSOIDAL DATA
def count(stop):
    input_dict = dict()
    while True:
        seq_times = tf.reshape(tf.linspace(0., 20., stop), [stop, 1])
        seq_times = tf.cast(seq_times, tf.float32)
        seq_magn  = tf.math.sin(seq_times)
        seq_magn = tf.cast(seq_magn, tf.float32)
        seq_err   = tf.random.normal([stop, 1], mean=0, stddev=1)
        seq_err = tf.cast(seq_err, tf.float32)

        # Save the true values
        orig_magn = seq_magn

        # [MASK] values
        mask_out = get_masked(seq_magn, 0.5)

        # [MASK] -> Same values
        seq_magn, mask_in = set_random(seq_magn,
                                       mask_out,
                                       seq_magn,
                                       0.2,
                                       name='set_same')

        # [MASK] -> Random value
        seq_magn, mask_in = set_random(seq_magn,
                                       mask_in,
                                       tf.random.shuffle(seq_magn),
                                       0.2,
                                       name='set_random')

        time_steps = tf.shape(seq_magn)[0]

        mask_out = tf.reshape(mask_out, [time_steps, 1])
        mask_in = tf.reshape(mask_in, [time_steps, 1])

        input_dict['input']    = seq_magn
        input_dict['output']   = orig_magn
        input_dict['times']    = seq_times
        input_dict['obserr']   = tf.zeros_like(seq_magn)
        input_dict['mask_in']  = mask_in
        input_dict['mask_out'] = mask_out
        input_dict['length']   = time_steps

        yield input_dict



def from_generator(len, n, batch_size):

    ds_counter = tf.data.Dataset.from_generator(count,
                                                args=[len],
                                                output_types={'input': tf.float32,
                                                              'output': tf.float32,
                                                              'times': tf.float32,
                                                              'obserr': tf.float32,
                                                              'mask_in': tf.float32,
                                                              'mask_out': tf.float32,
                                                              'length': tf.int32
                                                              },
                                                output_shapes ={'input': (len, 1),
                                                                'output': (len, 1),
                                                                'times': (len, 1),
                                                                'obserr': (len, 1),
                                                                'mask_in': (len, 1),
                                                                'mask_out': (len, 1),
                                                                'length': ()
                                                                })



    ds_counter = ds_counter.take(n).cache()
    ds_counter = ds_counter.batch(batch_size)
    return ds_counter



def _parse_pt_v2(sample, msk_prob, rnd_prob, same_prob, max_obs):
    '''
    Pretraining formater
    '''

    input_dict = get_sample(sample)
    input_dict_v2 = {}
    sequence = sample_lc(input_dict['input'], max_obs)
    
    pad_mask = tf.reduce_sum(sequence, 1)
    pad_mask = tf.math.divide_no_nan(pad_mask, pad_mask)
    curr_max_obs = tf.reduce_sum(pad_mask, 0)
    pad_mask = tf.expand_dims(pad_mask, 1)
    
    sequence, mean = standardize(sequence, return_mean=True)

    seq_time = tf.slice(sequence, [0, 0], [max_obs, 1])
    seq_magn = tf.slice(sequence, [0, 1], [max_obs, 1])
    seq_errs = tf.slice(sequence, [0, 2], [max_obs, 1])


    # Save the true values
    orig_magn = seq_magn

    # [MASK] values
    mask_out = get_masked(seq_magn, msk_prob)

    # [MASK] -> Same values
    seq_magn, mask_in = set_random(seq_magn,
                                   mask_out,
                                   seq_magn,
                                   same_prob,
                                   name='set_same')

    # [MASK] -> Random value
    seq_magn, mask_in = set_random(seq_magn,
                                   mask_in,
                                   tf.random.shuffle(seq_magn),
                                   rnd_prob,
                                   name='set_random')

    time_steps = tf.shape(seq_magn)[0]

    mask_out = tf.reshape(mask_out, [max_obs, 1])
    mask_out = tf.multiply(mask_out, pad_mask)
    
    mask_in = tf.reshape(mask_in, [max_obs, 1])
    mask_in = tf.maximum(1.-pad_mask, mask_in)



    # output_dict['output']   = orig_magn
    input_dict_v2['input']    = seq_magn
    input_dict_v2['times']    = seq_time
    # input_dict['mask_out'] = mask_out
    input_dict_v2['mask_in']  = mask_in
    # input_dict['length']   = curr_max_obs
    # input_dict['mean']     = mean
    # input_dict['obserr']   = seq_errs

    return input_dict_v2, input_dict['label']


def pretraining_records_v2(source, batch_size, shuffle=False, max_obs=100,
                        msk_frac=0.2, rnd_frac=0.1, same_frac=0.1):
    """
    Pretraining data loader.
    This method build the ASTROMER input format.
    ASTROMER format is based on the BERT masking strategy.

    Args:
        source (string): Record folder
        batch_size (int): Batch size
        no_shuffle (bool): Do not shuffle training and validation dataset
        max_obs (int): Max. number of observation per serie
        msk_frac (float): fraction of values to be predicted ([MASK])
        rnd_frac (float): fraction of [MASKED] values to replace with random values
        same_frac (float): fraction of [MASKED] values to replace with true values

    Returns:
        Tensorflow Dataset: Iterator withg preprocessed batches
    """
    fn = adjust_fn(_parse_pt_v2, msk_frac, rnd_frac, same_frac, max_obs)

    rec_paths = [os.path.join(source, folder, x) for folder in os.listdir(source) \
                 for x in os.listdir(os.path.join(source, folder))]

    dataset = tf.data.TFRecordDataset(rec_paths)
    if shuffle:
        print('[INFO] Shuffling')
        dataset = dataset.shuffle(10000)

    dataset = dataset.map(fn)
    dataset = dataset.cache()
    dataset = dataset.padded_batch(batch_size)
    dataset = dataset.prefetch(buffer_size=tf.data.AUTOTUNE)
    return dataset


def _parse_pt_numpy(sample, msk_prob, rnd_prob, same_prob, max_obs):
    '''
    Pretraining formater
    '''

    input_dict = {}
    sequence = sample_lc(sample, max_obs)
    
    pad_mask = tf.reduce_sum(sequence, 1)
    pad_mask = tf.math.divide_no_nan(pad_mask, pad_mask)
    curr_max_obs = tf.reduce_sum(pad_mask, 0)
    pad_mask = tf.expand_dims(pad_mask, 1)
    pad_mask = tf.cast(pad_mask, tf.float32)

    sequence, mean = standardize(sequence, return_mean=True)

    seq_time = tf.slice(sequence, [0, 0], [max_obs, 1])
    seq_time = tf.cast(seq_time, tf.float32)
    seq_magn = tf.slice(sequence, [0, 1], [max_obs, 1])
    seq_magn = tf.cast(seq_magn, tf.float32)
    seq_errs = tf.slice(sequence, [0, 2], [max_obs, 1])
    seq_errs = tf.cast(seq_errs, tf.float32)



    # # Save the true values
    orig_magn = seq_magn

    # [MASK] values
    mask_out = get_masked(seq_magn, msk_prob)

    # [MASK] -> Same values
    seq_magn, mask_in = set_random(seq_magn,
                                   mask_out,
                                   seq_magn,
                                   same_prob,
                                   name='set_same')

    # [MASK] -> Random value
    seq_magn, mask_in = set_random(seq_magn,
                                   mask_in,
                                   tf.random.shuffle(seq_magn),
                                   rnd_prob,
                                   name='set_random')

    # time_steps = tf.shape(seq_magn)[0]

    mask_out = tf.reshape(mask_out, [max_obs, 1])
    mask_out = tf.multiply(mask_out, pad_mask)
    
    mask_in = tf.reshape(mask_in, [max_obs, 1])
    mask_in = tf.maximum(1.-pad_mask, mask_in)

    #     if curr_max_obs < max_obs:
    #         print('Masking')
    #         filler    = tf.ones([max_obs-curr_max_obs, 1])
    #         mask_in   = tf.concat([mask_in, filler], 0)
    #         seq_magn  = tf.concat([seq_magn, 1.-filler], 0)
    #         seq_time  = tf.concat([seq_time, 1.-filler], 0)
    #         mask_out  = tf.concat([mask_out, 1.-filler], 0)
    #         orig_magn = tf.concat([orig_magn, 1.-filler], 0)

    input_dict['output']   = orig_magn
    input_dict['input']    = seq_magn
    input_dict['times']    = seq_time
    input_dict['mask_out'] = mask_out
    input_dict['mask_in']  = mask_in
    input_dict['length']   = curr_max_obs
    # input_dict['mean']     = mean
    # input_dict['obserr']   = seq_errs

    return input_dict
def pretraining_numpy(arr, batch_size, shuffle=False, max_obs=100,
                        msk_frac=0.2, rnd_frac=0.1, same_frac=0.1):
    """
    Pretraining data loader.
    This method build the ASTROMER input format.
    ASTROMER format is based on the BERT masking strategy.

    Args:
        source (string): Record folder
        batch_size (int): Batch size
        no_shuffle (bool): Do not shuffle training and validation dataset
        max_obs (int): Max. number of observation per serie
        msk_frac (float): fraction of values to be predicted ([MASK])
        rnd_frac (float): fraction of [MASKED] values to replace with random values
        same_frac (float): fraction of [MASKED] values to replace with true values

    Returns:
        Tensorflow Dataset: Iterator withg preprocessed batches
    """

    max_len_arr = max(list(map(lambda x:x.shape[0], arr)))
    padded_lcs = list(map(lambda x:np.pad(x, ((0,max_len_arr-x.shape[0]), (0,0))), arr))
    padded_lcs = np.array(padded_lcs)

    fn = adjust_fn(_parse_pt_numpy, msk_frac, rnd_frac, same_frac, max_obs)



    dataset = tf.data.Dataset.from_tensor_slices(padded_lcs)
    if shuffle:
        print('[INFO] Shuffling')
        dataset = dataset.shuffle(1000)

    dataset = dataset.map(fn)
    dataset = dataset.cache()
    dataset = dataset.padded_batch(batch_size)
    dataset = dataset.prefetch(buffer_size=tf.data.AUTOTUNE)
    return dataset


def pretraining_data(data, batch_size, shuffle=False, max_obs=100,
                        msk_frac=0.2, rnd_frac=0.1, same_frac=0.1, mode=None):
    modes = [None, "clf"]
    if mode not in modes:
        raise ValueError(f"Mode {mode} is not defined. Please select among {modes}")
    
    if isinstance(data, list):
        data =  pretraining_numpy(data, batch_size, shuffle=shuffle, max_obs=max_obs,
                        msk_frac=msk_frac, rnd_frac=rnd_frac, same_frac=same_frac)
        return data

    elif isinstance(data, str):
        if mode=="clf":
            data =  pretraining_records_v2(data, batch_size, shuffle=shuffle, max_obs=max_obs,
                            msk_frac=msk_frac, rnd_frac=rnd_frac, same_frac=same_frac)
        else:
            data =  pretraining_records(data, batch_size, shuffle=shuffle, max_obs=max_obs,
                            msk_frac=msk_frac, rnd_frac=rnd_frac, same_frac=same_frac)
        return data
    else:
        raise TypeError("pretraining_data only accepts either a list of numpy arrays containing lightcurves or a path to the record file(str)")