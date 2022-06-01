def thesaurus(ls):                                     
    d = {}
    for i in ls:
        d.setdefault(i[0], [])
        if i not in d:
            d[i[0]].append(i)
    return d


ls = ("Иван", "Мария", "Петр", "Илья")
print(thesaurus(ls))