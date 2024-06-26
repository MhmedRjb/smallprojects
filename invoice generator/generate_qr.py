import qrcode
import json

# Example JSON data
data = {
    "invoice_id": "INV-12345",
    "date": "2024-06-26",
    "due_date": "2024-07-26",
    "seller": {
        "name": "ABC Company",
        "email": "contact@abccompany.com",
        "phone": "+20 123 456 7890"
    },
    "buyer": {
        "name": "XYZ Enterprises",
        "email": "info@xyzenterprises.com",
        "phone": "+20 987 654 3210"
    },
    "items": [
        {
            "description": "Product 1",
            "quantity": 2,
            "unit_price": 50.00,
            "total": 100.00
        },
        {
            "description": "Product 2",
            "quantity": 1,
            "unit_price": 150.00,
            "total": 150.00
        }
    ],
    "subtotal": 250.00,
    "tax": 25.00,
    "total": 275.00,
    "status": "Unpaid"
}

# Convert JSON data to a string
json_data = json.dumps(data)

# Generate QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(json_data)
qr.make(fit=True)

# Create an image from the QR Code instance
img = qr.make_image(fill_color="black", back_color="white")

# Save the image
img.save("invoice_qr.png")
