"""Author: Henrik Pinholt
Created: Friday 6. July 2018 kl. 14.09
Script that grabs a .xyz position file containing a unit cell and translates the
cell in all directions n times.
"""

def coordshifter(mtimes,line):
    """Function that translate the atom specified in line along the mtimes vector
    --------------Parameters------------
    mtimes: np.array(1,3),
            vector specifying the translation direction ie. [1,0,0] means 1 time
            in the x-diretion and zero in the other directions
    line: str, xyz format
            string specifying the location of the atom to be translated like:
            "O         7.5735963725        0.4690575137        6.3748499338"
    """
    #Get location of atom
    vals = line.split()
    #Transport in all three dimensions x,y,z by looping
    for i,c in zip(range(3),mtimes):
        #Update position
        p = float(vals[i+1])
        p = p + blen*c
        vals[i+1] = p
    #Save in xyz format and append to the new file
    newline = "%s        %.18g        %.18g        %.18g" %(vals[0],float(vals[1]),float(vals[2]),float(vals[3]))
    newfile.append(newline)

#-------------Initialize-----------
n = 1 #Number of translations
path = "Cluster_start_NaCl_2M.xyz"
file = open(path,"r")
blen = 12.4138 #Å, the length of the unit cell used to translate
newfile = []
i = 0
shiftvals = []
filename = "NaCl-trans1small.xyz" # name of output file

#------------Generate the translation vectors--------
for x in range(n+1):
    for y in range(n+1):
        for z in range(n+1):
            shiftvals.append([x,y,z])

#-----------Itterate through the xyz file and translate all atoms---------
for line in file:
    #Copy header to new file
    if i ==1 or i == 0:
        newfile.append(line.strip("\n"))
    else:
        for coords in shiftvals: #Translate the atom in all directions
            coordshifter(coords,line)
    i += 1

# ----------Save the new xyz file---------
out = open(filename,"w")
out.write(str(len(newfile[2:])) + "\n")
for i in newfile[1:]:
    out.write("%s\n" % i.strip("\n"))
out.close()
