import os
import globalvar as gv

def writecommand():
    with open(os.path.join(gv.basedir,'allrun'),'wb') as cmdfile:
        cmdfile.write('#!/bin/sh\n'.encode())
        cmdfile.write('# Source tutorial run functions\n'.encode())
        cmdfile.write('. $WM_PROJECT_DIR/bin/tools/RunFunctions\n'.encode())
        cmdfile.write('\n'.encode())
        cmdfile.write('# Set application name\n'.encode())
        cmdfile.write('application="interFoam"\n'.encode())
        for lines in gv.files:
            cmdfile.write('\n'.encode())
            cmdfile.write(('cd %s\n' % lines).encode())
            cmdfile.write('    runApplication blockMesh\n'.encode())
            cmdfile.write('    runApplication setFields\n'.encode())
            cmdfile.write('    runApplication interFoam\n'.encode())
            # cmdfile.write('    runApplication decomposePar\n'.encode())
            # cmdfile.write('    runParallel $application 4\n'.encode())
            # cmdfile.write('    runApplication reconstructPar\n'.encode())
            cmdfile.write('    runApplication sample\n'.encode())
            # cmdfile.write('    runApplication foamToTecplot360\n'.encode())
            cmdfile.write('cd ..\n'.encode())
    # with open(os.path.join(gv.basedir,'allrun'),'rb') as cmdfile:
    #     bys=cmdfile.readlines()
    # with open(os.path.join(gv.basedir,'allrun'),'wb') as wfile:
    #     wfile.write(bys)


