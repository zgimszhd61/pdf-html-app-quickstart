from pdfminer.high_level import extract_text
from pdfminer.layout import LAParams
import os

def pdf_to_html(pdf_path, html_path):
    try:
        # Extract text from PDF
        laparams = LAParams()
        text = extract_text(pdf_path, laparams=laparams)
        
        # Wrap extracted text in basic HTML tags
        html_content = f"<html><body><pre>{text}</pre></body></html>"
        
        # Write the HTML content to a file
        with open(html_path, 'w') as html_file:
            html_file.write(html_content)
        
        print(f"Conversion successful: {html_path}")
    except Exception as e:
        print(f"Error during conversion: {e}")


# 指定PDF文件路径
pdf_path = '2405.14716v1.pdf'

# 指定输出的HTML文件路径
html_path = '2405.14716v1.html'

pdf_to_html(pdf_path, html_path)
