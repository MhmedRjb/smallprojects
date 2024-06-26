import cv2
from pyzbar.pyzbar import decode
import json

# Load the QR code image
image = cv2.imread('zap-qr-1.png')

# Decode the QR code
decoded_objects = decode(image)
if decoded_objects:
    qr_data = decoded_objects[0].data.decode('utf-8')
    # Convert the QR code data back to JSON
    json_data = json.loads(qr_data)
    
    # Save the JSON data to a file
    with open('decoded_data.json', 'w', encoding='utf-8') as json_file:
        json.dump(json_data, json_file, ensure_ascii=False, indent=4)
    
    print("JSON data has been saved to decoded_data.json")
else:
    print("No QR code found")
