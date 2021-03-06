import math

import globalvar as gv
from writeFiles.writesinMesh import writesinmesh


def writetridot(modelfile):
    modelfile.write('(%10.8f %10.8f %10.8f)\n' % (0, 0, 0))  # 0
    modelfile.write('(%10.8f %10.8f %10.8f)\n' % (0, gv.det, 0))  # 1
    modelfile.write('(%10.8f %10.8f %10.8f)\n' % (0, 4 * gv.det, 0))  # 2

    modelfile.write('(%10.8f %10.8f %10.8f)\n' % (gv.L_in, 0, 0))  # 3
    modelfile.write('(%10.8f %10.8f %10.8f)\n' % (gv.L_in, gv.det, 0))  # 4
    modelfile.write('(%10.8f %10.8f %10.8f)\n' % (gv.L_in, 4 * gv.det, 0))  # 5
    for i in range(1, gv.wnum + 1):
        modelfile.write('(%10.8f %10.8f %10.8f)\n' % (gv.L_in + gv.L / 2 * (2*i-1), -gv.A, 0))  # i*6
        modelfile.write('(%10.8f %10.8f %10.8f)\n' % (gv.L_in + gv.L / 2 * (2*i-1), gv.det, 0))  # i*6+1
        modelfile.write('(%10.8f %10.8f %10.8f)\n' % (gv.L_in + gv.L / 2 * (2*i-1), 4 * gv.det, 0))  # i*6+2

        modelfile.write('(%10.8f %10.8f %10.8f)\n' % (gv.L_in + gv.L * i, 0, 0))  # i*6+3
        modelfile.write('(%10.8f %10.8f %10.8f)\n' % (gv.L_in + gv.L * i, gv.det, 0))  # i*6+4
        modelfile.write('(%10.8f %10.8f %10.8f)\n' % (gv.L_in + gv.L * i, 4 * gv.det, 0))  # i*6+5

    modelfile.write('(%10.8f %10.8f %10.8f)\n' % (gv.L_in + gv.L_out + gv.L * gv.wnum, 0, 0))  # wnum*6+6
    modelfile.write('(%10.8f %10.8f %10.8f)\n' % (gv.L_in + gv.L_out + gv.L * gv.wnum, gv.det, 0))  # wnum*6+7
    modelfile.write('(%10.8f %10.8f %10.8f)\n' % (gv.L_in + gv.L_out + gv.L * gv.wnum, 4 * gv.det, 0))  # wnum*6+8

    modelfile.write('(%10.8f %10.8f %10.8f)\n' % (0, 0, gv.width))  # wnum*6+9
    modelfile.write('(%10.8f %10.8f %10.8f)\n' % (0, gv.det, gv.width))  # 1
    modelfile.write('(%10.8f %10.8f %10.8f)\n' % (0, 4 * gv.det, gv.width))  # 2

    modelfile.write('(%10.8f %10.8f %10.8f)\n' % (gv.L_in, 0, gv.width))  # 3
    modelfile.write('(%10.8f %10.8f %10.8f)\n' % (gv.L_in, gv.det, gv.width))  # 4
    modelfile.write('(%10.8f %10.8f %10.8f)\n' % (gv.L_in, 4 * gv.det, gv.width))  # 5
    for i in range(1, gv.wnum + 1):
        modelfile.write('(%10.8f %10.8f %10.8f)\n' % (gv.L_in + gv.L / 2 * (2*i-1), -gv.A, gv.width))  # i*6
        modelfile.write('(%10.8f %10.8f %10.8f)\n' % (gv.L_in + gv.L / 2 * (2*i-1), gv.det, gv.width))  # i*6+1
        modelfile.write('(%10.8f %10.8f %10.8f)\n' % (gv.L_in + gv.L / 2 * (2*i-1), 4 * gv.det, gv.width))  # i*6+2

        modelfile.write('(%10.8f %10.8f %10.8f)\n' % (gv.L_in + gv.L * i, 0, gv.width))  # i*6+3
        modelfile.write('(%10.8f %10.8f %10.8f)\n' % (gv.L_in + gv.L * i, gv.det, gv.width))  # i*6+4
        modelfile.write('(%10.8f %10.8f %10.8f)\n' % (gv.L_in + gv.L * i, 4 * gv.det, gv.width))  # i*6+5

    modelfile.write('(%10.8f %10.8f %10.8f)\n' % (gv.L_in + gv.L_out + gv.L * gv.wnum, 0, gv.width))  # wnum*6+6
    modelfile.write('(%10.8f %10.8f %10.8f)\n' % (gv.L_in + gv.L_out + gv.L * gv.wnum, gv.det, gv.width))  # wnum*6+7
    modelfile.write(
            '(%10.8f %10.8f %10.8f)\n' % (gv.L_in + gv.L_out + gv.L * gv.wnum, 4 * gv.det, gv.width))  # wnum*6+8


