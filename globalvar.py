from utils import getconfig

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