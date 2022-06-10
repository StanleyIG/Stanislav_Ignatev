from time import perf_counter
import sys

start = perf_counter()

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = []
for i in src:
    if src.count(i) == 1:
        result.append(i)
result_sum = sum(result)
print(sys.getsizeof(result))
#print(result, perf_counter() - start)
print(result_sum, perf_counter() - start)

new_src = (i for i in src if src.count(i)==1)
new_src_gen = sum(new_src)
print(sys.getsizeof(new_src))
print(new_src_gen, perf_counter() - start)

#new_src_comp = [i for i in src if src.count(i)==1]
#new_src_comp_sum = sum(new_src_comp)
#print(sys.getsizeof(new_src_comp))
#print(new_src_comp_sum, perf_counter() - start)









