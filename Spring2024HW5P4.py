import numpy as np

def printMatrix(M,n):
  prefix = "\\begin{table}[hp]\n    \\centering\n    \\begin{tabular}{ccccc}\n"
  postfix = "\n    \\end{tabular}\n    \\caption{Table $A^" + str(n) + "$}\n    \\label{tab:table_A_" + str(n) + "}\n\\end{table}\n"
  tableStr = "\\\\\n".join(["        " + " & ".join([str(int(M[i,j])) for j in range(5)]) for i in range(5)])
  print(prefix+tableStr+postfix)

def solution():
  I = np.identity(5)
  A = np.matrix([[0,1,0,0,1],[0,0,1,0,0],[0,0,0,1,1],[0,0,0,0,1],[0,0,0,0,0]])
  printMatrix(A,1)
  printMatrix(A**2,2)
  printMatrix(A**3,3)
  printMatrix(A**4,4)
  printMatrix(A**5,5)
  printMatrix(I+A+A**2+A**3+A**4+A**5,6)
