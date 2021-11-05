import pytesseract
import cv2 as cv

class getNumbers():

	def main():

		#This part needs to be sent by another program
		grid = {"Row 1": [cv.imread('row1 square1.png'), cv.imread('row1 square2.png')], "Row 2": [cv.imread('row2 square1.png'), cv.imread('row2 square2.png')]}
		grid_numbers = {}

		for k,v in grid.items():
			numbers = []

			for i in v:

				#Use the tesseract OCR to recognize each digit in each image and remove the form feed and new line characters
				y = pytesseract.image_to_string(i,config='--psm 10')

				#Remove noise
				for ch in y:
					if ch not in "1234567890":
						y = y.replace(ch, "")

				#Store the digits in grid_numbers, if there is no digit in image store "*"
				if y == "":
					numbers.append("*")
				else:
					numbers.append(y)

			grid_numbers[k] = numbers

		print(grid_numbers)

	if __name__ == '__main__':
		main()