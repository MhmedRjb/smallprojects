from jinja2 import Template

# Context data
context = {
    'brand_name': 'شركة الـــفــــولاني',
    'company_name': 'شركة العــــلاني',
    'address': '24 شارع النصر تفرع مصطفي صدقي -مدينة الهدى -القاهرة',
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
    'account_name': 'فولاني ابن علاني',
    'bank_details': 'أضف تفاصيل بنكية',
    'phone': '1234-567-890',
    'website': 'yourbusinesswebsite.com',  # لا توجد ترجمة محددة لاسم الموقع في هذا السياق
    'email': 'your@email.com',
    'contact_address': 'عمر مدينة نصر  - 40',
    'terms': 'تطبق الشروط والأحكام المتفق عليها طبقا للقواعد ',
}
context_en = {
    'brand_name': 'Brand Name',
    'company_name': 'Company Name',
    'address': '24 Lorem Street Area, Location, Lorem Ipsum 75484x',
    'invoice_date': '01/01/2020',
    'due_date': '10/01/2020',
    'invoice_no': '494512',
    'items': [
        {'description': 'Flyer Design', 'unit_price': '10.00', 'qty': 1, 'total': '10.00'},
        {'description': 'Brochure Design', 'unit_price': '5.00', 'qty': 2, 'total': '10.00'},
        {'description': 'Business Card', 'unit_price': '15.00', 'qty': 3, 'total': '45.00'},
        {'description': 'Lorem Ipsum Design', 'unit_price': '25.00', 'qty': 4, 'total': '100.00'},
        {'description': 'Lorem Ipsum Design', 'unit_price': '10.00', 'qty': 5, 'total': '50.00'}
    ],
    'sub_total': '535.00',
    'tax': '0.00',
    'grand_total': '535.00',
    'account_no': '123456789',
    'account_name': 'Lorem Ipsum',
    'bank_details': 'Add your Bank',
    'phone': '1234-567-890',
    'website': 'yourbusinesswebsite.com',
    'email': 'your@email.com',
    'contact_address': 'Lorem Ipsum - 40',
    'terms': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed diam nonummy nibh euismod tincidunt.'
}

# Load the template
with open('invoice_template.html', 'r', encoding='utf-8') as file:
    template_content = file.read()

# Create a Template instance
template = Template(template_content)

# Render the template with context data
rendered_html = template.render(context)

# Save the rendered HTML to a file (specifying UTF-8 encoding)
with open('invoice.html', 'w', encoding='utf-8') as file:
    file.write(rendered_html)


with open('invoice_template_en.html', 'r') as file:
    template_content = file.read()

# Create a Template instance
template = Template(template_content)

# Render the template with context data
rendered_html = template.render(context_en)

# Save the rendered HTML to a file (specifying UTF-8 encoding)
with open('invoice_en.html', 'w') as file:
    file.write(rendered_html)
