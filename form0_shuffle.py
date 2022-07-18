# Split text to questions
import re
import pdfplumber
from PyPDF2 import PdfReader

reader = PdfReader("example.pdf")
text = ""
for page in reader.pages:
    text += page.extract_text() + "\n"

test_arr = []
bold_keys = []
total_text = ""
with pdfplumber.open('example.pdf') as pdf:
    for i in range(16):
        total_text += pdf.pages[i].extract_text()
        text = pdf.pages[i]
        clean_text = text.filter(lambda obj: obj["object_type"] == "char" and "Bold" in obj["fontname"])
        bold_keys.append(clean_text.extract_text().split('\n'))
re.split("(:\d{1,2} רפסמ הלאש)", total_text))
split_text_to_ques = re.split("(:\d{1,2} רפסמ הלאש)",text)
for li in split_text_to_ques:
        current_answers_split = re.split('[.]\d{1,2}', li)
        test_arr.append((len(current_answers_split), current_answers_split))