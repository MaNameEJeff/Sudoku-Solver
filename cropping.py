import cv2 as cv
import numpy as np
import math

class cropping():

	def crop_image(self):

		img = cv.imread('Test2.png')
		img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
		img_canny = cv.Canny(img_gray, 30, 200)
		contours, hierarchy = cv.findContours(img_canny, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
		cv.drawContours(img, contours, -1, (0, 255, 0), 1)

		peri = cv.arcLength(contours[0], True) #Gets the perimeter of the contour.
		approx = cv.approxPolyDP(contours[0], 0.02*peri, True) #Get the corner points

		puzzle = img[approx[0][0][1]:approx[1][0][1], approx[1][0][0]:approx[2][0][0]].copy()

		h = puzzle.shape[0]
		w = puzzle.shape[1]

		#cv.imshow("puzzle", puzzle)
		#cv.waitKey(0)

		side = round((h + w)/2)
		increment = math.ceil(side/9)

		images = {}
		
		count = 1
		for y in range(0,side,increment):
			for x in range(0,side,increment):
				box = puzzle[y:y+increment, x:x+increment].copy()
				box = cv.cvtColor(box, cv.COLOR_BGR2GRAY)
				box = cv.GaussianBlur(box, (5, 5), 1)

				cv.imshow(str(count), box)
				cv.waitKey(0)

				if(("Row " + str(count)) not in images):
					images[("Row " + str(count))] = [box]
				else:
					images[("Row " + str(count))].append(box)
			count += 1
		
		return(images)

	if __name__ == '__main__':
		crop_image("Test")