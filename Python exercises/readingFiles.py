#fname = input("Enter file name: ")
#fh = open(fname)
#text = fh.read()
#print(text.upper())
# this code opens a words.txt file reads it and transforms all characters into
# upper case and prints it

fname = input("Enter file name: ")
fh = open(fname)
count = 0
av = 0
sl = 0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:") :
        count = count+1
        twodotspos = line.find(':')
        slice = line[twodotspos+1 : ]
        slice.strip()
        sl=float(slice)
        av=av+sl



print("Done")
print(count)
print(av)
print(av/count)

#print(avg/count)
