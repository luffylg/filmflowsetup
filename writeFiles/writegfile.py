import math
import globalvar as gv


def writegfile(glocation):
    with open(glocation, 'w') as gl:
        gl.write('/*--------------------------------*- C++ -*----------------------------------  \n')
        gl.write('| =========                 |                                                 |\n')
        gl.write('| \\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox           |\n')
        gl.write('|  \\    /   O peration     | Version:  1.7.1                                 |\n')
        gl.write('|   \\  /    A nd           | Web:      www.OpenFOAM.com                      |\n')
        gl.write('|    \\/     M anipulation  |                                                 |\n')
        gl.write('  ---------------------------------------------------------------------------*/\n')
        gl.write('FoamFile\n')
        gl.write('{\n')
        gl.write('version     2.0;\n')
        gl.write('    format      ascii;\n')
        gl.write('    class       uniformDimensionedVectorField;\n')
        gl.write('    location    "constant";\n')
        gl.write('    object      g;\n')
        gl.write('}\n')
        gl.write('// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //\n')
        gl.write('dimensions      [0 1 -2 0 0 0 0];\n')
        gl.write('value           (%10.8f  %10.8f 0);\n' % (
        gv.g * math.sin(math.radians(gv.ang)), -gv.g * math.cos(math.radians(gv.ang))))
        gl.write('// ************************************************************************* //\n')
