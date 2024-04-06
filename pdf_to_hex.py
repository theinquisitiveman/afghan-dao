import PyPDF2

def pdf_to_hexadecimal(pdf_path):
    try:
        with open(pdf_path, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            hex_strings = []
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text = page.extract_text()
                hex_string = text.encode('utf-8').hex()
                hex_strings.append(hex_string)
            return hex_strings
    except Exception as e:
        print(f"Error occurred: {e}")
        return None

# Replace 'your_pdf_file.pdf' with the path to your PDF file
pdf_path = '/Users/theinquisitiveman/Documents/eth-sample-code/Afghan_DAO_Example_PDF.pdf'
hex_strings = pdf_to_hexadecimal(pdf_path)
if hex_strings:
    for idx, hex_string in enumerate(hex_strings, start=1):
        print(f"Page {idx} Hexadecimal String: {hex_string}")
else:
    print("Failed to convert PDF to hexadecimal strings.")