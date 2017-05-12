def writeblockmesh(modelLocation, det):
    # with open(modelLocation, 'w') as modelfile:
    #     modelfile.write('/*--------------------------------*- C++ -*----------------------------------  \n')
    #     modelfile.write('| =========                 |                                                 |\n')
    #     modelfile.write('| \\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox           |\n')
    #     modelfile.write('|  \\    /   O peration     | Version:  1.7.1                                 |\n')
    #     modelfile.write('|   \\  /    A nd           | Web:      www.OpenFOAM.com                      |\n')
    #     modelfile.write('|    \\/     M anipulation  |                                                 |\n')
    #     modelfile.write('  ---------------------------------------------------------------------------*/\n')
    #     modelfile.write('FoamFile\n')
    #     modelfile.write('{\n')
    #     modelfile.write('    version     2.0\n')
    #     modelfile.write('    format      ascii\n')
    #     modelfile.write('    class       dictionary\n')
    #     modelfile.write('    object      blockMeshDict\n')
    #     modelfile.write('}\n')
    #     modelfile.write('// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //\n')
    #     modelfile.write('\n')
    #     modelfile.write('convertToMeters %10.8f\n' % 1)
    #     modelfile.write('\n')
    #     modelfile.write('vertices\n')
    #     modelfile.write('(\n')
    #     modelfile.write('(%10.8f %10.8f %10.8f)\n'%(0,0,0)) #0
    #     modelfile.write('(%10.8f %10.8f %10.8f)\n'%(0,det,0)) #1
    #     modelfile.write('(%10.8f %10.8f %10.8f)\n'%(0,4*det,0)) #2
    #
    #     modelfile.write('(%10.8f %10.8f %10.8f)\n'%(0.005,-0.002,0)#3
    #     modelfile.write('(%10.8f %10.8f %10.8f)\n'%(0.005,-0.002+det,0)#4
    #     modelfile.write('(%10.8f %10.8f %10.8f)\n'%(0.005,-0.002+4*det,0)#5
    #
    #     modelfile.write('(%10.8f %10.8f %10.8f)\n',0.01,0,0)%6
    #     modelfile.write('(%10.8f %10.8f %10.8f)\n',0.01,det,0)%7
    #     modelfile.write('(%10.8f %10.8f %10.8f)\n',0.01,4*det,0)%8
    #
    #     modelfile.write('(%10.8f %10.8f %10.8f)\n',0,0,0.0001)%9
    #     modelfile.write('(%10.8f %10.8f %10.8f)\n',0,det,0.0001)%10
    #     modelfile.write('(%10.8f %10.8f %10.8f)\n',0,4*det,0.0001)%11
    #
    #     modelfile.write('(%10.8f %10.8f %10.8f)\n',0.005,-0.002,0.0001)%12
    #     modelfile.write('(%10.8f %10.8f %10.8f)\n',0.005,-0.002+det,0.0001)%13
    #     modelfile.write('(%10.8f %10.8f %10.8f)\n',0.005,-0.002+4*det,0.0001)%14
    #
    #     modelfile.write('(%10.8f %10.8f %10.8f)\n',0.01,0,0.0001)%15
    #     modelfile.write('(%10.8f %10.8f %10.8f)\n',0.01,det,0.0001)%16
    #     modelfile.write('(%10.8f %10.8f %10.8f)\n',0.01,4*det,0.0001)%17
    #
    #     modelfile.write(')\n')
    #
    #     modelfile.write('blocks \n')
    #     modelfile.write('(\n')
    #
    #     modelfile.write('     hex (0 3 4 1 9 12 13 10) (%d 12 1) simpleGrading (1 1 1)\n',round(wnum*L*6/det))
    #     modelfile.write('     hex (1 4 5 2 10 13 14 11) (%d 36 1) simpleGrading (1 1 1)\n',round(wnum*L*6/det))
    #
    #     modelfile.write('     hex (3 6 7 4 12 15 16 13) (%d 12 1) simpleGrading (1 1 1)\n',round(wnum*L*6/det))
    #     modelfile.write('     hex (4 7 8 5 13 16 17 14) (%d 36 1) simpleGrading (1 1 1)\n',round(wnum*L*6/det))
    #
    #     modelfile.write(')\n')
    #     modelfile.write('\n')
    #
    #     modelfile.write('edges \n')
    #     modelfile.write('(\n')
    #     modelfile.write(')\n')
    #
    #     modelfile.write('\n')
    #     modelfile.write('patches \n')
    #
    #     modelfile.write('(\n')
    #
    #     modelfile.write('    patch liquidinlet\n')
    #     modelfile.write('    (\n')
    #     modelfile.write('        (0 1 10 9)\n')
    #     modelfile.write('    )\n')
    #
    #     modelfile.write('    patch liquidoutlet\n')
    #     modelfile.write('    (\n')
    #     modelfile.write('        (6 7 16 15)\n')
    #     modelfile.write('    )\n')
    #
    #     modelfile.write('    wall fixedwall \n')
    #     modelfile.write('    (\n')
    #     modelfile.write('        (0 3 12 9)\n')
    #     modelfile.write('        (3 6 15 12)\n')
    #
    #     modelfile.write('    )\n')
    #
    #     modelfile.write('    patch airinlet\n')
    #     modelfile.write('    (\n')
    #     modelfile.write('        (1 2 11 10)\n')
    #     modelfile.write('    )\n')
    #
    #     modelfile.write('    patch airoutlet\n')
    #     modelfile.write('    (\n')
    #     modelfile.write('        (7 8 17 16)\n')
    #     modelfile.write('    )\n')
    #
    #     modelfile.write('    patch airatmosphere \n')
    #     modelfile.write('    (\n')
    #     modelfile.write('        (2 5 14 11)\n')
    #     modelfile.write('        (5 8 17 14)\n')
    #     modelfile.write('    )\n')
    #
    #     modelfile.write('    empty frontAndBackPlanes\n')
    #     modelfile.write('    (\n')
    #     modelfile.write('        (0 3 4 1)\n')
    #     modelfile.write('        (9 12 13 10)\n')
    #     modelfile.write('        (1 4 5 2)\n')
    #     modelfile.write('        (10 13 14 11)\n')
    #     modelfile.write('        (3 6 7 4)\n')
    #     modelfile.write('        (4 7 8 5)\n')
    #     modelfile.write('        (12 15 16 13)\n')
    #     modelfile.write('        (13 16 17 14)\n')
    #     modelfile.write('    )\n')
    #
    #     modelfile.write(')\n')
    #     modelfile.write('mergePatchPairs\n')
    #     modelfile.write('(\n')
    #     modelfile.write(')\n')
    #     modelfile.write('// ************************************************************************* //\n')
    pass