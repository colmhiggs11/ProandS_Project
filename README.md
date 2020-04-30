<div align="center">

# Iris Data Set Project 

![Image description](https://github.com/colmhiggs11/ProandS_Project/blob/master/Pictures%20for%20README/GMIT.png?raw=true) 


<div align="center">


![Name and Id number](https://github.com/colmhiggs11/ProandS_Project/blob/master/Pictures%20for%20README/Name%20number%20box.PNG?raw=true)


<div align="left">

## Information
This repository contains the files for the project in the Programming and Scripting module 2020. Key files in this repository include the following files which will be explained in more detail below. *(For quick access to the files just click on them below)*

* [README.md](https://github.com/colmhiggs11/ProandS_Project/blob/master/README.md) *(Description and Analysis of the project)*
* [IRIS.csv](https://github.com/colmhiggs11/ProandS_Project/blob/master/IRIS.csv) *(Data File)*
* [2.analysis.py](https://github.com/colmhiggs11/ProandS_Project/blob/master/2.analysis.py) *(Program/Script to run functions)*
* [iris_functs](https://github.com/colmhiggs11/ProandS_Project/blob/master/iris_functs.py) *(Functions of code created to be called in main **[2.analysis.py]** file )*
* [Summary.txt](https://github.com/colmhiggs11/ProandS_Project/blob/master/summary.txt) *(Output of summary required for project)*
* [Plots](https://github.com/colmhiggs11/ProandS_Project/tree/master/Plots) *(Folder containing below outputs)* 
    * [Histogram Plots](https://github.com/colmhiggs11/ProandS_Project/tree/master/Plots/Histogram%20PNG's) *(PNG files required for project)*
    * [Scatter Plot](https://github.com/colmhiggs11/ProandS_Project/blob/master/Plots/Scatterplot%20of%20variables.png?raw=true) *(PNG files required for project)*
    * [Violin Plot](https://github.com/colmhiggs11/ProandS_Project/blob/master/Plots/Violin%20plot%20of%20variables.png?raw=true)
    * [Correlation Heatmap](https://github.com/colmhiggs11/ProandS_Project/blob/master/Plots/Correlation%20Heatmap.png?raw=true)

* **Other items**
    * [Project Plan](https://github.com/colmhiggs11/ProandS_Project/tree/master/Project%20Planning) *(Latest revision of the Project Plan - Broken down into sections with completion status)*
    * [Images used in the README.md](https://github.com/colmhiggs11/ProandS_Project/tree/master/Pictures%20for%20README)
    * [License](https://github.com/colmhiggs11/ProandS_Project/blob/master/LICENSE) *(MIT License)*
    * .gitignore


## Table of Contents
* [1. Introduction](#1-introduction)
    * [README Layout](#readme-layout)
* [2. Background R Fisher & Iris Data](#2-background-r-fisher--iris-data)
* [3. Code for analysis](#3-Code-for-analysis)
* [4. Analysis of Data](#4-analysis-of-data)
* [5. Summary / Conclusions](#5-Summary--Conclusions)
* [6. Licence](#6-Licence)
* [7. References](#7-References)



## 1.  Introduction
This project is an analysis of the well known Iris dataset for the Introduction to Programming and Scripting module as part fulfilment of the Higher Diploma in Science in Computing (Data Analytics). The project focuses on the widely known Fischer Iris. It requires research and analysis of the dataset and presentation of the findings. The main objective of this analysis is to try and classify the three species of Iris flower by using the four measurements of Sepal width, Sepal length, Petal width and Petal length. The analysis should show if this is possible and will be done in the steps laid out in the README. 

---
### 1.1 README Layout
#### [Background - Data Analysis / Fisher / IRIS data](#2-background-r-fisher--iris-data)
*This section will include a description of how an analysis/investigation of a dataset is completed and a brief introduction into Ronald Fisher and a look at some of his work.*
#### [Code for analysis](#3-Code-for-analysis)
*This section will discuss the code written to complete the analysis. A list of libraries used, instructions on how to run/download the program and details on what the program actually does will also be included.* 
#### [Analysis of Data](#4-analysis-of-data)
*This section will include discussion and analysis of the **outputs** (plots, histograms & summary files)*
#### [Summary / Conclusions](#5-Summary--Conclusions)
*This section will summarise the analysis section and give conclusions based on the data presented.*
#### [Licence](#6-Licence)
*Brief description of License used while completing this project.*
#### [References](#7-References)]
*This section will list all of the references used for research and analysis of Iris dataset*

## 2. Background R Fisher & Iris Data
### 2.1 Ronald Fisher 
Sir Ronald Fisher (1890-1962) was a British statistician and geneticist, also hailed as the greatest biologist since Charles Darwin he was one of the principal founders of population genetics. 
Fisher had a keen interest in [Eugenics](https://www.google.com/search?q=Eugenics&oq=Eugenics&aqs=chrome..69i57j69i61l3&sourceid=chrome&ie=UTF-8). He felt that “socially strong” people should be encouraged to have more children rather that those who were classified as “socially weak” Fishers interest in Eugenics paved the way for his work in the genetics of a population.  He investigated the link between genes for different traits and developed methods of multivariate analysis to complete the analysis. One of the most famous datasets used in Data Science is Fishers Iris Dataset. This dataset comes from his work in discriminant analysis and can be found in “The use of multiple measurements in taxonomic problems” (Fisher, 1936).

<div align="center">

|![Fisher Data Table](https://github.com/colmhiggs11/ProandS_Project/blob/master/Pictures%20for%20README/Fischer%20Data%20Table.PNG?raw=true)|
|:--:| 
| *Fishers Iris Dataset -“The use of multiple measurements in taxonomic problems” (Fisher, 1936)* |

<div align="left">

---
### 2.2 Data Analysis
Data analysis is a process of analysing a dataset using concepts from statistics & probability and presenting the results in tabular or graphical format. Typically there are three main types of datasets that are analysed. These include Univarite and Bivariate & Multivariate datasets. 
Univariate data consists of only one variable and is the simplest. It does not allow for analysis of relationships or causes, it is more often used in describing data. Examples of graphical representations are histograms, pie chart and bar charts.
Bivariate & Multivariate data consists of two or more variables which are classified as dependent or independent. These types of datasets do deal with causes and relationships and looks to find correlations between independent variables that allow the dependant variable to be easily distinguishable. This analysis will be a combination of Univariate and Bivariate. 
For more information on these click on the links. 


---
### 2.3 Iris Dataset
The Iris Dataset or “Fishers Iris Dataset” is one of the most recognisable databases found in the data analytics. Fisher's paper “Taxonometric paper” is a classic in the field and is one of the first papers to deal with classification. Whilst Fisher is linked with the dataset Edgar Anderson was actually responsible for collecting the measurements. The dataset is a multivariate dataset consisting of four measurements that would be described as the independent variables [Sepal length & width and Petal length & width] and finally a class as the dependant variable that is split into 3 types of flowers [setosa, versicolor, or virginica] There are 50 measurements of each variable for each of the three classes (i.e. a total of 150 measurements) The image below shows the three flower types and the measurements of each variable. The data should show that one flower type is linearly separable from the others and the remaining two are much more difficult to separate. 

<div align="center">

|![Iris Flower types](https://github.com/colmhiggs11/ProandS_Project/blob/master/Pictures%20for%20README/Flower%202.png?raw=true)|
|:--:| 
| *Iris flowers by species & measurements included in Fishers Dataset* |

<div align="left">

The dataset used in this analysis was obtained from [UCI archive](https://archive.ics.uci.edu/ml/datasets/iris). There were two errors which required updating the .csv file.
    
    This data differs from the data presented in Fishers article (identified by Steve Chadwick, spchadwick '@' espeedaz.net ).
    The 35th sample should be: 4.9,3.1,1.5,0.2,"Iris-setosa" where the error is in the fourth feature. The 38th sample:
    4.9,3.6,1.4,0.1,"Iris-setosa" where the errors are in the second and third features.


## 3. Code for analysis

### 3.1 How it was written
The analysis of the Iris dataset will be completed using [Python](https://en.wikipedia.org/wiki/Python_(programming_language)).

The version of python installed on my PC at time of completion of this project is: Python 3.7.4 [MSC v.1915 64 bit (AMD64)] :: Anaconda, Inc. on win32
 
---
### 3.2 How to run
To complete the analysis you will first need to download the repository from Github, download and install python with anaconda, read the below on what each function/program does and then run. 

---
### 3.3 Python Packages & libraries
To run the code the following Packages & libraries need to be imported as there are a number of mathematical functions, dataframes, plotting & graph features specific to each library that are required in the analysis. The comments in [iris_functs.py]() will show them in use but for more information on the packages or libraries see links below.
* [Pandas](https://pandas.pydata.org/)
* [Seaborn](https://seaborn.pydata.org/index.html) 
* [Matplotlib](https://matplotlib.org/)
* [Numpy](https://numpy.org/)

---
### 3.4 What the code does
The two main file that will provide the outputs for the analysis are *[iris_functs.py](https://github.com/colmhiggs11/ProandS_Project/blob/master/iris_functs.py)* and *[2.analysis.py](https://github.com/colmhiggs11/ProandS_Project/blob/master/2.analysis.py)*.

**iris_functs.py** -  is made up of functions and script that imports the codes and creates the environment for the analysis to take place. Pandas is used to create the dataframe and import the dataset as Iris.csv. Once the headings are assigned to the rows and variable Data assigned the dataset contents, the five functions are created. 

**2.analysis.py.** - calls the functions from iris_functs.py and executes script.
(*Explantions below*)


<div align="center">

---
#### iris_functs.py

<div align="left">

---
**IrSums():** - This function opens and writes to a text file called summary.txt with a summary of the following for each of the three species types. Mean, Standard deviation, minimum value, 25% percentile, 50% percentile, 75% percentile & maximum values. There is also a statement that will output whether there is any data missing from the dataset.
######################### put in links   #########################


**StdEmprule(Mestyp3):** - This function takes the standard deviation and mean and calculates the probability density funciton using the [Empirical rule](#-standard-deviation-std). An array is created using Numpy so the calculations can be completed and the data then forms a Dataframe for display. The arguement passed to the function is the type of Iris flower.

 **IrHist(Mestyp1):** - This function creates the histograms for each of the four independent variables with data on each histogram shown by species type (assigned as heading[4]). To do this [seaborns FacetGrid](https://seaborn.pydata.org/generated/seaborn.FacetGrid.html) object is initailised and the dataset is mapped onto the single plot. A distribution plot was used with the kde (kernel density estimate) turned off as this calculates the probable density and skews the y-axis values. The rest of the function is just formatting and saving the plots as .png files to the repository. The number of bins used was 25. As there are 50 measurements per species this allows the data to be easily visualised from the histograms. The argument required will be the measurement type otherwise known as one of the four independent variables.

**Sctrplt():** - The scatterplot was created using [seaborns pairplot](https://seaborn.pydata.org/generated/seaborn.pairplot.html). This plots pairwise variables in the dataset again by species type in a grid of plots. This was then saved to the repository as a .png file.

**Vioplots(Mestyp2):** - This function creates four violinplots as subplots using [seaborns violinplot](https://seaborn.pydata.org/generated/seaborn.violinplot.html). Using plt.subplot from [Matplotlib](https://matplotlib.org/3.2.1/api/_as_gen/matplotlib.pyplot.subplot.html) each plot can be assigned a position in the four figure plot. The argument required will be the measurement type otherwise known as one of the four independent variables. 

**Ir_Corrls():** - This function creates a heatmap correlation table. [Seaborns heatmap](https://seaborn.pydata.org/generated/seaborn.heatmap.html) function creates the colour encoded matrix once the correct data file is added. This particular heatmap shows correlation for overall file not by species type. The rest of the script is formatting. There was an issue with the heatmap function in Python 3.7.4 that cut out half of the top and bottom sections of the heatmap. To get around this below was used to [extend the y-axis](https://github.com/matplotlib/matplotlib/issues/14751) 

    ax.set_ylim(len(Iriscorrel)+0.5, -0.5)>

<div align="center">

---
#### 2.analysis.py
<div align="left">

---
**Importing Functions and list** - The functions created above were imported and the list assigned to variable heading also imported so that both could be called for execution. (*Shown below*)

    import iris_functs as ifs
    from iris_functs import heading,Data

**Calling functions** - Each of the functions were then called. Some required using the list **"heading"** to be passed through as the argument. (*Shown below*)


    ifs.IrSums()

    def Emprule():
        ifs.StdEmprule("Iris-setosa")
        ifs.StdEmprule("Iris-versicolor")
        ifs.StdEmprule("Iris-virginica")
    Emprule()

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
### 4.1 Summary.txt
The summary table below shows the output that can be found in the [summary.txt](https://github.com/colmhiggs11/ProandS_Project/blob/master/summary.txt) file using the describe() function that was executed on per species type of Iris flower. The values for each summary metric are discussed below the table.

<div align="center">

    Summary of Iris Setosa flower data
            sepal-length  sepal-width  petal-length  petal-width
    count      50.00000    50.000000     50.000000    50.000000
    mean        5.00600     3.428000      1.462000     0.246000
    std         0.35249     0.379064      0.173664     0.105386
    min         4.30000     2.300000      1.000000     0.100000
    25%         4.80000     3.200000      1.400000     0.200000
    50%         5.00000     3.400000      1.500000     0.200000
    75%         5.20000     3.675000      1.575000     0.300000
    max         5.80000     4.400000      1.900000     0.600000 

    Summary of Iris versicolor flower data
            sepal-length  sepal-width  petal-length  petal-width
    count     50.000000    50.000000     50.000000    50.000000
    mean       5.936000     2.770000      4.260000     1.326000
    std        0.516171     0.313798      0.469911     0.197753
    min        4.900000     2.000000      3.000000     1.000000
    25%        5.600000     2.525000      4.000000     1.200000
    50%        5.900000     2.800000      4.350000     1.300000
    75%        6.300000     3.000000      4.600000     1.500000
    max        7.000000     3.400000      5.100000     1.800000 

    Summary of Iris virginica flower data
            sepal-length  sepal-width  petal-length  petal-width
    count      50.00000    50.000000     50.000000     50.00000
    mean        6.58800     2.974000      5.552000      2.02600
    std         0.63588     0.322497      0.551895      0.27465
    min         4.90000     2.200000      4.500000      1.40000
    25%         6.22500     2.800000      5.100000      1.80000
    50%         6.50000     3.000000      5.550000      2.00000
    75%         6.90000     3.175000      5.875000      2.30000
    max         7.90000     3.800000      6.900000      2.50000


<div align="left">

---
#### Count
All values clearly show that measuremts were taken on 50 flowers in each of the three species.

---
#### Mean
Shows the average measurements taken for each of the flower types. 
|Name | Comment|
|:--|:--|
|Sepal-length:|This is the measurement with the least variation across all of the Iris flowers ranging from 5-6.58 cm for with Setosa being the smallest and Virginica the largest.|
|Sepal-width:|This measurement is shows very little variation between Virginica and Versicolor and also is the only average measurement where the Setosa flower is larger than the other two|
|Petal-length:|The average petal length across the three flowers shows some interesting results. Whilst Virginica and Versicolor don't differ greatly *(range of 4.26-5.55cm)* the Setosa flower shows some significant uniques qualities. It's average petal length is much smaller at 1.46 cm|
|Petal-width:|Whilst the average measurements for petal width are smaller than the petal length, they do show similar traits to petal width where Virginica and Versicolor don't differ greatly and the Setosa flower average is much lower.|

---
#### Standard Deviation (Std)
Shows how much the measurements differ from the mean. Typically if the (std) is low then the data would be seen to be clustered relatively closely around the mean. A high Std suggests that the data is more dispersed and would have a larger range. It also allows for the calculation of the Probability density function the formula shown below. Using the [Empirical or 68,95,99.7 Rule](https://towardsdatascience.com/understanding-the-68-95-99-7-rule-for-a-normal-distribution-b7b7cbf760c2) the percentage of values that fall within one and three standard deviations of the mean can be calculated. See graph below.

<div align="center">

|![Standard deviation table](https://github.com/colmhiggs11/ProandS_Project/blob/master/Pictures%20for%20README/Standard%20Deviation.png?raw=true)|![Probability Density formula](https://github.com/colmhiggs11/ProandS_Project/blob/master/Pictures%20for%20README/Probability%20Density.PNG?raw=true)|
|:--:|:--:|
| *Empirical rule distribution*  | *Probability Density formula* |


<div align="left">

The Empirical rule for each species and each measurement was completed and is shown in the tables below. Although the tables have six columns of data the data is actually broken into three sections of two columns with ranges for each of the measurements taken. The first two columns show the range that 68% of the data is estimated to be in, the second two columns show the range that 95% of the data is located in and the final two columns show the range that includes 99.7% of the data. 

<div align="center">

| *Standard deviation by measurement variable*  |
|:-----:|

Name | Comment
:--------------|:--
|Sepal-length:|In terms of sepal length 99.7% of the data for each of the flowers fall into the following ranges: **Setosa: 3.9 - 6.06cm**, **Versicolor: 4.38 - 7.48cm** and **Virginica: 4.6 - 8.49cm**|
|Sepal-width:|In terms of sepal width 99.7% of the data for each of the flowers fall into the following ranges: **Setosa: 2.29 - 4.56cm**, **Versicolor: 1.82 - 3.71cm** and **Virginica: 2.0 - 3.94cm**|
|Petal-length:|In terms of Petal-length 99.7% of the data for each of the flowers fall into the following ranges: **Setosa: 0.94 - 1.98cm**, **Versicolor: 2.85 - 5.6cm** and **Virginica: 3.89 - 7.20cm**|
|Petal-width:|In terms of Petal-width 99.7% of the data for each of the flowers fall into the following ranges: **Setosa: -0.07 - 0.56cm**, **Versicolor: 0.73 - 1.9cm** and **Virginica: 1.2 - 2.84cm**|

Empirical rule data for Iris-setosa

---
Measurement | 68% (mean-std)| 68%(mean-std)| 95%(mean-std(2))| 95%(mean-std(2))|99.7%(mean-std(3))|99.7%(mean-std(3))
:------------: | :------------: | :------------: | :------------: | :------------: | :------------: | :------------:                     
sepal-length|  4.653510 | 5.358490 | 4.301021 | 5.710979|   3.948531 |  6.063469
sepal-width|   3.048936 | 3.807064|  2.669871 | 4.186129 |  2.290807 |  4.565193
petal-length|  1.288336|  1.635664 | 1.114672 | 1.809328 |  0.941008  | 1.982992
petal-width|   0.140614 | 0.351386 | 0.035229 | 0.456771 | -0.070157  | 0.562157

Empirical rule data for Iris-versicolor

---
Measurement | 68% (mean-std)| 68%(mean-std)| 95%(mean-std(2))| 95%(mean-std(2))|99.7%(mean-std(3))|99.7%(mean-std(3))
:------------: | :------------: | :------------: | :------------: | :------------: | :------------: | :------------:     
sepal-length | 5.419829| 6.452171  |4.903658 | 6.968342  | 4.387487|   7.484513
sepal-width   |2.456202 | 3.083798 | 2.142403 | 3.397597  | 1.828605|   3.711395
petal-length  |3.790089 | 4.729911 | 3.320178 | 5.199822  | 2.850267 |  5.669733
petal-width  | 1.128247|  1.523753 | 0.930495 | 1.721505 |  0.732742  | 1.919258

Empirical rule data for Iris-versicolor

---
Measurement | 68% (mean-std)| 68%(mean-std)| 95%(mean-std(2))| 95%(mean-std(2))|99.7%(mean-std(3))|99.7%(mean-std(3))
:------------: | :------------: | :------------: | :------------: | :------------: | :------------: | :------------:    
sepal-length | 5.952120  |7.223880 | 5.316241 | 7.859759  | 4.680361 |  8.495639
sepal-width  | 2.651503  |3.296497 | 2.329007 | 3.618993  | 2.006510 |  3.941490
petal-length | 5.000105  |6.103895 | 4.448211 | 6.655789  | 3.896316 |  7.207684
petal-width  | 1.751350  |2.300650 | 1.476700 | 2.575300  | 1.202050 |  2.849950

<div align="left">

---
#### Minimum
Shows the minimum values of each measurement for the particular species. Again the minimum data is fairly similar for the Virginica and Versicolor while Setosa's show some differences.

---
#### Percentiles
Shows the number of measurements that fall below the stated percentage. 50% is the median if this value is similar to the mean value then it shows that the data is symmetrically distributed with a low number of datapoints outside the Probable distribution function.

---
#### Maximum
Shows the maximum values of each measurement for the particular species. Again the maximum data is fairly similar for the Virginica and Versicolor while Setosa's show some differences.

---
### 4.2 Histograms
Below shows the histogram plots for each measurement broken out per species. *(To enlarge the graph just click on them.)* The histograms show that for Petal length & width Setosa's are easily distinguishable whereas Virginica and Versicolor are slightly more difficult to differentiate. Also the Sepal measurements don't make it easy to classify the Iris flower type.


|![hist](https://github.com/colmhiggs11/ProandS_Project/blob/master/Plots/Histogram%20PNG's/sepal-length.png?raw=true)|![hist](https://github.com/colmhiggs11/ProandS_Project/blob/master/Plots/Histogram%20PNG's/sepal-width.png?raw=true)|
|:--:|:--:|
| *Sepal Length per Species* |*Sepal Width per Species*|

|![hist](https://github.com/colmhiggs11/ProandS_Project/blob/master/Plots/Histogram%20PNG's/petal-length.png?raw=true)|![hist](https://github.com/colmhiggs11/ProandS_Project/blob/master/Plots/Histogram%20PNG's/petal-width.png?raw=true)|
|:--:|:--:|
| *Petal Length per Species* |*Petal Width per Species*|

---
### 4.3 Scatterplots
The scatterplot shown below shows all of the possible bivariate relationships and most seperated clusters split by species type. The plots further confirm the ability to classify Setosa's is relatively simple compared to between Virginica and Versicolor.


|![Pairplot](https://github.com/colmhiggs11/ProandS_Project/blob/master/Plots/Scatterplot%20of%20variables.png?raw=true)
|:--:|
| *Scatterplot of measurements plotted against eachoher by species* |

---
### 4.4 Violin Plots
The violinplot shows the full distribution of data and makes it easy to spot the outliers when backed up with the dataset. The plot below has a number of features that tell a lot about each of the species. The median is identified as the white dot on the "violin" The [interquartile range](https://towardsdatascience.com/violin-plots-explained-fb1d115e023d) which is the the black bar in the middle of violin and the upper & lower adjacent values identified as the thin black line coming out of the interquartile range bar on the violinplot. 
The upper and lower values are calculated by: Upper - adding the third quartile(75% percentile) + 1.5 IQR(75% percentile - 25% percentile), Lower - subtracting first quartile(25% percentile) - 1.5 IQR(75% percentile - 25% percentile). Any values that fall outside of these ranges will then be seen as outliers.

|![Violin Plot of four measurements per species](https://github.com/colmhiggs11/ProandS_Project/blob/master/Plots/Violin%20plot%20of%20variables.png?raw=true)
|:--:|
| *Violinplot of four measurement variables per species* |

---
### 4.5 Correlations

|![Heatmap](https://github.com/colmhiggs11/ProandS_Project/blob/master/Plots/Correlation%20Heatmap.png?raw=true)
|:--:|
| *Overall correlation between measurment variables in Iris Dataset* |

|![Setosa Corr](https://github.com/colmhiggs11/ProandS_Project/blob/master/Pictures%20for%20README/Setosa%20Corr.PNG?raw=true)|![Versicolor Corr](https://github.com/colmhiggs11/ProandS_Project/blob/master/Pictures%20for%20README/Versi%20Corr.PNG?raw=true)|![Virginica Corr](https://github.com/colmhiggs11/ProandS_Project/blob/master/Pictures%20for%20README/Virgini%20Corr.PNG?raw=true)|
|:--:|:--:|:--:|
| *Correlation for Setosa flower* |*Correlation for Setosa flower*|*Correlation for Setosa flower*|

<div align="left">

## 5. Summary / Conclusions
Verginicas and versicoulours are difficult to separate
Attributes that single out particular flower type.

## 6. Licence
This project was completed using the [MIT License](https://opensource.org/licenses/MIT). Due to the limited restrictions it puts on reuse, it has a high license compatibility.
## 7. References
1.	https://www.google.com/search?q=Eugenics&oq=Eugenics&aqs=chrome..69i57j69i61l3&sourceid=chrome&ie=UTF-8 
2.	https://github.com/colmhiggs11/ProandS_Project/blob/master/Pictures%20for%20README/Fischer%20Data%20Table.PNG?raw=true
3.	https://onlinelibrary.wiley.com/doi/epdf/10.1111/j.1469-1809.1936.tb02137.x
4.	https://www.geeksforgeeks.org/univariate-bivariate-and-multivariate-data-and-its-analysis/
5.	https://www.statisticshowto.com/bivariate-analysis/
6.	https://en.wikipedia.org/wiki/Iris_flower_data_set
7.	https://archive.ics.uci.edu/ml/datasets/iris
8.	https://en.wikipedia.org/wiki/Python_(programming_language)
9.	http://anh.cs.luc.edu/handsonPythonTutorial/ch1.html
10.	https://wiki.python.org/moin/BeginnersGuide/Programmers 
11.	https://pandas.pydata.org/
12.	https://www.dataquest.io/blog/pandas-cheat-sheet/
13.	https://seaborn.pydata.org/index.html
14.	https://matplotlib.org/
15.	https://realpython.com/python-matplotlib-guide/
16.	https://seaborn.pydata.org/generated/seaborn.FacetGrid.html
17.	https://seaborn.pydata.org/generated/seaborn.distplot.html
18.	https://www.datacamp.com/community/tutorials/histograms-matplotlib
19.	https://seaborn.pydata.org/generated/seaborn.pairplot.html
20.	https://seaborn.pydata.org/generated/seaborn.violinplot.html
21.	https://matplotlib.org/3.2.1/api/_as_gen/matplotlib.pyplot.subplot.html
22.	https://seaborn.pydata.org/generated/seaborn.heatmap.html
23.	https://github.com/matplotlib/matplotlib/issues/14751 
24.	https://opensource.org/licenses/MIT
25.	https://stackoverflow.com/questions/24319505/how-can-one-display-images-side-by-side-in-a-github-readme-md
26.	https://www.youtube.com/watch?v=9lMwjk8jE48 - correlations 1,1,1,1
27.	https://www.youtube.com/watch?v=BrFEmO-zPuA
28. https://towardsdatascience.com/understanding-the-68-95-99-7-rule-for-a-normal-distribution-b7b7cbf760c2
29. https://numpy.org/
30. https://medium.com/casual-inference/the-most-time-efficient-ways-to-import-csv-data-in-python-cc159b44063d - pandas importing csv

