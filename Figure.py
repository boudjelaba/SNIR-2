import matplotlib
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,2*np.pi,0.1)
y = np.sin(x)

Age = 20
Nom = 'Carnus'
note1 = '10.5'
note2 = '13.0'

fig = plt.figure()
ax = plt.subplot(111)
ax.plot(x, y, label=r'$y = sin(\omega t)$')
ax.set_xlabel('Temps')
ax.set_ylabel('Amplitude')
plt.grid()
plt.title('BTS SNIR - Nom : '+Nom+', Age : '+str(Age)+' ans, Notes : '+str(note1)+', '+str(note2))
ax.legend()
plt.show()

#fig.savefig('/CHEMIN/ma_figure.png')
#fig.savefig('/CHEMIN/ma_figure1.pdf')
#fig.savefig('/CHEMIN/ma_figure3.svg')
#fig.savefig('/CHEMIN/ma_figure4.jpg',edgecolor ='w', facecolor ="g",dpi=300) 