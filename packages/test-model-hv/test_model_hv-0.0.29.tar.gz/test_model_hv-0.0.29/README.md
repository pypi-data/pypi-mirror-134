<<<<<<< HEAD
# Astromer
---
## Building light curve embeddings using transformers




Astromer is a deep learning model trained on millions of stars, it is inspired by the encoder based architecture of transformers similar to BERT for NLP.

- The input to the model is the light curve seen earlier and the goal is to learn the embedding associated to each timestamp and magnitude. 
- The embeddings can then be used to perform various tasks such as classification of variable stars into different classes, next sequence prediction etc.
---
## Features

- Through our experiments we see that the self attention based models for classification using MLP and LSTM considerably outperform simple LSTM based classifiers. 

---
## Tech

Astromer uses a number of open source projects to work properly:

- [Tensorflow] - Deeplearning Framework 
- [Dask] - Preprocessing medium size dataset
- 

And of course Astromer itself is open source with a [public repository][test-model-hv]
 on GitHub.
---
## Installation


```sh
pip install test-model-hv
```

For production environments...

```sh
tbd
```
---
## Docker

Astromer is very easy to install and deploy in a Docker container.


By default, the Docker will expose port 8080, so change this within the
Dockerfile if necessary. When ready, simply use the Dockerfile to
build the image.

To build the container use: 
```sh
docker-compose build
```
To start the container in detached mode (-d):
```sh
docker-compose up -d
```
Check that the container is already runing by typing:
```sh
docker container ls
```
---
## Documentation 

#### Model Module 

The encoder model is a class  -

```sh
from core.astromer import ASTROMER
model = ASTOMER(num_layers=2,
                 d_model=200,
                 num_heads=2,
                 dff=256,
                 base=10000,
                 dropout=0.1,
                 use_leak=False,
                 no_train=True,
                 maxlen=100,
                 batch_size=None,
                 pretrained_weights=False,
                 finetuning = None,
                 overwrite=False)
```
- **num_layers : int, default=2** : number of layers in the encoder 
- **d_model : int, default=200** : max length of input sequence*
- **num_heads : int, default=2** : number of heads in encoder
- **dff : int, default=256** : Lenght of input embeddings
- **base :int, default=10000** : Positional encoding* 
- **dropout :float, default=0.1** : Dropout in encoder 
- **use_leak :bool, default=False** : 
- **no_train : bool, default=True** : 
- **maxlen : int, default=100** : max length of input sequence*
- **batch_size : int, default = None** : Train and validation batch size 
- **finetuning : str, default=None** : 'ogle' / 'alcock' (astromer finetuned on smalller datasets)
- **pretrained_weights : bool=False** : loads model with random weights, True : loads model with pretrained weights on large dataset currently MACHO)
- **overwrite : bool, default=False** - Overwrite previous weights of the encoder



###### To call the model as a keras model use the get_model method function as follows. 

```sh
model = ASTOMER(pretrained_weights=True, finetuning = 'ogle').get_model()
```

###### To load configuration of the encoder model use the load_configuration method. 
Loads meta data for encoder astromer model.  
```sh
model = ASTOMER(pretrained_weights=False, finetuning = None).load_configuration()
```
###### To train the model use the train method as follows 
The train and validation data batches need to be created first using the pretrained_dataset function from the core.data module first. Once the data is available in batches in tf.record format or numpy format the data can be passed into the train method. 
```sh
model = ASTOMER(pretrained_weights=True, finetuning = 'ogle').train(train_dataset, validation_dataset, patience=20,exp_path='./experiments/test', epochs =1, finetuning =False, use_random=True, num_cls=2. lr=1e-3, verbose=1)
```
- **train_dataset : {array-like, sparse matrix} of shape (n_samples, n_features)** : Training Data, contains labels if num_classes  != -1
- **validation_dataset : {array-like, sparse matrix} of shape (n_samples, n_features)** : validation Data, contains labels if num_classes  != -1
- **patience : int, default=20** : Number of epochs for early stopping 
- **exp_path : str, default= './experiments/test'** : Path to store model weights 
- **epochs : int, defualt=1** : Number of epochs to train the model for 
- **finetuning : bool, default= False** : Finetune encoder weights if True, else encoder weights are frozen 
- **use_random : bool, default= False** :
- **num_classes : int, defualt=-1** : If labels not available, set num_classes to -1, if labels available in train and validation batches set num_classes to int value of number of labels 
- **lr : float, defualt=1e-3** : learning rate
- **verbose : int, defualt=1** : If verbose 1, see training, verbose 0, dont see training log and losses

