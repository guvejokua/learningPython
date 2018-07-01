def find(string):
    count = 0
    for i in range(len(string)):
        if string[i:i+len("baba")] == "baba":
            count = count + 1
    return count

string = "adalsşlsdflsdflsgdfgldgfbabadfgşkdfgk.." \
         "sdfjfdflkdgbabadfjkjlkgjdlfgjdlkfjglg..." \
         "sdfkldjglkdjfgjdfjgldjflgjdlfjgldjfgl..." \
         "djfkgldjfgjdlkfgjldfjgldjfgldjlfgjdfl..." \
         "sdskdflksdjfbabadfmçgdlkfgjldfjgdjflg..." \
         "dfkjlkgdbdslfbabffkdlkdfşgdkşgjfdjgdg..." \
         "sjdfkjsldkfjbabafdkgdljgdjlfgjdglkdfg..." \
         "dfslfkşsdfjbaabfdşdkfgdkfşglkdşfgkggg..." \
         "fdkgşldkfgldgfjdfgjdgfbabadlfgkdşgkşg..." \
         "dökfdsfdjfgjldkfjgldjfgjldfjgljbsfjlg..." \
         "dfkgkdfgdjfgkdjflgjdlfgjldfjgldjfgljf..." \
         "dfkgldjfgkjdbabaflgdkjgkjldfgklfjgljg"
F = open("sifre.txt")
stringReaded = F.read()
print(find(stringReaded))