def writerecdot(modelfile):
    modelfile.write('(%10.8f %10.8f %10.8f)\n' % (0, 0, 0))  # 0
    modelfile.write('(%10.8f %10.8f %10.8f)\n' % (0, gv.det, 0))  # 1
    modelfile.write('(%10.8f %10.8f %10.8f)\n' % (0, 4 * gv.det, 0))  # 2

    for i in range(1, gv.wnum + 1):
        modelfile.write('(%10.8f %10.8f %10.8f)\n' % (gv.L_in + gv.L / 4 * (4*i-3), -gv.A, 0))  # i*8-5
        modelfile.write('(%10.8f %10.8f %10.8f)\n' % (gv.L_in + gv.L / 4 * (4*i-3), 0, 0))  # i*8-4
        modelfile.write('(%10.8f %10.8f %10.8f)\n' % (gv.L_in + gv.L / 4 * (4*i-3), gv.det, 0))  # i*8-3
        modelfile.write('(%10.8f %10.8f %10.8f)\n' % (gv.L_in + gv.L / 4 * (4*i-3), 4 * gv.det, 0))  # i*8-2

        modelfile.write('(%10.8f %10.8f %10.8f)\n' % (gv.L_in + gv.L / 4 * (4*i-1), -gv.A, 0))  # i*8-1
        modelfile.write('(%10.8f %10.8f %10.8f)\n' % (gv.L_in + gv.L / 4 * (4*i-1), 0, 0))  # i*8
        modelfile.write('(%10.8f %10.8f %10.8f)\n' % (gv.L_in + gv.L / 4 * (4*i-1), gv.det, 0))  # i*8+1
        modelfile.write('(%10.8f %10.8f %10.8f)\n' % (gv.L_in + gv.L / 4 * (4*i-1), 4 * gv.det, 0))  # i*8+2

    modelfile.write('(%10.8f %10.8f %10.8f)\n' % (gv.L_in + gv.L_out + gv.L * gv.wnum, 0, 0))  # wnum*8+3
    modelfile.write('(%10.8f %10.8f %10.8f)\n' % (gv.L_in + gv.L_out + gv.L * gv.wnum, gv.det, 0))  # wnum*8+4
    modelfile.write('(%10.8f %10.8f %10.8f)\n' % (gv.L_in + gv.L_out + gv.L * gv.wnum, 4 * gv.det, 0))  # wnum*8+5

    modelfile.write('(%10.8f %10.8f %10.8f)\n' % (0, 0, gv.width))  # wnum*8+6
    modelfile.write('(%10.8f %10.8f %10.8f)\n' % (0, gv.det, gv.width))  # 1
    modelfile.write('(%10.8f %10.8f %10.8f)\n' % (0, 4 * gv.det, gv.width))  # 2

    for i in range(1, gv.wnum + 1):
        modelfile.write('(%10.8f %10.8f %10.8f)\n' % (gv.L_in + gv.L / 4 * (4*i-3), -gv.A, gv.width))  # i*8-5
        modelfile.write('(%10.8f %10.8f %10.8f)\n' % (gv.L_in + gv.L / 4 * (4*i-3), 0, gv.width))  # i*8-4
        modelfile.write('(%10.8f %10.8f %10.8f)\n' % (gv.L_in + gv.L / 4 * (4*i-3), gv.det, gv.width))  # i*8-3
        modelfile.write('(%10.8f %10.8f %10.8f)\n' % (gv.L_in + gv.L / 4 * (4*i-3), 4 * gv.det, gv.width))  # i*8-2

        modelfile.write('(%10.8f %10.8f %10.8f)\n' % (gv.L_in + gv.L / 4 * (4*i-1), -gv.A, gv.width))  # i*8-1
        modelfile.write('(%10.8f %10.8f %10.8f)\n' % (gv.L_in + gv.L / 4 * (4*i-1), 0, gv.width))  # i*8
        modelfile.write('(%10.8f %10.8f %10.8f)\n' % (gv.L_in + gv.L / 4 * (4*i-1), gv.det, gv.width))  # i*8+1
        modelfile.write('(%10.8f %10.8f %10.8f)\n' % (gv.L_in + gv.L / 4 * (4*i-1), 4 * gv.det, gv.width))  # i*8+2

    modelfile.write('(%10.8f %10.8f %10.8f)\n' % (gv.L_in + gv.L_out + gv.L * gv.wnum, 0, gv.width))  # wnum*8+3
    modelfile.write('(%10.8f %10.8f %10.8f)\n' % (gv.L_in + gv.L_out + gv.L * gv.wnum, gv.det, gv.width))  # wnum*8+4
    modelfile.write(
            '(%10.8f %10.8f %10.8f)\n' % (gv.L_in + gv.L_out + gv.L * gv.wnum, 4 * gv.det, gv.width))  # wnum*8+5


