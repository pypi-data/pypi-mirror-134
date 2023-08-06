
# The author: haoyan zhang
#E-mail: haoy.zhang@foxmail.com

from sfe.Node import *
from sfe.Element import *


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Beam 1Dim ~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class Beam1D11(Element):

    def __init__(self,nodes=None,E=None,A=None,I=None,dens=1):
        Element.__init__(self,nodes)
        self.E = E
        self.A = A
        self.I = I
        self.dens = dens

    def init_unknowns(self):
        for nd in self.nodes:
            nd.init_unknowns("Ux","Phz")  

        self._ndof = 3
                     
    def calc_T(self):
        TBase = _calc_Tbase_for_1d_beam(self.nodes)
        self._T = np.zeros((6,6))
        self._T[:3,:3] = self._T[3:,3:] = TBase
        
    def calc_ke(self):
        self._ke = _calc_ke_for_1d_beam(E = self.E,A = self.A,I = self.I,L = self.volume)

    def calc_me(self):
        self._me = _calc_me_for_1d_beam(E = self.E,A = self.A,I = self.I,L = self.volume,dens = self.dens)
        


    
def _calc_Tbase_for_1d_beam(nodes):
    
    x1,y1 = nodes[0].x,nodes[0].y
    x2,y2 = nodes[1].x,nodes[1].y
    le = np.sqrt((x2-x1)**2+(y2-y1)**2)

    lx = (x2-x1)/le
    mx = (y2-y1)/le
    T = np.array([[lx,mx,0.],
                  [-mx,lx,0.],
                  [0.,0.,1.]])
                  
    return T

def _calc_ke_for_1d_beam(E = 1.0,A = 1.0,I = 1.0,L = 1.0):
    a00 =  E*A/L
    a03 = -a00
    a11 = 12*E*I/L**3
    a12 = 6*E*I/L**2
    a14 = -a11
    a22 = 4*E*I/L
    a24 = -a12
    a25 = 2*E*I/L
    a45 = -a12
    
    


    ke =np.array([[a00, 0.,  0.,  a03,  0., 0.],
                  [ 0., a11, a12,  0., a14,a12],
                  [ 0., a12, a22,  0., a24,a25],
                  [a03,  0.,  0., a00,  0., 0.],
                  [ 0., a14, a24,  0.,a11, a45],
                  [ 0., a12, a25,  0.,a45, a22]])
    return ke

def _calc_me_for_1d_beam(E = 1.0,A = 1.0,I = 1.,L = 1.,dens=1.):
    a =dens*A*L/420
    M = a*np.array([[140,  0,     0,     70,  0,         0 ],
                    [ 0,  156,   22*L,   0,   54,    -13*L ],
                    [ 0,  22*L, 4*L**2,  0,  13*L,  -3*L**2],
                    [ 70,  0,     0,    140,   0,       0  ],
                    [ 0,  54,    13*L,   0,   156,    -22*L],
                    [ 0, -13*L, -3*L**2, 0, -22*L,  4*L**2]])
    return M       


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Euler BEAM ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class Euler_Beam(Element):

    def __init__(self,nodes=None,E=None,A=None,I=None,dens=1):
        Element.__init__(self,nodes)
        self.E = E
        self.A = A
        self.I = I
        self.dens = dens

    def init_unknowns(self):
        for nd in self.nodes:
            nd.init_unknowns("Uy","Phz") 

        self._ndof = 3
                     
    def calc_T(self):
        TBase = _calc_T_Euler_Beam(self.nodes)
        self._T = np.zeros((6,6))
        self._T[:3,:3] = self._T[3:,3:] = TBase
        
    def calc_ke(self):
        self._ke = _calc_ke_Euler_Beam(E = self.E,A = self.A,I = self.I,L = self.volume)

    def calc_me(self):
        self._me = _calc_me_Euler_Beam(E = self.E,A = self.A,I = self.I,L = self.volume,dens = self.dens)
        


    
def _calc_T_Euler_Beam(nodes):
    
    x1,y1 = nodes[0].x,nodes[0].y
    x2,y2 = nodes[1].x,nodes[1].y
    le = np.sqrt((x2-x1)**2+(y2-y1)**2)

    lx = (x2-x1)/le
    mx = (y2-y1)/le
    T = np.array([[lx,mx,0.],
                  [-mx,lx,0.],
                  [0.,0.,1.]])
                  
    return T

