import math
import os
import shutil

from writeFiles.writeblockMesh import writeblockmesh
from writeFiles.writecommand import writecommand
from writeFiles.writegfile import writegfile
from writeFiles.writesamplefile import writesample
from writeFiles.writesetfields import writesetfields
from writeFiles.writeudocument import writeudocument
import globalvar as gv


def pre_process():
    # calculate the thickness
    gv.det = math.pow(
            3.0 * gv.v * gv.v * gv.Re / (gv.g * math.sin(math.radians(gv.ang))),
            1.0 / 3)
    print('det:'+str(gv.det))


def copy_model(method):
    if method == "Reang":
        filename = "r{0}a{1}".format(gv.Re, gv.ang)
    if method == "h":
        filename = "r{0}a{1}h{2}".format(gv.Re, gv.ang, gv.A * 1000)
    if method == "wnum":
        filename = "r{0}a{1}w{2}".format(gv.Re, gv.ang, gv.wnum)
    gv.realfiledir = os.path.join(gv.basedir, filename)
    if os.path.exists(gv.realfiledir):
        raise Exception("alreadt exists {0}".format(gv.realfiledir))
    else:
        shutil.copytree("model", gv.realfiledir)
        gv.files.append([filename,gv.Re,gv.A,gv.wnum])
    writefiles(filename)


def writefiles(filename):
    modelLocation = os.path.join(gv.basedir, filename, 'constant', 'polyMesh', 'blockMeshDict')
    uLocation = os.path.join(gv.basedir, filename, '0', 'U')
    setFieldsLocation = os.path.join(gv.basedir, filename, 'system', 'setFieldsDict')
    gLocation = os.path.join(gv.basedir, filename, 'constant', 'g')
    sampleLocation = os.path.join(gv.basedir, filename, 'system', 'sampleDict')
    writeblockmesh(modelLocation)
    writeudocument(uLocation)
    writesetfields(setFieldsLocation)
    writegfile(gLocation)
    writesample(sampleLocation)


def do(method):
    gv.method=method
    bd = os.path.join(gv.base, gv.structure)
    # change Re in fixed angle
    if method == 'Reang':
        gv.basedir = os.path.join(bd, 'Reang')
        for i in [1, 5, 15]:
            gv.Re = i
            pre_process()
            copy_model("Reang")
    if method == 'height':
        # change height of corrugation
        gv.basedir = os.path.join(bd, 'height')
        for i in range(1, 5):
            gv.A = i / 1000
            for j in range(1, 102, 2):
                gv.Re = j
                pre_process()
                copy_model("h")
    if method == 'wavenums':
        # change wavenums
        gv.basedir = os.path.join(bd, 'wavenums')
        for i in range(2, 10):
            gv.wnum = i
            for j in range(1, 100, 5):
                gv.Re = j
                pre_process()
                copy_model("wnum")
    writecommand()


if __name__ == '__main__':
    # 一次只能运行一个
    # do('Reang')
    # do('height')
    do('wavenums')
