import math
import os
import shutil

from utils import getconfig
from writeFiles.writeblockMesh import writeblockmesh
from writeFiles.writegfile import writegfile
from writeFiles.writesetfields import writesetfields
from writeFiles.writeudocument import writeudocument


def pre_process():
    global g, det, ang, v, L
    L = float(getconfig("structure", "L"))
    v = float(getconfig("properties", "v"))
    g = float(getconfig("properties", "g"))
    ang = int(getconfig("properties", "ang"))
    # calculate the thickness
    det = math.pow(3.0 * v * v * Re / (g * math.sin(math.radians(ang))), 1.0 / 3)


def copy_model(method):
    if method == "Reang":
        filename = "r{0}a{1}".format(Re, ang)
    if method == "h":
        filename = "r{0}a{1}h{2}".format(Re, ang, A * 1000)
    if method == "wnum":
        filename = "r{0}a{1}w{2}".format(Re, ang, wnum)
    if os.path.exists(filename):
        raise Exception("alreadt exists {0}".format(filename))
    else:
        shutil.copytree("model", os.path.join(basedir,filename))
    writefiles(filename)



def writefiles(filename):
    modelLocation = os.path.join(basedir, filename, 'constant', 'polyMesh', 'blockMeshDict')
    uLocation = os.path.join(basedir,filename, '0', 'U')
    setFieldsLocation = os.path.join(basedir,filename, 'system', 'setFieldsDict')
    gLocation = os.path.join(basedir,filename, 'constant', 'g')
    writeblockmesh(modelLocation, det)
    writeudocument(uLocation, det, ang, v, g)
    writesetfields(setFieldsLocation, wnum, L, det)
    writegfile(gLocation, g, ang)


global Re, A, wnum, basedir
Re = int(getconfig("properties", "Re"))
A = float(getconfig("structure", "A"))
wnum = int(getconfig("structure", "wnum"))
base='calculate'

if __name__ == '__main__':
    # change Re in fixed angle
    basedir=os.path.join(base,'Reang')
    for i in range(1, 7, 2):
        Re = i
        pre_process()
        copy_model("Reang")
    # change height of corrugation
    basedir=os.path.join(base,'height')
    for i in range(1, 3):
        A = i / 1000
        pre_process()
        copy_model("h")
    # change wavenums
    basedir=os.path.join(base,'wavenums')
    for i in range(3, 6):
        wnum = i
        pre_process()
        copy_model("wnum")
