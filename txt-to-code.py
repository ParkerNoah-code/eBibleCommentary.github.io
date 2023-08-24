import pyperclip
import html

code_text = ""
clipboard_text = pyperclip.paste()
lines = clipboard_text.splitlines()

title = False

if title:
    code_text += "<h2>" + html.escape(lines[0].strip()) + "</h2>"
else:
    code_text += "<p>" + html.escape(lines[0].strip()) + "</p>"

for line in lines[1:]:
    code_text += "<p>" + html.escape(line.strip()) + "</p>"

code_text = code_text.replace("Gen_","Gen ")
code_text = code_text.replace("Deu_","Deut ")
code_text = code_text.replace("Psa_","Ps ")
code_text = code_text.replace("Mat_","Mat ")
code_text = code_text.replace("Mar_","Mk ")
code_text = code_text.replace("Luk_","Lk ")
code_text = code_text.replace("Joh_","Jn ")
code_text = code_text.replace("Act_","Acts ")
code_text = code_text.replace("Rom_","Rom ")
code_text = code_text.replace("1Co_","1 Cor ")
code_text = code_text.replace("2Co_","2 Cor ")
code_text = code_text.replace("1Th_","1 Thes ")
code_text = code_text.replace("2Th_","2 Thes ")
code_text = code_text.replace("Gal_","Gal ")
code_text = code_text.replace("Eph_","Eph ")
code_text = code_text.replace("Php_","Php ")
code_text = code_text.replace("Col_","Col ")
code_text = code_text.replace("Tit_","Titus ")
code_text = code_text.replace("Phm_","Phm ")
code_text = code_text.replace("1Ti_","1 Tim ")
code_text = code_text.replace("2Ti_","2 Tim ")
code_text = code_text.replace("Tit_","Titus ")
code_text = code_text.replace("Heb_","Heb ")
code_text = code_text.replace("Jas_","James ")
code_text = code_text.replace("Rev_","Rev ")

pyperclip.copy(code_text)