# This will contain the functions to be used in the analysis program
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

heading=["sepal-length","sepal-width","petal-length","petal-width","Species"]
Data = pd.read_csv('IRIS.csv',names = heading)


def IrSums():
    with open('summary.txt', 'w') as f:
        print("Summary of Iris Setosa flower data\n",Data[Data.Species == "Iris-setosa"].describe(),"\n",file = f)
        print("Summary of Iris Versicolor flower data\n",Data[Data.Species == "Iris-versicolor"].describe(),"\n",file = f)
        print("Summary of Iris Virginica flower data\n",Data[Data.Species == "Iris-virginica"].describe(),"\n",file = f)
        print(Data.isnull().sum())   


def IrHist(Mestyp1): 
    sns.set(font_scale=1.25)
    x = sns.FacetGrid(Data,hue = heading[4],height=10 , aspect=2)
    x.map(sns.distplot, Mestyp1, bins=25, kde=False)
    plt.ylabel("Frequency")
    plt.legend()
    plt.title("{} Histogram plot".format(Mestyp1))
    plt.tight_layout()
    plt.savefig("{}.png".format(Mestyp1))
    plt.clf
    plt.show()

def Sctrplt():
    sns.set()
    sns.pairplot(Data,hue=heading[4],aspect=2)
    plt.suptitle("Scatterplot of all possible combinations of Variables")
    plt.savefig("Scatterplot of variables.png")
    plt.clf
    plt.show()

def Vioplots(Mestyp2):
    sns.set(font_scale=1.25)
    plt.subplot(2,2,1)
    sns.violinplot(heading[4], heading[0], data=Data)
    plt.subplot(2,2,2)
    sns.violinplot(heading[4], heading[1], data=Data)
    plt.subplot(2,2,3)
    sns.violinplot(heading[4], heading[2], data=Data)
    plt.subplot(2,2,4)
    sns.violinplot(heading[4], heading[3], data=Data)
    plt.suptitle("Violin Plot of {} by Species type ".format(Mestyp2))
    plt.show()

def Ir_Corrls():
    Iriscorrel = Data.corr()
    sns.set(font_scale=1.1)
    ax=sns.heatmap(Iriscorrel, annot = True,linewidths=2.5,vmin=-1.1,
                    cmap="coolwarm_r",cbar_kws={'fraction' : 0.01})
    ax.set_ylim(len(Iriscorrel)+0.5, -0.5)
    plt.yticks(rotation=0)
    plt.tight_layout()
    sns.set(font_scale=1.5)
    plt.title("Correlation between Measurement Variables of Iris Dataset")
    plt.show()

def StdEmprule(Mestyp3):
    D1 = (Data[Data.Species == Mestyp3].std())
    D2 = (Data[Data.Species == Mestyp3].mean())
    Empheadings = ["68%" "-std","68%" "+std","95%" "-std","95%" "+std","99.7%" "-std","99.7%" "+std"]
   

    EmpirRule = (np.array(D2[:4])-np.array(D1[:4]),np.array(D2[:4])+np.array(D1[:4])
            ,np.array(D2[:4])-(np.array(D1[:4]))*2,np.array(D2[:4])+(np.array(D1[:4])*2)
            ,np.array(D2[:4])-(np.array(D1[:4]))*3,np.array(D2[:4])+(np.array(D1[:4])*3))

    Data121 = pd.DataFrame(EmpirRule,columns=heading[:4], index =Empheadings )

    print("Empirical rule data for {}\n".format(Mestyp3),Data121.transpose())

#print("Correlation of Iris Setosa flower data\n",Data[Data.Species == "Iris-setosa"].corr())
#print("Correlation of Iris versicolor flower data\n",Data[Data.Species == "Iris-versicolor"].corr())
#print("Correlation of Iris virginica flower data\n",Data[Data.Species == "Iris-virginica"].corr())
#print(Data.corr())

