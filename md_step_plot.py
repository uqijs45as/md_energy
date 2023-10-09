# -*- coding:utf-8 -*-

import os
import re
import linecache
import math
import numpy as np
from scipy import optimize
from matplotlib import pyplot as plt
os.chdir(os.path.split(os.path.realpath(__file__))[0])

plt.rcParams['font.sans-serif'] = ['Arial']
fontsize1=16
fontsize2=18

a = open('OUTCAR')
c = open('energy0', 'w+')
for n, line in enumerate(a):
    if "  FREE ENERGIE OF THE ION-ELECTRON SYSTEM" in line:
        a1 = linecache.getlines('OUTCAR')[n + 4]
        a1 = a1.strip()
        a1 = a1[-54:-36]
        c.write(a1 + '\n')
c.close()
a.close()

c = open('energy0')
b = open('md_step_ene.dat', 'w+')
for n, line in enumerate(c):
    line = line.strip()
    print(str(n + 1), ' ', line, file=b)
b.close()
c.close()

os.remove('energy0')

######

a1 = np.loadtxt('md_step_ene.dat', skiprows=0)
a2 = a1[:, 0]  # x
a3 = a1[:, 1]  # y
plt.xticks(fontsize=fontsize1)
plt.yticks(fontsize=fontsize1)
plt.xlabel('Time (fs)', fontsize=fontsize2)
plt.ylabel('Energy (eV)', fontsize=fontsize2)
plt.xlim(0, 5000)  # x显示区间
# plt.ylim(-130, -120)  # y显示区间

plt.grid(True)
plt.plot(a2, a3, 'tab:blue', label='xxx')

# plt.legend(loc='best', fontsize=fontsize1)
plt.tight_layout() #调整整体空白
plt.savefig('md_step_ene.jpg', dpi=300)  # 屏幕显示pic，可注释
# plt.show()














