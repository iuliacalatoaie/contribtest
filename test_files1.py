#!/usr/bin/env python3

import filecmp
import sys

# compare files byte by byte
# prints True if equals, False otherwise
def main() :
	# print confirmation
	print('Comparing files ')
	print(' > ' + sys.argv[1]) 
	print(' < ' + sys.argv[2])

	# print result
	print(filecmp.cmp(sys.argv[1], sys.argv[2]))

if __name__ == '__main__':
    main()
