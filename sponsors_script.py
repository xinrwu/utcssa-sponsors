# -*- coding: utf-8 -*-
import codecs
f = codecs.open('sponsors', 'r',encoding='utf-8')
w_html = open('sponsors_html', encoding='utf_8', mode='w')
w_js = open('sponsors_js', encoding='utf_8', mode='w')
def print_html(wf, sponsor_info):
    s = '<li id="sponsors"><span>'+ sponsor_info[0]+ '</span><br>' + sponsor_info[1] + '<br>' + sponsor_info[3] + '<br></li>\n'
    print(s)
    wf.write(s)

def print_js(wf, sponsor_info):
    s = ("{\n name: '" + sponsor_info[0]
    + "',\n address: '" + sponsor_info[1]
    + "',\n special: '" + sponsor_info[2]
    + "',\n phone: '" + sponsor_info[3]
    + "',\n location: {" + sponsor_info[4] +  "}\n},\n")
    wf.write(s)

for line in f:
    info = line.split('|')
    for i in range(len(info)):
        info[i] = info[i].strip()
    print_html(w_html, info)
    print_js(w_js, info)
f.close()
w_html.close()
w_js.close()
