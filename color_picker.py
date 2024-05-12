import cv2
import numpy as np

# Function to handle mouse click events
def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:  # If left mouse button is clicked
        blue = img[y, x, 0]  # Extract blue value of pixel
        green = img[y ,x, 1]  # Extract green value of pixel
        red = img[y ,x, 2]  # Extract red value of pixel
        
        # Draw a small circle on the clicked point
        cv2.circle(img, (x, y), 3, (0, 0, 255), -1)
        cv2.imshow("Image", img)
        
        # Create a new image with the selected color
        coloredImage = np.zeros((512, 512, 3), np.uint8)
        coloredImage[:] = [blue, green, red]  # Fill the image with the selected color
        
        # Add text displaying the RGB values of the selected color
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = "RGB : "+str(red)+", "+str(green)+", "+str(blue)
        cv2.putText(coloredImage, text, (10,30), font, 1, (255,255,255), 2)
        cv2.imshow("Color Picked", coloredImage)

# Load the image
img = cv2.imread("img1.jpg")
cv2.imshow("Image", img)

# Set mouse callback function on the image window
cv2.setMouseCallback("Image", click_event)

# Wait for any key press
cv2.waitKey(0)

# Close all OpenCV windows
cv2.destroyAllWindows()