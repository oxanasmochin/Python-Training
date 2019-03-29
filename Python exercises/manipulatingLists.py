fname = input("Enter file name: ")
fh = open(fname)
lst = list()
unique = list()
i=0
for line in fh:
    line=line.rstrip()
    print(line)

    words = line.split()
    lst.append(words)

for i in range(len(lst)):
    for elem in lst[i]:
        if elem not in unique:
            unique.append(elem)

unique.sort()
print(unique)


#newlst = list()
#newlst.append(lst[0]+lst[1]+lst[2]+lst[3])
