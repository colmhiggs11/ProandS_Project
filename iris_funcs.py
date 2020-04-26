# This will contain the functions to be used in the analysis program
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

heading=["sepal-length","sepal-width","petal-length","petal-width","Species"]
Data = pd.read_csv('iris.data',names = heading)
 
sns.pairplot(Data,hue="Species")
#plt.title("Plot of species vairables")
#plt.show()

def IrSums():
    #Irflowr = Data[Data.Species == Spec_name]
    #Irflowr.describe()
    #print(Data[Data.Species == "Iris-setosa"].describe(),file = f)
    #Vers_Sum = print(Data[Data.Species == "Iris-versicolor"].describe())
    #Virg_Sum = print(Data[Data.Species == "Iris-virginica"].describe())
    with open('summary.csv', 'w') as f:
        print("Summary of Iris Setosa flower data\n",Data[Data.Species == "Iris-setosa"].describe(),"\n",file = f)
       # print("#Summary of Iris versicolor flower data\n",Data[Data.Species == "Iris-versicolor"].describe(),"\n",file = f)
       # print("#Summary of Iris virginica flower data\n",Data[Data.Species == "Iris-virginica"].describe(),"\n",file = f)
        #print(Data[Data.Species == "Iris-versicolor"].describe(),file = f)
        #print(Data[Data.Species == "Iris-virginica"].describe(),file = f)
        #print("Summary of {} flower\n".format(Spec_name),Irflowr.describe(),file = f)
       # f.write(Seto_Sum,file = f)
    #print(Irflowr.describe())

#def IrHist(Spec_name1): 
    #import matplotlib.pyplot as plt
    #Irflowr = Data[Data.Species == Spec_name1]
    #Irflowr.hist()
    #plt.title("Histogram of Sepal width&length & Petal width&length for {} Flower".format(Spec_name1))
