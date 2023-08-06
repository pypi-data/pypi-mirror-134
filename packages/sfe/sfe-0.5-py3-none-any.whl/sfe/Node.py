
# The author: haoyan zhang
#E-mail: haoy.zhang@foxmail.com



import numpy as np

class Node(object): 
    
    def __init__(self,*coord):
        self.init_coord(*coord) 
        self._numb = None 
        self._nAk = None 
        self._nBk = None 
        self.init_keys() 
        self._dof = len(self.nAk) 
        self._disp = dict.fromkeys(self.nAk,0.) 
        self._force = dict.fromkeys(self.nBk,0.) 
     
    def __repr__(self):  
        return "Node:%r"%(self.coord)
    
    def init_coord(self,*coord): 
        self._x = 0
        self._y = 0
        self._z = 0
        
        if len(coord) == 1:
            self.dim = len(coord[0])
            if self.dim == 2:
                self._x = coord[0][0]*1.
                self._y = coord[0][1]*1.
                self.coord = (self.x,self.y)
            elif self.dim == 3:
                self._x = coord[0][0]*1.
                self._y = coord[0][1]*1.
                self._z = coord[0][2]*1.
                self.coord = (self.x,self.y,self.z)
            else:
                raise AttributeError("Node dimension is 2 or 3")
            
        elif len(coord) == 2:
            self.coord = tuple(coord)
            self.dim = 2
            self._x = coord[0]*1.
            self._y = coord[1]*1.
            self.coord = (self.x,self.y)
        elif len(coord) == 3:
            self.coord = tuple(coord)
            self.dim = 3
            self._x = coord[0]*1.
            self._y = coord[1]*1.
            self._z = coord[2]*1.
            self.coord = (self.x,self.y,self.z)
        else:
            raise AttributeError("Node dimension is 2 or 3")


    @property
    def nBk(self):
        return self._nBk

    @property
    def nAk(self):
        return self._nAk


    def set_nAk(self,val):
        self._nAk = val

    def get_nAk(self):
        return self._nAk

    def set_nBk(self,val):
        self._nBk = val

    def get_nBk(self):
        return self._nBk
    
    @property
    def x(self):
        return self._x
    
    @property
    def y(self):
        return self._y

    @property
    def z(self):
        return self._z

    @property
    def numb(self):
        return self._numb

    @property
    def force(self):
        return self._force
        
    @property
    def disp(self):
        return self._disp
        
    def init_keys(self):
        if self.dim == 2:
            self.set_nAk(("Ux","Uy","Phz"))
            self.set_nBk(("Fx","Fy","Mz"))
        elif self.dim == 3:
            self.set_nAk(("Ux","Uy","Uz","Phx","Phy","Phz"))
            self.set_nBk(("Fx","Fy","Fz","Mx","My","Mz"))

    def init_unknowns(self,*unknowns):
        for key in unknowns:
            if key in self.nAk:
                self._disp[key] = None
            else:
                raise AttributeError("Unknow disp name(%r)"%(unknowns,))
    
    def set_force(self,**forces):
        for key in forces.keys():
            if key in self.nBk:
                self._force[key] += forces[key]
            else:
                raise AttributeError("Unknow focre name(%r)"%(forces,))
    

    def get_force(self):
        return self._force

    def set_disp(self,**disp):
        for key in disp.keys():
            if key in self.nAk:
                self._disp[key] = disp[key]
            else:
                raise AttributeError("Unknow disp name(%r)"%(disp,))
              
    def get_disp(self):
        return self._disp
