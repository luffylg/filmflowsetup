from utils import getconfig


# class globalvar():
#     def __init__(self):
#         self.Re = int(getconfig("properties", "Re"))
#         self.A = float(getconfig("structure", "A"))
#         self.wnum = int(getconfig("structure", "wnum"))
#         self.base = 'calculate'
#         self.L = float(getconfig("structure", "L"))
#         self.v = float(getconfig("properties", "v"))
#         self.g = float(getconfig("properties", "g"))
#         self.ang = int(getconfig("properties", "ang"))
#         self.L_in = float(getconfig("structure", "L_in"))
#         self.L_out = float(getconfig("structure", "L_out"))
#         self.width = float(getconfig("structure", "width"))
#         self.structure = getconfig("structure", "structure")
#         self.realfiledir = ''
#         self.samedirecasflow = True
files=[]
Re = int(getconfig("properties", "Re"))
A = float(getconfig("structure", "A"))
wnum = int(getconfig("structure", "wnum"))
base = 'calculate'
L = float(getconfig("structure", "L"))
v = float(getconfig("properties", "v"))
g = float(getconfig("properties", "g"))
ang = int(getconfig("properties", "ang"))
L_in=float(getconfig("structure", "L_in"))
L_out=float(getconfig("structure", "L_out"))
width=float(getconfig("structure", "width"))
structure=getconfig("structure", "structure")
realfiledir=''
samedirecasflow=True
is3d=True