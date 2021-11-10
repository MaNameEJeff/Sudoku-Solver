import cv2 as cv
import numpy as np
import math

class cropping():

	def crop_image(self):

		img = cv.imread('Test5.png')
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
				box = cv.resize(box, None, fx=5, fy=5, interpolation=cv.INTER_CUBIC)
				kernel = np.ones((1, 1), np.uint8)
				box = cv.dilate(box, kernel, iterations=2)
				box = cv.erode(box, kernel, iterations=1)
				box = cv.threshold(cv.medianBlur(box, 5), 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)[1]

				height = box.shape[1]
				width = box.shape[0]

				if(count == 9):
					box = box = box[int(height/10):(box.shape[1] - int(height/10)), int(width/10):(box.shape[0]-int(width/10))].copy()
				else:
					box = box[int(height/10):(box.shape[1] - int(height/20)), int(width/10):(box.shape[0]-int(width/10))].copy()

				if(("Row " + str(count)) not in images):
					images[("Row " + str(count))] = [box]
				else:
					images[("Row " + str(count))].append(box)
			count += 1
		
		return(images)