def writeblockmesh(modelLocation):
    if gv.structure == 'sin' or gv.structure == 'plate':
        writesinmesh(modelLocation)
        return
    with open(modelLocation, 'w') as modelfile:
        # define the 'blockMeshDict' document
        modelfile.write('/*--------------------------------*- C++ -*----------------------------------  \n')
        modelfile.write('| =========                 |                                                 |\n')
        modelfile.write('| \\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox           |\n')
        modelfile.write('|  \\    /   O peration     | Version:  1.7.1                                 |\n')
        modelfile.write('|   \\  /    A nd           | Web:      www.OpenFOAM.com                      |\n')
        modelfile.write('|    \\/     M anipulation  |                                                 |\n')
        modelfile.write('  ---------------------------------------------------------------------------*/\n')
        modelfile.write('FoamFile\n')
        modelfile.write('{\n')
        modelfile.write('    version     2.0;\n')
        modelfile.write('    format      ascii;\n')
        modelfile.write('    class       dictionary;\n')
        modelfile.write('    object      blockMeshDict;\n')
        modelfile.write('}\n')
        modelfile.write('// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //\n')
        modelfile.write('\n')
        modelfile.write('convertToMeters %10.8f;\n' % 1)
        modelfile.write('\n')
        modelfile.write('vertices\n')
        modelfile.write('(\n')

        if gv.structure == 'tri':
            writetridot(modelfile)

        if gv.structure == 'rec':
            writerecdot(modelfile)

        modelfile.write(');\n')
        modelfile.write('blocks \n')
        modelfile.write('(\n')
        dmi = gv.det / gv.wanggemidu
        # z方向网格密度
        zdmi = 0.0004
        # z方向网格数
        if gv.width == 0.0001 or not gv.is3d:
            znum = 1
        else:
            znum = math.ceil(gv.width/zdmi)

        if gv.structure == 'tri':
            opch = gv.wnum * 6 + 9
            for i in range(0, 2 * gv.wnum + 2):
                CELLS = math.ceil(gv.L / 2 / dmi)
                if i == 0:
                    CELLS = math.ceil(gv.L_in / dmi)
                if i == 2 * gv.wnum + 1:
                    CELLS = math.ceil(gv.L_out / dmi)
                modelfile.write('     hex (%d %d %d %d %d %d %d %d) (%d 24 %d) simpleGrading (1 1 1)\n' % (
                    i * 3, (i + 1) * 3, (i + 1) * 3 + 1, i * 3 + 1, i * 3 + opch,
                    (i + 1) * 3 + opch,
                    (i + 1) * 3 + 1 + opch, i * 3 + 1 + opch, CELLS, znum))
                modelfile.write('     hex (%d %d %d %d %d %d %d %d) (%d 25 %d) simpleGrading (1 2 1)\n' % (
                    i * 3 + 1, (i + 1) * 3 + 1, (i + 1) * 3 + 1 + 1, i * 3 + 1 + 1, i * 3 + opch + 1,
                    (i + 1) * 3 + opch + 1, (i + 1) * 3 + 1 + opch + 1,
                    i * 3 + 1 + opch + 1, CELLS, znum))

        if gv.structure == 'rec':
            opch = gv.wnum * 8 + 6
            if gv.wanggemidu!=12:
                modelfile.write('     hex (0 4 5 1 %d %d %d %d) (%d %d %d) simpleGrading (1 1 1)\n' % (
                    opch, opch + 4, opch + 5, opch + 1, math.ceil(gv.L_in / dmi),gv.wanggemidu*2, znum))
                modelfile.write('     hex (1 5 6 2 %d %d %d %d) (%d %d %d) simpleGrading (1 2 1)\n' % (
                    opch + 1, opch + 5, opch + 6, opch + 2, math.ceil(gv.L_in / dmi), gv.wanggemidu*2,znum))
            else:
                modelfile.write('     hex (0 4 5 1 %d %d %d %d) (%d 24 %d) simpleGrading (1 1 1)\n' % (
                    opch, opch + 4, opch + 5, opch + 1, math.ceil(gv.L_in / dmi), znum))
                modelfile.write('     hex (1 5 6 2 %d %d %d %d) (%d 25 %d) simpleGrading (1 2 1)\n' % (
                    opch + 1, opch + 5, opch + 6, opch + 2, math.ceil(gv.L_in / dmi), znum))

            CELLS = math.ceil(gv.L / 2 / dmi)
            for i in range(1, 2 * gv.wnum):
                if i % 2 == 1:
                    a0 = 4 * (i - 1) + 3
                    modelfile.write('     hex (%d %d %d %d %d %d %d %d) (%d %d %d) simpleGrading (1 1 1)\n' % (
                        a0, a0 + 4, a0 + 4 + 1, a0 + 1,
                        a0 + opch, a0 + 4 + opch, a0 + 4 + 1 + opch,
                        a0 + 1 + opch, CELLS, math.ceil(gv.A / dmi), znum))

                a0 = 4 * (i - 1) + 4
                if gv.wanggemidu!=12:
                    modelfile.write('     hex (%d %d %d %d %d %d %d %d) (%d %d %d) simpleGrading (1 1 1)\n' % (
                        a0, a0 + 4, a0 + 4 + 1, a0 + 1,
                        a0 + opch, a0 + 4 + opch, a0 + 4 + 1 + opch,
                        a0 + 1 + opch, CELLS, gv.wanggemidu*2,znum))

                    a0 = 4 * (i - 1) + 5
                    modelfile.write('     hex (%d %d %d %d %d %d %d %d) (%d %d %d) simpleGrading (1 2 1)\n' % (
                        a0, a0 + 4, a0 + 4 + 1, a0 + 1,
                        a0 + opch, a0 + 4 + opch, a0 + 4 + 1 + opch,
                        a0 + 1 + opch, CELLS, gv.wanggemidu*2,znum))
                else:
                    modelfile.write('     hex (%d %d %d %d %d %d %d %d) (%d 24 %d) simpleGrading (1 1 1)\n' % (
                        a0, a0 + 4, a0 + 4 + 1, a0 + 1,
                        a0 + opch, a0 + 4 + opch, a0 + 4 + 1 + opch,
                        a0 + 1 + opch, CELLS, znum))

                    a0 = 4 * (i - 1) + 5
                    modelfile.write('     hex (%d %d %d %d %d %d %d %d) (%d 25 %d) simpleGrading (1 2 1)\n' % (
                        a0, a0 + 4, a0 + 4 + 1, a0 + 1,
                        a0 + opch, a0 + 4 + opch, a0 + 4 + 1 + opch,
                        a0 + 1 + opch, CELLS, znum))

            a0 = 4 * (2 * gv.wnum - 1) + 4
            if gv.wanggemidu!=12:
                modelfile.write('     hex (%d %d %d %d %d %d %d %d) (%d %d %d) simpleGrading (1 1 1)\n' % (
                    a0, a0 + 3, a0 + 3 + 1,
                    a0 + 1, a0 + opch, a0 + 3 + opch,
                    a0 + 3 + 1 + opch, a0 + 1 + opch,
                    math.ceil(gv.L_out / dmi),gv.wanggemidu*2, znum))
                modelfile.write('     hex (%d %d %d %d %d %d %d %d) (%d %d %d) simpleGrading (1 2 1)\n' % (
                    a0 + 1, a0 + 3 + 1, a0 + 3 + 1 + 1,
                    a0 + 1 + 1, a0 + opch + 1,
                    a0 + 3 + opch + 1, a0 + 3 + 1 + opch + 1,
                    a0 + 1 + opch + 1, math.ceil(gv.L_out / dmi), gv.wanggemidu*2,znum))
            else:
                modelfile.write('     hex (%d %d %d %d %d %d %d %d) (%d 24 %d) simpleGrading (1 1 1)\n' % (
                    a0, a0 + 3, a0 + 3 + 1,
                    a0 + 1, a0 + opch, a0 + 3 + opch,
                    a0 + 3 + 1 + opch, a0 + 1 + opch,
                    math.ceil(gv.L_out / dmi), znum))
                modelfile.write('     hex (%d %d %d %d %d %d %d %d) (%d 25 %d) simpleGrading (1 2 1)\n' % (
                    a0 + 1, a0 + 3 + 1, a0 + 3 + 1 + 1,
                    a0 + 1 + 1, a0 + opch + 1,
                    a0 + 3 + opch + 1, a0 + 3 + 1 + opch + 1,
                    a0 + 1 + opch + 1, math.ceil(gv.L_out / dmi), znum))

        modelfile.write(');\n')
        modelfile.write('\n')

        modelfile.write('edges \n')
        modelfile.write('(\n')
        modelfile.write(');\n')

        modelfile.write('\n')
        modelfile.write('patches \n')

        modelfile.write('(\n')

        modelfile.write('    patch liquidinlet\n')
        modelfile.write('    (\n')
        if gv.structure == 'tri':
            modelfile.write('        (0 1 %d %d)\n' % (opch + 1, opch))
        if gv.structure == 'rec':
            modelfile.write('        (0 1 %d %d)\n' % (opch + 1, opch))

        modelfile.write('    )\n')

        modelfile.write('    patch liquidoutlet\n')
        modelfile.write('    (\n')
        if gv.structure == 'tri':
            a0 = (2 * gv.wnum + 2) * 3
            modelfile.write('        (%d %d %d %d)\n' % (a0, a0 + 1, a0 + opch + 1, a0 + opch))

        if gv.structure == 'rec':
            a0 = 4 * (2 * gv.wnum - 1) + 4 + 3
            modelfile.write('        (%d %d %d %d)\n' % (a0, a0 + 1, a0 + opch + 1, a0 + opch))

        modelfile.write('    )\n')

        modelfile.write('    wall fixedwall \n')
        modelfile.write('    (\n')
        if gv.structure == 'tri':
            opch = gv.wnum * 6 + 9
            for i in range(0, 2 * gv.wnum + 2):
                a0 = 3 * i
                modelfile.write('        (%d %d %d %d)\n' % (a0, a0 + 3, a0 + 3 + opch, a0 + opch))
                if gv.is3d:
                    modelfile.write('        (%d %d %d %d)\n' % (a0, a0 + 3, a0 + 3 + 1, a0 + 1))
                    modelfile.write('        (%d %d %d %d)\n' % (a0 + 1, a0 + 3 + 1, a0 + 3 + 1 + 1, a0 + 1 + 1))
                    modelfile.write('        (%d %d %d %d)\n' % (a0 + opch, a0 + 3 + opch, a0 + 3 + 1 + opch, a0 + 1 + opch))
                    modelfile.write('        (%d %d %d %d)\n' % (a0 + 1 + opch, a0 + 3 + 1 + opch, a0 + 3 + 1 + 1 + opch, a0 + 1 + 1 + opch))

        if gv.structure == 'rec':
            opch = gv.wnum * 8 + 6
            modelfile.write('        (0 4 %d %d)\n' % (4 + opch, opch))
            if gv.is3d:
                modelfile.write('        (%d %d %d %d)\n' % (0 + opch, 4 + opch, 5 + opch, 1 + opch))
                modelfile.write('        (%d %d %d %d)\n' % (1 + opch, 5 + opch, 6 + opch, 2 + opch))
                modelfile.write('        (0 4 5 1)\n')
                modelfile.write('        (1 5 6 2)\n')

            for i in range(1, 2 * gv.wnum):
                if i % 2 == 1:
                    a0 = 4 * (i - 1) + 3
                    modelfile.write('        (%d %d %d %d)\n' % (a0, a0 + 1, a0 + 1 + opch, a0 + opch))
                    modelfile.write('        (%d %d %d %d)\n' % (a0, a0 + 4, a0 + 4 + opch, a0 + opch))
                    modelfile.write('        (%d %d %d %d)\n' % (a0 + 4, a0 + 4 + 1, a0 + 4 + 1 + opch, a0 + 4 + opch))
                    if gv.is3d:
                        modelfile.write('        (%d %d %d %d)\n' % (a0, a0 + 4, a0 + 4 + 1, a0 + 1))
                        modelfile.write('        (%d %d %d %d)\n' % (a0 + 1, a0 + 4 + 1, a0 + 4 + 1 + 1, a0 + 1 + 1))
                        modelfile.write('        (%d %d %d %d)\n' % (a0 + 2, a0 + 4 + 2, a0 + 4 + 1 + 2, a0 + 1 + 2))
                        modelfile.write('        (%d %d %d %d)\n' % (a0 + opch, a0 + 4 + opch, a0 + 4 + 1 + opch, a0 + 1 + opch))
                        modelfile.write('        (%d %d %d %d)\n' % (a0 + 1 + opch, a0 + 4 + 1 + opch, a0 + 4 + 1 + 1 + opch, a0 + 1 + 1 + opch))
                        modelfile.write('        (%d %d %d %d)\n' % (a0 + 2 + opch, a0 + 4 + 2 + opch, a0 + 4 + 1 + 2 + opch, a0 + 1 + 2 + opch))
                else:
                    a0 = 4 * (i - 1) + 4
                    modelfile.write('        (%d %d %d %d)\n' % (a0, a0 + 4, a0 + 4 + opch, a0 + opch))
                    if gv.is3d:
                        modelfile.write('        (%d %d %d %d)\n' % (a0, a0 + 4, a0 + 4 + 1, a0 + 1))
                        modelfile.write('        (%d %d %d %d)\n' % (a0 + 1, a0 + 4 + 1, a0 + 4 + 1 + 1, a0 + 1 + 1))
                        modelfile.write('        (%d %d %d %d)\n' % (a0 + opch, a0 + 4 + opch, a0 + 4 + 1 + opch, a0 + 1 + opch))
                        modelfile.write('        (%d %d %d %d)\n' % (a0 + 1 + opch, a0 + 4 + 1 + opch, a0 + 4 + 1 + 1 + opch, a0 + 1 + 1 + opch))

            a0 = 4 * (2 * gv.wnum - 1) + 4
            modelfile.write('        (%d %d %d %d)\n' % (a0, a0 + 3, a0 + 3 + opch, a0 + opch))
            if gv.is3d:
                modelfile.write('        (%d %d %d %d)\n' % (a0, a0 + 3, a0 + 3 + 1, a0 + 1))
                modelfile.write('        (%d %d %d %d)\n' % (a0 + 1, a0 + 3 + 1, a0 + 3 + 1 + 1, a0 + 1 + 1))
                modelfile.write('        (%d %d %d %d)\n' % (a0 + opch, a0 + 3 + opch, a0 + 3 + 1 + opch, a0 + 1 + opch))
                modelfile.write('        (%d %d %d %d)\n' % (a0 + 1 + opch, a0 + 3 + 1 + opch, a0 + 3 + 1 + 1 + opch, a0 + 1 + 1 + opch))

        if gv.isUpWall:
            if gv.structure == 'tri':
                opch = gv.wnum * 6 + 9
                for i in range(0, 2 * gv.wnum + 2):
                    a0 = 3 * i + 2
                    modelfile.write('        (%d %d %d %d)\n' % (a0, a0 + 3, a0 + 3 + opch, a0 + opch))

            if gv.structure == 'rec':
                opch = gv.wnum * 8 + 6
                modelfile.write('        (2 6 %d %d)\n' % (6 + opch, 2+opch))

                for i in range(1, 2 * gv.wnum):
                    a0 = 4 * (i - 1) + 4 + 2
                    modelfile.write('        (%d %d %d %d)\n' % (a0, a0 + 4, a0 + 4 + opch, a0 + opch))

                a0 = 4 * (2 * gv.wnum - 1) + 4 + 2
                modelfile.write('        (%d %d %d %d)\n' % (a0, a0 + 3, a0 + 3 + opch, a0 + opch))

        modelfile.write('    )\n')
        if gv.samedirecasflow:
            # same direction as liquid inlet
            modelfile.write('    patch airinlet\n')
        else:
            modelfile.write('    patch airoutlet\n')
        modelfile.write('    (\n')
        if gv.structure == 'tri':
            modelfile.write('        (1 2 %d %d)\n' % (opch + 2, opch+1))
        if gv.structure == 'rec':
            modelfile.write('        (1 2 %d %d)\n' % (opch + 2, opch+1))
        modelfile.write('    )\n')

        if gv.samedirecasflow:
            modelfile.write('    patch airoutlet\n')
        else:
            modelfile.write('    patch airinlet\n')
        modelfile.write('    (\n')

        if gv.structure == 'tri':
            a0 = (2 * gv.wnum + 2) * 3 + 1
            modelfile.write('        (%d %d %d %d)\n' % (a0, a0 + 1, a0 + opch + 1, a0 + opch))

        if gv.structure == 'rec':
            a0 = 4 * (2 * gv.wnum - 1) + 4 + 3 + 1
            modelfile.write('        (%d %d %d %d)\n' % (a0, a0 + 1, a0 + opch + 1, a0 + opch))


        modelfile.write('    )\n')

        modelfile.write('    patch airatmosphere \n')
        modelfile.write('    (\n')
        if not gv.isUpWall:
            if gv.structure == 'tri':
                opch = gv.wnum * 6 + 9
                for i in range(0, 2 * gv.wnum + 2):
                    a0 = 3 * i + 2
                    modelfile.write('        (%d %d %d %d)\n' % (a0, a0 + 3, a0 + 3 + opch, a0 + opch))

            if gv.structure == 'rec':
                opch = gv.wnum * 8 + 6
                modelfile.write('        (2 6 %d %d)\n' % (6 + opch, 2+opch))

                for i in range(1, 2 * gv.wnum):
                    a0 = 4 * (i - 1) + 4 + 2
                    modelfile.write('        (%d %d %d %d)\n' % (a0, a0 + 4, a0 + 4 + opch, a0 + opch))

                a0 = 4 * (2 * gv.wnum - 1) + 4 + 2
                modelfile.write('        (%d %d %d %d)\n' % (a0, a0 + 3, a0 + 3 + opch, a0 + opch))
        modelfile.write('    )\n')

        modelfile.write('    empty frontAndBackPlanes\n')
        modelfile.write('    (\n')
        # modelfile.write('        (0 3 4 1)\n');
        # modelfile.write('        (9 12 13 10)\n');
        # modelfile.write('        (1 4 5 2)\n');
        # modelfile.write('        (10 13 14 11)\n');
        # modelfile.write('        (3 6 7 4)\n');
        # modelfile.write('        (4 7 8 5)\n');
        # modelfile.write('        (12 15 16 13)\n');
        # modelfile.write('        (13 16 17 14)\n');
        modelfile.write('    )\n')

        modelfile.write(');\n')
        modelfile.write('mergePatchPairs\n')
        modelfile.write('(\n')
        modelfile.write(');\n')
        modelfile.write('// ************************************************************************* //\n')
