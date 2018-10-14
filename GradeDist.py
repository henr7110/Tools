import matplotlib.pyplot as plt
labels = ['didnt show',"-3","00","02","4","7","10","12"]
gradeconv = dict(zip(labels,range(len(labels))))
#Grade stistics
KemiOe = [24,9,20,22,21,29,30,10]
Uorge = [3,4,21,19,24,29,23,12]
Matintroe = [5,9,20,12,21,43,31,14]
F1e = [10,4,6,7,6,14,6,1]
F2e = [10,2,2,6,2,8,6,8]
termo = [1,0,4,3,3,9,5,8]
Nanobio1 = [1,0,1,5,6,10,3,6]
Nanobio2 = [3,4,8,4,4,4,5,5]
Nanokvant = [3,0,11,8,5,3,3,5]
Nano3 = [1,0,1,3,5,9,6,7]
KemiKs = [3,1,0,0,3,9,11,23]
Statfys = [7,5,18,14,22,24,14,10]

Kursusnavn = ['KemiO', 'Uorganisk Kemi', 'Matintro', 'F1', 'F2',"Termo",
              "Nanobio1","Nanobio2","Nanokvant","Nano3","KemiKS","Stat Fys"]
karakterer = [KemiOe, Uorge, Matintroe, F1e, F2e,termo,Nanobio1,Nanobio2,
              Nanokvant,Nano3,KemiKs,Statfys]
own = ["12", "12", "12", "10", "12","12","12","12","12","12","12","12"]
def Better(own,other):
    """Calculates fraction above and below own grade
    ---Parameters---
    own: int,
        index of own grade in list ['didnt show',"-3","00","02","4","7","10","12"]
    other: list
        grades given at exam
    ---Returns---
    tuple: (fraction below,fraction at,fraction above)
    """
    #Remove own grade stats from other
    below = float(sum([other[i] for i in range(len(other)) if i < gradeconv[own]]))
    at = other[gradeconv[own]]
    above = float(sum([other[i] for i in range(len(other)) if i > gradeconv[own]]))
    return (below/(below+above+at),at/(below+above+at),(above/(below+above+at)))
    
below,at,above=[],[],[]
for o,k in zip(own,karakterer):
    i = Better(o,k)
    below.append(i[0])
    at.append(i[1])
    above.append(i[2])
fig = plt.figure
ax= plt.subplot()
for b,t in zip([below,at,above],["below","at","above"]):
    ax.hist(b,label=t)
    ax.set_xlim(0,1)
    ax.set_xlabel("fraction")
plt.legend()
plt.tight_layout()
plt.show()
