fname = input("Enter file name: ")
fh = open(fname)
lst=list()
unique = list()
new=list()
i = 0
count =0
for line in fh:
    line = line.rstrip()
    if line.startswith("From"):
        splitedline = line.split()
        lst.append(splitedline)

for i in range(len(lst)):
    if i % 2 == 0 :
        unique.append(lst[i])

for i in range(len(unique)):
        new.append(unique[i][1])

for email in new:
    count=count + 1
    print(email)

print(count)


#for email in lst:
    #if email not in unique:
        #unique.append(email)
