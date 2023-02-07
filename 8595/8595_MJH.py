N = input()
string = input()
result = 0
tmpstr = ''
for letter in string:
    if 48 <= ord(letter) <= 57:
        tmpstr += letter
    elif len(tmpstr) > 0:
        result += int(tmpstr)
        tmpstr = ''
if len(tmpstr) > 0:
    result += int(tmpstr)
print(result)