import math
import globalvar as gv


def writeudocument(ulocation):
    # define the 'U' document
    uave = gv.det * gv.det * gv.g * math.sin(math.radians(gv.ang)) / gv.v / 3
    umax = uave * 1.5
    aa = 1 / gv.det
    ab = gv.g * math.sin(math.radians(gv.ang)) * gv.det * gv.det / gv.v

    # begin to write the txt into the document
    with open(ulocation, 'w') as ufile:
        ufile.write('/*--------------------------------*- C++ -*----------------------------------  \n')
        ufile.write('| =========                 |                                                 |\n')
        ufile.write('| \\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox           |\n')
        ufile.write('|  \\    /   O peration     | Version:  1.7.1                                 |\n')
        ufile.write('|   \\  /    A nd           | Web:      www.OpenFOAM.com                      |\n')
        ufile.write('|    \\/     M anipulation  |                                                 |\n')
        ufile.write('  ---------------------------------------------------------------------------*/\n')
        ufile.write('FoamFile\n')
        ufile.write('{\n')
        ufile.write('    version     2.0;\n')
        ufile.write('    format      ascii;\n')
        ufile.write('    class       volVectorField;\n')
        ufile.write('    location    "0";\n')
        ufile.write('    object      U;\n')
        ufile.write('}\n')
        ufile.write('// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //\n')
        ufile.write('\n')
        ufile.write('dimensions      [0 1 -1 0 0 0 0];\n')
        ufile.write('\n')
        ufile.write('internalField   uniform (%10.6f 0 0);\n' % uave)
        ufile.write('\n')
        ufile.write('boundaryField\n')
        ufile.write('{\n')
        ufile.write('    liquidinlet\n')
        ufile.write('    {\n')
        ufile.write('        type            groovyBC;\n')
        ufile.write('        variables "dy=(pos().y)*%10.6f;vx=%8.6f*(dy-0.5*pow(dy,2));";\n' % (aa, ab))
        ufile.write('        valueExpression "vector(vx,0,0)";\n')
        ufile.write('        value           uniform (0 0 0);\n')
        ufile.write('    }\n')
        ufile.write('    liquidoutlet\n')
        ufile.write('    {\n')
        ufile.write('        type            groovyBC;\n')
        ufile.write('        variables "dy=(pos().y)*%10.6f;vx=%8.6f*(dy-0.5*pow(dy,2));";\n' % (aa, ab))
        ufile.write('        valueExpression "vector(vx,0,0)";\n')
        ufile.write('        value           uniform (0 0 0);\n')
        ufile.write('    }\n')
        ufile.write('    fixedwall\n')
        ufile.write('    {\n')
        ufile.write('        type            fixedValue;\n')
        ufile.write('        value           uniform (0 0 0);\n')
        ufile.write('    }\n')
        ufile.write('    airatmosphere\n')
        ufile.write('    {\n')
        ufile.write('        type            pressureInletOutletVelocity;\n')
        ufile.write('        value           uniform (0 0 0);\n')
        ufile.write('    }\n')
        ufile.write('    airinlet\n')
        ufile.write('    {\n')
        if gv.air_speed == 0:
             ufile.write('        type            zeroGradient;\n')
        else:
            ufile.write('        type            fixedValue;\n')
            if gv.samedirecasflow:
                ufile.write('        value           uniform (%10.8f 0 0);\n' % gv.air_speed)
            else:
                ufile.write('        value           uniform (%10.8f 0 0);\n' % -gv.air_speed)
        ufile.write('    }\n')
        ufile.write('    airoutlet\n')
        ufile.write('    {\n')
        if gv.air_speed == 0:
            ufile.write('        type            fixedValue;\n')
            ufile.write('        value           uniform (%10.8f 0 0);\n' % umax)
        else:
            ufile.write('        type            pressureInletOutletVelocity;\n')
            ufile.write('        value           uniform (0 0 0);\n')
        ufile.write('    }\n')
        ufile.write('    frontAndBackPlanes\n')
        ufile.write('    {\n')
        ufile.write('        type            empty;\n')
        ufile.write('    }\n')
        ufile.write('}\n')
        ufile.write('\n')
        ufile.write('// ************************************************************************* //\n')
