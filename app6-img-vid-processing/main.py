# opencv-python library for img and video processing
import cv2

# grayscale 0 as second option or 1 if black & white, -1 colored
img = cv2.imread("galaxy.jpg", 0)


print(type(img))
print(img)
print(img.shape)  # how many pixel / resolution
print(img.ndim)  # how many dimension

# resize img
resized_image = cv2.resize(
    img, (int(img.shape[1]/2), int(img.shape[0]/2)))  # tuple img size x by y

# display on screen

cv2.imshow("Galaxy", resized_image)
cv2.imwrite("Galaxy_resized.jpg", resized_image)  # save the resized image
cv2.waitKey(0)  # 0 close window any button, 2000 time in ms
cv2.destroyAllWindows()
