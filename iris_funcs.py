# This will contain the functions to be used in the analysis program
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

heading=["sepal-length","sepal-width","petal-length","petal-width","Species"]
Data = pd.read_csv('iris.data',names = heading)
 

sns.distplot( Data["sepal-length"] , color="blue", label="Sepal Length")
sns.distplot( Data["sepal-width"] , color="red", label="Sepal Width")
#sns.distplot( Data["petal-length"] , color="green", label="Petal Length")
#sns.distplot( Data["petal-width"] , color="orange", label="Petal Width")
plt.show()

sns.pairplot(Data,hue="Species")
#plt.title("Plot of species vairables")
plt.show()



def IrSums(Spec_name):
    Irflowr = Data[Data.Species == Spec_name]
   # print("Summary of {} flower\n".format(Spec_name),Irflowr.describe(),"\n")
    with open ('summary.csv', 'w') as f:
        print(Irflowr.describe(),file=f)
    
def IrHist(Spec_name1): 
    import matplotlib.pyplot as plt
    Irflowr = Data[Data.Species == Spec_name1]
    Irflowr.hist()
    plt.title("Histogram of Sepal width&length & Petal width&length for {} Flower".format(Spec_name1))
    plt.show()

