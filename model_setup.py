import math
import os
import shutil

from writeFiles.writeblockMesh import writeblockmesh
from writeFiles.writegfile import writegfile
from writeFiles.writesetfields import writesetfields
from writeFiles.writeudocument import writeudocument
import globalvar


def pre_process():
    # calculate the thickness
    globalvar.det = math.pow(
            3.0 * globalvar.v * globalvar.v * globalvar.Re / (globalvar.g * math.sin(math.radians(globalvar.ang))),
            1.0 / 3)


def copy_model(method):
    if method == "Reang":
        filename = "r{0}a{1}".format(globalvar.Re, globalvar.ang)
    if method == "h":
        filename = "r{0}a{1}h{2}".format(globalvar.Re, globalvar.ang, globalvar.A * 1000)
    if method == "wnum":
        filename = "r{0}a{1}w{2}".format(globalvar.Re, globalvar.ang, globalvar.wnum)
    if os.path.exists(filename):
        raise Exception("alreadt exists {0}".format(filename))
    else:
        shutil.copytree("model", os.path.join(basedir, filename))
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
    # change Re in fixed angle
    basedir = os.path.join(globalvar.base, 'Reang')
    for i in range(1, 7, 2):
        globalvar.Re = i
        pre_process()
        copy_model("Reang")
    # change height of corrugation
    basedir = os.path.join(globalvar.base, 'height')
    for i in range(1, 3):
        globalvar.A = i / 1000
        pre_process()
        copy_model("h")
    # change wavenums
    basedir = os.path.join(globalvar.base, 'wavenums')
    for i in range(3, 6):
        globalvar.wnum = i
        pre_process()
        copy_model("wnum")
