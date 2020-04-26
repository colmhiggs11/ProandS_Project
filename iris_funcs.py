# This will contain the functions to be used in the analysis program
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

heading=["sepal-length","sepal-width","petal-length","petal-width","Species"]
Data = pd.read_csv('IRIS.csv',header =0,names = heading)
 
def IrSums():
    Data[Data.Species == "Iris-setosa"].describe().to_csv("Colm.csv")
    Data[Data.Species == "Iris-versicolor"].describe().to_csv("Colm.csv")
    Data[Data.Species == "Iris-virginica"].describe().to_csv("Colm.csv")

   # with open('summary.txt', 'w') as f:
      #  print("Summary of Iris Setosa flower data\n",Data[Data.Species == "Iris-setosa"].describe(),"\n",file = f)
      #  print("Summary of Iris versicolor flower data\n",Data[Data.Species == "Iris-versicolor"].describe(),"\n",file = f)
       # print("Summary of Iris virginica flower data\n",Data[Data.Species == "Iris-virginica"].describe(),"\n",file = f)    

#def IrHist(Spec_name1): 
    #import matplotlib.pyplot as plt
    #Irflowr = Data[Data.Species == Spec_name1]
    #Irflowr.hist()
    #plt.title("Histogram of Sepal width&length & Petal width&length for {} Flower".format(Spec_name1))

sns.pairplot(Data,hue="Species")
#plt.title("Plot of species vairables")
plt.show()