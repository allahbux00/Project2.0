  
import pytesseract  
from PIL import Image  
import pdfplumber  

def process_document(file):  
    if file.type == "application/pdf":  
        text = ""  
        with pdfplumber.open(file) as pdf:  
            for page in pdf.pages:  
                text += page.extract_text() + "\n"  
        return text  
    else:  
        return file.getvalue().decode("utf-8")  

def process_image(image_file):  
    image = Image.open(image_file)  
    return pytesseract.image_to_string(image)  
    