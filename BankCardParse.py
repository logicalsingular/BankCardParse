# uncleared_text = input("Please, type Bank Card ")
text_1 = "1234 1234 1234 1234"
text_2 = "Alex 12/12 1234123412341234"
text_3 = "Alex 12/12 1234 1234 1234 1234"

def parser(text):
    for n in range(len(text)):
        if text[n:n+16:1].isdigit():
            return text[n:n+16:1]       
        elif text[n:n+4:1].isdigit() and text[n+5:n+5+4:1].isdigit() and text[n+10:n+10+4:1].isdigit() and text[n+15:n+15+4:1].isdigit():
            return text[n:n+4:1]+text[n+5:n+5+4:1]+text[n+10:n+10+4:1]+text[n+15:n+15+4:1]


print(parser(text_1))
print(parser(text_2))
print(parser(text_3))