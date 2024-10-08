def main():
    s = input()
    order = s.split()
    ans = 0
    j = 0
    p1 = 0
    p2 = 0
    for i in range(len(order)):
        if order[i] == "+":
            j = i
            p1 = "!"
            p2 = "!"
            while j >= 0:
                j -= 1
                if "+-*/~!#@".count(str(order[j])) == 0:
                    if p1 == "!":
                        p1 = j
                    elif p2 == "!":
                        p2 = j
                        break
            order[p1] = int(order[p1]) + int(order[p2])
            order[p2] = "*"
        elif order[i] == "-":
            j = i
            p1 = "!"
            p2 = "!"
            while j >= 0:
                j -= 1
                if "+-*/~!#@".count(str(order[j])) == 0:
                    if p1 == "!":
                        p1 = j
                    elif p2 == "!":
                        p2 = j
                        break
            order[p1] = int(order[p2]) - int(order[p1])
            order[p2] = "*"
        elif order[i] == "*":
            j = i
            p1 = "!"
            p2 = "!"
            while j >= 0:
                j -= 1
                if "+-*/~!#@".count(str(order[j])) == 0:
                    if p1 == "!":
                        p1 = j
                    elif p2 == "!":
                        p2 = j
                        break
            order[p1] = int(order[p1]) * int(order[p2])
            order[p2] = "*"
        elif order[i] == "/":
            j = i
            p1 = "!"
            p2 = "!"
            while j >= 0:
                j -= 1
                if "+-*/~!#@".count(str(order[j])) == 0:
                    if p1 == "!":
                        p1 = j
                    elif p2 == "!":
                        p2 = j
                        break
            order[p1] = int(order[p2]) // int(order[p1])
            order[p2] = "*"
        elif order[i] == "~":
            j = i
            p1 = "!"
            while j >= 0:
                j -= 1
                if "+-*/~!#@".count(str(order[j])) == 0:
                    if p1 == "!":
                        p1 = j
                        break
            order[p1] = -int(order[p1])
        elif order[i] == "#":
            j = i
            p1 = "!"
            while j >= 0:
                j -= 1
                if "+-*/~!#@".count(str(order[j])) == 0:
                    if p1 == "!":
                        p1 = j
                        break
            order[i] = int(order[p1])
        elif order[i] == "!":
            j = i
            p1 = "!"
            while j >= 0:
                j -= 1
                if "+-*/~!#@".count(str(order[j])) == 0:
                    if p1 == "!":
                        p1 = j
                        break
            tempus = int(order[p1])
            order[p1] = 1
            for k in range(2, tempus + 1):
                order[p1] = order[p1] * k
        elif order[i] == "@":
            j = i
            p1 = "!"
            p2 = "!"
            p3 = "!"
            while j >= 0:
                j -= 1
                if "+-*/~!#@".count(str(order[j])) == 0:
                    if p1 == "!":
                        p1 = j
                    elif p2 == "!":
                        p2 = j
                    elif p3 == "!":
                        p3 = j
                        break
            tempus = int(order[p3])
            order[p3] = int(order[p2])
            order[p2] = int(order[p1])
            order[p1] = tempus
        ans = order[p1]
    print(ans)


if __name__ == "__main__":
    main()
