N = input()
library = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for i in library:

    N = N.replace(i , "1")
print(len(N))



