import cv2 as cv

class showAnswer():

	def display(self, answer):

		answer_image = cv.imread("template.png")
		row = 0

		for y in range(0,225,25):
			column = 0
			for x in range(0,225,25):	
				cv.putText(answer_image, str(answer[row][column]), (x+5, y+20), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)
				column += 1
			row += 1

		cv.imshow("Test", answer_image)
		cv.waitKey(0)
		cv.destroyAllWindows()