def _calc_ke_Euler_Beam(E = 1.0,A = 1.0,I = 1.0,L = 1.0):
    a00 =  E*A/L
    a03 = -a00
    a11 = 12*E*I/L**3
    a12 = 6*E*I/L**2
    a14 = -a11
    a22 = 4*E*I/L
    a24 = -a12
    a25 = 2*E*I/L
    a45 = -a12
    
    


    ke =np.array([[a00, 0.,  0.,  a03,  0., 0.],
                  [ 0., a11, a12,  0., a14,a12],
                  [ 0., a12, a22,  0., a24,a25],
                  [a03,  0.,  0., a00,  0., 0.],
                  [ 0., a14, a24,  0.,a11, a45],
                  [ 0., a12, a25,  0.,a45, a22]])
    return ke

def _calc_me_Euler_Beam(E = 1.0,A = 1.0,I = 1.,L = 1.,dens=1.):
    a =dens*A*L/420
    M = a*np.array([[140,  0,     0,     70,  0,         0 ],
                    [ 0,  156,   22*L,   0,   54,    -13*L ],
                    [ 0,  22*L, 4*L**2,  0,  13*L,  -3*L**2],
                    [ 70,  0,     0,    140,   0,       0  ],
                    [ 0,  54,    13*L,   0,   156,    -22*L],
                    [ 0, -13*L, -3*L**2, 0, -22*L,  4*L**2]])
    return M       


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ G Euler beam ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class G_Euler_Beam(Element):

    def __init__(self,nodes=None,E=None,A=None,I=None,l =1,G=1,k=1,rho=1):
        Element.__init__(self,nodes)
        self.E = E
        self.A = A
        self.I = I
        self.l=l
        self.k=k
        self.G=G
        self.rho = rho
        

    def init_unknowns(self):
        for nd in self.nodes:
            nd.init_unknowns("Uy","Phz") 

        self._ndof = 3
                     
    def calc_T(self):
        TBase = _calc_T_Euler_Beam(self.nodes)
        self._T = np.zeros((6,6))
        self._T[:3,:3] = self._T[3:,3:] = TBase
        
    def calc_ke(self):
        self._ke = G_calc_ke_Euler_Beam(E = self.E,A = self.A,I = self.I,l = self.l,G=self.G,k=self.k)

    def calc_me(self):
        self._me = G_calc_me_Euler_Beam(E = self.E,A = self.A,I = self.I,l = self.l,G=self.G,k=self.k,rho = self.rho)
        


    
def G_calc_T_Euler_Beam(nodes):
    
    x1,y1 = nodes[0].x,nodes[0].y
    x2,y2 = nodes[1].x,nodes[1].y
    le = np.sqrt((x2-x1)**2+(y2-y1)**2)

    lx = (x2-x1)/le
    mx = (y2-y1)/le
    T = np.array([[lx,mx,0.],
                  [-mx,lx,0.],
                  [0.,0.,1.]])
                  
    return T

def G_calc_ke_Euler_Beam(E = 1.0,A = 1.0,I = 1.0,l = 1.0,k=1,G=1):

    b=12*k*E*I/(G*A*l**2)
    


    ke=(E*I/((1+b)*l**3))*np.array([[0,   0,    0,           0,   0,     0],
                                    [0,   12,   6*l,         0,   -12,   6*l],
                                    [0,   6*l,  (4+b)*l**2,  0,   -6*l,  (2-b)*l**2],
                                    [0,   0,    0,           0,   0,     0],
                                    [0,   -12,  -6*l,        0,   12,    -6*l],
                                    [0,   6*l,  (2-b)*l**2,  0,   -6*l,  (4+b)*l**2]])
    return ke

