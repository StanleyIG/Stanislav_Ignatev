def add_sale(argv):
    with open('bakery.csv', 'a', encoding='utf-8') as f:
            program, *args = argv
            f.writelines(str(*args) + '\n')

if __name__ == '__main__':
    import sys
    exit(add_sale(sys.argv))

