import math
from smallBox import smallBox
from getNumbers import getNumbers

ocr = getNumbers()
grid = ocr.get_numbers()

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
grid = []
not_completed = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

for key, value in grid_rows.items():
	grid.append(value)

def make_small_boxes():	

	for row in range(1, 10):
		arg1 = math.ceil(row/3)

		for column in range(1, 10):

			arg2 = math.ceil(column/3)
			args = str(arg1) + str(arg2)
			small_boxes_numbers[args].append(grid[row-1][column-1])

	for k, v in small_boxes_numbers.items():
		small_boxes[k] = smallBox(k, v)

def show_solution():
	for loc, box in small_boxes.items():
		print(loc)
		print(box.digits)
		print()

def solve_puzzle(digit):

	unfilled_boxes = []

	number_in = {
		"11": small_boxes["11"].has(digit),
		"12": small_boxes["12"].has(digit),
		"13": small_boxes["13"].has(digit),
		"21": small_boxes["21"].has(digit),
		"22": small_boxes["22"].has(digit),
		"23": small_boxes["23"].has(digit),
		"31": small_boxes["31"].has(digit),
		"32": small_boxes["32"].has(digit),
		"33": small_boxes["33"].has(digit)
	}

	for location, value in number_in.items():
		if(value == False):
			unfilled_boxes.append(small_boxes[location])

	if(len(unfilled_boxes) == 0):
		not_completed.remove(str(digit))
		return

	for box in unfilled_boxes:
		slots = box.get_empty()
		row_col_of_box = [int(box.location[0]), int(box.location[1])]

		#Check columns
		boxes_to_check_y = []
		
		y = row_col_of_box[0] - 1
		while(y > 0):
			boxes_to_check_y.append(small_boxes[str(y) + str(row_col_of_box[1])])
			y -= 1

		y = row_col_of_box[0] + 1
		while(y < 4):
			if(small_boxes[str(y) + str(row_col_of_box[1])] not in boxes_to_check_y):
				boxes_to_check_y.append(small_boxes[str(y) + str(row_col_of_box[1])])
			y += 1

		#Check rows
		boxes_to_check_x = []

		x = row_col_of_box[1] - 1
		while(x > 0):
			boxes_to_check_x.append(small_boxes[str(row_col_of_box[0]) + str(x)])
			x -= 1

		x = row_col_of_box[1] + 1
		while(x < 4):
			boxes_to_check_x.append(small_boxes[str(row_col_of_box[0]) + str(x)])
			x += 1

		viable_slots_1 = []
		viable_slots_2 = []
		viable_slots = []

		for x_box in boxes_to_check_x:
			l = []
			for loc in slots:
				if(digit not in x_box.digits[loc[0]]):
					l.append(loc)

			viable_slots_1.append(l)

		for y_box in boxes_to_check_y:
			l = []
			for loc in slots:
				if(digit not in y_box.get_columns()[loc[1]]):
					l.append(loc)

			viable_slots_2.append(l)

		if(len(viable_slots_1) != 1):
			viable_slots_1 = list(set(viable_slots_1[0]) & set(viable_slots_1[1]))
		else:
			viable_slots_1 = viable_slots_1[0]

		if(len(viable_slots_2) != 1):
			viable_slots_2 = list(set(viable_slots_2[0]) & set(viable_slots_2[1]))
		else:
			viable_slots_2 = viable_slots_2[0]

		viable_slots = list(set(viable_slots_1) & set(viable_slots_2))

		if(len(viable_slots) == 1):
			box.update(viable_slots[0], digit)

if __name__ == '__main__':
	make_small_boxes()

	while(len(not_completed) != 0):
		for i in not_completed:
			solve_puzzle(i)


	show_solution()