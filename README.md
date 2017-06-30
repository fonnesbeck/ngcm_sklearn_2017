# Machine Learning using `scikit-learn`

## NGCM Summer Academy 2017



## Instructors

Christopher Fonnesbeck (Vanderbilt University Medical Center)  
Skipper Seabold (Civis Analytics)

## Outline

### Thursday, June 29

**09:30 - 10:45** (Chris Fonnesbeck)

*Introduction to machine learning with scikit-learn*

- 1.a) [Introduction](notebooks/1a-Scikit-Learn.ipynb)
- 1.b) [Data preparation and preprocessing](notebooks/1b-Data-Preprocessing.ipynb)

**11:00 - 13:15** (Chris Fonnesbeck)

*Unsupervised learning*

- 1.c) [PCA and transformations](notebooks/1c-Dimensionality-Reduction.ipynb)
- 1.d) [Clustering](notebooks/1d-Clustering.ipynb)


**13:15 - 14:15 Lunch**

**14:15 - 16:00**

*Supervised Learning* (Skipper Seabold)

- 2.a) [Support vector machines](notebooks/2a-Support-Vector-Machines.ipynb)
- 2.b) [Decision trees and Random Forests](notebooks/2b-Decision-Trees-and-Random-Forests.ipynb)

**16:15 - 17:30** 

*Model selection* (Skipper Seabold)

- 2.c) [Model selection and validation](notebooks/2c-Model-selection-and-validation.ipynb)

### Friday, June 30

**09:30 - 10:45**

*Supervised Learning* (Chris Fonnesbeck)

- 3.a) [Linear regression](notebooks/3a-Regression-Analysis.ipynb)
- 3.b) [Logistic regression](3a-Regression-Analysis-ipynb)

**11:00 - 13:15** (Chris Fonnesbeck)

*Ensemble Supervised Learning*

- 3.c) [Boosting](notebooks/4a-Boosting.ipynb)
- 3.d) [Gaussian processes](notebooks/4b-Gaussian-Processes.ipynb)

**13:15 - 14:15 Lunch**

**14:15 - 16:00** (Skipper Seabold)

*Advanced topics*

- 4.a) [Pipelining](notebooks/4a-Pipelines.ipynb)
- 4.b) [Feature selection](notebooks/4b-Feature-Selection)

**16:15 - 17:30** (Skipper Seabold)

*Advanced topics*

- 4.c) [Text feature extraction](notebooks/5a-Text-Data.ipynb)
- 4.d) [Big Data Strategies](notebooks/5b-Big-Data-Strategies.ipynb)


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

This will create an **environment** called `sklearn` that includes the packages required for the course.    
​    
If you are not using the Anaconda Python distribution, you will need to manually install the packages listed in `environment.yml` using `pip`.

Which you probably don't want to do.

So install Anaconda.

To use the environment, you may type:

    source activate sklearn
