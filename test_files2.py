#!/usr/bin/env python3

import sys
from pathlib import Path

def compare_lines(f1, f2):
	# read the first line from each file
	f1_line = f1.readline()
	f2_line = f2.readline()

	# counter for line number
	count = 0

	while f1_line != '' or f2_line != '':
       	# compare the lines from both file
		if f1_line != f2_line:
			return False

		f1_line = f1.readline()
		f2_line = f2.readline()
		count += 1

	return True

	


def main():
	size_1 = Path(sys.argv[1]).stat().st_size
	size_2 = Path(sys.argv[2]).stat().st_size

	# if sizes differ there is no chance they are equal
	if size_1 != size_2:
		print(False)
		exit

	# open files
	f1 = open(sys.argv[1])
	f2 = open(sys.argv[2])

	# print confirmation
	print('Comparing files ')
	print(' > ' + sys.argv[1]) 
	print(' < ' + sys.argv[2])

	print(compare_lines(f1, f2))

	# close files
	f1.close()
	f2.close()

if __name__ == '__main__':
	main()