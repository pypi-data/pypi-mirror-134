
# The author: haoyan zhang
#E-mail: haoy.zhang@foxmail.com



from sfeee.Node import *
from sfeee.Element import *
from sfeee.Element_Type import *




class cal_comb(object):

    def __init__(self,l=1,R=1,L=1,rho=1,Omega=0,A=1,element='Beam1D11',E=1,G=5/6,I=1,k=1):
        self.nodes = {}
        self.elements = {}
        self._mndof = None
        self._nAk = None
        self._nBk = None
        self._dim = 0
        self._Force = {}
        self._Disp = {}        
        self._is_inited = False
        self._is_force_added = False
        self._is_disp_added = False
        self._is_system_solved = False
        self.L=L
        self.rho=rho
        self.A=A
        self.l=l
        self.R=R
        self.Omega=Omega
        self.element=element
        self.E=E
        self.G=G
        self.I=I
        self.k=k

        
    
        
    @property
    def mndof(self): 
        return self._mndof
    
    @property
    def dim(self):
        return self._dim
    
    @property
    def nAk(self):
        return self._nAk
    @property
    def nBk(self):
        return self._nBk
    @property
    def non(self):
        return len(self.nodes)

    @property
    def noe(self): 
        return len(self.elements)
    
    def add_node(self,node):
        assert issubclass(type(node),Node),"Must be Node type"
        n = self.non
        if node.numb is None:
            node._numb = n
        self.nodes[node.numb] = node

    def add_element(self,element):
        assert issubclass(type(element),Element),"Must be Element type"
        n = self.noe
        if element.numb is None:
            element._numb = n
        self.elements[element.numb] = element

    def add_nodes(self,*nodes):
        for nd in nodes:
            if isinstance(nd,list) or isinstance(nd,tuple) or isinstance(nd,np.ndarray):
                for n in nd:
                    self.add_node(n)
            else:
                self.add_node(nd)
                
    def add_elements(self,*els):
        for el in els:
            if isinstance(el,list) or isinstance(el,tuple) or isinstance(el,np.ndarray):
                for e in el:
                    self.add_element(e)
            else:
                self.add_element(el)


    def get_nodes(self):
        return self.nodes.values()

    def get_elements(self):
        return self.elements.values()



    def __repr__(self):
        return "%dD System: \nNodes: %d\nElements: %d"\
               %(self.dim,self.non,self.noe,)
    
    @property
    def Force(self):
        return self._Force


    @property
    def Disp(self):
        return self._Disp

    @property
    def DispValue(self):
        return self._DispValue

    @property
    def ForceValue(self):
        return self._ForceValue
    
    @property
    def KC(self):
        return self.calc_KC(l=self.l,R=self.R,L=self.L,rho=self.rho,Omega=self.Omega,A=self.A,element=self.element,E=self.E,I=self.I,G=self.G,k=self.k)
    
    @property
    def KG(self):
        return self._KG+self.KC
    
    @property
    def MG(self):
        return self._MG
    


    @property
    def KG_keeped(self):
        return self._KG_keeped
    


    @property
    def MG_keeped(self):
        return self._MG_keeped

    @property
    def Force_keeped(self):
        return self._Force_keeped

    @property
    def Disp_keeped(self):
        return self._Disp_keeped

    @property
    def deleted(self):
        return self._deleted

    @property
    def keeped(self):
        return self._keeped


    def init(self):
        self._mndof = max(el.ndof for el in self.get_elements())
        self._nAk = self.nodes[0].nAk[:self.mndof]
        self._nBk = self.nodes[0].nBk[:self.mndof]
        self._dim = self.nodes[0].dim

    def calc_KG(self):
        self.init()
        n = self.non
        m = self.mndof
        shape = n*m
        self._KG = np.zeros((shape,shape))
        for el in self.get_elements():
            numb = [nd.numb for nd in el.nodes]
            el.calc_Ke()
            M = el.ndof
            for N1,I in enumerate(numb):
                for N2,J in enumerate(numb):
                    self._KG[m*I:m*I+M,m*J:m*J+M] += el.Ke[M*N1:M*(N1+1),M*N2:M*(N2+1)]

        self._is_inited = True
        
    def calc_MG(self):
        self.init()
        n = self.non
        m = self.mndof
        shape = n*m
        self._MG = np.zeros((shape,shape))
        for el in self.get_elements():
            numb = [nd.numb for nd in el.nodes]
            el.calc_Me()
            M = el.ndof
            for N1,I in enumerate(numb):
                for N2,J in enumerate(numb):
                    self._MG[m*I:m*I+M,m*J:m*J+M] += el.Me[M*N1:M*(N1+1),M*N2:M*(N2+1)]

    def calc_KC(self,l=None,R=None,L=None,rho=None,Omega=None,A=None,element=None,E=None,I=None,G=None,k=None):

        if element=='Euler_Beam':
            self.init()
            n = self.non
            m = self.mndof
            shape = n*m
            self._KC = np.zeros((shape,shape))
            t=[]
    
            for i in range(self.noe):
                Z=i*l
                
                a0=R*L+Z*L+(L**2)/2-R*Z-3*(Z**2)/2
                a1=-R-2*Z
                a2=-1/2
        
                k11=6*a0/(5*l)+3*a1/5+12*l*a2/35
                k12=a0/10+l*a1/10+l**2*a2/14
                k13=-6*a0/(5*l)-3*a1/5-12*l*a2/35
                k14=a0/10-(l**2)*a2/35
                k22=l*(28*a0+7*l*a1+4*l**2*a2)/210
                k23=-k12
                k24=-l*(14*a0+7*l*a1+6*l**2*a2)/420
                k33=6*a0/(5*l)+12*l*a2/35+3*a1/5
                k34=-k14
                k44=l*(28*a0+21*l*a1+18*(l**2)*a2)/210
                
    
                kec=rho*A*Omega**2*np.array([[0,0,0,0,0,0],
                                             [0,k11,k12,0,k13,k14],
                                             [0,k12,k22,0,k23,k24],
                                             [0,0,0,0,0,0],
                                             [0,k13,k23,0,k33,k34],
                                             [0,k14,k24,0,k34,k44]])
                t.append(kec)
                
            for i,j in enumerate(t):
                
                self._KC[3*i:3*i+6,3*i:3*i+6]+=j
        elif element=='G_Euler_Beam':
            self.init()
            n = self.non
            m = self.mndof
            shape = n*m
            self._KC = np.zeros((shape,shape))
            t=[]
            for i in range(self.noe):
                Z=i*l
                
                a0=R*L+Z*L+(L**2)/2-R*Z-3*(Z**2)/2
                a1=-R-2*Z
                a2=-1/2

                kec=rho*A*Omega**2*np.array([[0,0,0,0,0,0],
                                             [0,(3*(4*a2*A**2*G**2*l**6 + 7*a1*A**2*G**2*l**5 + 14*a0*A**2*G**2*l**4 + 84*a2*E*I*A*G*k*l**4 + 140*a1*E*I*A*G*k*l**3 + 280*a0*E*I*A*G*k*l**2 + 560*a2*E**2*I**2*k**2*l**2 + 840*a1*E**2*I**2*k**2*l + 1680*a0*E**2*I**2*k**2))/(35*l*(A*G*l**2 + 12*k*E*I)**2),                                                        (l*(5*a2*A**2*G**2*l**5 + 7*a1*A**2*G**2*l**4 + 7*a0*A**2*G**2*l**3 + 98*a2*E*I*A*G*k*l**3 + 112*a1*E*I*A*G*k*l**2 + 840*a2*E**2*I**2*k**2*l + 840*a1*E**2*I**2*k**2))/(70*(A*G*l**2 + 12*k*E*I)**2),0, -(3*(4*a2*A**2*G**2*l**6 + 7*a1*A**2*G**2*l**5 + 14*a0*A**2*G**2*l**4 + 84*a2*E*I*A*G*k*l**4 + 140*a1*E*I*A*G*k*l**3 + 280*a0*E*I*A*G*k*l**2 + 560*a2*E**2*I**2*k**2*l**2 + 840*a1*E**2*I**2*k**2*l + 1680*a0*E**2*I**2*k**2))/(35*l*(A*G*l**2 + 12*k*E*I)**2),                                                                          -(l*(2*a2*A**2*G**2*l**5 - 7*a0*A**2*G**2*l**3 + 126*a2*E*I*A*G*k*l**3 + 112*a1*E*I*A*G*k*l**2 + 840*a2*E**2*I**2*k**2*l + 840*a1*E**2*I**2*k**2))/(70*(A*G*l**2 + 12*k*E*I)**2)],
                                             [0,(l*(5*a2*A**2*G**2*l**5 + 7*a1*A**2*G**2*l**4 + 7*a0*A**2*G**2*l**3 + 98*a2*E*I*A*G*k*l**3 + 112*a1*E*I*A*G*k*l**2 + 840*a2*E**2*I**2*k**2*l + 840*a1*E**2*I**2*k**2))/(70*(A*G*l**2 + 12*k*E*I)**2),   (l*(4*a2*A**2*G**2*l**6 + 7*a1*A**2*G**2*l**5 + 28*a0*A**2*G**2*l**4 + 84*a2*E*I*A*G*k*l**4 + 126*a1*E*I*A*G*k*l**3 + 420*a0*E*I*A*G*k*l**2 + 1008*a2*E**2*I**2*k**2*l**2 + 1260*a1*E**2*I**2*k**2*l + 2520*a0*E**2*I**2*k**2))/(210*(A*G*l**2 + 12*k*E*I)**2),              0,                                       -(l*(5*a2*A**2*G**2*l**5 + 7*a1*A**2*G**2*l**4 + 7*a0*A**2*G**2*l**3 + 98*a2*E*I*A*G*k*l**3 + 112*a1*E*I*A*G*k*l**2 + 840*a2*E**2*I**2*k**2*l + 840*a1*E**2*I**2*k**2))/(70*(A*G*l**2 + 12*k*E*I)**2),  -(l*(6*a2*A**2*G**2*l**6 + 7*a1*A**2*G**2*l**5 + 14*a0*A**2*G**2*l**4 + 336*a2*E*I*A*G*k*l**4 + 420*a1*E*I*A*G*k*l**3 + 840*a0*E*I*A*G*k*l**2 + 2016*a2*E**2*I**2*k**2*l**2 + 2520*a1*E**2*I**2*k**2*l + 5040*a0*E**2*I**2*k**2))/(420*(A*G*l**2 + 12*k*E*I)**2)],
                                             [0,0,0,0,0,0],
                                             [0,-(3*(4*a2*A**2*G**2*l**6 + 7*a1*A**2*G**2*l**5 + 14*a0*A**2*G**2*l**4 + 84*a2*E*I*A*G*k*l**4 + 140*a1*E*I*A*G*k*l**3 + 280*a0*E*I*A*G*k*l**2 + 560*a2*E**2*I**2*k**2*l**2 + 840*a1*E**2*I**2*k**2*l + 1680*a0*E**2*I**2*k**2))/(35*l*(A*G*l**2 + 12*k*E*I)**2),                                                       -(l*(5*a2*A**2*G**2*l**5 + 7*a1*A**2*G**2*l**4 + 7*a0*A**2*G**2*l**3 + 98*a2*E*I*A*G*k*l**3 + 112*a1*E*I*A*G*k*l**2 + 840*a2*E**2*I**2*k**2*l + 840*a1*E**2*I**2*k**2))/(70*(A*G*l**2 + 12*k*E*I)**2), 0, (3*(4*a2*A**2*G**2*l**6 + 7*a1*A**2*G**2*l**5 + 14*a0*A**2*G**2*l**4 + 84*a2*E*I*A*G*k*l**4 + 140*a1*E*I*A*G*k*l**3 + 280*a0*E*I*A*G*k*l**2 + 560*a2*E**2*I**2*k**2*l**2 + 840*a1*E**2*I**2*k**2*l + 1680*a0*E**2*I**2*k**2))/(35*l*(A*G*l**2 + 12*k*E*I)**2),                                                                           (l*(2*a2*A**2*G**2*l**5 - 7*a0*A**2*G**2*l**3 + 126*a2*E*I*A*G*k*l**3 + 112*a1*E*I*A*G*k*l**2 + 840*a2*E**2*I**2*k**2*l + 840*a1*E**2*I**2*k**2))/(70*(A*G*l**2 + 12*k*E*I)**2)],
                                             [0,-(l*(2*a2*A**2*G**2*l**5 - 7*a0*A**2*G**2*l**3 + 126*a2*E*I*A*G*k*l**3 + 112*a1*E*I*A*G*k*l**2 + 840*a2*E**2*I**2*k**2*l + 840*a1*E**2*I**2*k**2))/(70*(A*G*l**2 + 12*k*E*I)**2), -(l*(6*a2*A**2*G**2*l**6 + 7*a1*A**2*G**2*l**5 + 14*a0*A**2*G**2*l**4 + 336*a2*E*I*A*G*k*l**4 + 420*a1*E*I*A*G*k*l**3 + 840*a0*E*I*A*G*k*l**2 + 2016*a2*E**2*I**2*k**2*l**2 + 2520*a1*E**2*I**2*k**2*l + 5040*a0*E**2*I**2*k**2))/(420*(A*G*l**2 + 12*k*E*I)**2),                                    0,                                    (l*(2*a2*A**2*G**2*l**5 - 7*a0*A**2*G**2*l**3 + 126*a2*E*I*A*G*k*l**3 + 112*a1*E*I*A*G*k*l**2 + 840*a2*E**2*I**2*k**2*l + 840*a1*E**2*I**2*k**2))/(70*(A*G*l**2 + 12*k*E*I)**2), (l*(18*a2*A**2*G**2*l**6 + 21*a1*A**2*G**2*l**5 + 28*a0*A**2*G**2*l**4 + 252*a2*E*I*A*G*k*l**4 + 294*a1*E*I*A*G*k*l**3 + 420*a0*E*I*A*G*k*l**2 + 1008*a2*E**2*I**2*k**2*l**2 + 1260*a1*E**2*I**2*k**2*l + 2520*a0*E**2*I**2*k**2))/(210*(A*G*l**2 + 12*k*E*I)**2)]])
                t.append(kec)
                
            for i,j in enumerate(t):
                
                self._KC[3*i:3*i+6,3*i:3*i+6]+=j
        elif element=='Timoshenko_Beam':
            self.init()
            n = self.non
            m = self.mndof
            shape = n*m
            self._KC = np.zeros((shape,shape))
            t=[]
    
            for i in range(self.noe):
                Z=i*l
                
                a0=R*L+Z*L+(L**2)/2-R*Z-3*(Z**2)/2
                a1=-R-2*Z
                a2=-1/2

                kec=rho*A*Omega**2*np.array([[0,0,0,0,0,0],
                                             [0,                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         (3*a1)/5 + (12*a2*l)/35 - (l**2*((48*a2*E**2*I**2)/35 - 24*A*G*a0*k*E*I) - l**4*((6*a0*A**2*G**2*k**2)/5 - (36*E*I*a2*A*G*k)/35) - 144*E**2*I**2*a0 + (72*E**2*I**2*a1*l)/5 + (12*A*E*G*I*a1*k*l**3)/5)/(l*(12*E*I + A*G*k*l**2)**2),                                                                                                                                                                                                                                                                                                            (72*E**2*I**2*a0*l**2)/(A**2*G**2*k**2*l**6 + 24*A*E*G*I*k*l**4 + 144*E**2*I**2*l**2) - (36*E**2*I**2*a1*l**2)/(A**2*G**2*k**2*l**5 + 24*A*E*G*I*k*l**3 + 144*E**2*I**2*l) - (24*E**2*I**2*a2*l**3)/(A**2*G**2*k**2*l**5 + 24*A*E*G*I*k*l**3 + 144*E**2*I**2*l) - (72*E**2*I**2*a0*l)/(A**2*G**2*k**2*l**5 + 24*A*E*G*I*k*l**3 + 144*E**2*I**2*l) + (48*E**2*I**2*a1*l**3)/(A**2*G**2*k**2*l**6 + 24*A*E*G*I*k*l**4 + 144*E**2*I**2*l**2) + (36*E**2*I**2*a2*l**4)/(A**2*G**2*k**2*l**6 + 24*A*E*G*I*k*l**4 + 144*E**2*I**2*l**2) + (68*A**2*G**2*a0*k**2*l**5)/(5*(A**2*G**2*k**2*l**5 + 24*A*E*G*I*k*l**3 + 144*E**2*I**2*l)) + (21*A**2*G**2*a1*k**2*l**6)/(2*(A**2*G**2*k**2*l**5 + 24*A*E*G*I*k*l**3 + 144*E**2*I**2*l)) + (60*A**2*G**2*a2*k**2*l**7)/(7*(A**2*G**2*k**2*l**5 + 24*A*E*G*I*k*l**3 + 144*E**2*I**2*l)) - (6*A**2*G**2*a0*k**2*l**6)/(A**2*G**2*k**2*l**6 + 24*A*E*G*I*k*l**4 + 144*E**2*I**2*l**2) - (24*A**2*G**2*a1*k**2*l**7)/(5*(A**2*G**2*k**2*l**6 + 24*A*E*G*I*k*l**4 + 144*E**2*I**2*l**2)) - (4*A**2*G**2*a2*k**2*l**8)/(A**2*G**2*k**2*l**6 + 24*A*E*G*I*k*l**4 + 144*E**2*I**2*l**2) - (15*A**2*G**2*a0*k**2*l**4)/(2*(A**2*G**2*k**2*l**4 + 24*A*E*G*I*k*l**2 + 144*E**2*I**2)) - (28*A**2*G**2*a1*k**2*l**5)/(5*(A**2*G**2*k**2*l**4 + 24*A*E*G*I*k*l**2 + 144*E**2*I**2)) - (9*A**2*G**2*a2*k**2*l**6)/(2*(A**2*G**2*k**2*l**4 + 24*A*E*G*I*k*l**2 + 144*E**2*I**2)) + (6*A*E*G*I*a0*k*l**4)/(A**2*G**2*k**2*l**6 + 24*A*E*G*I*k*l**4 + 144*E**2*I**2*l**2) + (8*A*E*G*I*a1*k*l**5)/(5*(A**2*G**2*k**2*l**6 + 24*A*E*G*I*k*l**4 + 144*E**2*I**2*l**2)) - (18*A*E*G*I*a0*k*l**2)/(A**2*G**2*k**2*l**4 + 24*A*E*G*I*k*l**2 + 144*E**2*I**2) - (12*A*E*G*I*a1*k*l**3)/(A**2*G**2*k**2*l**4 + 24*A*E*G*I*k*l**2 + 144*E**2*I**2) - (9*A*E*G*I*a2*k*l**4)/(A**2*G**2*k**2*l**4 + 24*A*E*G*I*k*l**2 + 144*E**2*I**2) + (12*A*E*G*I*a0*k*l**3)/(A**2*G**2*k**2*l**5 + 24*A*E*G*I*k*l**3 + 144*E**2*I**2*l) + (12*A*E*G*I*a1*k*l**4)/(A**2*G**2*k**2*l**5 + 24*A*E*G*I*k*l**3 + 144*E**2*I**2*l) + (52*A*E*G*I*a2*k*l**5)/(5*(A**2*G**2*k**2*l**5 + 24*A*E*G*I*k*l**3 + 144*E**2*I**2*l)),                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     0,    (l**2*((48*a2*E**2*I**2)/35 - 24*A*G*a0*k*E*I) - l**4*((6*a0*A**2*G**2*k**2)/5 - (36*E*I*a2*A*G*k)/35) - 144*E**2*I**2*a0 + (72*E**2*I**2*a1*l)/5 + (12*A*E*G*I*a1*k*l**3)/5)/(l*(12*E*I + A*G*k*l**2)**2) - (12*a2*l)/35 - (3*a1)/5,                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          -(l*(2*a2*A**2*G**2*k**2*l**5 - 7*a0*A**2*G**2*k**2*l**3 + 126*a2*A*E*G*I*k*l**3 + 112*a1*A*E*G*I*k*l**2 + 840*a2*E**2*I**2*l + 840*a1*E**2*I**2))/(70*(12*E*I + A*G*k*l**2)**2)],
                                             [0,(72*E**2*I**2*a0*l**2)/(A**2*G**2*k**2*l**6 + 24*A*E*G*I*k*l**4 + 144*E**2*I**2*l**2) - (36*E**2*I**2*a1*l**2)/(A**2*G**2*k**2*l**5 + 24*A*E*G*I*k*l**3 + 144*E**2*I**2*l) - (24*E**2*I**2*a2*l**3)/(A**2*G**2*k**2*l**5 + 24*A*E*G*I*k*l**3 + 144*E**2*I**2*l) - (72*E**2*I**2*a0*l)/(A**2*G**2*k**2*l**5 + 24*A*E*G*I*k*l**3 + 144*E**2*I**2*l) + (48*E**2*I**2*a1*l**3)/(A**2*G**2*k**2*l**6 + 24*A*E*G*I*k*l**4 + 144*E**2*I**2*l**2) + (36*E**2*I**2*a2*l**4)/(A**2*G**2*k**2*l**6 + 24*A*E*G*I*k*l**4 + 144*E**2*I**2*l**2) + (68*A**2*G**2*a0*k**2*l**5)/(5*(A**2*G**2*k**2*l**5 + 24*A*E*G*I*k*l**3 + 144*E**2*I**2*l)) + (21*A**2*G**2*a1*k**2*l**6)/(2*(A**2*G**2*k**2*l**5 + 24*A*E*G*I*k*l**3 + 144*E**2*I**2*l)) + (60*A**2*G**2*a2*k**2*l**7)/(7*(A**2*G**2*k**2*l**5 + 24*A*E*G*I*k*l**3 + 144*E**2*I**2*l)) - (6*A**2*G**2*a0*k**2*l**6)/(A**2*G**2*k**2*l**6 + 24*A*E*G*I*k*l**4 + 144*E**2*I**2*l**2) - (24*A**2*G**2*a1*k**2*l**7)/(5*(A**2*G**2*k**2*l**6 + 24*A*E*G*I*k*l**4 + 144*E**2*I**2*l**2)) - (4*A**2*G**2*a2*k**2*l**8)/(A**2*G**2*k**2*l**6 + 24*A*E*G*I*k*l**4 + 144*E**2*I**2*l**2) - (15*A**2*G**2*a0*k**2*l**4)/(2*(A**2*G**2*k**2*l**4 + 24*A*E*G*I*k*l**2 + 144*E**2*I**2)) - (28*A**2*G**2*a1*k**2*l**5)/(5*(A**2*G**2*k**2*l**4 + 24*A*E*G*I*k*l**2 + 144*E**2*I**2)) - (9*A**2*G**2*a2*k**2*l**6)/(2*(A**2*G**2*k**2*l**4 + 24*A*E*G*I*k*l**2 + 144*E**2*I**2)) + (6*A*E*G*I*a0*k*l**4)/(A**2*G**2*k**2*l**6 + 24*A*E*G*I*k*l**4 + 144*E**2*I**2*l**2) + (8*A*E*G*I*a1*k*l**5)/(5*(A**2*G**2*k**2*l**6 + 24*A*E*G*I*k*l**4 + 144*E**2*I**2*l**2)) - (18*A*E*G*I*a0*k*l**2)/(A**2*G**2*k**2*l**4 + 24*A*E*G*I*k*l**2 + 144*E**2*I**2) - (12*A*E*G*I*a1*k*l**3)/(A**2*G**2*k**2*l**4 + 24*A*E*G*I*k*l**2 + 144*E**2*I**2) - (9*A*E*G*I*a2*k*l**4)/(A**2*G**2*k**2*l**4 + 24*A*E*G*I*k*l**2 + 144*E**2*I**2) + (12*A*E*G*I*a0*k*l**3)/(A**2*G**2*k**2*l**5 + 24*A*E*G*I*k*l**3 + 144*E**2*I**2*l) + (12*A*E*G*I*a1*k*l**4)/(A**2*G**2*k**2*l**5 + 24*A*E*G*I*k*l**3 + 144*E**2*I**2*l) + (52*A*E*G*I*a2*k*l**5)/(5*(A**2*G**2*k**2*l**5 + 24*A*E*G*I*k*l**3 + 144*E**2*I**2*l)),                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    (l*(4*a2*A**2*G**2*k**2*l**6 + 7*a1*A**2*G**2*k**2*l**5 + 28*a0*A**2*G**2*k**2*l**4 + 84*a2*A*E*G*I*k*l**4 + 126*a1*A*E*G*I*k*l**3 + 420*a0*A*E*G*I*k*l**2 + 1008*a2*E**2*I**2*l**2 + 1260*a1*E**2*I**2*l + 2520*a0*E**2*I**2))/(210*(12*E*I + A*G*k*l**2)**2), 0,(72*E**2*I**2*a0*l)/(A**2*G**2*k**2*l**5 + 24*A*E*G*I*k*l**3 + 144*E**2*I**2*l) + (36*E**2*I**2*a1*l**2)/(A**2*G**2*k**2*l**5 + 24*A*E*G*I*k*l**3 + 144*E**2*I**2*l) + (24*E**2*I**2*a2*l**3)/(A**2*G**2*k**2*l**5 + 24*A*E*G*I*k*l**3 + 144*E**2*I**2*l) - (72*E**2*I**2*a0*l**2)/(A**2*G**2*k**2*l**6 + 24*A*E*G*I*k*l**4 + 144*E**2*I**2*l**2) - (48*E**2*I**2*a1*l**3)/(A**2*G**2*k**2*l**6 + 24*A*E*G*I*k*l**4 + 144*E**2*I**2*l**2) - (36*E**2*I**2*a2*l**4)/(A**2*G**2*k**2*l**6 + 24*A*E*G*I*k*l**4 + 144*E**2*I**2*l**2) - (68*A**2*G**2*a0*k**2*l**5)/(5*(A**2*G**2*k**2*l**5 + 24*A*E*G*I*k*l**3 + 144*E**2*I**2*l)) - (21*A**2*G**2*a1*k**2*l**6)/(2*(A**2*G**2*k**2*l**5 + 24*A*E*G*I*k*l**3 + 144*E**2*I**2*l)) - (60*A**2*G**2*a2*k**2*l**7)/(7*(A**2*G**2*k**2*l**5 + 24*A*E*G*I*k*l**3 + 144*E**2*I**2*l)) + (6*A**2*G**2*a0*k**2*l**6)/(A**2*G**2*k**2*l**6 + 24*A*E*G*I*k*l**4 + 144*E**2*I**2*l**2) + (24*A**2*G**2*a1*k**2*l**7)/(5*(A**2*G**2*k**2*l**6 + 24*A*E*G*I*k*l**4 + 144*E**2*I**2*l**2)) + (4*A**2*G**2*a2*k**2*l**8)/(A**2*G**2*k**2*l**6 + 24*A*E*G*I*k*l**4 + 144*E**2*I**2*l**2) + (15*A**2*G**2*a0*k**2*l**4)/(2*(A**2*G**2*k**2*l**4 + 24*A*E*G*I*k*l**2 + 144*E**2*I**2)) + (28*A**2*G**2*a1*k**2*l**5)/(5*(A**2*G**2*k**2*l**4 + 24*A*E*G*I*k*l**2 + 144*E**2*I**2)) + (9*A**2*G**2*a2*k**2*l**6)/(2*(A**2*G**2*k**2*l**4 + 24*A*E*G*I*k*l**2 + 144*E**2*I**2)) - (6*A*E*G*I*a0*k*l**4)/(A**2*G**2*k**2*l**6 + 24*A*E*G*I*k*l**4 + 144*E**2*I**2*l**2) - (8*A*E*G*I*a1*k*l**5)/(5*(A**2*G**2*k**2*l**6 + 24*A*E*G*I*k*l**4 + 144*E**2*I**2*l**2)) + (18*A*E*G*I*a0*k*l**2)/(A**2*G**2*k**2*l**4 + 24*A*E*G*I*k*l**2 + 144*E**2*I**2) + (12*A*E*G*I*a1*k*l**3)/(A**2*G**2*k**2*l**4 + 24*A*E*G*I*k*l**2 + 144*E**2*I**2) + (9*A*E*G*I*a2*k*l**4)/(A**2*G**2*k**2*l**4 + 24*A*E*G*I*k*l**2 + 144*E**2*I**2) - (12*A*E*G*I*a0*k*l**3)/(A**2*G**2*k**2*l**5 + 24*A*E*G*I*k*l**3 + 144*E**2*I**2*l) - (12*A*E*G*I*a1*k*l**4)/(A**2*G**2*k**2*l**5 + 24*A*E*G*I*k*l**3 + 144*E**2*I**2*l) - (52*A*E*G*I*a2*k*l**5)/(5*(A**2*G**2*k**2*l**5 + 24*A*E*G*I*k*l**3 + 144*E**2*I**2*l)), (72*E**2*I**2*a0*l**2)/(A**2*G**2*k**2*l**5 + 24*A*E*G*I*k*l**3 + 144*E**2*I**2*l) - (12*E**2*I**2*a2*l**3)/(A**2*G**2*k**2*l**4 + 24*A*E*G*I*k*l**2 + 144*E**2*I**2) - (18*E**2*I**2*a1*l**2)/(A**2*G**2*k**2*l**4 + 24*A*E*G*I*k*l**2 + 144*E**2*I**2) + (48*E**2*I**2*a1*l**3)/(A**2*G**2*k**2*l**5 + 24*A*E*G*I*k*l**3 + 144*E**2*I**2*l) + (36*E**2*I**2*a2*l**4)/(A**2*G**2*k**2*l**5 + 24*A*E*G*I*k*l**3 + 144*E**2*I**2*l) - (36*E**2*I**2*a0*l)/(A**2*G**2*k**2*l**4 + 24*A*E*G*I*k*l**2 + 144*E**2*I**2) - (48*E**2*I**2*a0*l**3)/(A**2*G**2*k**2*l**6 + 24*A*E*G*I*k*l**4 + 144*E**2*I**2*l**2) - (36*E**2*I**2*a1*l**4)/(A**2*G**2*k**2*l**6 + 24*A*E*G*I*k*l**4 + 144*E**2*I**2*l**2) - (144*E**2*I**2*a2*l**5)/(5*(A**2*G**2*k**2*l**6 + 24*A*E*G*I*k*l**4 + 144*E**2*I**2*l**2)) - (11*A**2*G**2*a0*k**2*l**6)/(2*(A**2*G**2*k**2*l**5 + 24*A*E*G*I*k*l**3 + 144*E**2*I**2*l)) - (64*A**2*G**2*a1*k**2*l**7)/(15*(A**2*G**2*k**2*l**5 + 24*A*E*G*I*k*l**3 + 144*E**2*I**2*l)) - (7*A**2*G**2*a2*k**2*l**8)/(2*(A**2*G**2*k**2*l**5 + 24*A*E*G*I*k*l**3 + 144*E**2*I**2*l)) + (8*A**2*G**2*a0*k**2*l**7)/(3*(A**2*G**2*k**2*l**6 + 24*A*E*G*I*k*l**4 + 144*E**2*I**2*l**2)) + (2*A**2*G**2*a1*k**2*l**8)/(A**2*G**2*k**2*l**6 + 24*A*E*G*I*k*l**4 + 144*E**2*I**2*l**2) + (8*A**2*G**2*a2*k**2*l**9)/(5*(A**2*G**2*k**2*l**6 + 24*A*E*G*I*k*l**4 + 144*E**2*I**2*l**2)) + (14*A**2*G**2*a0*k**2*l**5)/(5*(A**2*G**2*k**2*l**4 + 24*A*E*G*I*k*l**2 + 144*E**2*I**2)) + (9*A**2*G**2*a1*k**2*l**6)/(4*(A**2*G**2*k**2*l**4 + 24*A*E*G*I*k*l**2 + 144*E**2*I**2)) + (66*A**2*G**2*a2*k**2*l**7)/(35*(A**2*G**2*k**2*l**4 + 24*A*E*G*I*k*l**2 + 144*E**2*I**2)) - (8*A*E*G*I*a0*k*l**5)/(A**2*G**2*k**2*l**6 + 24*A*E*G*I*k*l**4 + 144*E**2*I**2*l**2) - (6*A*E*G*I*a1*k*l**6)/(A**2*G**2*k**2*l**6 + 24*A*E*G*I*k*l**4 + 144*E**2*I**2*l**2) - (24*A*E*G*I*a2*k*l**7)/(5*(A**2*G**2*k**2*l**6 + 24*A*E*G*I*k*l**4 + 144*E**2*I**2*l**2)) - (6*A*E*G*I*a0*k*l**3)/(A**2*G**2*k**2*l**4 + 24*A*E*G*I*k*l**2 + 144*E**2*I**2) - (3*A*E*G*I*a1*k*l**4)/(A**2*G**2*k**2*l**4 + 24*A*E*G*I*k*l**2 + 144*E**2*I**2) - (2*A*E*G*I*a2*k*l**5)/(A**2*G**2*k**2*l**4 + 24*A*E*G*I*k*l**2 + 144*E**2*I**2) + (12*A*E*G*I*a0*k*l**4)/(A**2*G**2*k**2*l**5 + 24*A*E*G*I*k*l**3 + 144*E**2*I**2*l) + (8*A*E*G*I*a1*k*l**5)/(A**2*G**2*k**2*l**5 + 24*A*E*G*I*k*l**3 + 144*E**2*I**2*l) + (6*A*E*G*I*a2*k*l**6)/(A**2*G**2*k**2*l**5 + 24*A*E*G*I*k*l**3 + 144*E**2*I**2*l)],
                                             [0,0,0,0,0,0],
                                             [0,                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         (l**2*((48*a2*E**2*I**2)/35 - 24*A*G*a0*k*E*I) - l**4*((6*a0*A**2*G**2*k**2)/5 - (36*E*I*a2*A*G*k)/35) - 144*E**2*I**2*a0 + (72*E**2*I**2*a1*l)/5 + (12*A*E*G*I*a1*k*l**3)/5)/(l*(12*E*I + A*G*k*l**2)**2) - (12*a2*l)/35 - (3*a1)/5,                                                                                                                                                                                                                                                                                                            (72*E**2*I**2*a0*l)/(A**2*G**2*k**2*l**5 + 24*A*E*G*I*k*l**3 + 144*E**2*I**2*l) + (36*E**2*I**2*a1*l**2)/(A**2*G**2*k**2*l**5 + 24*A*E*G*I*k*l**3 + 144*E**2*I**2*l) + (24*E**2*I**2*a2*l**3)/(A**2*G**2*k**2*l**5 + 24*A*E*G*I*k*l**3 + 144*E**2*I**2*l) - (72*E**2*I**2*a0*l**2)/(A**2*G**2*k**2*l**6 + 24*A*E*G*I*k*l**4 + 144*E**2*I**2*l**2) - (48*E**2*I**2*a1*l**3)/(A**2*G**2*k**2*l**6 + 24*A*E*G*I*k*l**4 + 144*E**2*I**2*l**2) - (36*E**2*I**2*a2*l**4)/(A**2*G**2*k**2*l**6 + 24*A*E*G*I*k*l**4 + 144*E**2*I**2*l**2) - (68*A**2*G**2*a0*k**2*l**5)/(5*(A**2*G**2*k**2*l**5 + 24*A*E*G*I*k*l**3 + 144*E**2*I**2*l)) - (21*A**2*G**2*a1*k**2*l**6)/(2*(A**2*G**2*k**2*l**5 + 24*A*E*G*I*k*l**3 + 144*E**2*I**2*l)) - (60*A**2*G**2*a2*k**2*l**7)/(7*(A**2*G**2*k**2*l**5 + 24*A*E*G*I*k*l**3 + 144*E**2*I**2*l)) + (6*A**2*G**2*a0*k**2*l**6)/(A**2*G**2*k**2*l**6 + 24*A*E*G*I*k*l**4 + 144*E**2*I**2*l**2) + (24*A**2*G**2*a1*k**2*l**7)/(5*(A**2*G**2*k**2*l**6 + 24*A*E*G*I*k*l**4 + 144*E**2*I**2*l**2)) + (4*A**2*G**2*a2*k**2*l**8)/(A**2*G**2*k**2*l**6 + 24*A*E*G*I*k*l**4 + 144*E**2*I**2*l**2) + (15*A**2*G**2*a0*k**2*l**4)/(2*(A**2*G**2*k**2*l**4 + 24*A*E*G*I*k*l**2 + 144*E**2*I**2)) + (28*A**2*G**2*a1*k**2*l**5)/(5*(A**2*G**2*k**2*l**4 + 24*A*E*G*I*k*l**2 + 144*E**2*I**2)) + (9*A**2*G**2*a2*k**2*l**6)/(2*(A**2*G**2*k**2*l**4 + 24*A*E*G*I*k*l**2 + 144*E**2*I**2)) - (6*A*E*G*I*a0*k*l**4)/(A**2*G**2*k**2*l**6 + 24*A*E*G*I*k*l**4 + 144*E**2*I**2*l**2) - (8*A*E*G*I*a1*k*l**5)/(5*(A**2*G**2*k**2*l**6 + 24*A*E*G*I*k*l**4 + 144*E**2*I**2*l**2)) + (18*A*E*G*I*a0*k*l**2)/(A**2*G**2*k**2*l**4 + 24*A*E*G*I*k*l**2 + 144*E**2*I**2) + (12*A*E*G*I*a1*k*l**3)/(A**2*G**2*k**2*l**4 + 24*A*E*G*I*k*l**2 + 144*E**2*I**2) + (9*A*E*G*I*a2*k*l**4)/(A**2*G**2*k**2*l**4 + 24*A*E*G*I*k*l**2 + 144*E**2*I**2) - (12*A*E*G*I*a0*k*l**3)/(A**2*G**2*k**2*l**5 + 24*A*E*G*I*k*l**3 + 144*E**2*I**2*l) - (12*A*E*G*I*a1*k*l**4)/(A**2*G**2*k**2*l**5 + 24*A*E*G*I*k*l**3 + 144*E**2*I**2*l) - (52*A*E*G*I*a2*k*l**5)/(5*(A**2*G**2*k**2*l**5 + 24*A*E*G*I*k*l**3 + 144*E**2*I**2*l)),                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     0,    (3*a1)/5 + (12*a2*l)/35 - (l**2*((48*a2*E**2*I**2)/35 - 24*A*G*a0*k*E*I) - l**4*((6*a0*A**2*G**2*k**2)/5 - (36*E*I*a2*A*G*k)/35) - 144*E**2*I**2*a0 + (72*E**2*I**2*a1*l)/5 + (12*A*E*G*I*a1*k*l**3)/5)/(l*(12*E*I + A*G*k*l**2)**2)                                                                                                                                         ,                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             (l*(2*a2*A**2*G**2*k**2*l**5 - 7*a0*A**2*G**2*k**2*l**3 + 126*a2*A*E*G*I*k*l**3 + 112*a1*A*E*G*I*k*l**2 + 840*a2*E**2*I**2*l + 840*a1*E**2*I**2))/(70*(12*E*I + A*G*k*l**2)**2)],
                                             [0,                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               -(l*(2*a2*A**2*G**2*k**2*l**5 - 7*a0*A**2*G**2*k**2*l**3 + 126*a2*A*E*G*I*k*l**3 + 112*a1*A*E*G*I*k*l**2 + 840*a2*E**2*I**2*l + 840*a1*E**2*I**2))/(70*(12*E*I + A*G*k*l**2)**2), (72*E**2*I**2*a0*l**2)/(A**2*G**2*k**2*l**5 + 24*A*E*G*I*k*l**3 + 144*E**2*I**2*l) - (12*E**2*I**2*a2*l**3)/(A**2*G**2*k**2*l**4 + 24*A*E*G*I*k*l**2 + 144*E**2*I**2) - (18*E**2*I**2*a1*l**2)/(A**2*G**2*k**2*l**4 + 24*A*E*G*I*k*l**2 + 144*E**2*I**2) + (48*E**2*I**2*a1*l**3)/(A**2*G**2*k**2*l**5 + 24*A*E*G*I*k*l**3 + 144*E**2*I**2*l) + (36*E**2*I**2*a2*l**4)/(A**2*G**2*k**2*l**5 + 24*A*E*G*I*k*l**3 + 144*E**2*I**2*l) - (36*E**2*I**2*a0*l)/(A**2*G**2*k**2*l**4 + 24*A*E*G*I*k*l**2 + 144*E**2*I**2) - (48*E**2*I**2*a0*l**3)/(A**2*G**2*k**2*l**6 + 24*A*E*G*I*k*l**4 + 144*E**2*I**2*l**2) - (36*E**2*I**2*a1*l**4)/(A**2*G**2*k**2*l**6 + 24*A*E*G*I*k*l**4 + 144*E**2*I**2*l**2) - (144*E**2*I**2*a2*l**5)/(5*(A**2*G**2*k**2*l**6 + 24*A*E*G*I*k*l**4 + 144*E**2*I**2*l**2)) - (11*A**2*G**2*a0*k**2*l**6)/(2*(A**2*G**2*k**2*l**5 + 24*A*E*G*I*k*l**3 + 144*E**2*I**2*l)) - (64*A**2*G**2*a1*k**2*l**7)/(15*(A**2*G**2*k**2*l**5 + 24*A*E*G*I*k*l**3 + 144*E**2*I**2*l)) - (7*A**2*G**2*a2*k**2*l**8)/(2*(A**2*G**2*k**2*l**5 + 24*A*E*G*I*k*l**3 + 144*E**2*I**2*l)) + (8*A**2*G**2*a0*k**2*l**7)/(3*(A**2*G**2*k**2*l**6 + 24*A*E*G*I*k*l**4 + 144*E**2*I**2*l**2)) + (2*A**2*G**2*a1*k**2*l**8)/(A**2*G**2*k**2*l**6 + 24*A*E*G*I*k*l**4 + 144*E**2*I**2*l**2) + (8*A**2*G**2*a2*k**2*l**9)/(5*(A**2*G**2*k**2*l**6 + 24*A*E*G*I*k*l**4 + 144*E**2*I**2*l**2)) + (14*A**2*G**2*a0*k**2*l**5)/(5*(A**2*G**2*k**2*l**4 + 24*A*E*G*I*k*l**2 + 144*E**2*I**2)) + (9*A**2*G**2*a1*k**2*l**6)/(4*(A**2*G**2*k**2*l**4 + 24*A*E*G*I*k*l**2 + 144*E**2*I**2)) + (66*A**2*G**2*a2*k**2*l**7)/(35*(A**2*G**2*k**2*l**4 + 24*A*E*G*I*k*l**2 + 144*E**2*I**2)) - (8*A*E*G*I*a0*k*l**5)/(A**2*G**2*k**2*l**6 + 24*A*E*G*I*k*l**4 + 144*E**2*I**2*l**2) - (6*A*E*G*I*a1*k*l**6)/(A**2*G**2*k**2*l**6 + 24*A*E*G*I*k*l**4 + 144*E**2*I**2*l**2) - (24*A*E*G*I*a2*k*l**7)/(5*(A**2*G**2*k**2*l**6 + 24*A*E*G*I*k*l**4 + 144*E**2*I**2*l**2)) - (6*A*E*G*I*a0*k*l**3)/(A**2*G**2*k**2*l**4 + 24*A*E*G*I*k*l**2 + 144*E**2*I**2) - (3*A*E*G*I*a1*k*l**4)/(A**2*G**2*k**2*l**4 + 24*A*E*G*I*k*l**2 + 144*E**2*I**2) - (2*A*E*G*I*a2*k*l**5)/(A**2*G**2*k**2*l**4 + 24*A*E*G*I*k*l**2 + 144*E**2*I**2) + (12*A*E*G*I*a0*k*l**4)/(A**2*G**2*k**2*l**5 + 24*A*E*G*I*k*l**3 + 144*E**2*I**2*l) + (8*A*E*G*I*a1*k*l**5)/(A**2*G**2*k**2*l**5 + 24*A*E*G*I*k*l**3 + 144*E**2*I**2*l) + (6*A*E*G*I*a2*k*l**6)/(A**2*G**2*k**2*l**5 + 24*A*E*G*I*k*l**3 + 144*E**2*I**2*l),                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       0,                         (l*(2*a2*A**2*G**2*k**2*l**5 - 7*a0*A**2*G**2*k**2*l**3 + 126*a2*A*E*G*I*k*l**3 + 112*a1*A*E*G*I*k*l**2 + 840*a2*E**2*I**2*l + 840*a1*E**2*I**2))/(70*(12*E*I + A*G*k*l**2)**2),                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 (l*(18*a2*A**2*G**2*k**2*l**6 + 21*a1*A**2*G**2*k**2*l**5 + 28*a0*A**2*G**2*k**2*l**4 + 252*a2*A*E*G*I*k*l**4 + 294*a1*A*E*G*I*k*l**3 + 420*a0*A*E*G*I*k*l**2 + 1008*a2*E**2*I**2*l**2 + 1260*a1*E**2*I**2*l + 2520*a0*E**2*I**2))/(210*(12*E*I + A*G*k*l**2)**2)]])
                t.append(kec)
  
            for i,j in enumerate(t):
                
                self._KC[3*i:3*i+6,3*i:3*i+6]+=j
        elif element=='Beam1D11':
            n = self.non
            m = self.mndof
            shape = n*m
            self._KC=np.zeros((shape,shape))
        else: 
            raise TypeError("Incorrect input beam element")

        return self._KC

    def add_node_force(self,nid,**forces):
        if not self._is_inited:
            self.calc_KG()
            
        assert nid+1 <= self.non,"Element does not exist"
        for key in forces.keys():
            assert key in self.nBk,"Check if the node forces applied are correct"

        self.nodes[nid].set_force(**forces)   
        self._is_force_added = True
        

    def add_node_disp(self,nid,**disp):
        if not self._is_inited:
            self.calc_KG()
        assert nid+1 <= self.non,"Element does not exist"
        for key in disp.keys():
            assert key in self.nAk,"Check if the node disp applied are correct"  
        self.nodes[nid].set_disp(**disp)
        val = disp.values()
        if len(val):
            self._is_disp_added = True
        

            
    def add_fixed_sup(self,*nids):
        if not self._is_inited:
            self.calc_KG()
        for nid in nids:
            if isinstance(nid,list) or isinstance(nid,tuple) or isinstance(nid,np.ndarray):
                for n in nid:
                    for key in self.nAk:
                        self.nodes[n]._disp[key] = 0.
            else:
                for key in self.nAk:
                    self.nodes[nid]._disp[key] = 0.

    def add_hinged_sup(self,*nids):
        if not self._is_inited:
            self.calc_KG()
        for nid in nids:
            if isinstance(nid,list) or isinstance(nid,tuple) or isinstance(nid,np.ndarray):
                for n in nid:
                    for key in self.nAk[:-1]:
                        self.nodes[n]._disp[key] = 0.
            else:
                for key in self.nAk[:-1]:
                    self.nodes[nid]._disp[key] = 0.
    def moca_yueshu(self,nid,direction):
        if not self._is_inited:
            self.calc_KG()
        if self.dim == 2:
            assert direction in ["x","y"],"Support dirction is x,y"
            if direction == "x":
                self.nodes[nid].set_disp(Ux = 0.)
            
            elif direction == "y":
                self.nodes[nid].set_disp(Phz = 0.)
                
    def add_rolled_sup(self,nid,direction = "x"):
        if not self._is_inited:
            self.calc_KG()
        if self.dim == 2:
            assert direction in ["x","y"],"Support dirction is x,y"
            if direction == "x":
                self.nodes[nid].set_disp(Ux = 0.)
            
            elif direction == "y":
                self.nodes[nid].set_disp(Uy = 0.)
                
        elif self.dim == 3:
            assert direction in ["x","y","z"],"Support dirction is x,y,and z"
            if direction == "x":
                self.nodes[nid].set_disp(Ux = 0.)
            
            elif direction == "y":
                self.nodes[nid].set_disp(Uy = 0.)
                
            elif direction == "z":
                self.nodes[nid].set_disp(Uz = 0.)

            
    def calc_deleted_KG_matrix(self):
        self._Force = [nd.force for nd in self.get_nodes()]
        self._Disp = [nd.disp for nd in self.get_nodes()]
        self._ForceValue = [val[key] for val in self.Force for key in self.nBk]
        self._DispValue = [val[key] for val in self.Disp for key in self.nAk]
        self._deleted = [row for row,val in enumerate(self.DispValue) if val is not None]
        self._keeped = [row for row,val in enumerate(self.DispValue) if val is None]
        if self._is_disp_added:
            self.check_boundary_condition(self.KG)
            
        self._Force_keeped = np.delete(self._ForceValue,self._deleted,0)
        self._KG_keeped = np.delete(np.delete(self.KG,self._deleted,0),self._deleted,1)
        



    def calc_deleted_MG_matrix(self):
        self._MG_keeped = np.delete(np.delete(self._MG,self._deleted,0),self._deleted,1)



        




