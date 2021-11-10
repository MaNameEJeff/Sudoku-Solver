#Each 3x3 box in the 9x9 puzzle

class smallBox:

	def __init__(self, location, digits):
		#Where it is in the whole puzzle
		self.location = location

		#Set the digits in the 3x3 box
		rows = []
		count = 0

		while(count < 10):
			rows.append(digits[count:(count+3)])
			count += 3

		rows.pop() #The last item will always be [] so remove it from the list of digits in the small box
		self.digits = rows

	#Change the digit at the location to given number
	def update(self, loc, number):
		self.digits[loc[0]][loc[1]] = str(number)

	#Check if the small box has a certain digit or not
	def has(self, number):
		for row in self.digits:
			if number in row:
				return True
		return False

	#Return the digits of the small box in the form of columns instead of rows
	def get_columns(self):

		columns = []

		for i in range(len(self.digits)):
			l = []

			for j in range(len(self.digits[i])):
				l.append(self.digits[j][i])

			columns.append(l)

		return(columns)

	#Check if there are any empty spaces in the small box
	def get_empty(self):

		locations = []
		
		for i in range(len(self.digits)):
			for j in range(len(self.digits[i])):
				if (self.digits[i][j] == "*"):
					locations.append((i, j))

		return(locations)