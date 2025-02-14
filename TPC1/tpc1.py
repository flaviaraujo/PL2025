on = True
r = 0

while True:
    try:
        line = input()
    except EOFError:
        print(r)
        break

    i = 0
    while i < len(line):
        if line[i:i+2].lower() == "on":
            on = True
            i += 2
        elif line[i:i+3].lower() == "off":
            on = False
            i += 3
        elif line[i] == "=":
            print(r)
            i += 1
        elif line[i].isdigit() and on:
            n = ""
            while i < len(line) and line[i].isdigit():
                n += line[i]
                i += 1
            r += int(n)
        else:
            i += 1
