import math

"""BU KÜTÜPHANE 'TKİNTER' KÜTÜPHANESİNDE 'RGB' RENK KODLARINI KULLANABİLMEK İÇİN 2020 EYLÜL'DE YAZILMIŞTIR.
KULLANILMASI VE PAYLAŞILMASI ÜCRETSİZDİR.KÜTÜPHANENİN GELİŞTİRME AŞAMALARI DEVAM ETMEKTEDİR.
KÜTÜPHANEYİ DÜZGÜN VE/VEYA DAHA İYİ BİR ŞEKİLDE KULLANABİLMEK İÇİN EN AZ GİRİŞ SEVİYESİNDE 'RGB' RENK KODU
SİSTEMİ BİLİNMELİDİR.
BU KÜTÜPHANEYİ KULLANARAK ÇOK RAHAT(!) BİR ŞEKİLDE
HOVER İŞLEMLERİ YAPILABİLMEKTEDİR.

KÜTÜPHANEYİ YAZAN: YİİT VE SAM@
TEST EDEN:         YİNE YİİT

 ̶1̶7̶/̶0̶9̶/̶2̶0̶2̶0̶  -> 16/01/2022
"""

class GeçersizDeğer(Exception):
    pass

def hex(r, g, b) -> int:
    if type(r) is not int or type(g) is not int or type(b) is not int:
        raise GeçersizDeğer("Değerlerin türü int olmalıdır.")
    r = 255 if r > 255 else r
    g = 255 if g > 255 else g
    b = 255 if b > 255 else b
    return f"#{r:02x}{g:02x}{b:02x}".format(r, g, b)

def rgb(hex):
    if type(hex) is not str:
        raise GeçersizDeğer("Değerlerin türü str olmalıdır.")
    if hex[0] != "#":
        raise GeçersizDeğer("Değerlerin ilk karakteri # olmalıdır.")
    if len(hex) != 7:
        raise GeçersizDeğer("Değerlerin uzunluğu 7 olmalıdır.")
    r = int(hex[1:3], 16)
    g = int(hex[3:5], 16)
    b = int(hex[5:7], 16)
    r = 255 if r > 255 else r
    g = 255 if g > 255 else g
    b = 255 if b > 255 else b
    return (r, g, b)

def bind(widget,text="",bg="",color=""):
    if text == "":
        text = widget["text"]
    elif text != "":
        widget["text"] = text
    if bg == "":
        bg = widget["bg"]
    elif bg != "":
        widget["bg"] = bg
    if color == "":
        color = widget["fg"]
    elif color != "":
        widget["fg"] = color

def hover(widget,text="",bg="",color=""):
    global bg_old
    text_old = widget["text"]
    bg_old = widget["bg"]
    color_old = widget["fg"]
    widget.bind("<Enter>",lambda x: bind(widget,text=text,bg=bg,color=color))
    widget.bind("<Leave>",lambda y: bind(widget,text=text_old,bg=bg_old,color=color_old))
