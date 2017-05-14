import math
import os
import shutil

from writeFiles.writeblockMesh import writeblockmesh
from writeFiles.writegfile import writegfile
from writeFiles.writesetfields import writesetfields
from writeFiles.writeudocument import writeudocument
import globalvar as gv


def pre_process():
    # calculate the thickness
    gv.det = math.pow(
            3.0 * gv.v * gv.v * gv.Re / (gv.g * math.sin(math.radians(gv.ang))),
            1.0 / 3)


def copy_model(method):
    if method == "Reang":
        filename = "r{0}a{1}".format(gv.Re, gv.ang)
    if method == "h":
        filename = "r{0}a{1}h{2}".format(gv.Re, gv.ang, gv.A * 1000)
    if method == "wnum":
        filename = "r{0}a{1}w{2}".format(gv.Re, gv.ang, gv.wnum)
    gv.realfiledir = os.path.join(basedir, filename)
    if os.path.exists(gv.realfiledir):
        raise Exception("alreadt exists {0}".format(gv.realfiledir))
    else:
        shutil.copytree("model", gv.realfiledir)
    writefiles(filename)


def writefiles(filename):
    modelLocation = os.path.join(basedir, filename, 'constant', 'polyMesh', 'blockMeshDict')
    uLocation = os.path.join(basedir, filename, '0', 'U')
    setFieldsLocation = os.path.join(basedir, filename, 'system', 'setFieldsDict')
    gLocation = os.path.join(basedir, filename, 'constant', 'g')
    writeblockmesh(modelLocation)
    writeudocument(uLocation)
    writesetfields(setFieldsLocation)
    writegfile(gLocation)


if __name__ == '__main__':
    bd = os.path.join(gv.base, gv.structure)
    # change Re in fixed angle
    basedir = os.path.join(bd, 'Reang')
    for i in range(1, 7, 2):
        gv.Re = i
        pre_process()
        copy_model("Reang")
    # change height of corrugation
    basedir = os.path.join(bd, 'height')
    for i in range(1, 3):
        gv.A = i / 1000
        pre_process()
        copy_model("h")
    # change wavenums
    basedir = os.path.join(bd, 'wavenums')
    for i in range(2, 5):
        gv.wnum = i
        pre_process()
        copy_model("wnum")
