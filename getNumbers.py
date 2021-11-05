import pytesseract
import cv2 as cv

class getNumbers():

	def main():

		#This part needs to be sent by another program
		grid = {
			"Row 1": [cv.imread('row1 square1.png'), cv.imread('row1 square2.png')],
			"Row 2": [cv.imread('row2 square1.png'), cv.imread('row2 square2.png')]
		}

		grid_numbers = {}

		for key,value in grid.items():
			numbers = []

			for img in value:

				#Use the tesseract OCR to recognize each digit in each image
				digit = pytesseract.image_to_string(img,config='--psm 10')

				#Remove noise
				for ch in digit:
					if ch not in "1234567890":
						digit = digit.replace(ch, "")

				#Store the digits in grid_numbers, if there is no digit in image store "*"
				if digit == "":
					numbers.append("*")
				else:
					numbers.append(digit)

			grid_numbers[key] = numbers

		print(grid_numbers)

	if __name__ == '__main__':
		main()