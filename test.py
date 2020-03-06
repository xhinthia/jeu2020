import os
import sys
import os.path

liste2 = []
with open("specialisation_selection.txt","r") as f_read:
	for line in f_read:
		line=line.strip()
		liste2.append(line)
f_read.close()
input()
