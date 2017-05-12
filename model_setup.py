import math
import os

import shutil

from utils import getconfig
from writeblockMesh import writeblockmesh


def pre_process():
    global g, det, ang, Re, v, A, wnum
    v = float(getconfig("properties", "v"))
    g = float(getconfig("properties", "g"))
    ang = int(getconfig("properties", "ang"))
    Re = float(getconfig("properties", "Re"))
    A=float(getconfig("structure","A"))
    wnum=int(getconfig("structure","wnum"))
    # calculate the thickness
    det = math.pow(3.0 * v * v * Re / (g * math.sin(math.radians(ang))), 1.0 / 3)


def copy_model(method):
    if method is "Reang":
        filename="r{0}a{1}".format(Re,ang)
    if method is "h":
        filename="r{0}a{1}h{2}".format(Re,ang,A*1000)
    if method is "wnum":
        filename="r{0}a{1}w{2}".format(Re,ang,wnum)
    if os.path.exists(filename):
        raise Exception("alreadt exists {0}".format(filename))
    else:
        shutil.copytree("model",filename)




if __name__ == '__main__':
    modelLocation = getconfig("locations", "modelLocation")
    uLocation = getconfig('locations', "uLocation")
    setFieldsLocation = getconfig("locations", "setFieldsLocation")
    gLocation = getconfig('locations', "gLocation")
    pre_process()
    copy_model("Reang")
    # with open(uLocation) as ufile, open(setFieldsLocation) as setfile, open(
    #         gLocation) as gfile:
        # define the 'blockMeshDict' document
    writeblockmesh(modelLocation, det)
