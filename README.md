<div align="center">

# Iris Data Set Project 

![Image description](https://github.com/colmhiggs11/ProandS_Project/blob/master/Pictures%20for%20README/GMIT.png?raw=true) 


<center>

Name | ID Number
------------ | -------------
Colm Higgins| G00287906

*##############Look at why table isnt centered##########*
<div align="left">

This repository contains the files for the project in the Programming and Scripting module 2020. Key files in this repository include the following files which will be explained in more detail below.

*(For quick acces to the files just click on them below)*

* [README.md](https://github.com/colmhiggs11/ProandS_Project/blob/master/README.md) *(Description and Analysis of the project)*
* [IRIS.csv](https://github.com/colmhiggs11/ProandS_Project/blob/master/IRIS.csv) *(Data File)*
* [analysis.py](https://github.com/colmhiggs11/ProandS_Project/blob/master/1.%20analysis.py) *(Program/Script to run functions)*
* [iris_funcs](https://github.com/colmhiggs11/ProandS_Project/blob/master/iris_funcs.py) *(Functions of code created to be called in main **[analysis.py](https://github.com/colmhiggs11/ProandS_Project/blob/master/1.%20analysis.py)** file )*
* [Summary.txt](https://github.com/colmhiggs11/ProandS_Project/blob/master/summary.txt) *(Output of summary required for project)*
* [Plots]() *(Folder containing below outputs)* 
    * Histogram Plots *(PNG files required for project)*
    * Scatter Plots *(PNG files required for project)*
    * Violin Plots
    * Correlation Heatmap

* **Other items**
    * [Project Plan](https://github.com/colmhiggs11/ProandS_Project/blob/master/Programming%20Project%20Plan%20rev2.png?raw=true) *(Latest revision of the Project Plan - Broken down into sections with completion status)*
    * [Images used in the README.md](https://github.com/colmhiggs11/ProandS_Project/tree/master/Pictures%20for%20README)
    * [License](https://github.com/colmhiggs11/ProandS_Project/blob/master/LICENSE) *(MIT License)*
    * .gitignore

##########
Add links for each of plots
Check if there is any other files that need to be mentioned.##########

## Table of Contents
* [1. Introduction](#1-introduction)
* [2. Iris Data](#2-Usage)
* [3. Code](#2-installation)
* [3. Summary / Outcomes](#2-contributors)
* [3. References](#2-installation)
* [3. License](#4-License)
* [3. References](#2-installation)

### <span style="color: navy;">README Layout</span> 

>
## 1.  Introduction
What - This project is an analysis of the well known Iris dataset for the Intoduction to Programming and Scripting module as part fulfilment of the Higher Diploma in Science in Computing (Data Analytics). The project focuses on the widely known Fischer Iris. It requires research and analysis of the dataset and presentation of the findings. The main objective of this analysis is to try and classify the three species of Iris flower by using the four measurements of Sepal width, Sepal length, Petal width and Petal length. The analysis should show if this is possible and will be done in the steps laid out in the README. 
### **<span style="color: navy;">README Layout</span>**
### **<span style="color: red;">README Layout</span>**
### **<span style="color: grey;">README Layout</span>**
### README Layout
#### Background - Data Analysis / Fisher / IRIS data
*This section will include a description of how an analysis/investigation of a dataset is completed and a brief introduction into Ronald Fisher and a look at some of his work.*
#### Code
*This section will discuss the code written to complete the analysis. A list of libraries used, instructions on how to run/download the program and details on what the program actually does will also be included.* 
#### Analysis of Data
*This section will include discussion and analysis of the **outputs** (plots, histograms & summary files)*
#### Summary / Outcomes / Conclusions
*This section will summarise the analysis section and give conclusions based on the data presented.*
#### License
*Brief description of License used while completing this project.*
#### References
*This section will list all of the references used for research and analysis of Iris dataset*

## 2. Background Iris Data
 Multivaraite analysis vs bivariate etc

![Iris Flower types](https://github.com/colmhiggs11/ProandS_Project/blob/master/Pictures%20for%20README/Flower%202.png?raw=true)
How to analyse/investigate a dataset.

### R Fisher 
### Data
    Data that was wrong and why/how I changed it.
![Fisher Data Table](https://github.com/colmhiggs11/ProandS_Project/blob/master/Pictures%20for%20README/Fischer%20Data%20Table.PNG?raw=true)

The use of multiple measurements in taxonomic problems as an example of linear discriminant analysis"
The dataset consists of 50 samples from each of three species of IRIS. Four features from each of the species were measured including: Sepal length & width and Petal length & width
### Assumptions / Analysis

## 3. Code
### How it was written/ How to run
#### Python
Pandas 
Seaborn 
Matplotlib
### What it does

## Analysis of Data
	Histograms
	Scatterplots
	Summary.txt
		Data 
		Explanation
		Images 
	Violin Plots
	Correlations

Program - Analysis.py
	Functions
		Scatterplot of Variables
		Histogram Of Variables
		Summary of Variables to .txt file
			Commets included for all
		Correlation
		Violin Plots


## Summary / Outcomes
	Verginicas and versicoulours are difficult to separate
	Attributes that single out particular flower type.

## Licence
## References



## Contents of Repository
    Histogram.PNG
    Scatterplot.PNG
    Violin.PNG
    Correlation table.PNG
    Summary.txt
    README.md
    IRIS.csv 
    Analysis.PY





<div align="center">

---
## Correlation of Overall Iris flower data
Name | sepal-length| sepal-width| petal-length| petal-width
------------ | ------------- | ------------ | ------------- | -------------
**sepal-length**| 1.000000 |  -0.117570  |    0.871754 |   0.817941
**sepal-width** |-0.117570 |   1.000000  |  -0.428440  |  -0.366126
**petal-length**| 0.871754 |  -0.428440  |   1.000000  |  0.962865
**petal-width** | 0.817941 |  -0.366126  |   0.962865  |  1.000000

---
## Correlation of Iris Setosa flower data
Name | sepal-length| sepal-width| petal-length| petal-width
------------ | ------------- | ------------ | ------------- | -------------
**sepal-length**| 1.000000 |   0.742547  |    0.267176 |   0.278098
**sepal-width** | 0.742547 |  1.000000  |  0.177700   |  0.232752
**petal-length**| 0.267176 |   0.177700  |   1.000000  |  0.331630
**petal-width** | 0.278098 |  0.232752  |   0.331630  |  1.000000

---
## Correlation of Iris versicolor flower data
Name | sepal-length| sepal-width| petal-length| petal-width
------------ | ------------- | ------------ | ------------- | -------------
**sepal-length**| 1.000000 |   0.525911  |    0.754049 |   0.546461
**sepal-width** | 0.525911 |  1.000000  |  0.560522   |  0.663999
**petal-length**| 0.754049 |   0.560522  |   1.000000  |  0.786668
**petal-width** | 0.546461 |  0.663999  |   0.786668  |  1.000000

---
## Correlation of Iris virginica flower data
Name | sepal-length| sepal-width| petal-length| petal-width
------------ | ------------- | ------------ | ------------- | -------------
**sepal-length**| 1.000000 |   0.457228  |    0.864225 |   0.281108
**sepal-width** | 0.457228 |  1.000000  |  0.401045   |  0.537728
**petal-length**| 0.864225 |   0.401045  |   1.000000  |  0.322108
**petal-width** | 0.281108 |  0.537728  |   0.322108  |  1.000000
---
## Summary of Iris Flower Dataset
Name | sepal-length| sepal-width| petal-length| petal-width
------------ | ------------- | ------------ | ------------- | -------------
**count**  |  150.000000  | 150.000000  |  150.000000 |  150.000000
**mean**   |    5.843333  |   3.057333  |    3.758000 |    1.199333
**std**    |    0.828066  |   0.435866  |    1.765298 |    0.762238
**min**    |    4.300000  |   2.000000  |    1.000000 |    0.100000
**25%**    |    5.100000  |   2.800000  |    1.600000 |    0.300000
**50%**    |    5.800000  |   3.000000  |    4.350000 |    1.300000
**75%**    |    6.400000  |   3.300000  |    5.100000 |    1.800000
**max**    |    7.900000  |   4.400000  |    6.900000 |    2.500000




Fischer Paper - https://onlinelibrary.wiley.com/doi/epdf/10.1111/j.1469-1809.1936.tb02137.x  -THE USE OF MULTIPLE MEASUREMENTS IN TAXONOMIC  PROBLEMS

# Multivariate Analysis
P.K. Bhattacharya, Prabir Burman, in Theory and Methods of Statistics, 2016

12.1 Introduction
Multivariate analysis is an area of statistics which deals with observations that are vector valued. Almost all univariate statistical methods have their multivariate counterparts. For instance, when comparing two species of the same animal, various measures such as height, length, tail length, etc., may be measured. One can then compare these two species using a multivariate version of two-sample t-test. Fisher’s famous Iris data set contains four measurements for each of the three species: petal length, petal width, sepal length, and sepal width. In order to compare the three species, a multivariate analog of analysis of variance has been developed. If there is a new observation vector (of unknown species) with four measurements, then allocation of this observation vector to one of the species is known as the problem of classification.

Another class of procedures has been developed for multivariate data which deal with dimensionality reduction. If many measurements are taken on children where each measurement is a measure of intelligence, then it is often the case that these various measures are correlated with each other. If there are 20 measurements for each child, it may be reasonable to look for a few summaries which contain most of the information. These summaries are often expressed as appropriate linear combinations of the measurements. This class of methods is known as principal components and factor analyses.

We describe these methods in a systematic manner starting with a few technical results on the Wishart distribution, which is a multivariate generalization of the chi-squared distribution.