import os
import globalvar as gv

def writecommand():
    with open(os.path.join(gv.basedir,'allrun'),'wb') as cmdfile:
        cmdfile.write('#!/bin/sh\n')
        cmdfile.write('# Source tutorial run functions\n')
        cmdfile.write('. $WM_PROJECT_DIR/bin/tools/RunFunctions\n')
        cmdfile.write('\n')
        cmdfile.write('# Set application name\n')
        cmdfile.write('application="interFoam"\n')
        for lines in gv.files:
            cmdfile.write('\n')
            cmdfile.write('cd %s\n' % lines)
            cmdfile.write('    runApplication blockMesh\n')
            cmdfile.write('    runApplication setFields\n')
            cmdfile.write('    runApplication decomposePar\n')
            cmdfile.write('    runParallel $application 4\n')
            cmdfile.write('    runApplication reconstructPar\n')
            cmdfile.write('    runApplication sample\n')
            # cmdfile.write('    runApplication foamToTecplot360\n')
            cmdfile.write('cd ..\n')
