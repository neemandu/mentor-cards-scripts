import boto3
import pdfkit

# DynamoDB setup
dynamodb = boto3.resource('dynamodb')

table_name = 'CardsPack-ffx5lo4aivekbbvot2z2rsyojy-prod'
table = dynamodb.Table(table_name)

def generate_html_for_item(item):
    html_content = """<html><head><meta charset="UTF-8"><style>body { font-size: 150%; line-height: 1.2; font-family: Arial, sans-serif; direction: rtl; } .header { position: fixed; top: 10; right: 75%; width: 100%; background-color: #fff; } .header img { width: 200px; ; margin-left: 20px;} .footer-text { text-align: center; width: 100%; } .description {width: 70%;margin-left: auto;margin-right: auto;text-align: center;} .guidebook { float: right; width: 90%; text-align: right; }h2, h3, p { font-size: inherit; margin: 0; padding: 0; line-height: 1.2;}.item { clear: both; padding: 20px; }.item img { width: 300px; height: auto; display: block; margin: 0 auto; }</style></head><body>"""
    
    html_content += f'<div class="header"><img src="https://master-cards.s3.eu-west-2.amazonaws.com/Logo+(2).png" alt="Logo"></div>'

    html_content += f'<div class="item">'
    if 'imgUrl' in item:
        html_content += f'<img src="{item["imgUrl"]}">'
    if 'name' in item:
        html_content += f'<h1 style="text-align:center;">{item["name"]}</h1>'
    if 'description' in item:
        # Removing specific string from description
        description = item["description"]
        html_content += f'<p class="description">{description}</p>'

    # GuideBook
    if 'guideBook' in item:
        html_content += '<div class="guidebook">'
        def process_guidebook_element(elements, depth=0, numbers=[]):
            nonlocal html_content  # Ensure html_content is accessible within the function
            for index, element in enumerate(elements):
                current_numbers = numbers + [str(index + 1)]  # Append the current index (1-based) to the path
                number_str = ".".join(current_numbers)  # Join numbers with dots for the current element
                indent = depth * 20  # Increase indentation by 20px for each level
                
                # Remove the specified string from element name if exists and apply numbering
                element_name = element["name"].replace("לפתיחה לחצו כאן", "")
                if depth == 0:
                    html_content += "<br>"
                    html_content += f'<h2 style="margin-right:{indent}px;"><b>{number_str} {element_name}</b></h2>'
                elif depth == 1:
                    html_content += "<br>"
                    html_content += f'<h3 style="margin-right:{indent}px;"><b>{number_str} {element_name}</b></h3>'
                else:
                    html_content += f'<p style="margin-right:{indent}px;">{number_str} {element_name}</p>'
                
                # Process sub-elements if any, increasing the depth and passing the current numbering path
                if 'subElements' in element:
                    process_guidebook_element(element['subElements'], depth + 1, current_numbers)

        # When calling process_guidebook_element initially, start with an empty list for numbers
        process_guidebook_element(item['guideBook'], 0, [])

        html_content += '</div>'
    
    html_content += '</div></body></html>'
    
    return html_content


# Fetch all items from DynamoDB table
response = table.scan()
items = response['Items']

# Placeholder paths for HTML and PDF files
html_file_paths = []
pdf_file_paths = []

# Loop through each item and generate HTML and PDF
for index, item in enumerate(items):
    # Generate HTML content
    html_content = generate_html_for_item(item)
    
    # Save HTML to a file
    html_file_path = f"C:\\Users\\neema\\mentor-cards\\cards_{index + 1}.html"
    with open(html_file_path, 'w', encoding='utf-8') as file:
        file.write(html_content)
    html_file_paths.append(html_file_path)
    
    # Convert HTML to PDF
    pdf_file_path = f"C:\\Users\\neema\\mentor-cards\\mentor_cards_{item["id"]}.pdf"
    pdfkit.from_file(html_file_path, pdf_file_path, configuration=pdfkit.configuration(wkhtmltopdf=r'C:\Users\neema\source\wkhtmltox\bin\wkhtmltopdf.exe'))
    pdf_file_paths.append(pdf_file_path)

html_file_paths, pdf_file_paths


