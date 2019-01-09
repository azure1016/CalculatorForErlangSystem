
import matplotlib.pyplot as plt
import math
import numpy as np
import matplotlib.patches as mpatches
import statistics
import scipy
from statistics import mode
from scipy.stats import skew
from decimal import getcontext
from decimal import Decimal
import plotly.plotly as pl
import plotly.graph_objs as go

getcontext().prec = 3

base = []

with open('breast-cancer-wisconsin.data.txt','r') as file:
	data = file.readlines()

	for line in data:
		per = line.split(',')
		base.append(per)

#transform the base
t_base = []
for i in range(0, 9):
	t_base.append([int(x[i+1]) for x in base])

#get the mean
mean = []
for l in t_base:
	mean.append(np.mean(l))

#print(type(x))
mean = [Decimal(float(x)).quantize(Decimal("0.00")) for x in mean]

print(mean)

#get the mode
mod = []
for l in t_base:
    mod.append(mode(l))

#print(mod)


#get the skewness:
sk = []
for l in t_base:
    sk.append(skew(np.array(l).astype(np.float)))
#print(sk)


#get the deviation
stdevs = []
for l in t_base:
   stdevs.append(statistics.stdev(l))
#print(stdevs)

#get the variance
vars = []
for l in t_base:
    vars.append(np.var(l))
#print(vars)

#calculate the pcc:
col = []
tab = []
for i in range(0, 9):
    col.clear()
    for j in range(0, 9):
        if i != j:
            col.append(scipy.stats.pearsonr(t_base[i], t_base[j]))
    tab.append(col)


#req 1: mode ,skew, stc
trace = go.Table(
	header = dict(values = ["mean", "mode", "skewness", "standard deviation", "variance"]),
	cells = dict(values = [mean, mod, sk, stdevs, vars])
)

data = [trace]
pl.plot(data, filename = "req1")

def pic(log, y1, y1_error, y2, y2_error, leg, ylabel, y1label, y2label, title):
	x = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]

	plt.grid(True)
	plt.errorbar(x, y1, yerr=y1_error, fmt='-o', label = y1label)
	plt.errorbar(x, y2, yerr=y2_error, fmt='-o', label = y2label)
	plt.legend(loc=leg)
	plt.xlabel('Number of Vertices')
	plt.title('Approximation Ratio of APR1 & APR2')
	plt.ylabel(ylabel)
	if log > 0:
		plt.semilogy(x, y1)
		plt.semilogy(x, y2)
	plt.title(title)
	plt.show()

def pic3(log, y1, y1_error, y2, y2_error, y3, y3_error, leg, ylabel, y1label, y2label, y3label, title):
	x = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]

	plt.grid(True)
	plt.errorbar(x, y3, yerr=y3_error, fmt='-o', label = y3label)
	plt.errorbar(x, y1, yerr=y1_error, fmt='-o', label=y1label)
	plt.errorbar(x, y2, yerr=y2_error, fmt='-o', label = y2label)
	plt.legend(loc=leg)
	plt.xlabel('Number of Vertices')
	plt.ylabel(ylabel)
	if log > 0:
		plt.semilogy(x, y1)
		plt.semilogy(x, y2)
		plt.semilogy(x, y3)
	plt.title(title)
	plt.show()

def pic1(log, y1, y1_error, leg, ylabel, y1label, title):
	x = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]

	plt.grid(True)
	plt.errorbar(x, y1, yerr=y1_error, fmt='-o', label=y1label)
	plt.legend(loc=leg)
	plt.xlabel('Number of Vertices')
	plt.ylabel(ylabel)
	if log > 0:
		plt.semilogy(x, y1)
	plt.title(title)
	plt.show()
