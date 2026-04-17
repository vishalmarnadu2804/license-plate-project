import cv2
import pytesseract
import os
import re

folder = "."

for file in os.listdir(folder):
    if file.endswith((".jpg", ".png", ".jpeg", ".webp")):
        print("\nProcessing:", file)

        img = cv2.imread(file)

        if img is None:
            print("Error loading:", file)
            continue

        # Preprocessing
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray = cv2.resize(gray, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
        gray = cv2.GaussianBlur(gray, (5, 5), 0)
        gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

        # OCR (flexible mode)
        text = pytesseract.image_to_string(gray, config='--psm 11')

        # 🔥 Clean output (IMPORTANT)
        text = re.sub(r'[^A-Z0-9]', '', text.upper())

        print("Detected Number:", text)

        cv2.imshow("Processed Image", gray)
        cv2.waitKey(0)

cv2.destroyAllWindows()