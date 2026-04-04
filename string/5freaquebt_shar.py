def freaquent_char(s):
    dict_char={}
    max_key=None
    max_value=None
    for char in s:
        if char in dict_char:
            dict_char[char]+=1
        else:
            dict_char[char]=1
    for chr in dict_char:
        if max_value is None or dict_char[char]>max_value:
            max_value=dict_char[char]
            max_key=char
    print(f"max_value is{max_value} of {max_key}")
freaquent_char("abcaacaa")