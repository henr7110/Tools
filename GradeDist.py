import matplotlib.pyplot as plt
labels = ['didnt show',-3,00,02,4,7,10,12]
KemiOe = [24,9,20,22,21,29,30,10]
KemiOr = [4,2,3,3,4,3,0,0]
Uorge = [3,4,21,19,24,29,23,12]
Uorgr = [2,1,9,3,3,3,0,0]
Matintroe = [5,9,20,12,21,43,31,14]
Matintror = [0,2,5,4,2,2,0,0]
F1e = [10,4,6,7,6,14,6,1]
F1r = [0,0,3,1,2,1,1,0]
F2e = [10,2,2,6,2,8,6,8]
F2r = [None]

Kursusnavn = ['KemiO', 'Uorganisk Kemi', 'Matintro', 'F1', 'F2']
karakterer = [KemiOe, Uorge, Matintroe, F1e, F2e]
[len(i) for i in karakterer]
own = [12, 12, 12, 10, 12]
count = 0
fig, (ax1,ax2,ax3,ax4,ax5) = plt.subplots(5,1)
for i,kursus,navn in zip((ax1,ax2,ax3,ax4,ax5),karakterer,Kursusnavn):
    i.bar(labels,kursus)
    i.set_label(navn)
plt.show()
