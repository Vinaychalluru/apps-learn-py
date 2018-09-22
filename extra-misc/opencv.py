import cv2
# opencv is referred as cv2 in Python
# In the case of color images, the decoded images will have the channels stored in **B G R** order.

img_g1 = cv2.imread('../assets/sample-gray-5x3.png',0)
print(img_g1)

img_g2 = cv2.imread('../assets/sample-gray-5x3.png',1)
print(img_g2)

print("  --  Observe the output differences between a gray scale image and a color image  --  ")
img_c1 = cv2.imread('../assets/sample-color-bar-50x10.png',0)
print(img_c1[0])
print(img_c1[9])

# Passing 1 would print the B G R values rather than a single value as printed when 0 is passed
img_c2 = cv2.imread('../assets/sample-color-bar-50x10.png',1)
# print(img_c2[0]) # This would print 50 lists * 10 rows each with  B G R representation of a pixel of the image 
print(img_c2[0:9,0:1])

cv2.imwrite('../assets/sample-gray-out-5x3.png',img_g1)
