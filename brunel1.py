import numpy as np
import matplotlib.pyplot as pl

data = np.genfromtxt('fileUno.csv')

select= np.array([d for d in data if d[1]<30])
data1= select.transpose()
pl.xlim(500,600)
pl.scatter(data1[0],data1[1],alpha=0.8, edgecolors='none');
pl.show();
n, bins, patches = pl.hist(data1[0], 200, range=(500,600), normed=0, alpha=0.75)
pl.show(); 
