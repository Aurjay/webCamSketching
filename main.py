import cv2
print (cv2.__version__)

def x_cord_contour(contour):
    # This function take a contour from findContours
    # it then outputs the x centroid coordinates
    M = cv2.moments(contour)
    print(M)
    return (int(M['m10'] / M['m00']))

def makeSquare(not_square):
    # This function takes an image and makes the dimenions square
    # It adds black pixels as the padding where needed

    BLACK = [0, 0, 0]
    img_dim = not_square.shape
    height = img_dim[0]
    width = img_dim[1]
    # print("Height = ", height, "Width = ", width)
    if (height == width):
        square = not_square
        return square
    else:
        doublesize = cv2.resize(not_square, (2 * width, 2 * height), interpolation=cv2.INTER_CUBIC)
        height = height * 2
        width = width * 2
        # print("New Height = ", height, "New Width = ", width)
        if (height > width):
            pad = int((height - width) / 2)
            # print("Padding = ", pad)
            doublesize_square = cv2.copyMakeBorder(doublesize, 0, 0, pad, pad, cv2.BORDER_CONSTANT, value=BLACK)
        else:
            pad = (width - height) / 2
            # print("Padding = ", pad)
            doublesize_square = cv2.copyMakeBorder(doublesize, pad, pad, 0, 0, \
                                                   cv2.BORDER_CONSTANT, value=BLACK)
    doublesize_square_dim = doublesize_square.shape
    # print("Sq Height = ", doublesize_square_dim[0], "Sq Width = ", doublesize_square_dim[1])
    return doublesize_square

def resize_to_pixel(dimensions, image):
    # This function then re-sizes an image to the specificied dimenions
    buffer_pix = 4
    dimensions = dimensions - buffer_pix
    squared = image
    r = float(dimensions) / squared.shape[1]
    dim = (dimensions, int(squared.shape[0] * r))
    resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
    img_dim2 = resized.shape
    height_r = img_dim2[0]
    width_r = img_dim2[1]
    BLACK = [0, 0, 0]
    if (height_r > width_r):
        resized = cv2.copyMakeBorder(resized, 0, 0, 0, 1, cv2.BORDER_CONSTANT, value=BLACK)
    if (height_r < width_r):
        resized = cv2.copyMakeBorder(resized, 1, 0, 0, 0, cv2.BORDER_CONSTANT, value=BLACK)
    p = 2
    ReSizedImg = cv2.copyMakeBorder(resized, p, p, p, p, cv2.BORDER_CONSTANT, value=BLACK)
    img_dim = ReSizedImg.shape
    height = img_dim[0]
    width = img_dim[1]
    # print("Padded Height = ", height, "Width = ", width)
    return ReSizedImg

# Our sketch generating function
def sketch(image):
    # Convert image to grayscale
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Clean up image using Guassian Blur
    img_gray_blur = cv2.GaussianBlur(img_gray, (5, 5), 0)

    # Extract edges
    canny_edges = cv2.Canny(img_gray_blur, 30, 60)

    # Do an invert binarize the image
    ret, mask = cv2.threshold(canny_edges, 240, 255, cv2.THRESH_BINARY_INV)

    return mask


# Initialize webcam, cap is the object provided by VideoCapture
# It contains a boolean indicating if it was sucessful (ret)
# It also contains the images collected from the webcam (frame)
cap = cv2.VideoCapture(0)
cap2 = cv2.VideoCapture(1)
# Get the Default resolutions
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

while True:
    ret, frame = cap.read()
    ret1, frame1 = cap2.read()
    cv2.imshow('Original', (frame))
    cv2.imshow('Our Live Sketcher', sketch(frame))
    if cv2.waitKey(1) == 13:  # 13 is the Enter Key
        break

# Release camera and close windows
cap.release()
cap2.release()
cv2.destroyAllWindows()