name = input("Enter file:")
handle = open(name)
dictionary = dict()
lst= list()
for line in handle:
    line = line.rstrip()
    if line.startswith("From"):
        words = line.split()
        lst.append(words)
        #print(words)

for i in range(len(lst)):
    if i % 2 == 0 :continue
else:
        lst.pop(i)

for i in range(len(lst)):
    if lst[i][1] not in dictionary:
        dictionary[lst[i][1]] = 1
    else:
        dictionary[lst[i][1]] += 1

for k,v in dictionary.items():
    print(k,v)
    
