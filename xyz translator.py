path = "/Users/Henrik/Documents/Studie:karriere/Bachelor/OneDrive - Københav"+\
       "ns Universitet/forskning/Improving ab inito simulations of ion hydra"+\
       "tion/scripts/Cluster_start_NaCl_2M.xyz"
file = open(path,"r")
blen = 12.4138 #Å
def coordshifter(mtimes,line):
    vals = line.split()
    for i,c in zip(range(3),mtimes):
        if c != 0:
            p = float(vals[i+1])
            p = p + blen*c
            vals[i+1] = p
    newline = "%s        %.18g        %.18g        %.18g" %(vals[0],float(vals[1]),float(vals[2]),float(vals[3]))
    newfile.append(newline)
newfile = []
i = 0
shiftvals = []
for x in [0]:
    for y in [0]:
        for z in [0]:
            shiftvals.append([x,y,z])
for line in file:
    if i ==1 or i == 0:
        print "header: " + line
        newfile.append(line.strip("\n"))
    else:
        print line
        for coords in shiftvals:
            coordshifter(coords,line)
        vals = line.split()
        newline = "%s        %.18g        %.18g        %.18g" %(vals[0],float(vals[1]),float(vals[2]),float(vals[3]))
        newfile.append(line[1:])
    i += 1
out = open("NaCl-trans1small.xyz","w")
# s = list(newfile[0])
# s[-3:] = list(str(len(newfile)))
# newfile[0] = "".join(s)
out.write(str(len(newfile[2:])) + "\n")
for i in newfile[1:]:
    out.write("%s\n" % i.strip("\n"))
out.close()
