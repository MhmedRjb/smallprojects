from jinja2 import Template

# Context data
context = {
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
with open('invoice_template.html', 'r') as file:
    template_content = file.read()

# Create a Template instance
template = Template(template_content)

# Render the template with context data
rendered_html = template.render(context)

# Save the rendered HTML to a file
with open('invoice.html', 'w') as file:
    file.write(rendered_html)

