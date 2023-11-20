from docx import Document

doc = Document('D:/Work/Python/PycharmProjects/untitled/Rave-ALS/CRF1.docx')

tables = doc.tables
num = len(tables)

for table in tables:
    table.add_row()
    for row in table.rows:
        rownum = len(table.rows)
        for cell in row.cells:
            # 处理每个单元格的内容
            data = cell.text
print('num: '+str(num))