def G_calc_me_Euler_Beam(E = 1.0,A = 1.0,I = 1.,l = 1.0,k=1,G=1.,rho=1.):
    b=12*k*E*I/(G*A*l**2)
    M=(rho*A*l/(420*(1+b)**2))*np.array([[0,    0,                              0,                                0,    0,                               0],
                                         [0,    140*b**2+294*b+156,             (35/2)*l*b**2+(77/2)*b*l+22*l,    0,    70*b**2+126*b+54,                -(35/2)*l*b**2-(63/2)*b*l-13*l],
                                         [0,    (35/2)*l*b**2+(77/2)*b*l+22*l,  (7/2)*b**2*l**2+7*b*l**2+4*l**2,  0,    (35/2)*b**2*l+(63/2)*b*l+13*l,   -(7/2)*b**2*l**2-7*b*l**2-3*l**2],
                                         [0,    0,                              0,                                0,    0,                               0],
                                         [0,    70*b**2+126*b+54,               35/2*b**2*l+63/2*b*l+13*l,        0,    140*b**2+294*b+156,              -(35/2)*b**2*l-(77/2)*b*l-22*l],
                                         [0,    -(35/2)*l*b**2-(63/2)*b*l-13*l, -(7/2)*b**2*l**2-7*b*l**2-3*l**2, 0,    -(35/2)*b**2*l-(77/2)*b*l-22*l,  (7/2)*(b**2)*(l**2)+7*b*l**2+4*l**2]])
    return M       


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Timoshenko Beam ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Timoshenko_Beam(Element):

    def __init__(self,nodes=None,E=None,A=1,I=None,l=1,G=1,k=1,rho=1):
        Element.__init__(self,nodes)
        self.E = E
        self.A = A
        self.I = I
        self.l=l
        self.G = G
        self.k=k
        self.rho=rho
        

    def init_unknowns(self):
        for nd in self.nodes:
            nd.init_unknowns("Uy","Phz") 

        self._ndof = 3
                     
    def calc_T(self):
        TBase = _calc_T_Euler_Beam(self.nodes)
        self._T = np.zeros((6,6))
        self._T[:3,:3] = self._T[3:,3:] = TBase
        
    def calc_ke(self):
        self._ke = _calc_ke_Timoshenko_Beam(E = self.E,A = self.A,I = self.I,l =self.l,G=self.G,k=self.k)

    def calc_me(self):
        self._me = _calc_me_Timoshenko_Beam(E =self.E,A =self.A,I = self.I,l =self.l,G=self.G,k=self.k,rho=self.rho)
        


    
def _calc_T_Timoshenko_Beam(nodes):
    
    x1,y1 = nodes[0].x,nodes[0].y
    x2,y2 = nodes[1].x,nodes[1].y
    le = np.sqrt((x2-x1)**2+(y2-y1)**2)

    lx = (x2-x1)/le
    mx = (y2-y1)/le
    T = np.array([[lx,mx,0.],
                  [-mx,lx,0.],
                  [0.,0.,1.]])
                  
    return T

