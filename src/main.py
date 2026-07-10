import uno

def hello():
    doc = XSCRIPTCONTEXT.getDocument()
    sheet = doc.CurrentController.ActiveSheet
    sheet.getCellByPosition(0, 0).String = "Merhaba"

g_exportedScripts = (hello,)
