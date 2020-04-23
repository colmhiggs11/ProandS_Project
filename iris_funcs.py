# This will contain the functions to be used in the analysis program

def IrSums(Spec_name):
    import pandas as pd
    import matplotlib.pyplot as plt
    import numpy as np

    heading=["sepal-length","sepal-width","petal-length","petal-width","Species"]
    Data = pd.read_csv('iris.data',names = heading)
    print("Minimum Values for {}\n",Data[Data.Species == Spec_name].min())
    print("Maximum Values for {}\n",Data[Data.Species == Spec_name].max())
    print("Standard Deviation Values for {}\n",Data[Data.Species == Spec_name].std())
   

IrSums("Iris-setosa")
IrSums("Iris-versicolor")
IrSums("Iris-virginica")
    #print(Data)
    #print(Data.describe())
    #fig,ax = plt.subplots()
    #MeanValues = Data.groupby(['Species']).mean()
    #StdValues = Data.groupby(['Species']).std()
    #minValues = Data.groupby(['Species']).min()
    #maxValues = Data.groupby(['Species']).max()
    #print(MeanValues)
    #print(StdValues)
    #print(minValues)
    #print(maxValues)
    #ax.plot()
    #ax.legend()
    #fig.show()
    #input()