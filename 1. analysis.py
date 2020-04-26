## Colm Higgins
## program to analyse data for project
import iris_funcs as ifs

ifs.IrSums()

def Createhist():
  ifs.IrHist("sepal-length")
  ifs.IrHist("sepal-width")
  ifs.IrHist("petal-length")
  ifs.IrHist("petal-width")
Createhist()


