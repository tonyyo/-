if __name__ == '__main__':
    List = []
    while True:
        string = input()
        if string == "":
            break
        List.append(string)
    file_handle = open('./1.txt', mode='w')
    for string in List:
        file_handle.write("\"" + string.lower() + "\"" + ":" + " " * (21 - len(string)) + string + "," + "\n")
        # file_handle.write(string[2:] + " ")
    file_handle.close()
    print(List)