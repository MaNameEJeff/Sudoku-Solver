import math
from smallBox import smallBox

global box

grid_rows = {
	'Row 1': ['*', '*', '*', '5', '8', '9', '*', '*', '*'],
	'Row 2': ['*', '*', '9', '*', '3', '6', '*', '*', '4'],
	'Row 3': ['*', '5', '8', '4', '1', '*', '*', '*', '*'],
	'Row 4': ['4', '7', '*', '*', '*', '*', '*', '2', '9'],
	'Row 5': ['3', '*', '*', '*', '*', '*', '*', '*', '5'],
	'Row 6': ['5', '9', '*', '*', '*', '*', '*', '1', '7'],
	'Row 7': ['*', '*', '*', '*', '5', '7', '2', '4', '*'],
	'Row 8': ['8', '*', '*', '6', '9', '*', '7', '*', '*'],
	'Row 9': ['*', '*', '*', '3', '2', '8', '*', '*', '*']
}

small_boxes_numbers = {
	"11": [],
	"12": [],
	"13": [],
	"21": [],
	"22": [],
	"23": [],
	"31": [],
	"32": [],
	"33": [],
}

small_boxes = {}

def make_small_boxes():	

	for row in range(1, 10):
		arg1 = math.ceil(row/3)

		for column in range(1, 10):

			arg2 = math.ceil(column/3)
			args = str(arg1) + str(arg2)
			small_boxes_numbers[args].append(grid[row-1][column-1])

	for k, v in small_boxes_numbers.items():
		small_boxes[k] = smallBox(k, v)

if __name__ == '__main__':
	make_small_boxes()