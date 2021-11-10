import pytesseract
import cv2 as cv

class getNumbers():

	def get_numbers(self, images):

		image_numbers = []
		valid = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '']

		for key,value in images.items():
			numbers = []

			for img in value:

				#img = cv.resize(img, (0,0), fx=1, fy=1)

				#Use the tesseract OCR to recognize each digit in each image
				digit = pytesseract.image_to_string(img,config='--psm 10')

				#print(digit)
				#cv.imshow("test", img)
				#cv.waitKey(0)

				#Remove noise
				for ch in digit:
					if ch not in "1234567890":
						digit = digit.replace(ch, "")

				if(len(digit) > 1):
					digit = digit[1:]

				#Store the digits in images_numbers, if there is no digit in image store "*"

				if digit == "":
					#print("*")
					numbers.append("*")
				else:
					#print(digit)
					numbers.append(digit)

			image_numbers.append(numbers)

		return(image_numbers)