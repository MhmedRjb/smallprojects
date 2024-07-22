from jinja2 import Template

# Context data
context = {
    'company': 'شركة الـــفــــولاني',
    'customer_name': 'شركة العــــلاني',
    'custom_party_balance': '24 شارع النصر تفرع مصطفي صدقي -مدينة الهدى -القاهرة',
    'invoice_date': '1 يناير 2020',
    'due_date': '10 يناير 2020',
    'name4512',
    'items': [
        {'item_code': 'تصميم نشرة', 'rate': '$10', 'qty': 1, 'base_total': '$10'},
        {'item_code': 'تصميم كتيب', 'rate': '$5', 'qty': 2, 'base_total': '$10'},
        {'item_code': 'بطاقة أعمال', 'rate': '$15', 'qty': 3, 'base_total': '$45'},
        {'item_code': 'تصميم لوريم إيبسوم', 'rate': '$25', 'qty': 4, 'base_total': '$100.00'},
        {'item_code': 'تصميم لوريم إيبسوم', 'rate': '$10', 'qty': 5, 'base_total': '$50.00'},
    ],
    'base_total': '$535',
    'tax': '$0.00',
    'base_total': '$535',
    'account_no': '123456789',
    'account_name': 'فولاني ابن علاني',
    'bank_details': 'أضف تفاصيل بنكية',
    'phone': '1234-567-890',
    'website': 'yourbusinesswebsite.com',  # لا توجد ترجمة محددة لاسم الموقع في هذا السياق
    'email': 'your@email.com',
    'contact_custom_party_balance': 'عمر مدينة نصر  - 40',
    'terms': 'تطبق الشروط والأحكام المتفق عليها طبقا للقواعد ',
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
