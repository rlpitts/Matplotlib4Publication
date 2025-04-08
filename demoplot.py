import numpy as np
import matplotlib.pyplot as plt
# import matplotlib as mpl
# mpl.use('TkAgg') #use at command line
#mpl.use('Qt5Agg') #if PyQt5 loaded

#mpl.rcParams.update(mpl.rcParamsDefault)
x = np.linspace(-5,5)
# fig, ax = plt.subplots()
# ax.plot(x, np.cos(x),'b-',label='a')
# ax.plot(x, 1/(1+np.exp(-x)), 'r--',label='b')
# ax.set_xlabel('X')
# ax.set_ylabel('Y')
# ax.legend(loc='lower center')
# plt.show()

fig, axes = plt.subplots(ncols=2, figsize=(9,4.5))
axes[0].plot(x, np.cos(x),'b-',  label=r'cos($x$)')
axes[0].plot(x, 1/(1+np.exp(-x)), 'r--',
              label=r'$1/(1+\mathrm{e}^{-x})$')
axes[0].set_xlabel('X')
axes[0].set_ylabel('Y')
axes[0].legend(loc='lower center')
axes[0].tick_params(axis='both', which='both',
                    top=True, right=True) 
axes[0].grid()

Z = np.random.randint(1, 100, (50,50))
img = axes[1].imshow(Z, origin='lower', interpolation='bicubic')
axes[1].set_xlabel(r'$\alpha$')
axes[1].set_ylabel(r'$\delta$')
axes[1].grid(color='k', ls='--')
cb = plt.colorbar(img)
plt.show()
