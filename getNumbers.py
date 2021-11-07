import pytesseract

class getNumbers():

	def get_numbers(self, images):

		image_numbers = []

		for key,value in images.items():
			numbers = []

			for img in value:

				#Use the tesseract OCR to recognize each digit in each image
				digit = pytesseract.image_to_string(img,config='--psm 10')

				#Remove noise
				for ch in digit:
					if ch not in "1234567890":
						digit = digit.replace(ch, "")

				#Store the digits in images_numbers, if there is no digit in image store "*"
				if digit == "":
					numbers.append("*")
				else:
					numbers.append(digit)

			image_numbers.append(numbers)

		return(image_numbers)