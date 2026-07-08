# -*- coding: utf-8 -*-

from datetime import datetime


def update_sheet(sheet, rates):

    row = 0

    while True:
        code = sheet.getCellByPosition(0, row).String.strip().upper()

        if code == "":
            break

        if code in rates:
            item = rates[code]

            sheet.getCellByPosition(1, row).String = item["Alis"]
            sheet.getCellByPosition(2, row).String = item["Satis"]
            sheet.getCellByPosition(3, row).String = item["Aciklama"]

        row += 1

    # Güncelleme zamanı
    sheet.getCellByPosition(5, 0).String = "Güncelleme"
    sheet.getCellByPosition(6, 0).String = datetime.now().strftime(
        "%d.%m.%Y %H:%M:%S"
    )
