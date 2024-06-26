import qrcode
import json

# Example JSON data with Arabic text
context = {
    'brand_name': 'اسم العلامة التجارية',
    'company_name': 'اسم الشركة',
    'address': '24 شارع لوريم، منطقة لوريم إيبسوم 75484x',
    'invoice_date': '1 يناير 2020',
    'due_date': '10 يناير 2020',
    'invoice_no': '494512',
    'items': [
        {'description': 'تصميم نشرة', 'unit_price': '$10', 'qty': 1, 'total': '$10'},
        {'description': 'تصميم كتيب', 'unit_price': '$5', 'qty': 2, 'total': '$10'},
        {'description': 'بطاقة أعمال', 'unit_price': '$15', 'qty': 3, 'total': '$45'},
        {'description': 'تصميم لوريم إيبسوم', 'unit_price': '$25', 'qty': 4, 'total': '$100.00'},
        {'description': 'تصميم لوريم إيبسوم', 'unit_price': '$10', 'qty': 5, 'total': '$50.00'},
    ],
    'sub_total': '$535',
    'tax': '$0.00',
    'grand_total': '$535',
    'account_no': '123456789',
    'account_name': 'لوريم إيبسوم',
    'bank_details': 'أضف تفاصيل بنكية',
    'phone': '1234-567-890',
    'website': 'yourbusinesswebsite.com',
    'email': 'your@email.com',
    'contact_address': 'لوريم إيبسوم - 40',
    'terms': 'لوريم إيبسوم يعني نص بمعنى السخرية والنقد باللاتينية، ويعود تاريخه إلى القرن الأول الميلادي',
}

# Convert JSON data to a string
json_data = json.dumps(context, ensure_ascii=False)

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
img.save("zap-qr-1.png")
