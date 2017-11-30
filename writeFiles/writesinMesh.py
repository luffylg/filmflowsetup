import math

import globalvar as gv


def writesinmesh(modelLocation):
    def frange(start, stop, step=1.0):
        while start < stop:
            yield start
            start += step

    points = []
    for x in frange(gv.L_in, gv.L_in + gv.L * gv.wnum, gv.L / 256):
        if gv.structure == 'sin':
            y = gv.A * math.cos(2 * math.pi / gv.L * (x - gv.L_in))/2 - gv.A/2
        else:
            y = 0
        points.append([x, y])

    # %define the corrugations in the bottom
    with open(modelLocation, 'w') as modelfile:
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
        modelfile.write('(%10.8f %10.8f %10.8f)\n' % (gv.L_in, 0, 0))  # 0
        modelfile.write('(%10.8f %10.8f %10.8f)\n' % (gv.L_in, gv.det, 0))  # 1
        modelfile.write('(%10.8f %10.8f %10.8f)\n' % (gv.L_in, 4 * gv.det, 0))  # 2

        modelfile.write('(%10.8f %10.8f %10.8f)\n' % (gv.L_in + gv.wnum * gv.L, 0, 0))  # 3
        modelfile.write('(%10.8f %10.8f %10.8f)\n' % (gv.L_in + gv.wnum * gv.L, gv.det, 0))  # 4
        modelfile.write('(%10.8f %10.8f %10.8f)\n' % (gv.L_in + gv.wnum * gv.L, 4 * gv.det, 0))  # 5

        modelfile.write('(%10.8f %10.8f %10.8f)\n' % (gv.L_in, 0, 0.0001))  # 6
        modelfile.write('(%10.8f %10.8f %10.8f)\n' % (gv.L_in, gv.det, 0.0001))  # 7
        modelfile.write('(%10.8f %10.8f %10.8f)\n' % (gv.L_in, 4 * gv.det, 0.0001))  # 8

        modelfile.write('(%10.8f %10.8f %10.8f)\n' % (gv.L_in + gv.wnum * gv.L, 0, 0.0001))  # 9
        modelfile.write('(%10.8f %10.8f %10.8f)\n' % (gv.L_in + gv.wnum * gv.L, gv.det, 0.0001))  # 10
        modelfile.write('(%10.8f %10.8f %10.8f)\n' % (gv.L_in + gv.wnum * gv.L, 4 * gv.det, 0.0001))  # 11

        modelfile.write('(%10.8f %10.8f %10.8f)\n' % (0, 0, 0))  # 12
        modelfile.write('(%10.8f %10.8f %10.8f)\n' % (0, gv.det, 0))  # 13
        modelfile.write('(%10.8f %10.8f %10.8f)\n' % (0, 4 * gv.det, 0))  # 14

        modelfile.write('(%10.8f %10.8f %10.8f)\n' % (0, 0, 0.0001))  # 15
        modelfile.write('(%10.8f %10.8f %10.8f)\n' % (0, gv.det, 0.0001))  # 16
        modelfile.write('(%10.8f %10.8f %10.8f)\n' % (0, 4 * gv.det, 0.0001))  # 17

        modelfile.write('(%10.8f %10.8f %10.8f)\n' % (gv.L_in + gv.L_out + gv.wnum * gv.L, 0, 0))  # 18
        modelfile.write('(%10.8f %10.8f %10.8f)\n' % (gv.L_in + gv.L_out + gv.wnum * gv.L, gv.det, 0))  # 19
        modelfile.write('(%10.8f %10.8f %10.8f)\n' % (gv.L_in + gv.L_out + gv.wnum * gv.L, 4 * gv.det, 0))  # 20

        modelfile.write('(%10.8f %10.8f %10.8f)\n' % (gv.L_in + gv.L_out + gv.wnum * gv.L, 0, 0.0001))  # 21
        modelfile.write('(%10.8f %10.8f %10.8f)\n' % (gv.L_in + gv.L_out + gv.wnum * gv.L, gv.det, 0.0001))  # 22
        modelfile.write('(%10.8f %10.8f %10.8f)\n' % (gv.L_in + gv.L_out + gv.wnum * gv.L, 4 * gv.det, 0.0001))  # 23

        modelfile.write(');\n')

        modelfile.write('blocks \n')
        modelfile.write('(\n')

        dmi = gv.det / 12
        CELLS = math.ceil(gv.L * gv.wnum / dmi)

        modelfile.write('     hex (0 3 4 1 6 9 10 7) (%d 12 1) simpleGrading (1 1 1)\n' % CELLS)
        modelfile.write('     hex (1 4 5 2 7 10 11 8) (%d 36 1) simpleGrading (1 1 1)\n' % CELLS)

        CELLS = math.ceil(gv.L_in / dmi / 2)

        modelfile.write('     hex (12 0 1 13 15 6 7 16) (%d 12 1) simpleGrading (1 1 1)\n' % CELLS)
        modelfile.write('     hex (13 1 2 14 16 7 8 17) (%d 36 1) simpleGrading (1 1 1)\n' % CELLS)

        CELLS = math.ceil(gv.L_out / dmi / 2)

        modelfile.write('     hex (3 18 19 4 9 21 22 10) (%d 12 1) simpleGrading (1 1 1)\n' % CELLS)
        modelfile.write('     hex (4 19 20 5 10 22 23 11) (%d 36 1) simpleGrading (1 1 1)\n' % CELLS)

        modelfile.write(');\n')
        modelfile.write('\n')

        modelfile.write('edges \n')
        modelfile.write('(\n')

        modelfile.write('spline 0 3\n')  # 固定边
        modelfile.write('(\n')
        for point in points:
            modelfile.write('( %10.8f %10.8f %10.8f) \n' % (point[0], point[1], 0))
        modelfile.write(')\n')

        modelfile.write('spline 1 4\n')  # 气液边界
        modelfile.write('(\n')
        for point in points:
            modelfile.write('( %10.8f %10.8f %10.8f) \n' % (point[0], gv.det, 0))
        modelfile.write(')\n')

        modelfile.write('spline 2 5\n')  # 气相边界
        modelfile.write('(\n')
        for point in points:
            modelfile.write('( %10.8f %10.8f %10.8f) \n' % (point[0], 4 * gv.det, 0))
        modelfile.write(')\n')

        modelfile.write('spline 6 9\n')
        modelfile.write('(\n')
        for point in points:
            modelfile.write('( %10.8f %10.8f %10.8f) \n' % (point[0], point[1], 0.0001))
        modelfile.write(')\n')

        modelfile.write('spline 7 10\n')
        modelfile.write('(\n')
        for point in points:
            modelfile.write('( %10.8f %10.8f %10.8f) \n' % (point[0], gv.det, 0.0001))
        modelfile.write(')\n')

        modelfile.write('spline 8 11\n')
        modelfile.write('(\n')
        for point in points:
            modelfile.write('( %10.8f %10.8f %10.8f) \n' % (point[0], 4 * gv.det, 0.0001))
        modelfile.write(')\n')

        modelfile.write(');\n')

        modelfile.write('\n')
        modelfile.write('patches \n')

        modelfile.write('(\n')

        modelfile.write('    patch liquidinlet\n')
        modelfile.write('    (\n')
        modelfile.write('        (12 13 16 15)\n')
        modelfile.write('    )\n')

        modelfile.write('    patch liquidoutlet\n')
        modelfile.write('    (\n')
        modelfile.write('        (18 19 22 21)\n')

        modelfile.write('    )\n')

        modelfile.write('    wall fixedwall\n')
        modelfile.write('    (\n')
        modelfile.write('        (0 3 9 6)\n')
        modelfile.write('        (0 12 15 6)\n')
        modelfile.write('        (18 3 9 21)\n')
        modelfile.write('    )\n')
        modelfile.write('    patch airinlet\n')
        modelfile.write('    (\n')
        if gv.samedirecasflow:
            modelfile.write('        (13 14 17 16)\n')
        else:
            modelfile.write('        (19 20 23 22)\n')
        modelfile.write('    )\n')

        modelfile.write('    patch airoutlet\n')
        modelfile.write('    (\n')
        if gv.samedirecasflow:
            modelfile.write('        (19 20 23 22)\n')
        else:
            modelfile.write('        (13 14 17 16)\n')
        modelfile.write('    )\n')

        modelfile.write('    patch airatmosphere\n')
        modelfile.write('    (\n')
        modelfile.write('        (2 5 11 8)\n')
        modelfile.write('        (2 14 17 8)\n')
        modelfile.write('        (20 5 11 23)\n')
        modelfile.write('    )\n')

        modelfile.write('    empty frontAndBackPlanes\n')
        modelfile.write('    (\n')
        modelfile.write('        (0 3 4 1)\n')
        modelfile.write('        (1 4 5 2)\n')
        modelfile.write('        (0 12 13 1)\n')
        modelfile.write('        (18 3 4 19)\n')
        modelfile.write('        (1 13 14 2)\n')
        modelfile.write('        (19 4 5 20)\n')

        modelfile.write('    )\n')

        modelfile.write(');\n')
        modelfile.write('mergePatchPairs\n')
        modelfile.write('(\n')

        modelfile.write(');\n')
        modelfile.write('// ************************************************************************* //\n')
