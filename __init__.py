if __name__ == '__main__':
    List = []
    while True:
        string = input()
        if string == "":
            break
        List = string.split()
    file_handle = open('面试题/1.txt', mode='w')
    for string in List:
        # file_handle.write("\"" + string.lower() + "\"" + ":" + " " * (21 - len(string)) + string + "," + "\n")
        file_handle.write(string + "\n")
    file_handle.close()
    print(List)