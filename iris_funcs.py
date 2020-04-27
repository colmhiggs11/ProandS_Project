# This will contain the functions to be used in the analysis program
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

heading=["sepal-length","sepal-width","petal-length","petal-width","Species"]
Data = pd.read_csv('IRIS.csv',names = heading)
print(Data.isnull().sum())

def IrSums():
    with open('summary.txt', 'w') as f:
        print("Summary of Iris Setosa flower data\n",Data[Data.Species == "Iris-setosa"].describe(),"\n",file = f)
        print("Summary of Iris versicolor flower data\n",Data[Data.Species == "Iris-versicolor"].describe(),"\n",file = f)
        print("Summary of Iris virginica flower data\n",Data[Data.Species == "Iris-virginica"].describe(),"\n",file = f)    

def IrHist(Flwrtyp1): 
    sns.set()
    x = sns.FacetGrid(Data,hue = heading[4],height=10 , aspect=2)
    x.map(sns.distplot, Flwrtyp1, bins=25, kde=False)
    plt.ylabel("Frequency")
    plt.legend()
    plt.title("{} Histogram plot".format(Flwrtyp1))
    plt.tight_layout()
    plt.savefig("{}.png".format(Flwrtyp1))
    plt.clf
    plt.show()

def Sctrplt():
    sns.pairplot(Data,hue=heading[4],aspect=2)
    plt.savefig("Scatterplot of variables.png")
    plt.clf
    plt.show()

#def Vioplots(Flwrtyp2):
sns.set()
plt.subplot(2,2,1)
sns.violinplot(heading[4], y = 'sepal-length', data=Data)
plt.subplot(2,2,2)
sns.violinplot(heading[4], y = 'sepal-width', data=Data)
plt.subplot(2,2,3)
sns.violinplot(heading[4], y = 'petal-length', data=Data)
plt.subplot(2,2,4)
sns.violinplot(heading[4], y = 'petal-width', data=Data)
#plt.title("{} Violin Plot".format(Flwrtyp2))
#plt.savefig("Violin plot of variables.png")
plt.show()

#print("Correlation of Iris Setosa flower data\n",Data[Data.Species == "Iris-setosa"].corr())
#print("Correlation of Iris versicolor flower data\n",Data[Data.Species == "Iris-versicolor"].corr())
#print("Correlation of Iris virginica flower data\n",Data[Data.Species == "Iris-virginica"].corr())
#print(Data.corr())

corr = Data.corr()
sns.heatmap(corr, annot = True,linewidths=2.5,vmin=-1,cmap="coolwarm_r" )
plt.tight_layout()
plt.show()
