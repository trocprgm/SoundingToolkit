import cv2 as cv

testimg = cv.imread('testImage.jpg')
#cv.imshow('image',testimg)
#cv.waitKey(0)

def rescaleFrame(frame, scale):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


resize = rescaleFrame(testimg, 0.25)

canny = cv.Canny(resize, 150, 175)


cv.imshow('image', canny)
cv.waitKey(0)


