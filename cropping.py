import cv2 as cv
import numpy as np
import math

class cropping():

	def crop_image(self):

		img = cv.imread('Test2.png')
		img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
		img_canny = cv.Canny(img_gray, 30, 200)
		contours, hierarchy = cv.findContours(img_canny, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)

		peri = cv.arcLength(contours[0], True) #Gets the perimeter of the contour.
		approx = cv.approxPolyDP(contours[0], 0.02*peri, True) #Get the corner points

		puzzle = img_gray[approx[0][0][1]:approx[1][0][1], approx[1][0][0]:approx[2][0][0]].copy()

		h = puzzle.shape[0]
		w = puzzle.shape[1]

		side = round((h + w)/2)
		increment = math.ceil(side/9)

		images = {}		
		count = 1

		for y in range(0,side,increment):
			for x in range(2,side,increment):
				box = puzzle[y:y+increment, x:x+increment].copy()
				box = cv.resize(box, None, fx=3, fy=3, interpolation=cv.INTER_CUBIC)
				kernel = np.ones((1, 1), np.uint8)
				#box = cv.dilate(box, kernel, iterations=2)
				#box = cv.erode(box, kernel, iterations=1)
				#box = cv.threshold(cv.medianBlur(box, 3), 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)[1]
				#box = cv.threshold(cv.bilateralFilter(box, 5, 75, 75), 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)[1]
				box = cv.adaptiveThreshold(cv.bilateralFilter(box, 9, 75, 75), 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 31, 2)
				#box = cv.GaussianBlur(box, (3, 3), 0)
				box = box[15:box.shape[1]-3, 5:box.shape[0]-13].copy()

				if(count == 9):
					box = box[0:box.shape[1]-10, 0:box.shape[0]].copy()

				if(("Row " + str(count)) not in images):
					images[("Row " + str(count))] = [box]
				else:
					images[("Row " + str(count))].append(box)
			count += 1
		
		return(images)