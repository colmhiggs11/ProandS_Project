<div align="center">

# Iris Data Set Project 

![Image description](https://github.com/colmhiggs11/ProandS_Project/blob/master/Pictures%20for%20README/GMIT.png?raw=true) 


<div align="center">

Name | ID Number
------------ | -------------
Colm Higgins| G00287906

*##############Look at why table isnt centered##########*
<div align="left">

## Information
This repository contains the files for the project in the Programming and Scripting module 2020. Key files in this repository include the following files which will be explained in more detail below.*(For quick acces to the files just click on them below)*

* [README.md](https://github.com/colmhiggs11/ProandS_Project/blob/master/README.md) *(Description and Analysis of the project)*
* [IRIS.csv](https://github.com/colmhiggs11/ProandS_Project/blob/master/IRIS.csv) *(Data File)*
* [2. analysis.py](https://github.com/colmhiggs11/ProandS_Project/blob/master/1.%20analysis.py) *(Program/Script to run functions)*
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
    * [README Layout](#readme-layout)
* [2. Background R Fisher & Iris Data](#2-background-r-fisher--iris-data)
* [3. Code](#3-code)
* [4. Summary / Outcomes](#4-summary-outcomes)
* [5. License](#5-License)
* [6. References](#6-references)

### <span style="color: navy;">README Layout</span> 

## 1.  Introduction
What - This project is an analysis of the well known Iris dataset for the Intoduction to Programming and Scripting module as part fulfilment of the Higher Diploma in Science in Computing (Data Analytics). The project focuses on the widely known Fischer Iris. It requires research and analysis of the dataset and presentation of the findings. The main objective of this analysis is to try and classify the three species of Iris flower by using the four measurements of Sepal width, Sepal length, Petal width and Petal length. The analysis should show if this is possible and will be done in the steps laid out in the README. 

### README Layout
#### [Background - Data Analysis / Fisher / IRIS data](#2-background-r-fisher--iris-data)
*This section will include a description of how an analysis/investigation of a dataset is completed and a brief introduction into Ronald Fisher and a look at some of his work.*
#### [Code](#3-code)
*This section will discuss the code written to complete the analysis. A list of libraries used, instructions on how to run/download the program and details on what the program actually does will also be included.* 
#### Analysis of Data
*This section will include discussion and analysis of the **outputs** (plots, histograms & summary files)*
#### Summary / Outcomes / Conclusions
*This section will summarise the analysis section and give conclusions based on the data presented.*
#### License
*Brief description of License used while completing this project.*
#### References
*This section will list all of the references used for research and analysis of Iris dataset*

## 2. Background R Fisher & Iris Data
### Ronald Fisher 
Sir Ronald Fisher (1890-1962) was a British statistician and geneticist, also hailed as the greatest biologist since Charles Darwin he was one of the principal founders of population genetics.. 
Fisher had a keen interest in [Eugenics](https://www.google.com/search?q=Eugenics&oq=Eugenics&aqs=chrome..69i57j69i61l3&sourceid=chrome&ie=UTF-8). He felt that “socially strong” people should be encouraged to have more children rather that those who were classified as “socially weak” Fishers interest in Eugenics paved the way for his work in the genetics of a population.  He investigated the link between genes for different traits and developed methods of multivariate analysis to complete the analysis. One of the most famous datasets used in Data Science is Fishers Iris Dataset. This dataset comes from his work in discriminant analysis and can be found in “The use of multiple measurements in taxonomic problems” (Fisher, 1936).

<center>

|![Fisher Data Table](https://github.com/colmhiggs11/ProandS_Project/blob/master/Pictures%20for%20README/Fischer%20Data%20Table.PNG?raw=true)|
|:--:| 
| *Fishers Iris Dataset -“The use of multiple measurements in taxonomic problems” (Fisher, 1936)* |

<div align="left">
Fischer Paper:

    https://onlinelibrary.wiley.com/doi/epdf/10.1111/j.1469-1809.1936.tb02137.x  -THE USE OF MULTIPLE MEASUREMENTS IN TAXONOMIC  PROBLEMS


### Data Analysis
Data analysis is a process of analysing a dataset using concepts from statistics & probability and presenting the results in tabular or graphical format. Typically there are three main types of datasets that are analysed. These include Univarite and Bivariate & Multivariate datasets. 
Univariate data consists of only one variable and is the simplest. It does not allow for analysis of relationships or causes, it is more often used in describing data. Examples of graphical representations are histograms, pie chart and bar charts.
Bivariate & Multivariate data consists of two or more variables which are classified as dependent or independent. These types of datasets do deal with causes and relationships and looks to find correlations between independent variables that allow the dependant variable to be easily distinguishable. This analysis will be a combination of Univariate and Bivariate. 
For more information on these click on the links. 
https://www.geeksforgeeks.org/univariate-bivariate-and-multivariate-data-and-its-analysis/
https://www.statisticshowto.com/bivariate-analysis/

### Iris Dataset
The Iris Dataset or “Fishers Iris Dataset” is one of the most recognisable databases found in the data analytics. Fisher's paper “Taxonometric paper” is a classic in the field and is one of the first papers to deal with classification. Whilst Fisher is linked with the dataset Edgar Anderson was actually responsible for collecting the measurements. The dataset is a multivariate dataset consisting of four measurements that would be described as the independent variables [Sepal length & width and Petal length & width] and finally a class as the dependant variable that is split into 3 types of flowers [setosa, versicolor, or virginica] There are 50 measurements of each variable for each of the three classes (i.e. a total of 150 measurements) The image below shows the three flower types and the measurements of each variable. The data should show that one flower type is linearly separable from the others and the remaining two are much more difficult to separate. 

|![Iris Flower types](https://github.com/colmhiggs11/ProandS_Project/blob/master/Pictures%20for%20README/Flower%202.png?raw=true)|
|:--:| 
| *Iris flowers by species & measurements included in Fishers Dataset* |

https://en.wikipedia.org/wiki/Iris_flower_data_set
https://archive.ics.uci.edu/ml/datasets/iris 


## 3. Code for analysis
### How it was written
The analysis of the Iris dataset will be completed using [Python](https://en.wikipedia.org/wiki/Python_(programming_language)).
The version of python installed on my PC at time of completion of this project is :Python 3.7.4 (default, Aug  9 2019, 18:34:13) [MSC v.1915 64 bit (AMD64)] :: Anaconda, Inc. on win32
http://anh.cs.luc.edu/handsonPythonTutorial/ch1.html
https://wiki.python.org/moin/BeginnersGuide/Programmers 
### How to run
To complete the analysis you will first need to download the repository from Github, download and install pyton with anaconda, read the below on what each function/program does and then run. 
### Python Packages & libraries
To run the code the following Packages & libraries need to be imported as there are a number of functions, dataframes, plotting & graph features specific to each library that are required in the analysis. The comments in [iris_funcs.py]() will show them in use but for more information on the packages or libraries see links below.
[Pandas](https://pandas.pydata.org/) 
[Seaborn](https://seaborn.pydata.org/index.html) 
[Matplotlib](https://matplotlib.org/)

### What code does
The two main file that will provide the outputs for the analysis are *[iris_funcs.py]()* and *[2. analysis.py](https://github.com/colmhiggs11/ProandS_Project/blob/master/1.%20analysis.py)*. 
iris_funcs.py is made up of functions and script that imports the codes and creates the environment for the analysis to take place. Pandas is used to create the dataframe and import the dataset as Iris.csv. Once the headings are assigned to the rows and variable Data assigned the dataset contents, the five functions are created. Explanantions below.

#### iris_func.py
**IrSums():** - This function opens and writes to a text file called summary.txt with a summary of the following for each of the three species types. Mean, Standard deviation, minimum value, 25% percentile,50% percentile, 75% percentile & maximum values. There is also a statement that will output whether there is any data missing from the dataset.
######################### put in links   #########################

---
 **IrHist(Mestyp1):** - This function creates the histograms for each of the four independant variables with data on each histogram shown by species type (assigned as heading[4]). To do this [seaborns FacetGrid](https://seaborn.pydata.org/generated/seaborn.FacetGrid.html) object is initalised and the dataset is mapped onto the single plot. A distribution plot was used with the kde(kernel density estimate) turned off as this calculates the probable density and skews the y-axis values. The rest of the function is just formatting and saving the plots as .png files to the repository. The number of bins used was 25. As there are 50 measurements per species this allows the data to be easily visualised from the histograms. The arguement required will be the measurement type otherwise known as one of the four independent variables.

---
**Sctrplt():** - The scatterplot was created using [seaborns pairplot](https://seaborn.pydata.org/generated/seaborn.pairplot.html). This plots pairwise variables in the dataset again by species type in a grid of plots. This was then saved to the repository as a .png file.

---
**Vioplots(Mestyp2):** - This function creates four violinplots as subplots using [seaborns violinplot](https://seaborn.pydata.org/generated/seaborn.violinplot.html). Using plt.subplot from [Matplotlib](https://matplotlib.org/3.2.1/api/_as_gen/matplotlib.pyplot.subplot.html) each plot can be assigned a position in the four figure plot. The arguement required will be the measurement type otherwise known as one of the four independent variables. 

---
**Ir_Corrls():** - This function creates a heatmap correlation table. [Seaborns heatmap](https://seaborn.pydata.org/generated/seaborn.heatmap.html) function creates the color encoded matrix once the correct data file is added. This particular heatmap shows correlation for overall file not by species type. The rest of the script is formatting. There was an issue with the heatmap function in Python 3.7.4 that cut out half of the top and bottom sections of the heatmap. To get around this below was used to [extend the y-axis](https://github.com/matplotlib/matplotlib/issues/14751) 

    ax.set_ylim(len(Iriscorrel)+0.5, -0.5)>


#### analysis.py
**Importing Functions and list** - The functions created above were imported and the list assigned to variable heading also imported so that both could be called for execution. (*Shown below*)

    import iris_funcs as ifs
    from iris_funcs import heading

**Calling functions** - Each of the functions were then called. Some required using the list **"heading"** to be passed through as the arguement. (*Shown below*)

    ifs.IrSums()
    ifs.Sctrplt()
    ifs.Ir_Corrls()

    def Createhist():
        ifs.IrHist(heading[0])
        ifs.IrHist(heading[1])
        ifs.IrHist(heading[2])
        ifs.IrHist(heading[3])
    Createhist()        

    def CreateVioplot():
        ifs.Vioplots(heading[0:4])
    CreateVioplot()

## 4. Analysis of Data
Histograms
Scatterplots
Summary.txt
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







### **<span style="color: navy;">README Layout</span>** 