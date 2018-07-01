def find(string):
    for i in range(len(string)):
        if string[i:i+len("@")] == "@":
            return True
    return False

def textWrite(string):
    file = open("textnew.txt", "a")
    file.write("\n")
    file.write(string)
    file.close()

f = open("text.txt", "r")
for line in f:
    searchWord = f.readline()
    if find(searchWord):
        textWrite(searchWord)