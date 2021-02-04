def parser(text):
    for n in range(len(text)-15):
        if text[n:n+16].isdigit():
            return text[n:n+16]     
        elif   text[n:n+4].isdigit() and text[n+5:n+5+4].isdigit() and text[n+10:n+10+4].isdigit() and text[n+15:n+15+4].isdigit():
            if len(text[n:n+4])==4 and len(text[n+5:n+5+4])==4 and len(text[n+10:n+10+4])==4 and len(text[n+15:n+15+4])==4:
                spaceless_text = text[n:n+19].replace(" ","")
                if len(spaceless_text)==16:
                    return spaceless_text
    return False