from docx import Document

doc = Document('D:/Work/Python/PycharmProjects/untitled/Rave-ALS/CRF1.docx')

tables = doc.tables
num = len(tables)

for table in tables:
    for row in table.rows:
        rownum = len(table.rows)
        for cell in row.cells:
            for i in range(0, rownum):
                data = cell(i, 0).text
                print(data)
        #for cell in row.cells:
            # 处理每个单元格的内容
            #data = cell.text
print('num: '+str(num))