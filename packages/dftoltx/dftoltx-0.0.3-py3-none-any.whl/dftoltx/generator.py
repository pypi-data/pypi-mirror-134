import pandas as pd 
# add more imports here

def convert_to_tex(df):
	columns = df.columns

	try:
		title = df.name
	except AttributeError:
		title = "Placeholder"

	col_len = len(columns)
	# initialize header information

	output_str = ""
	output_str += "\\begin{table}[H]\n"
	# start table code

	output_str += "\t\\begin{center}\n"
	# create a centered table style
	# TODO(aakamishra) change style for future

	output_str += "\t \\begin{{tabular}}{{|{}|}} \\hline\n".format(("c "*col_len)[:-1])
	# allocate space for columns in table

	output_str += "\t \\textbf{{ {} }} {}\\\\ [0.5ex]\n\t \\hline\n\t \\hline\n".format(title, ("& "*col_len)[:-2])
	# add title to table and line buffe\hline\hliner

	output_str += "\t {} \\\\ [0.5ex]\n\t \\hline\\hline\n".format(" & ".join(str(col) for col in columns))
	# add column names to table

	for row in df.iterrows():
		output_str += "\t {} \\\\\n\t \\hline\n".format(" & ".join(str(row[1][col]) for col in columns))
	# add table data

	output_str += "\t\\end{tabular}\n\t\\end{center}\n"
	# end tab spacing and centering of table

	output_str += "\t\\caption{placeholder}\n\t\\label{tab:placeholder}\n"
	# add placeholder caption and label

	output_str += "\\end{table}"

	return output_str