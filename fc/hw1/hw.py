import random

hw = open('tex/hw.tex', 'w')
solved = open('tex/solved.tex', 'w')

MAX_EXERCISES = 6
MAX_INT = 255

def writef(towrite, solution=""):
	hw.write(towrite + '\n')
	solved.write(towrite + solution + '\n')

# document start
writef("\documentclass[a4paper,12pt]{article}\n\\usepackage{fancyhdr}\n\pagestyle{fancy}")

writef("\lhead{FC}\n\chead{2019-2020}\n\\rhead{HOMEWORK 1}\\begin{document}")

students = open("students.txt", 'r')
for line in students:
	writef("NAME: " + line + "\\newline\\newline")
	# 1. Convert from DEC to BIN
	writef("1. Convert the following numbers from decimal to binary\n\\begin{itemize}")
	for i in range(MAX_EXERCISES):
		num = random.randint(1,MAX_INT)
		writef("\item $" + str(num) + "_{10}$", "\quad - \quad{0:08b}".format(num))
	writef("\\end{itemize}")

	# 2. Convert from BIN to DEC
	writef("2. Convert the following numbers from binary to decimal \n\\begin{itemize}")
	for i in range(MAX_EXERCISES):
		num = random.randint(1,MAX_INT)
		writef("\item $" + "{0:08b}".format(num) + "_{2}$", "\quad - \quad" + str(num))
	writef("\\end{itemize}")

	# 3. Convert from OCTAL to BIN
	writef("3. Convert the following numbers from octal to binary \n\\begin{itemize}")
	for i in range(MAX_EXERCISES):
		num = random.randint(1,MAX_INT)
		writef("\item $" + "{0:o}".format(num) + "_{8}$", "\quad - \quad" + "{0:08b}".format(num))
	writef("\\end{itemize}\\newpage")

	# 4. Convert from HEX to BIN
	writef("4. Convert the following numbers from hexadecimal to binary \n\\begin{itemize}")

	for i in range(MAX_EXERCISES):
		num = random.randint(1,MAX_INT)
		writef("\item $" + "{0:x}".format(num).upper() + "_{16}$", "\quad - \quad" + "{0:08b}".format(num))
	writef("\\end{itemize}")

	# 5. Convert from BIN to HEX
	writef("5. Convert the following numbers from binary to hexadecimal \n\\begin{itemize}")
	for i in range(MAX_EXERCISES):
		num = random.randint(1,MAX_INT)
		writef("\item $" + "{0:08b}".format(num) + "_{2}$", "\quad - \quad" + " {0:x}".format(num).upper())
	writef("\\end{itemize}\\newpage")

writef("\end{document}")
hw.close()
solved.close()
print("\n--------------------------------\nPython script successful\n--------------------------------\n")
