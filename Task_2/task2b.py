import cv2

yellow_min = (37,136,204)
yellow_max = (100,227,255)

img = cv2.imread('/Users/mahadevanaiduparimi/Downloads/PYTHON/eYantra/Task_2/yellow_detect.jpeg')
mask = cv2.inRange(img, yellow_min, yellow_max)
mask_contours, order = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) 
   
if len(mask_contours) != 0:
    for mask_contour in mask_contours:
        x, y, w, h = cv2.boundingRect(mask_contour)

print(int(x+w/2), int(y+h/2))
