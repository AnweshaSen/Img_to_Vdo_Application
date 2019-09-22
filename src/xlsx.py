import xlrd

def parseXlsx(path):
    try:
        book = xlrd.open_workbook(path)
        sheet_no = len(book.sheet_names())
        finallist = []
        for k in range(sheet_no):
            sheet = book.sheet_by_index(k)
            col_no = sheet.ncols
            row_no = sheet.nrows
            outlist = []
            for j in range(1, row_no):
                dict = {}
                dict["outfile"] = sheet.cell(j, 1).value
                dict["overlay"] = sheet.cell(j, 3).value
                dict["trans"] = sheet.cell(j, 4).value
                i = 5
                lst = []
                while (i + 1) < col_no:
                    lst.append((sheet.cell(j, i).value, sheet.cell(j, i + 1).value))
                    i = i + 2
                dict["infile"] = lst
                outlist.append(dict)
            finallist.append(outlist)
        return finallist
    except:
        print("Selected file not an Excel File... Exiting...")
        exit()

if __name__ == "__main__":
    path = ".\Data\Sheet1.xlsx"
    outlist = parseXlsx(path)
    # print(outlist)
    sheetcount = 0
    for sheet in outlist:
        sheetcount = sheetcount + 1
        print ("Sheet:", sheetcount)
        itemcount = 0
        for item in sheet:
            itemcount = itemcount + 1
            print(itemcount, item)
