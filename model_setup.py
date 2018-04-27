import math
import os
import shutil

from writeFiles.writeblockMesh import writeblockmesh
from writeFiles.writecommand import writecommand
from writeFiles.writegfile import writegfile
from writeFiles.writesamplefile import writesample
from writeFiles.writesetfields import writesetfields
from writeFiles.writetransportProperties import writetransportProperties
from writeFiles.writeudocument import writeudocument
import globalvar as gv


def pre_process():
    # calculate the thickness
    gv.det = math.pow(
            3.0 * gv.v * gv.v * gv.Re / (gv.g * math.sin(math.radians(gv.ang))),
            1.0 / 3)
    print('det:' + str(gv.det))


def copy_model(method):
    if method == 'density':
        filename = "r{0}a{1}density{2}".format(gv.Re, gv.ang, gv.density)
    if method == 'sigma':
        filename = "r{0}a{1}sigma{2}".format(gv.Re, gv.ang, gv.sigma)
    if method == 'wangge':
        filename = "r{0}a{1}wg{2}".format(gv.Re, gv.ang, gv.wanggemidu)
    if method == "Reang":
        filename = "r{0}a{1}".format(gv.Re, gv.ang)
    if method == "h":
        filename = "r{0}a{1}h{2}".format(gv.Re, gv.ang, gv.A * 1000)
    if method == "wnum":
        filename = "r{0}a{1}w{2}".format(gv.Re, gv.ang, gv.wnum)
    if method == "niandu":
        filename = "r{0}a{1}niandu{2}".format(gv.Re, gv.ang, int(gv.v * 10000000))

    gv.realfiledir = os.path.join(gv.basedir, filename)
    if os.path.exists(gv.realfiledir):
        raise Exception("alreadt exists {0}".format(gv.realfiledir))
    else:
        if gv.air_speed==0:
            shutil.copytree("model", gv.realfiledir)
        else:
            shutil.copytree("twophasemodel", gv.realfiledir)
        gv.files.append([filename, gv.Re, gv.A, gv.wnum, gv.v, gv.ang, gv.density, gv.sigma, gv.L])
    writefiles(filename)


def writefiles(filename):
    modelLocation = os.path.join(gv.basedir, filename, 'constant', 'polyMesh', 'blockMeshDict')
    uLocation = os.path.join(gv.basedir, filename, '0', 'U')
    setFieldsLocation = os.path.join(gv.basedir, filename, 'system', 'setFieldsDict')
    gLocation = os.path.join(gv.basedir, filename, 'constant', 'g')
    sampleLocation = os.path.join(gv.basedir, filename, 'system', 'sampleDict')
    transportPropertiesLocation = os.path.join(gv.basedir, filename, 'constant', 'transportProperties')
    writeblockmesh(modelLocation)
    writeudocument(uLocation)
    writesetfields(setFieldsLocation)
    writegfile(gLocation)
    writesample(sampleLocation)
    writetransportProperties(transportPropertiesLocation)


def do(method):
    gv.method = method
    bd = os.path.join(gv.base, gv.structure)
    if method == 'density':
        gv.basedir = os.path.join(bd, 'density')
        a=1227
        for i in [0.8,0.4]:
            gv.density=i*a
            if i==0.4:
                for j in frange(46, 55, 0.5):
                    gv.Re = j
                    pre_process()
                    copy_model("density")
            if i==0.8:
                for j in frange(37, 40, 0.5):
                    gv.Re = j
                    pre_process()
                    copy_model("density")

    if method == 'sigma':
        gv.basedir = os.path.join(bd, 'sigma')
        a=671
        for i in [2,0.8,1.5]:
            gv.sigma = a*i / 10000

            if i==2:
                for j in frange(43, 45.5, 0.5):
                    gv.Re = j
                    pre_process()
                    copy_model("sigma")
            if i==0.8:
                for j in frange(26.5, 33, 0.5):
                    gv.Re = j
                    pre_process()
                    copy_model("sigma")
            if i==1.5:
                for j in frange(34, 45, 0.5):
                    gv.Re = j
                    pre_process()
                    copy_model("sigma")

    if method == 'wangge':
        gv.basedir = os.path.join(bd, 'wangge')
        for i in range(40, 46):
            gv.wanggemidu = i
            gv.Re = 40
            pre_process()
            copy_model("wangge")
    # change Re in fixed angle
    if method == 'Reang':
        gv.basedir = os.path.join(bd, 'Reang')
        for i in [11]:
            gv.ang = i
            if i==11:
                for j in range(1,101,2):
                    gv.Re = j
                    pre_process()
                    copy_model("Reang")



    if method == 'height':
        # change height of corrugation
        gv.basedir = os.path.join(bd, 'height')
        for i in range(1, 4):
            gv.A = 0.001*i
            for j in range(1, 102, 2):
                gv.Re = j
                pre_process()
                copy_model("h")
    if method == 'wavenums':
        # change wavenums
        gv.basedir = os.path.join(bd, 'wavenums')
        for i in range(2, 10):
            if i == 5:
                continue
            gv.wnum = i
            for j in range(1, 102, 2):
                gv.Re = j
                pre_process()
                copy_model("wnum")
    if method == 'niandu':

        # change wavenums
        gv.basedir = os.path.join(bd, 'niandu')
        a=11.6
        gv.v *= 0.1
        gv.density*=0.1
        gv.sigma*=0.1

        for j in frange(408,432,2):
            gv.Re = j
            pre_process()
            copy_model("niandu")

            # if i==0.2:
            #     for j in [101,119.5,120.5,121.5,114,116]:
            #         gv.Re = j
            #         pre_process()
            #         copy_model("niandu")



    writecommand()


def frange(start, stop, step=1.0):
    while start < stop:
        yield start
        start += step

if __name__ == '__main__':
    # 一次只能运行一个
    # do('Reang')
    # do('height')
    # do('wavenums')
    do('niandu')
    # do('wangge')
    # do('density')
    # do('sigma')