```sh
model = ASTOMER(pretrained_weights=False, finetuning = None).predict(dataset, predict_proba=False)
```
- **dataset : {array-like, sparse matrix} of shape (n_samples, n_features)** : Data to predict on
- **predict_proba : bool, default= False** : If false, returns class labels, if True returns probability of class labels.

---
#### Data Module 
###### Create record example from numpy values 
```sh
example = get_example(lcid, label, lightcurve)
```
- **lcid : str, defualt=None** : object id
- **label : int, defualt=None** : class code
- **lightcurve : numpy array** : time, magnitudes and observational error
- **returns** : example in record format

###### Create train, validation and test tuples from dataset
```sh
train, val, test = divide_training_subset(frame, train, val)
```

- **frame : dataframe** : Dataframe following the astro standard format
- **train : float** : train fraction
- **val : float** : validation fraction
- **Returns:** : tuple x3 : (name of subset, subframe with metadata)
- **Notice** that test = 1-(train + val)

###### Create tensorflow records for available dataset from source and store at target destination, uses meta data to parse through the data. 
```sh
dataset = create_dataset(meta_df,
                        source='data/raw_data/macho/MACHO/LCs',
                        target='data/records/macho/',
                        n_jobs=None,
                        subsets_frac=(0.5, 0.25),
                        max_lcs_per_record=100)
```
- **meta_df : dataframe** : contains table which has details about the data 
- **source : str** : path to data source directory 
- **target : str** : path to target directory 
- **n_jobs : int** : multiprocessing *
- **subset_frac : (float, float)** : *
- **max_lcs_per_record : int ** : number of lightcurves per shard of record. 

###### Pretraning data loader, this method build the ASTROMER input format. ASTROMER format is based on the bert masking strategy.
```sh
dataset = pretraining_dataset(source,
                                batch_size,
                                shuffle=False,
                                max_obs=100,
                                msk_frac=0.2, 
                                rnd_frac=0.1, 
                                same_frac=0.1,
                                n_classes = -1)
```
 
- **source (string)** : Record folder
- **batch_size (int)** : Batch size
- **no_shuffle (bool)** : Do not shuffle training and validation dataset
- **max_obs (int)** : Max. number of observation per serie
- **msk_frac (float)** : fraction of values to be predicted ([MASK])
- **rnd_frac (float)**: fraction of [MASKED] values to replace with random values
- **same_frac (float)**: fraction of [MASKED] values to replace with true values
- **n_classes (int)** : if -1, data does not contain labels. else number should be equal to number of classes in dataset. 
Returns :
- **Tensorflow Dataset** : Iterator with preprocessed batches

---
## License

MIT

**Free Software, Hell Yeah!**
=======
# Astromer 
ASTROMER is a deep learning model trained on million of stars. It is inspired by NLP architecture BERT which combine different tasks to create a useful representation of the input. This representation corresponds to the **attention vector** which we can then use to train another models.

### Creating Data Pipelines 

1. Getting record example from numpy dataset. 


from core.data import get_example
example = get_example(lcid = 'object id', label = (int)Class code, lightcurve = array)

returns tensorflow record for that observation. 


>>>>>>> 79acdcd4a9a66a08dd94eedda82c4eb882ead343
