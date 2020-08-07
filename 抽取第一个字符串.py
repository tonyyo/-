List = []
while True:
    try:
        s1, s2 = input().split()
        List.append(s1)
    except:
        break
file_handle = open('./3.txt', mode='w')
for string in List:
    first = string
    for i in string:
        num = ord(i)  # 得到ASCII码
        if (65 <= num <= 90):
            string = string.replace(i, "_" + chr(num + 32))
    file_handle.write("%type <" + first + "> " + string + "\n")
file_handle.close()