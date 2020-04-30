# #Colm Higgins Iris Data Project
## program to analyse data for project

# Import functions and variables from iris_functs.py
import iris_functs as ifs
from iris_functs import heading,Data

# Call the functions and where necessary pass arguements for multiple functions
ifs.IrSums()

def Emprule():
  ifs.StdEmprule("Iris-setosa")
  ifs.StdEmprule("Iris-versicolor")
  ifs.StdEmprule("Iris-virginica")
Emprule()

ifs.Sctrplt()

ifs.Ir_Corrls()


def Createhist():
  ifs.IrHist(heading[0])
  ifs.IrHist(heading[1])
  ifs.IrHist(heading[2])
  ifs.IrHist(heading[3])
Createhist()

def CreateVioplot():
  ifs.Vioplots(heading[0:4])
CreateVioplot()
