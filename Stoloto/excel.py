import xlsxwriter
import top
import loto_five as loto5
import loto_six as six
import rapido

data_top = top.get_data()
data_5x36 = loto5.get_data()
data_6x45 = six.get_data()
data_rapido = rapido.get_data()

# Создайте новый файл Excel и добавьте листы.
workbook = xlsxwriter.Workbook('/home/stariylis/PycharmProjects/Learning_Code/Excel_file/stoloto.xlsx')

sheet_5x36 = workbook.add_worksheet('5x36')
sheet_6x45 = workbook.add_worksheet('6x45')
sheet_top = workbook.add_worksheet('Top-3')
sheet_rapido = workbook.add_worksheet('Rapido')

# Добавляем форматирование для выделения ячеек.
cell_format = workbook.add_format(
    {'font_name': 'Liberation Sans', 'bold': True, 'font_color': '#0000AA', 'align': 'center'})
cell_format_1 = workbook.add_format(
    {'font_name': 'Liberation Sans', 'italic': True, 'bold': True, 'font_color': '#AA0000', 'align': 'center'})
cell_format_2 = workbook.add_format(
    {'font_name': 'Liberation Sans', 'bold': True, 'font_color': '#015d1d', 'align': 'center', 'font_size': 15})
empty_column = workbook.add_format({'fg_color': '#969696'})

# Устанавливаем размер колонок
sheet_top.set_column(0, 0, 17)
sheet_top.set_column(1, 3, 4)
sheet_top.set_column(4, 5, 2, empty_column)
sheet_top.set_column(6, 7, 9)

sheet_5x36.set_column('A:A', 17)
sheet_5x36.set_column('B:F', 3)
sheet_5x36.set_column('G:H', 2, empty_column)
sheet_5x36.set_column('I:J', 9)
sheet_5x36.set_column('K:K', 2, empty_column)
sheet_5x36.set_column('L:AU', 3)

sheet_6x45.set_column('A:A', 17)
sheet_6x45.set_column('B:G', 4)
sheet_6x45.set_column('H:I', 2, empty_column)
sheet_6x45.set_column('J:K', 9)
sheet_6x45.set_column('L:L', 2, empty_column)
sheet_6x45.set_column('M:BE', 3)

sheet_rapido.set_column('A:A', 17)
sheet_rapido.set_column('B:I', 4)
sheet_rapido.set_column('J:J', 2, empty_column)
sheet_rapido.set_column('K:K', 4)
sheet_rapido.set_column('L:M', 2, empty_column)
sheet_rapido.set_column('N:O', 9)


# Функции записи данных в таблицу
def excel_top_writer(colm, date, ball, c_nec=[]):
    sheet_top.write_row('A1', colm, cell_format_1)
    sheet_top.write_column('A2', date, cell_format)

    row = 1
    for i in ball:
        col = 1
        for j in i:
            sheet_top.write(row, col, j, cell_format_2)
            col += 1
        row += 1

    row1 = 1
    for ch in c_nec:
        col1 = 6
        for tmp in ch:
            sheet_top.write(row1, col1, tmp, cell_format_2)
            col1 += 1
        row1 += 1


def excel_5x36_writer(colm, date, ball, c_nec=[]):
    sheet_5x36.write_row('A1', colm, cell_format_1)
    sheet_5x36.write_column('A2', date, cell_format)
    row = 1
    row1 = 1
    for i in ball:
        col = 1
        for j in i:
            sheet_5x36.write(row, col, j, cell_format_2)
            col += 1
        row += 1
    for ch in c_nec:
        col1 = 8
        for tmp in ch:
            sheet_5x36.write(row1, col1, tmp, cell_format_2)
            col1 += 1
        row1 += 1

    row2 = 1
    for i in ball:
        for j in i:
            sheet_5x36.write(row2, 10 + j, j, cell_format_2)
        row2 += 1


def excel_6x45_writer(colm, date, ball, c_nec=[]):
    sheet_6x45.write_row('A1', colm, cell_format_1)
    sheet_6x45.write_column('A2', date, cell_format)
    row = 1
    row1 = 1
    for i in ball:
        col = 1
        for j in i:
            sheet_6x45.write(row, col, j, cell_format_2)
            col += 1
        row += 1
    for ch in c_nec:
        col1 = 9
        for tmp in ch:
            sheet_6x45.write(row1, col1, tmp, cell_format_2)
            col1 += 1
        row1 += 1
    row2 = 1
    for i in ball:
        for j in i:
            sheet_6x45.write(row2, 11 + j, j, cell_format_2)
        row2 += 1


def excel_rapido_writer(colm, date, ball, c_nec=[]):
    sheet_rapido.write_row('A1', colm, cell_format_1)
    sheet_rapido.write_column('A2', date, cell_format)
    row = 1
    row1 = 1
    for i in ball:
        sheet_rapido.write(row, 10, i[8], cell_format_2)
        col = 1
        for j in i[:-1]:
            sheet_rapido.write(row, col, j, cell_format_2)
            col += 1
        row += 1

    for ch in c_nec:
        col1 = 13
        for tmp in ch:
            sheet_rapido.write(row1, col1, tmp, cell_format_2)
            col1 += 1
        row1 += 1


excel_top_writer(*data_top)
excel_5x36_writer(*data_5x36)
excel_6x45_writer(*data_6x45)
excel_rapido_writer(*data_rapido)

workbook.close()
