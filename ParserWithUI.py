import PySimpleGUI as sg
from bs4 import BeautifulSoup as BS
import requests
layout = [
    [sg.Text('Найти по ключевым словам(через &)'), sg.InputText(),sg.Text('Бюджет от'), sg.InputText(size=(7,7)),sg.Text('руб. до'), sg.InputText(size=(7,7)),sg.Text('руб.')],
    [sg.Text('Kол-во заявок на одной странице'), sg.InputText(default_text="10",size=(3,7))],
    [sg.Output(size=(150, 20))],

    [sg.Button("Далее")]
]
def fl(x,minb,maxb):
    for j in range(z):
        pages = []
        ans = ""
        pages.append(requests.get('https://www.fl.ru/projects/?page=' + str(x)))
        for r in pages:
            html = BS(r.content, 'html.parser')
            for i in html.select(".b-post"):
                name = list(map(str, list(map(str, str(i.select(".b-post__link")).split('>')))[1].split('<')))[0]
                title = list(map(str, list(map(str, str(i).split('<div class="b-post__txt "> ')))[1].split('</div>')))[
                    0]
                mon = list(map(str, list(map(str, str(i).split('&nbsp;')))[0].split('>')))[-1]
                url = "fl.ru" + \
                      list(map(str, list(map(str, str(i).split('class="b-post__link" href="')))[1].split('"')))[0]
                if list(map(str, str(i).split('&nbsp;')))[1][0] == '₽':
                    realmon=int(mon)
                    mon += "₽"
                else:
                    try:
                        realmon = int(mon) * 73
                        mon += "$"
                    except:
                        realmon = minb + 1

                ans += name + "   " + mon + "   " + url + "   " + "\n" + title + "\n\n========================================================================================================================\n"
                if realmon >= minb and realmon <= maxb:
                    for l in range(len(list(map(str, values[0].split("&"))))):
                        if ' ' + words[l] + ' ' in ans:
                            print(ans)
                else:
                    x = fl(x, minb, maxb)
                ans = ""
                break
            x += 1
    return(x)
def fh(x1,minb,maxb):
    for j in range(z):
        pages = []
        ans = ""
        pages.append(requests.get('https://freelance.habr.com/tasks?page=' + str(x1)))
        for r in pages:
            html = BS(r.content, 'html.parser')
            for i in html.select(".content-list__item"):
                try:
                    name = list(map(str, list(map(str, str(i.select(".task__title")).split('title="')))[1].split('">')))[0]
                except:
                    name=i.select(".task__title")
                title = ""
                try:
                    mon = list(map(str, list(map(str, str(i.select(".count")).split('count">')))[1].split('<')))[0]
                    realmon=""
                    for q in range(len(list(map(str, list(map(str, list(map(str, str(i.select(".count")).split('count">')))[1].split('<')))[0][:-6].split(' '))))):
                        realmon+=list(map(str, list(map(str, list(map(str, str(i.select(".count")).split('count">')))[1].split('<')))[0][:-6].split(' ')))[q]
                except:
                    mon = "Договорнаяя"
                    realmon=minb+1
                url = 'https://freelance.habr.com/' +list(map(str, list(map(str, str(i).split('href="')))[1].split('"')))[0]
                ans += name + "   " + mon + "   " + url + "   " + "\n" + title + "\n\n========================================================================================================================\n"
                if int(realmon) >= minb and int(realmon) <= maxb:
                    for l in range(len(list(map(str, values[0].split("&"))))):
                        if ' ' + words[l] + ' ' in ans:
                            print(ans)
                else:
                    x1 = fh(x1, minb, maxb)
                ans = ""
                break
            x1 += 1
    return (x1)



window = sg.Window('File Compare', layout)
x=1
x1=1
tf1=1
while True:
    event, values = window.read()
    isitago = 1
    if '&'in values[0]:
        words=list(map(str, values[0].split("&")))
    else:
        words = [values[0]]
    if values[1] != '':
        minb=int(values[1])
    else:
        minb=0
    if values[2] != '':
        maxb=int(values[2])
    else:
        maxb=99999999
    z=int(values[3])
    if event == 'Далее':
        tf=1
        tf1+=1
        if tf1 == 2:
            tf1=0

    if tf == 1:
        if tf1 == 0:
            x=fl(x,minb,maxb)
        if tf1 == 1:
            x1=fh(x1,minb,maxb)

        tf=0

