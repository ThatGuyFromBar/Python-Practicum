

def main():
    sumup = 0
    with open("numbers.num", 'rb') as file:
        while (chunk := file.read(2)):
            sumup += int.from_bytes(chunk)
    print(sumup % 0x10000)


if __name__ == "__main__":
    main()
