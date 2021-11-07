import cv2 as cv
import numpy as np

class cropping():

	def crop_image(self):

		img = cv.imread('Original.png')
		h = img.shape[0]
		w = img.shape[1]
		
		images = {}
		
		count = 1
		for y in range(0,225,25):
			for x in range(0,225,25):
				box = img[y:y+25, x:x+25].copy()
				box = cv.cvtColor(box, cv.COLOR_BGR2GRAY)
				box = cv.GaussianBlur(box, (5, 5), 0.5)
	
				if(("Row " + str(count)) not in images):
					images[("Row " + str(count))] = [box]
				else:
					images[("Row " + str(count))].append(box)
			count += 1
		
		return(images)