
# The author: haoyan zhang
#E-mail: haoy.zhang@foxmail.com



import numpy as np

class solve(object):
    def __init__(self):
        pass
    def sta_a(self,c):
    
        c.calc_deleted_KG_matrix()
    
        KG,Force = c.KG_keeped,c.Force_keeped
        c._Disp_keeped = np.linalg.solve(KG,Force)
    
    
        for i,val in enumerate(c.keeped):
            I = val%c.mndof
            J = int(val/c.mndof)
            c.nodes[J].disp[c.nAk[I]] = c.Disp_keeped[i]
    
                    
        for el in c.get_elements():
            el.evaluate()
    
        c._is_c_solved = True

    def kin_a(self,c):
        from scipy import linalg as sl
        if not c._is_inited:
            c.calc_KG()
        c.calc_deleted_KG_matrix()
        c.calc_MG()
        c.calc_deleted_MG_matrix()
        
        w1,self.model = sl.eig(c.KG_keeped,c.MG_keeped)
        self.w = np.sqrt(w1)
        T = 2*np.pi/self.w
        self.freq = 1/T
        
    def newmark_beta(self,c,omega,pxi1=0.02,pxi2=0.04,n1=256,delta=0.5,beta=0.25):

        from scipy import linalg as sl
        w1,model = sl.eigh(c.KG_keeped,c.MG_keeped)
        f = np.sqrt(w1)
        omega1= f[1]
        omega2= f[0]
        aa=2*omega1*omega2*(pxi1*omega2-pxi2*omega1)/(omega2**2-omega1**2)
        bb=2*(omega2*pxi2-omega1*pxi1)/(omega2**2-omega1**2)
        C=aa* c._MG_keeped+bb* c._KG_keeped
    
        dt=2*np.pi/(omega*n1)
        
        N=60*n1
        self.wy=np.zeros(( c._KG_keeped.shape[0],N+1))
        sd=np.zeros(( c._KG_keeped.shape[0],N+1))
        jsd=np.zeros(( c._KG_keeped.shape[0],N+1))
        a0=1/(beta*dt**2);
        a1=delta/(beta*dt)
        a2=1/(beta*dt)
        a3=1/(2*beta)-1
        a4=delta/beta-1
        a5=dt/2*(delta/beta-2)
        a6=dt*(1-delta)
        a7=delta*dt
        P1=a0* c._MG_keeped+a1* C+ c._KG_keeped
        for i in np.arange(0,N):
            t=i*dt
            Qe= c._Force_keeped*np.sin(omega*t)+np.dot( c._MG_keeped,(a0* self.wy[:,i-1]+a2* sd[:,i-1]+a3* jsd[:,i-1]))+np.dot( C,(a1* self.wy[:,i-1]+a4* sd[:,i-1]+a5* jsd[:,i-1]))
            self.wy[:,i]=np.dot(np.linalg.inv( P1), Qe)
            jsd[:,i]=a0*( self.wy[:,i]- self.wy[:,i-1])-a2* sd[:,i-1]-a3* jsd[:,i-1]
            sd[:,i]= sd[:,i-1]+a6* jsd[:,i-1]+a7* jsd[:,i]


    def nonl_fri(self,K,M,Omega,n,n_0,freq1=253.52,freq2=1582.96,rho=7850,b=0.06, h=0.007,L=0.15,R=0.35,y1=0.04,y2=0.04,Amp_ex=500,kjq=8e6,miu=0.2,alfa=0.25,beta=0.5):
        
        sdof=2*(1+n)-1
        omega_ex=n_0*Omega
        sunalpha=(1/3)*np.pi
        sunbeta=sunalpha
        A=b*h
        oumiga1=freq1*2*np.pi;oumiga2=freq2*2*np.pi;
        
        alafa=2*(y2/oumiga2-y1/oumiga1)/(1/(oumiga2**2)-1/(oumiga1**2));
        beita=2*(y2*oumiga2-y1*oumiga1)/(oumiga2**2-oumiga1**2);
        C=alafa*M+beita*K;
        
        n3=512;
        dt=2*np.pi/(omega_ex*n3);
        nt=600*n3;
        
        f_fric=np.random.rand(1)/1e30;f_fric_v=np.zeros((sdof,1));
        f_fric_v[0]=-2*f_fric;
        f0=np.zeros((sdof,1));
        d_former=np.random.rand(1)/1e30;w_former=np.random.rand(1)/1e30;
        
        N1=rho*A*Omega**2*(((R+L)**2-R**2)/2)
        N2=N1*(np.cos(sunbeta)/np.sin(sunalpha+sunbeta))
        
        x1=np.random.rand(sdof,1)/1e30
        v1=np.random.rand(sdof,1)/1e30
        
        aa=np.dot(np.linalg.inv(M),f0-np.dot(C,v1)-np.dot(K,x1))
        a0=1/(alfa*dt**2);
        a1=beta/(alfa*dt)
        a2=1/(alfa*dt)
        a3=1/(2*alfa)-1
        a4=beta/alfa-1
        a5=dt/2*(beta/alfa-2)
        a6=dt*(1-beta)
        a7=beta*dt
        ke=K+a0*M+a1*C
        
        self.xt=[]
        self.xo=[]
        self.fo=[]
        self.xd=[]
        for i in range(nt):
            
            t=(i+1)*dt
            fi=Amp_ex*np.cos(omega_ex*t)
            f0[29]=fi
    
            f2=f0+f_fric_v
            fe=f2+np.dot(M,a0*x1+a2*v1+a3*aa)+np.dot(C,a1*x1+a4*v1+a5*aa)
            x2=np.dot(np.linalg.inv(ke),fe)
            aa2=a0*(x2-x1)-a2*v1-a3*aa
            v2=v1+a6*aa+a7*aa2
            x1=x2
            v1=v2
            aa=aa2
            d_curent=x1[0]/np.sin(sunalpha)
            
            if kjq*(abs(d_curent-w_former)[0])<miu*N2:
                f_fric=kjq*(d_curent-w_former)
                w_curent=w_former
            elif kjq*(abs(d_curent-w_former)[0])>=miu*N2:
                f_fric=miu*N2*np.sign(d_curent-w_former)
                w_curent=d_curent-miu*N2/kjq*np.sign(f_fric)
            f_fric_v[0]=-2*f_fric*np.sin(sunalpha)
            d_former=d_curent
            w_former=w_curent
            
            if i+1>100*n3:
    
                self.xt.append(t)
                self.xo.append(x1[0])
                self.fo.append(f_fric)
                self.xd.append(v1[0])



