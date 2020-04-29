# This will contain the functions to be used in the analysis program
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

heading=["sepal-length","sepal-width","petal-length","petal-width","Species"]
Data = pd.read_csv('IRIS.csv',names = heading)


def IrSums():
    with open('summary.txt', 'w') as f:
        print("Summary of Iris Setosa flower data\n",Data[Data.Species == "Iris-setosa"].describe(),"\n",file = f)
        print("Summary of Iris versicolor flower data\n",Data[Data.Species == "Iris-versicolor"].describe(),"\n",file = f)
        print("Summary of Iris virginica flower data\n",Data[Data.Species == "Iris-virginica"].describe(),"\n",file = f)
        print("Check for missing data", Data.isnull().sum(), sep="\n")   


def IrHist(Flwrtyp1): 
    sns.set(font_scale=1.25)
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
    sns.set()
    sns.pairplot(Data,hue=heading[4],aspect=2)
    plt.suptitle("Scatterplot of all possible combinations of Variables")
    plt.savefig("Scatterplot of variables.png")
    plt.clf
    plt.show()

def Vioplots(Flwrtyp2):
    sns.set(font_scale=1.25)
    plt.subplot(2,2,1)
    sns.violinplot(heading[4], y = 'sepal-length', data=Data)
    plt.subplot(2,2,2)
    sns.violinplot(heading[4], y = 'sepal-width', data=Data)
    plt.subplot(2,2,3)
    sns.violinplot(heading[4], y = 'petal-length', data=Data)
    plt.subplot(2,2,4)
    sns.violinplot(heading[4], y = 'petal-width', data=Data)
    plt.suptitle("Violin Plot of {} by Species type ".format(Flwrtyp2))
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

#print("Correlation of Iris Setosa flower data\n",Data[Data.Species == "Iris-setosa"].corr())
#print("Correlation of Iris versicolor flower data\n",Data[Data.Species == "Iris-versicolor"].corr())
#print("Correlation of Iris virginica flower data\n",Data[Data.Species == "Iris-virginica"].corr())
#print(Data.corr())