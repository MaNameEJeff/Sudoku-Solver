class smallBox:

	def __init__(self, location, digits):
		self._location = location
		self.setdigits(digits)

	def setdigits(self, digits):
		l = []
		count = 0

		while(count < 10):
			l.append(digits[count:(count+3)])
			count += 3

		l.pop()
		self.digits = l


	def is_in(self, number):
		for row in self.digits:
			if number in row:
				return True

		return False