def _calc_ke_Timoshenko_Beam(E = 1.0,A = 1.0,I = 1.0,l = 1.0,G=1,k=1):
    

    ke=np.array([[0,0,0,0,0,0],
                 [0,(12*A**2*E*G**2*I*l)/(A*G*l**2 + 10*E*I)**2 + (864*A*E**2*G*I**2)/(5*l*(A*G*l**2 + 10*E*I)**2),   (6*A**2*E*G**2*I*l**2)/(A*G*l**2 + 10*E*I)**2 + (432*A*E**2*G*I**2*l)/(5*(A*G*l**2 + 10*E*I)*(A*G*l**3 + 10*E*I*l)),           0,          - (12*A**2*E*G**2*I*l)/(A*G*l**2 + 10*E*I)**2 - (864*A*E**2*G*I**2)/(5*l*(A*G*l**2 + 10*E*I)**2),   (6*A**2*E*G**2*I*l**2)/(A*G*l**2 + 10*E*I)**2 + (432*A*E**2*G*I**2*l)/(5*(A*G*l**2 + 10*E*I)*(A*G*l**3 + 10*E*I*l))],
                 [0,(6*A**2*E*G**2*I*l**2)/(A*G*l**2 + 10*E*I)**2 + (432*A*E**2*G*I**2*l)/(5*(A*G*l**2 + 10*E*I)*(A*G*l**3 + 10*E*I*l)),              E*I*(1/l + (3*A**2*G**2*l**3)/(A*G*l**2 + 10*E*I)**2) + (216*A*E**2*G*I**2*l)/(5*(A*G*l**2 + 10*E*I)**2), 0,- (6*A**2*E*G**2*I*l**2)/(A*G*l**2 + 10*E*I)**2 - (432*A*E**2*G*I**2*l)/(5*(A*G*l**2 + 10*E*I)*(A*G*l**3 + 10*E*I*l)),              (216*A*E**2*G*I**2*l)/(5*(A*G*l**2 + 10*E*I)**2) - E*I*(1/l - (3*A**2*G**2*l**3)/(A*G*l**2 + 10*E*I)**2)],
                 [0,0,0,0,0,0],
                 [0,- (12*A**2*E*G**2*I*l)/(A*G*l**2 + 10*E*I)**2 - (864*A*E**2*G*I**2)/(5*l*(A*G*l**2 + 10*E*I)**2), - (6*A**2*E*G**2*I*l**2)/(A*G*l**2 + 10*E*I)**2 - (432*A*E**2*G*I**2*l)/(5*(A*G*l**2 + 10*E*I)*(A*G*l**3 + 10*E*I*l)),          0,             (12*A**2*E*G**2*I*l)/(A*G*l**2 + 10*E*I)**2 + (864*A*E**2*G*I**2)/(5*l*(A*G*l**2 + 10*E*I)**2), - (6*A**2*E*G**2*I*l**2)/(A*G*l**2 + 10*E*I)**2 - (432*A*E**2*G*I**2*l)/(5*(A*G*l**2 + 10*E*I)*(A*G*l**3 + 10*E*I*l))],
                 [0,(6*A**2*E*G**2*I*l**2)/(A*G*l**2 + 10*E*I)**2 + (432*A*E**2*G*I**2*l)/(5*(A*G*l**2 + 10*E*I)*(A*G*l**3 + 10*E*I*l)),              (216*A*E**2*G*I**2*l)/(5*(A*G*l**2 + 10*E*I)**2) - E*I*(1/l - (3*A**2*G**2*l**3)/(A*G*l**2 + 10*E*I)**2), 0,- (6*A**2*E*G**2*I*l**2)/(A*G*l**2 + 10*E*I)**2 - (432*A*E**2*G*I**2*l)/(5*(A*G*l**2 + 10*E*I)*(A*G*l**3 + 10*E*I*l)),              E*I*(1/l + (3*A**2*G**2*l**3)/(A*G*l**2 + 10*E*I)**2) + (216*A*E**2*G*I**2*l)/(5*(A*G*l**2 + 10*E*I)**2)]])
    return ke


def _calc_me_Timoshenko_Beam(E = 1.0,A = 1.0,I = 1.,l = 1.,G=1,k=1,rho=1):
    
    M=np.array([[0,0,0,0,0,0],
                 [0, (13*A*l*rho)/35 - ((18*G*k*rho*A**2*E*I*l**3)/35 + (192*rho*A*E**2*I**2*l)/35)/(12*E*I + A*G*k*l**2)**2, (11*A*l**2*rho)/210 - ((11*G*k*rho*A**2*E*I*l**4)/70 + (54*rho*A*E**2*I**2*l**2)/35)/(12*E*I + A*G*k*l**2)**2,   0,   ((18*G*k*rho*A**2*E*I*l**3)/35 + (192*rho*A*E**2*I**2*l)/35)/(12*E*I + A*G*k*l**2)**2 + (9*A*l*rho)/70, - ((11*G*k*rho*A**2*E*I*l**4)/70 + (54*rho*A*E**2*I**2*l**2)/35)/(12*E*I + A*G*k*l**2)**2 - (13*A*l**2*rho)/420],
                 [0, (11*A*l**2*rho)/210 - ((11*G*k*rho*A**2*E*I*l**4)/70 + (54*rho*A*E**2*I**2*l**2)/35)/(12*E*I + A*G*k*l**2)**2,                                  (A*l**3*rho)/120 + (A**3*G**2*k**2*l**7*rho)/(840*(12*E*I + A*G*k*l**2)**2),0, ((11*G*k*rho*A**2*E*I*l**4)/70 + (54*rho*A*E**2*I**2*l**2)/35)/(12*E*I + A*G*k*l**2)**2 + (13*A*l**2*rho)/420,                                    (A**3*G**2*k**2*l**7*rho)/(840*(12*E*I + A*G*k*l**2)**2) - (A*l**3*rho)/120],
                 [0,0,0,0,0,0],
                 [0,((18*G*k*rho*A**2*E*I*l**3)/35 + (192*rho*A*E**2*I**2*l)/35)/(12*E*I + A*G*k*l**2)**2 + (9*A*l*rho)/70, ((11*G*k*rho*A**2*E*I*l**4)/70 + (54*rho*A*E**2*I**2*l**2)/35)/(12*E*I + A*G*k*l**2)**2 + (13*A*l**2*rho)/420,   0,  (13*A*l*rho)/35 - ((18*G*k*rho*A**2*E*I*l**3)/35 + (192*rho*A*E**2*I**2*l)/35)/(12*E*I + A*G*k*l**2)**2,   ((11*G*k*rho*A**2*E*I*l**4)/70 + (54*rho*A*E**2*I**2*l**2)/35)/(12*E*I + A*G*k*l**2)**2 - (11*A*l**2*rho)/210],
                 [0, - ((11*G*k*rho*A**2*E*I*l**4)/70 + (54*rho*A*E**2*I**2*l**2)/35)/(12*E*I + A*G*k*l**2)**2 - (13*A*l**2*rho)/420,                                  (A**3*G**2*k**2*l**7*rho)/(840*(12*E*I + A*G*k*l**2)**2) - (A*l**3*rho)/120, 0,((11*G*k*rho*A**2*E*I*l**4)/70 + (54*rho*A*E**2*I**2*l**2)/35)/(12*E*I + A*G*k*l**2)**2 - (11*A*l**2*rho)/210,                                    (A*l**3*rho)/120 + (A**3*G**2*k**2*l**7*rho)/(840*(12*E*I + A*G*k*l**2)**2)]])
    return M       

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Spring ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class Spring1D11(Element):
    def __init__(self,nodes,ke=None,me=None,dens = 2):
        Element.__init__(self,nodes)
        self.k = ke
        self.dens = dens
        self.m = me      

    def init_unknowns(self):
        for nd in self.nodes:
            nd.init_unknowns("Ux")

        self._ndof = 1
            
    def init_keys(self):
        self.set_eIk(["N"])
        
    def calc_T(self):
        self._T = np.array([[1,0],
                            [0,1]])

    def calc_ke(self):
        self._ke = _calc_ke_for_spring(ke = self.k)
        
    def calc_me(self):
        self._me = _calc_me_for_spring(me = self.m) 



