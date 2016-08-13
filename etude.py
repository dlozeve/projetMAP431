
# coding: utf-8

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().magic('matplotlib inline')


evP1 = pd.read_table("fleche/eigenvaluesP1.txt",
                     dtype={'names': ['points', 'l1', 'l2', 'l3', 'l4', 'l5', 'l6', 'l7', 'l8', 'l9', 'l10', 'l11', 'l12'],
                                             'formats': ['i', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f']},
                     names = ['points', 'l1', 'l2', 'l3', 'l4', 'l5', 'l6', 'l7', 'l8', 'l9', 'l10', 'l11', 'l12'],
                     delim_whitespace=True, header=0)
evP2 = pd.read_table("fleche/eigenvaluesP2.txt",
                     dtype={'names': ['points', 'l1', 'l2', 'l3', 'l4', 'l5', 'l6', 'l7', 'l8', 'l9', 'l10', 'l11', 'l12'],
                                             'formats': ['i', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f']},
                     names = ['points', 'l1', 'l2', 'l3', 'l4', 'l5', 'l6', 'l7', 'l8', 'l9', 'l10', 'l11', 'l12'],
                     delim_whitespace=True, header=0)
evP3 = pd.read_table("fleche/eigenvaluesP3.txt",
                     dtype={'names': ['points', 'l1', 'l2', 'l3', 'l4', 'l5', 'l6', 'l7', 'l8', 'l9', 'l10', 'l11', 'l12'],
                                             'formats': ['i', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f']},
                     names = ['points', 'l1', 'l2', 'l3', 'l4', 'l5', 'l6', 'l7', 'l8', 'l9', 'l10', 'l11', 'l12'],
                     delim_whitespace=True, header=0)


plt.figure(figsize=(12,8*3),dpi=80)
for i in range(1,13):
    plt.subplot(6,2,i)
    plt.plot(evP1.points,evP1['l'+str(i)],evP2.points,evP2['l'+str(i)],evP3.points,evP3['l'+str(i)])


plt.figure(figsize=(12,8),dpi=80)
sns.set_style("whitegrid")
plt.plot(evP1.points,evP1['l1'],evP2.points,evP2['l1'],evP3.points,evP3['l1'])


