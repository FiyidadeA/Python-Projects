fname = input('Enter filename: ')
if len(fname) < 1 : fname = 'mbox.txt'
legs = open(fname)

di = dict()
for line in legs:
    lin = line.rstrip()
    #print(lin)
    spl = lin.split()
    for x in spl:
        #print(x)
        di[x] = di.get(x,0) +1
        #print(x,di[x])

highest = 0
word = None
for k,v in di.items() :
    if (v) > highest:
        highest = v
        word = k
        print('The most common word in this file is: ', word, highest)
