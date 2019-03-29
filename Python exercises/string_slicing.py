text = "X-DSPAM-Confidence:    0.8475"
nolpos = text.find('0') //23
fivepos = text.find('5') //28
slice = text[nolpos : fivepos + 1]
float(slice)
