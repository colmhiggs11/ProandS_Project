## Colm Higgins
## program to analyse data for project
import iris_funcs as ifs

def CreateSum():
    ifs.IrSums("Iris-setosa")
    ifs.IrSums("Iris-versicolor")
    ifs.IrSums("Iris-virginica")
#CreateSum()

def Createhist():
    ifs.IrHist("Iris-setosa")
    ifs.IrHist("Iris-versicolor")
    ifs.IrHist("Iris-virginica")
Createhist()
#with open ('summary.txt', 'w') as f:
  #  f.write(CreateSum(),file=f)


