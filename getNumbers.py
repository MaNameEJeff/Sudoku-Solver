import easyocr
import cv2 as cv

class getNumbers():

	def get_numbers(self, images):

		reader = easyocr.Reader(['en'])

		image_numbers = []
		valid = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '']

		for key,value in images.items():
			numbers = []

			for img in value:

				#Use the tesseract OCR to recognize each digit in each image
				result = reader.readtext(img)
				if (len(result) == 0):
					digit = ""
				else:
					digit = result[0][1]

				#Remove noise
				for ch in digit:
					if ch not in "1234567890":
						digit = digit.replace(ch, "")

				if(len(digit) > 1):
					digit = digit[1:]

				#Store the digits in images_numbers, if there is no digit in image store "*"

				if digit == "":
					numbers.append("*")
				else:
					numbers.append(digit)

			image_numbers.append(numbers)

		return(image_numbers)