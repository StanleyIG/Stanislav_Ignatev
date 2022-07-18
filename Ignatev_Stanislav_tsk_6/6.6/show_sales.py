def show_sales(argv):
    with open('bakery.csv.', 'r', encoding='utf-8') as f:
        if len(argv) == 2 and argv[1].isdigit():
            print(*f.readlines()[int(argv[1])])
        elif len(argv) == 3 and argv[1].isdigit() and argv[2].isdigit():\
            print(*f.readlines()[int(argv[1]):int(argv[2])])
        return f.read()


if __name__ == '__main__':
    import sys

    exit(show_sales(sys.argv))
