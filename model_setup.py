import math
from utils import getconfig
from writeblockMesh import writeblockmesh


def pre_process():
    global g, det, ang, Re, v
    v = float(getconfig("properties", "v"))
    g = float(getconfig("properties", "g"))
    ang = float(getconfig("properties", "ang"))
    Re = float(getconfig("properties", "Re"))
    # calculate the thickness
    det = math.pow(3.0 * v * v * Re / (g * math.sin(math.radians(ang))), 1.0 / 3)

if __name__ == '__main__':
    modelLocation = getconfig("locations", "modelLocation")
    uLocation = getconfig('locations', "uLocation")
    setFieldsLocation = getconfig("locations", "setFieldsLocation")
    gLocation = getconfig('locations', "gLocation")
    pre_process()

    # with open(uLocation) as ufile, open(setFieldsLocation) as setfile, open(
    #         gLocation) as gfile:
        # define the 'blockMeshDict' document
    writeblockmesh(modelLocation, det)
