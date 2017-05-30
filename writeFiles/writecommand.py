import os
import re

import globalvar as gv


def writecommand():
    with open(os.path.join(gv.basedir, 'allrun'), 'wb') as cmdfile:
        cmdfile.write('#!/bin/sh\n'.encode())
        cmdfile.write('# Source tutorial run functions\n'.encode())
        cmdfile.write('. $WM_PROJECT_DIR/bin/tools/RunFunctions\n'.encode())
        cmdfile.write('\n'.encode())
        cmdfile.write('# Set application name\n'.encode())
        cmdfile.write('application="interFoam"\n'.encode())
        for line in gv.files:
            lines = line[0]
            cmdfile.write('\n'.encode())
            cmdfile.write(('cd %s\n' % lines).encode())
            cmdfile.write(('    echo "%s handling"\n' % lines).encode())
            cmdfile.write('    runApplication blockMesh\n'.encode())
            cmdfile.write('    runApplication setFields\n'.encode())
            cmdfile.write('    runApplication interFoam\n'.encode())
            cmdfile.write('    runApplication sample\n'.encode())
            cmdfile.write(
                ('    python3 ../../../handlesample.py %s %s\n' % (lines, gv.L_in + 3 / 2 * gv.L)).encode())

            # cmdfile.write(
            #     ('    python3 ../../../handlesample_tmp.py %s %s\n' % (lines,gv.L_in + 3 / 2 * gv.L)).encode())
            cmdfile.write('    rm log.sample\n'.encode())
            cmdfile.write('    runApplication sample\n'.encode())
            cmdfile.write('cd ..\n'.encode())
        for line in gv.files:
            lines = line[0]
            cmdfile.write('\n'.encode())
            cmdfile.write(('cd %s\n' % lines).encode())
            gv.Re = line[1]
            gv.A = line[2]
            gv.wnum = line[3]
            gv.v = line[4]
            gv.ang=line[5]
            cmdfile.write(('    python3 ../../../dataprocess.py %s %s %s %s %s %s %s %s %s\n' % (
            'fuzhi', gv.Re, gv.ang, gv.A, gv.L, gv.wnum, gv.structure, gv.L_in, gv.v)).encode())
            cmdfile.write(('    python3 ../../../dataprocess.py %s %s %s %s %s %s %s %s %s\n' % (
            'yspeed', gv.Re, gv.ang, gv.A, gv.L, gv.wnum, gv.structure, gv.L_in, gv.v)).encode())
            cmdfile.write(('    python3 ../../../dataprocess.py %s %s %s %s %s %s %s %s %s\n' % (
            'yspeedabs', gv.Re, gv.ang, gv.A, gv.L, gv.wnum, gv.structure, gv.L_in, gv.v)).encode())
            cmdfile.write(('    python3 ../../../dataprocess.py %s %s %s %s %s %s %s %s %s\n' % (
            'yintensity_surface', gv.Re, gv.ang, gv.A, gv.L, gv.wnum, gv.structure, gv.L_in, gv.v)).encode())
            cmdfile.write(('    python3 ../../../dataprocess.py %s %s %s %s %s %s %s %s %s\n' % (
            'yintensity_bogu', gv.Re, gv.ang, gv.A, gv.L, gv.wnum, gv.structure, gv.L_in, gv.v)).encode())

            cmdfile.write('cd ..\n'.encode())
