#!python
print("content-type:text/html\n")

import cgi, cgitb
form = cgi.FieldStorage()

def popular_word(text):
    text=text.lower()

    splitted_words=text.split()
    answer={}

    want=''
    a=0

    for s in splitted_words:
        answer[s]=splitted_words.count(s)

        if answer[s]>a:
            a=answer[s]
            want=s

    return want, a

text = form.getvalue('text_o')
print (popular_word(text))
