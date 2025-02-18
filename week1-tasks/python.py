ls = [1,2,3,4,5]
ls = [items*2 for items in ls]
print(list(filter(lambda x: x%2==0, ls)))