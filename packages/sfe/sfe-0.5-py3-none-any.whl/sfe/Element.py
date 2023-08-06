
# The author: haoyan zhang
#E-mail: haoy.zhang@foxmail.com


from sfe.Node import *




class Element(object):

    def __init__(self,nodes):
        for nd in nodes:
            assert issubclass(type(nd),Node),"Must be Node type"
            
        self._nodes = nodes
        self._dim = 1
        self._etype = self.__class__.__name__
        self._numb = None
        self._eIk = None
        self._ndof = None 
        self._Ke = None
        self._Me = None
        self._volume = None
        self.init_keys()
        self.init_nodes(nodes)
        self.init_unknowns()
        self._force =  dict.fromkeys(self.eIk,0.)
        self.dens = None
        self.t = 1.
        
         
    def __repr__(self):
        return "%s Element: %r"%(self.etype,self.nodes,)
    
    @property
    def volume(self):
        return self._volume

    @property
    def B(self):
        return self._B

    @property
    def D(self):
        return self._D

    @property
    def dim(self):
        return self.nodes[0].dim
    
    @property
    def eIk(self):
        return self._eIk
    
    @property
    def Ke(self):
        return self._Ke

    @property
    def Me(self):
        return self._Me
    
    @property
    def ndof(self):
        return self._ndof
    
        
    @property
    def nodes(self):
        return self._nodes
    
    @property
    def etype(self):
        return self._etype
        
    @property
    def numb(self):
        return self._numb
    
    @property
    def non(self):
        return len(self._nodes)
    
    def set_eIk(self,val):
        self._eIk = val

    def get_eIk(self):
        return self._eIk

    def get_ndof(self):
        return self._ndof
    
    def get_element_type(self):
        return self._etype

    def get_nodes(self):
        return self._nodes

    def init_nodes(self,nodes):
        v = np.array(nodes[0].coord)-np.array(nodes[1].coord)
        le = np.linalg.norm(v)
        self._volume = le
        

    def init_keys(self):
        if self.dim == 2:
            self.set_eIk(("N","Ty","Mz"))
        if self.dim == 3:
            self.set_eIk(("N","Ty","Tz","Mx","My","Mz"))
        

    @property
    def T(self):
        return self._T

    @property
    def me(self):
        return self._me
    
    @property
    def ke(self):
        return self._ke

    @property
    def force(self):
        return self._force

    def calc_Ke(self):
        self.calc_T()
        self.calc_ke()
        self._Ke = self.t*np.dot(np.dot(self.T.T,self.ke),self.T)

    def calc_Me(self):
        self.calc_T()
        self.calc_me()
        self._Me = np.dot(np.dot(self.T.T,self.me),self.T)
        
    def evaluate(self):
        u = np.array([[nd.disp[key] for nd in self.nodes for key in nd.nAk[:self.ndof]]])
        self._undealed_force = np.dot(self.T,np.dot(self.Ke,u.T))
        self.distribute_force()

    def distribute_force(self):
        n = len(self.eIk)
        for i,val in enumerate(self.eIk):
            self._force[val] += self._undealed_force[i::n]