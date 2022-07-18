src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
#for i in range(len(src)-1):
    #a = src[i]
    #i += 1
    #b = src[i]
    #if b > a:
        #print(b)
def func_src():
    for i in range(len(src)-1):
        a = src[i]
        i += 1
        b = src[i]
        if b > a:
            yield b

new_src = func_src()
print(type(new_src))
print(next(new_src), next(new_src))
for i in new_src:
    print(i)


