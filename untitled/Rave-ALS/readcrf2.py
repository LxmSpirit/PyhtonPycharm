from docx import Document

doc = Document('D:/Work/Python/PycharmProjects/untitled/Rave-ALS/CRF1.docx')

paragraphs = doc.paragraphs
num=0;
for paragraph in paragraphs:
    if paragraph.style.name == 'Heading 1':
        print(paragraph.text)
        num = num +1
        # 这是一级标题

print('num: '+str(num))