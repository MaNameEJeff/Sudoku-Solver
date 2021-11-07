class smallBox:

	def __init__(self, location, digits):
		self.location = location
		self.setdigits(digits)

	def setdigits(self, digits):
		l = []
		count = 0

		while(count < 10):
			l.append(digits[count:(count+3)])
			count += 3

		l.pop()
		self.digits = l

	def update(self, loc, number):
		self.digits[loc[0]][loc[1]] = str(number)

	def has(self, number):
		for row in self.digits:
			if number in row:
				return True

		return False

	def get_columns(self):

		columns = []

		for i in range(len(self.digits)):
			l = []

			for j in range(len(self.digits[i])):
				l.append(self.digits[j][i])

			columns.append(l)

		return(columns)

	def get_empty(self):

		locations = []
		
		for i in range(len(self.digits)):
			for j in range(len(self.digits[i])):
				if (self.digits[i][j] == "*"):
					locations.append((i, j))

		return(locations)