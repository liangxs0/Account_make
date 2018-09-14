#绘制折现函数

import matplotlib.pyplot as plt
from pylab import *

def DrawLine():
    mpl.rcParams['font.sans-serif'] = ['SimHei']
    names = ['5','10','15','20','25']
    x = range(len(names))
    y = [0.86,0.85,0.84,0.83,0.82]
    y1 = [0.855,0.84,0.839,0.83,0.81]
    #pl.xlim() 限定横轴的范围
    #pl.ylim() 限定纵轴的范围
    plt.plot(x,y,marker='o',mec='r',mfc='w',label=u'y=x^2曲线图')
    plt.plot(x,y1,marker='*', ms=10,label=u'y=x^3曲线图')
    plt.legend()#图列生效
    plt.xticks(x,names,rotation=45)
    plt.margins(0)
    plt.subplots_adjust(bottom=0.15)
    plt.xlabel(u"times(s)邻居")
    plt.ylabel(u"RMES")
    plt.title("------")
    plt.show()


