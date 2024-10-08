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
                if order[j] != "+" and order[j] != "-" and order[j] != "*":
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
                if order[j] != "+" and order[j] != "-" and order[j] != "*":
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
                if order[j] != "+" and order[j] != "-" and order[j] != "*":
                    if p1 == "!":
                        p1 = j
                    elif p2 == "!":
                        p2 = j
                        break
            order[p1] = int(order[p1]) * int(order[p2])
            order[p2] = "*"
        ans = order[p1]
    print(ans)


if __name__ == "__main__":
    main()
