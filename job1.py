
''' function that takes name of file and returns its contents'''
def get_text_from_file(filename):
    return(open(filename, "r").read())


'''function that takes text and whitespaces and returns list of tokens'''
def tonenize(text, whitespaces):
    tokens = []
    word = ""
    for i in text:
        if i not in whitespaces:
            word += i  # add character to temporary word variable
        elif word in whitespaces:
            word = "" # clear word (in case to skip containing whitespaces token)
        elif word != "":
            tokens.append(word) # add correct token to list
            word = "" 
    if word != "":        
        tokens.append(word) # last case: add the last character if it exists
    return tokens

whitespaces = [" ", "if"]
text = "ab c  ifer def"

print(tonenize(text, whitespaces))
        
#print(tonenize(get_text_from_file(), whitespaces))        
        