def _calc_ke_for_spring(ke = 1.0):
    return np.array([[ ke,-ke],
                     [ -ke,ke]])
def _calc_me_for_spring(me = 1.0):
    return np.array([[ 0,0],
                     [ 0,me]])

class Beam3D11(Element):

    def __init__(self,nodes,E,G,A,I,dens = 2):
        Element.__init__(self,nodes)
        self.E = E
        self.G = G
        self.A = A
        self.Ix = I[0]
        self.Iy = I[1]
        self.Iz = I[2]
        self.dens = dens

    def init_unknowns(self):
        for nd in self.nodes:
            nd.init_unknowns("Ux","Uy","Uz","Phx","Phy","Phz")

        self._ndof = 6
        
    def calc_T(self):
        TBase = _calc_Tbase_for_3d_beam(self.nodes)
        self._T = np.zeros((12,12))
        n = 3
        m = 4
        for i in range(m):
            self._T[n*i:n*(i+1),n*i:n*(i+1)] = TBase
            
    def calc_ke(self):
        self._ke = _calc_ke_for_3d_beam(E = self.E,
                                        G = self.G,
                                        A = self.A,
                                        I = [self.Ix,self.Iy,self.Iz],
                                        L = self.volume)
    def calc_me(self):
        self._me = _calc_me_for_3d_beam(E=self.E,
                                        G = self.G,
                                        A = self.A,
                                        I = self.Ix,
                                        L = self.volume,
                                        dens = self.dens)
        

    
    

##
def _calc_Tbase_for_3d_beam(nodes):
    x1,y1,z1 = nodes[0].x,nodes[0].y,nodes[0].z
    x2,y2,z2 = nodes[1].x,nodes[1].y,nodes[1].z
    if x1 == x2 and y1 == y2:
        if z2 > z1:
            return np.array([[0.,0.,1.],
                             [0.,1.,0.],
                             [-1.,0.,0.]])
        else:
            return np.array([[0.,0.,-1.],
                             [0.,1.,0.],
                             [1.,0.,0.]])
    else:
        le = np.sqrt((x1-x2)**2+(y1-y2)**2+(z1-z2)**2)
        lx = (x2-x1)/le
        mx = (y2-y1)/le
        nx = (z2-z1)/le

        d = np.sqrt(lx**2+mx**2)

        ly = -mx/d
        my = lx/d
        ny = 0.

        lz = -lx*nx/d
        mz = -mx*nx/d
        nz = d
        return np.array([[lx,mx,nx],
                         [ly,my,ny],
                         [lz,mz,nz]])

