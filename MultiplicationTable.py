def MultiplicationTable(n):
  # Given an integer n
  # Generate the corresponding LaTeX table printing the multiplication table mod n
  # Texts are properly aligned
  prefix = "\\begin{table}\n    \\centering\n    \\begin{tabular}{c|" + "c" * n + "}\n"
  postfix = "\n    \\end{tabular}\n    \\caption{Multiplication table (mod " + str(n) + ")}\n    \\label{tab:mult_table_" + str(n) + "}\n\\end{table}\n"
  name = f"$\\times_{n}$"
  n_digits = len(str(n))
  first_col_just = max(len(name), n_digits)
  tableStrs = []
  for i in range(n+1):
    rowStrs = []
    for j in range(n+1):
      if (i == j == 0):
        rowStrs.append(name.rjust(first_col_just))
      elif (i == 0):
        rowStrs.append(str(j-1).rjust(n_digits))
      elif (j == 0):
        rowStrs.append(str(i-1).rjust(first_col_just))
      else:
        mod = ((i-1)*(j-1)) % n
        rowStrs.append(str(mod).rjust(n_digits))
    tableStrs.append(" & ".join(rowStrs))
    if (i == 0):
      tableStrs.append("\\hline")
  tableStr = "\\\\\n".join(tableStrs)
  tableStr.replace("hline\\\\", "hline")
  result = prefix + tableStr + postfix
  print(result)
