# ==========================================
# Codeaura Python Course: 03_pencil_sketch_filter.py
# ==========================================
# Concept: Edge Detection (Kinare pehchan na)
# Real Life Example: Photo ko aisi drawing me badalna jaise kisi ne pencil se sketch banaya ho.

import cv2
import os

print("--- Magic Filter: Pencil Sketch ---")

image_path = "../logo.png"

if not os.path.exists(image_path):
    print("Error: 'logo.png' not found!")
else:
    # Step 1: Photo read karna
    img = cv2.imread(image_path)
    
    # Step 2: Pehle photo ko blur (dhundhla) karna aur black & white me badalna
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred_img = cv2.GaussianBlur(gray_img, (5, 5), 0)
    
    # Step 3: Canny Edge Detector (Ye photo ki outlines/kinare nikalta hai)
    # Jaise hum pencil se sirf outline banate hain
    pencil_sketch = cv2.Canny(blurred_img, 50, 150)
    
    # Step 4: Dikhana
    print("Look at your screen! Press any key to close the window.")
    cv2.imshow("Original Photo", img)
    cv2.imshow("Pencil Sketch Drawing", pencil_sketch)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Note for Students: Canny Edge detector robots aur self-driving cars me use hota hai road ki lines dekhne ke liye!
