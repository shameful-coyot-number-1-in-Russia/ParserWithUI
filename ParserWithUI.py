import PySimpleGUI as sg
from bs4 import BeautifulSoup as BS
import requests
layout = [
    [sg.Text('Найти по ключевым словам(через &)'), sg.InputText()],
    [sg.Text('Kол-во заявок на одной странице'), sg.InputText(default_text="10",size=(3,7))],
    [sg.Output(size=(150, 20))],

    [sg.Button("Далее")]
]
window = sg.Window('File Compare', layout)
x=1
while True:
    event, values = window.read()
    isitago = 1
    if '&'in values[0]:
        words=list(map(str, values[0].split("&")))
    else:
        words = [values[0]]
    z=int(values[1])
    if event == 'Далее':
        tf=1
    if tf == 1:
        for j in range(z):
            pages = []
            shit = ""
            shits = ""
            ans = ""
            pages.append(requests.get('https://www.fl.ru/projects/?page=' + str(x)))
            for r in pages:
                html = BS(r.content, 'html.parser')
                for i in html.select(".b-post"):
                    text = list(map(str, str(i.select(".b-post__link")).split('>')))
                    texts = list(map(str, text[1].split('<')))
                    op = list(map(str, str(i).split('<div class="b-post__txt "> ')))
                    ops = list(map(str, op[1].split('</div>')))
                    mon = list(map(str, str(i).split("&nbsp;")))
                    mons = list(map(str, mon[0].split('>')))
                    url = list(map(str, str(i).split('class="b-post__link" href="')))
                    urls = list(map(str, url[1].split('"')))
                    ans += texts[0] + "   "
                    if mon[1][0] == '₽':
                        ans += mons[-1] + mon[1][0]
                    else:
                        ans += mons[-1] + "$"
                    ans += "   " + "fl.ru" + urls[0] + "   "
                    ans += "\n" + ops[0] + "\n\n"
                    for l in range(len(list(map(str, values[0].split("&"))))):
                        if ' ' +words[l]+ ' ' in ans:
                            print(ans)
                    ans=""
                    tf=0
                    break
                x += 1
