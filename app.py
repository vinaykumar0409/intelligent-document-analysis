import cv2
import pytesseract

# Read the image
img = cv2.imread('sample images/index_page.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
text = pytesseract.image_to_string(thresh, config='--psm 6')
print(text)

# Get the bounding boxes
boxes = pytesseract.image_to_boxes(img, config='--psm 6')

# Draw bounding boxes on the image
for b in boxes.splitlines():
    b = b.split()
    char = b[0]
    x_min, y_min, x_max, y_max = int(b[1]), int(b[2]), int(b[3]), int(b[4])
    
    # Convert y-coordinates since OpenCV's coordinate system starts from the top-left corner
    height, width, _ = img.shape
    y_min = height - y_min
    y_max = height - y_max
    
    # Draw the rectangle around the character
    cv2.rectangle(img, (x_min, y_max), (x_max, y_min), (0, 255, 0), 2)
    cv2.putText(img, char, (x_min, y_min), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

# Show the image with bounding boxes
cv2.imshow('Bounding Boxes', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