def _calc_ke_for_3d_beam(E = 1.0,G = 1.0,A = 1.0,I = [1.,1.,1.],L = 1.):
    Ix = I[0]
    Iy = I[1]
    Iz = I[2]
    
    a00 = E*A/L
    a06 = -a00

    a11 = 12.*E*Iz/L**3
    a15 = 6.*E*Iz/L**2
    a17 = -a11

    a22 = 12.*E*Iy/L**3
    a24 = -6.*E*Iy/L**2
    a28 = -a22

    a33 = G*Ix/L
    a39 = -a33

    a44 = 4.*E*Iy/L
    a48 = 6.*E*Iy/L**2
    a410 = 2.*E*Iy/L

    a55 = 4.*E*Iz/L
    a57 = -a15
    a511 = 2.*E*Iz/L

    a711 = -a15
    a810 = a48

    
    K = np.array([[a00, 0,   0,  0,    0,   0, a06,    0,   0,   0,     0,     0],
                  [0, a11,   0,  0,    0, a15,   0,  a17,   0,   0,     0,   a15],
                  [0,   0, a22,  0,  a24,   0,   0,    0, a28,   0,   a24,     0],
                  [0,   0,   0,a33,   0,    0,   0,    0,   0, a39,     0,     0],
                  [0,   0, a24,  0,  a44,   0,   0,    0, a48,   0,  a410,     0],
                  [0, a15,   0,  0,    0, a55,   0,  a57,   0,   0,     0,  a511],
                  [a06, 0,   0,  0,    0,   0, a00,    0,   0,   0,     0,     0],
                  [0, a17,   0,  0,    0, a57,   0,  a11,   0,   0,     0,  a711],
                  [0,   0, a28,  0,  a48,   0,   0,    0, a22,   0,  a810,     0],
                  [0,   0,   0,a39,    0,   0,   0,    0,   0, a33,     0,     0],
                  [0,   0, a24,  0, a410,   0,   0,    0,a810,   0,   a44,     0],
                  [0, a15,   0,  0,    0,a511,   0, a711,   0,   0,     0,   a55]])
   
    return K

def _calc_me_for_3d_beam(E = 1.0,G = 1.0,A = 1.0,I = 1.,L = 1.,dens = 20.):
    a = dens*A*L/210.
    r = I/A
    

    
    M = a*np.array([[70.,     0.,     0.,    0.,        0.,        0.,    35.,     0.,      0.,      0.,         0.,         0.],
                    [ 0.,    78.,     0.,    0.,        0.,      11*L,     0.,    27.,      0.,      0.,         0.,     -6.5*L],
                    [ 0.,     0.,    78.,    0.,    -11.*L,        0.,     0.,     0.,     27.,      0.,      6.5*L,         0.],
                    [ 0.,     0.,     0., 70.*r,        0.,        0.,     0.,     0.,      0.,  -35.*r,         0.,         0.],
                    [ 0.,     0., -11.*L,    0.,    2*L**2,        0.,     0.,     0.,  -6.5*L,      0.,  -1.5*L**2,         0.],
                    [ 0.,   11*L,     0.,    0.,        0.,    2*L**2,     0.,  6.5*L,      0.,      0.,         0.,  -1.5*L**2],
                    [35.,     0.,     0.,    0.,        0.,        0.,    70.,     0.,      0.,      0.,         0.,         0.],
                    [ 0.,    27.,     0.,    0.,        0.,     6.5*L,     0.,    78.,      0.,      0.,         0.,     -11.*L],
                    [ 0.,     0.,    27.,    0.,    -6.5*L,        0.,     0.,     0.,     78.,      0.,       11*L,         0.],
                    [ 0.,     0.,     0.,-35.*r,        0.,        0.,     0.,     0.,      0.,   70.*r,         0.,         0.],
                    [ 0.,     0.,  6.5*L,    0., -1.5*L**2,        0.,     0.,     0.,   11.*L,      0.,    2.*L**2,         0.],
                    [ 0., -6.5*L,     0.,    0.,        0., -1.5*L**2,     0., -11.*L,      0.,      0.,         0.,    2.*L**2]])
   
    return M
