# Machine Learning using `scikit-learn`

## NGCM Summer Academy 2017



## Instructors

Christopher Fonnesbeck (Vanderbilt University Medical Center)  
Skipper Seabold (Civis Analytics)

## Outline

### Thursday, June 29

**09:30 - 10:45** (Chris Fonnesbeck)

*Introduction to machine learning with scikit-learn*

- Data preparation
- Preprocessing


**11:00 - 13:15** (Chris Fonnesbeck)

*Unsupervised learning*

- PCA and transformations
- Clustering


**13:15 - 14:15 Lunch**

**14:15 - 16:00**

*Supervised Learning* (Skipper Seabold)

- Support vector machines
- Decision trees
- Random forests

**16:15 - 17:30** 

*Model selection* (Skipper Seabold)

- Cross-validation
- Model evaluation and performance metrics


### Friday, June 30

**09:30 - 10:45**

*Supervised Learning* (Chris Fonnesbeck)

- Linear regression
- Logistic regression
- Non-linear regression

**11:00 - 13:15** (Chris Fonnesbeck)

*Ensemble Supervised Learning*

- Boosting
- Regression trees

**13:15 - 14:15 Lunch**

**14:15 - 16:00** (Skipper Seabold)

*Advanced topics*

- Pipelining
- Feature selection


**16:15 - 17:30** (Skipper Seabold)

*Advanced topics*

- Text feature extraction
- Parallelism with Dask


## Prerequisites

This is an intermediate-level computing course, so some previous experience with Python is required. Some undergraduate-level statistics is also recommended.

## Software Requirements

Python 3.5 or 3.6. We recommend installing the free Anaconda distribution of Python, available from Continuum Analytics.

The following packages should be installed on your system:

- jupyter
- ipython>=4.0
- numpy>=1.10
- pandas>=0.18
- scipy
- matplotlib
- scikit-learn
- dask

If you have installed Anaconda, most of these may already be available to you.

## Getting this repository

    git clone https://github.com/fonnesbeck/ngcm_sklearn_2017.git

If you are not familiar with Git and GitHub, you can simply download the zip file of the repository at the top of the main repository page.

Then, move to the directory created by the clone/zip file:

    cd ngcm_sklearn_2017

and install everything using `conda`:

    conda config --add channels conda-forge
    conda env create -f environment.yml

This will create an **environment** called `ngcm` that includes the packages required for the course.    
​    
If you are not using the Anaconda Python distribution, you will need to manually install the packages listed in `environment.yml` using `pip`.

Which you probably don't want to do.

So install Anaconda.

To use the environment, you may type:

    source activate ngcm
