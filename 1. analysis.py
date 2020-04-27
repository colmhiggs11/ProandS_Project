## Colm Higgins
## program to analyse data for project
import iris_funcs as ifs
from iris_funcs import heading

#ifs.IrSums()
#ifs.Sctrplt()

#def Createhist():
 # ifs.IrHist(heading[0])
 # ifs.IrHist(heading[1])
 # ifs.IrHist(heading[2])
  #ifs.IrHist(heading[3])
#Createhist()

def CreateVioplot():
  ifs.Vioplots(heading[0])
  ifs.Vioplots(heading[1])
  ifs.Vioplots(heading[2])
  ifs.Vioplots(heading[3])
CreateVioplot()
