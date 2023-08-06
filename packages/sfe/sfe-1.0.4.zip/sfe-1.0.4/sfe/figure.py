
# The author: haoyan zhang
#E-mail: haoy.zhang@foxmail.com


def no_conn(L,end = False):
    pool = tuple(L)
    n = len(pool)
    assert n >=2,"Length of iterable must greater than 3"
    if end is True:
        indices = list(range(n))
        for i in indices:
            if i < n -1:
                yield (pool[i],pool[i+1])
            else:
                yield (pool[i],pool[0])
    if end is False:
        indices = list(range(n-1))
        for i in indices:
            yield (pool[i],pool[i+1])
    
import matplotlib.pyplot as plt
import numpy as np

from matplotlib.font_manager import FontProperties
font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=15)

def Resp(nn,wy,n1=256):
    N=60*n1
    T=np.linspace(0,N+1,N+1)
    xX1=wy[2*nn-1,:]
    plt.figure(1)
    plt.plot(T,xX1,'b')
    plt.title('pyplot x1-t')
    plt.xlabel('time(s)')
    plt.ylabel('x1')
    return plt.figure(1)

def Vib_mode(model,n,L,ord_n):
    V1=model[:,2*n-ord_n]
    V1=V1[0:2*n:2]
    V_1=np.zeros(n+1)
    V_1[0]=0
    V_1[1:n]=V1[0:n-1]
    x=np.arange(0,n+1,1)
    plt.figure(2)
    plt.plot(x*(L/n)*1000,V_1/max(abs(V_1)))
    plt.xlim(0,1200)
    plt.title('振型图',fontproperties=font)
    return plt.figure(2)

def Spectrum(omega,nn,wy,n1=256):
    signal=wy[2*nn-1,9000:]
    dt=2*np.pi/(omega*n1)
    Fs=1/dt
    Num=len(signal)
    Num1=int(Num/2)
    X=signal-np.mean(signal)
    y=np.fft.fft(X,Num-1)
    y1=2*abs(y)/Num
    n2=np.arange(0,Num1,1)
    f=Fs*n2/Num
    plt.figure(3,figsize=(8,8)) 
    f_out=f[1:Num1]
    y1_out=y1[1:Num1]
    plt.plot(f_out,y1_out)

    plt.title('频谱图',fontproperties=font)
    return plt.figure(3)

def With_fri_resp(x,y):
    plt.figure(4)
    plt.plot(x,y)

def Frictional_resp(x,y):
    plt.figure(5)
    plt.plot(x,y)
    
def Fri_hysteresis_curve(x,y):
    plt.figure(6)
    plt.plot(x,y)