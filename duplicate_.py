def read(name_of_textfile):
    step = ""
    f = open(name_of_textfile, "r")
    step = f.read()
    f.close()
    return step


def split(text):
    return text.split()


def my_function(x):
    return list(dict.fromkeys(x))


def write(textfile, text):
    f = open(textfile, "a")
    f.write(text)
    f.close()


def main(textfile):
    step = read(textfile)
    print(len(step))
    print(1)
    contlist = split(step)
    print(contlist)
    print(len(contlist))
    const2list = my_function(contlist)
    print(const2list)
    print(len(const2list))
    compiled_list = ""
    for new in const2list:
        compiled_list = compiled_list + new + " "

    write("ans.txt", compiled_list)
    print(compiled_list)
    print(4)


if __name__ == '__main__':
    main("ans.txt")
