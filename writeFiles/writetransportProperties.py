import globalvar as gv

def writetransportProperties(transportPropertiesLocation):
    with open(transportPropertiesLocation, 'w') as tl:
        tl.write('/*--------------------------------*- C++ -*----------------------------------  \n')
        tl.write('| =========                 |                                                 |\n')
        tl.write('| \\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox           |\n')
        tl.write('|  \\    /   O peration     | Version:  2.4.0                                 |\n')
        tl.write('|   \\  /    A nd           | Web:      www.OpenFOAM.org                      |\n')
        tl.write('|    \\/     M anipulation  |                                                 |\n')
        tl.write('  ---------------------------------------------------------------------------*/\n')
        tl.write('FoamFile\n')
        tl.write('{\n')
        tl.write('    version     2.0;\n')
        tl.write('    format      ascii;\n')
        tl.write('    class       dictionary;\n')
        tl.write('    location    "constant";\n')
        tl.write('    object      transportProperties;\n')
        tl.write('}\n')
        tl.write('// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //\n')
        tl.write('\n')
        tl.write('phases (water air);\n')
        tl.write('water\n')
        tl.write('{\n')
        tl.write('    transportModel  Newtonian;\n')
        tl.write('    nu              nu [ 0 2 -1 0 0 0 0 ] %10.8f;\n' % gv.v)
        tl.write('    rho             rho [ 1 -3 0 0 0 0 0 ] %10.8f;\n' % gv.density)
        tl.write('    CrossPowerLawCoeffs\n')
        tl.write('    {\n')
        tl.write('        nu0             nu0 [ 0 2 -1 0 0 0 0 ] 1e-06;\n')
        tl.write('        nuInf           nuInf [ 0 2 -1 0 0 0 0 ] 1e-06;\n')
        tl.write('        m               m [ 0 0 1 0 0 0 0 ] 1;\n')
        tl.write('        n               n [ 0 0 0 0 0 0 0 ] 0;\n')
        tl.write('    }\n')
        tl.write('\n')
        tl.write('    BirdCarreauCoeffs\n')
        tl.write('    {\n')
        tl.write('        nu0             nu0 [ 0 2 -1 0 0 0 0 ] 0.0142515;\n')
        tl.write('        nuInf           nuInf [ 0 2 -1 0 0 0 0 ] 1e-06;\n')
        tl.write('        k               k [ 0 0 1 0 0 0 0 ] 99.6;\n')
        tl.write('        n               n [ 0 0 0 0 0 0 0 ] 0.1003;\n')
        tl.write('    }\n')
        tl.write('}\n')
        tl.write('\n')
        tl.write('air\n')
        tl.write('{\n')
        tl.write('    transportModel  Newtonian;\n')
        tl.write('    nu              nu [ 0 2 -1 0 0 0 0 ] 1.46e-5;\n')
        tl.write('    rho             rho [ 1 -3 0 0 0 0 0 ] 1.225;\n')
        tl.write('    CrossPowerLawCoeffs\n')
        tl.write('    {\n')
        tl.write('        nu0             nu0 [ 0 2 -1 0 0 0 0 ] 1e-06;\n')
        tl.write('        nuInf           nuInf [ 0 2 -1 0 0 0 0 ] 1e-06;\n')
        tl.write('        m               m [ 0 0 1 0 0 0 0 ] 1;\n')
        tl.write('        n               n [ 0 0 0 0 0 0 0 ] 0;\n')
        tl.write('    }\n')
        tl.write('\n')
        tl.write('    BirdCarreauCoeffs\n')
        tl.write('    {\n')
        tl.write('        nu0             nu0 [ 0 2 -1 0 0 0 0 ] 0.0142515;\n')
        tl.write('        nuInf           nuInf [ 0 2 -1 0 0 0 0 ] 1e-06;\n')
        tl.write('        k               k [ 0 0 1 0 0 0 0 ] 99.6;\n')
        tl.write('        n               n [ 0 0 0 0 0 0 0 ] 0.1003;\n')
        tl.write('    }\n')
        tl.write('}\n')
        tl.write('\n')
        tl.write('sigma           sigma [ 1 0 -2 0 0 0 0 ] %10.8f;\n' % gv.sigma)
        tl.write('\n')
        tl.write('\n')
        tl.write('// ************************************************************************* //\n')
