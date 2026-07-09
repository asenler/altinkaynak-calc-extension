# -*- coding: utf-8 -*-

from .api import get_rates
from .calc import update_sheet


def update_current_sheet(doc):
    """
    Aktif Calc sayfasını Altınkaynak kurları ile günceller.
    """

    sheet = doc.CurrentController.ActiveSheet

    rates = get_rates()

    update_sheet(sheet, rates)

    return True
