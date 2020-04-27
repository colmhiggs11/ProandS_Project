# This will contain the functions to be used in the analysis program
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

heading=["sepal-length","sepal-width","petal-length","petal-width","Species"]
Data = pd.read_csv('IRIS.csv',names = heading)
 
def IrSums():
    with open('summary.txt', 'w') as f:
        print("Summary of Iris Setosa flower data\n",Data[Data.Species == "Iris-setosa"].describe(),"\n",file = f)
        print("Summary of Iris versicolor flower data\n",Data[Data.Species == "Iris-versicolor"].describe(),"\n",file = f)
        print("Summary of Iris virginica flower data\n",Data[Data.Species == "Iris-virginica"].describe(),"\n",file = f)    

def IrHist(Measurement): 
    sns.set()
    x = sns.FacetGrid(Data,hue = "Species",height=10 , aspect=2)
    x.map(sns.distplot, Measurement, bins=25, kde=False)
    plt.ylabel("Frequency")
    plt.legend()
    plt.title("{} Histogram plot".format(Measurement))
    plt.tight_layout()
    plt.savefig("{}.png".format(Measurement))
    plt.clf
    plt.show()


def Sctrplt():
    sns.pairplot(Data,hue="Species",aspect=2)
    plt.savefig("Scatterplot of variables.png")
    plt.clf
    #plt.title("Plot of species vairables")
    plt.show()

#print(Data.groupby('Species').count())

#x = np.linspace(1.0,5,149)
#Data.groupby('sepal-length')
#fig, ax =plt.subplots()
##ax.plot(x,Data)
#fig.show()
#input()

#Data[Data.Species == "Iris-versicolor"].hist()
#plt.title("Histogram of Sepal width&length & Petal width&length for {} Flower".format(Spec_name1))
#plt.savefig("CH")
#plt.show()