## Colm Higgins
## program to analyse data for project
import iris_functs as ifs
from iris_functs import heading,Data

#ifs.IrSums()

def Emprule():
  ifs.StdEmprule("Iris-setosa")
  ifs.StdEmprule("Iris-versicolor")
  ifs.StdEmprule("Iris-virginica")
#Emprule()

#ifs.Sctrplt()

ifs.Ir_Corrls()


def Createhist():
  ifs.IrHist(heading[0])
  ifs.IrHist(heading[1])
  ifs.IrHist(heading[2])
  ifs.IrHist(heading[3])
#Createhist()

def CreateVioplot():
  ifs.Vioplots(heading[0:4])
CreateVioplot()
