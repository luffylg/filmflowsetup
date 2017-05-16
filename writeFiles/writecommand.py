import os
import globalvar as gv


def writecommand():
    with open(os.path.join(gv.basedir, 'allrun'), 'wb') as cmdfile:
        cmdfile.write('#!/bin/sh\n'.encode())
        cmdfile.write('# Source tutorial run functions\n'.encode())
        cmdfile.write('. $WM_PROJECT_DIR/bin/tools/RunFunctions\n'.encode())
        cmdfile.write('\n'.encode())
        cmdfile.write('# Set application name\n'.encode())
        cmdfile.write('application="interFoam"\n'.encode())
        for lines in gv.files:
            cmdfile.write('\n'.encode())
            cmdfile.write(('cd %s\n' % lines).encode())
            cmdfile.write(('    echo "%s handling"\n' % lines).encode())
            # cmdfile.write('    runApplication blockMesh\n'.encode())
            # cmdfile.write('    runApplication setFields\n'.encode())
            # cmdfile.write('    runApplication interFoam\n'.encode())
            # cmdfile.write('    runApplication sample\n'.encode())
            # cmdfile.write(('    python3 ../../../handlesample.py %s %s %s\n' % (lines,ypositon,gv.realfiledir)).encode())
            cmdfile.write(
                ('    python3 ../../../handlesample_tmp.py %s %s\n' % (lines,gv.L_in + 3 / 2 * gv.L)).encode())
            cmdfile.write('    runApplication sample\n'.encode())
            cmdfile.write('cd ..\n'.encode())
