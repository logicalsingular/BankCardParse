from BankCardParse import parser

text_1 = "1134 1234 1234 1234"
text_2 = "Alex 12/12 1234123412341234"
text_3 = "Alex 12/12 12341234123412349"
text_4 = "Alex 01/21 1334 1234 1234 1234"
text_5 = "Alex 01/21 1434 1234 56785678"
print(parser(text_1))
print(parser(text_2))
print(parser(text_3))
print(parser(text_4))
print(parser(text_5))