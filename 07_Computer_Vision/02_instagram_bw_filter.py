# ==========================================
# Codeaura Python Course: 02_instagram_bw_filter.py
# ==========================================
# Concept: Using OpenCV to convert a color image to Black & White.
# Real Life Example: Instagram ya Snapchat ka vintage (purana) B&W filter.

import cv2
import os

print("--- Instagram Filter: Black & White ---")

# Hum pichle folder me rakhe hue 'logo.png' ko use karenge
image_path = "../logo.png"

# Check if the file exists
if not os.path.exists(image_path):
    print("Error: 'logo.png' not found! Make sure the logo is in the main folder.")
else:
    # Step 1: Photo ko Computer me load karna (Padhna)
    # cv2.imread is used to read an image
    color_image = cv2.imread(image_path)

    # Step 2: Photo par B&W Filter lagana
    # cv2.cvtColor rang badalne ke kaam aata hai (Color to Gray)
    bw_image = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)

    # Step 3: Photo ko screen par dikhana
    print("Opening the photo... Press any key on the photo window to close it.")
    cv2.imshow("Original Color Photo", color_image)
    cv2.imshow("Instagram B&W Filter", bw_image)

    # Wait for the user to press a key, then close the windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Note for Students: Aap 'logo.png' ki jagah apni khud ki photo ka path dekar test kar sakte hain!
