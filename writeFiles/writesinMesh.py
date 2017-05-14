def writesinmesh(modelLocation):
    pass
#     # x=0:10e-3/256:30e-3;%提取256个点
#     # y=1e-3*cos(2*pi/10e-3.*x)-1e-3;
#     # n=length(x);
#     # z=zeros(n,1);
#     # curve1=[x' y' z];
#     #
#     #
#     # y1=y+det;
#     # curve2=[x' y1' z];
#     #
#     # %define the top
#     # y2=y+det*5;
#     # curve3=[x' y2' z];
#     #
#     # curve1z=[curve1(:,1:2) curve1(:,3)+1e-4];
#     # curve2z=[curve2(:,1:2) curve2(:,3)+1e-4];
#     # curve3z=[curve3(:,1:2) curve3(:,3)+1e-4];
#     # %define the corrugations in the bottom
#     with open(modelLocation, 'w') as modelfile:
#
#
#         modelfile.write('/*--------------------------------*- C++ -*----------------------------------  \n');
#         modelfile.write('| =========                 |                                                 |\n');
#         modelfile.write('| \\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox           |\n');
#         modelfile.write('|  \\    /   O peration     | Version:  1.7.1                                 |\n');
#         modelfile.write('|   \\  /    A nd           | Web:      www.OpenFOAM.com                      |\n');
#         modelfile.write('|    \\/     M anipulation  |                                                 |\n');
#         modelfile.write('  ---------------------------------------------------------------------------*/\n');
#         modelfile.write('FoamFile\n');
#         modelfile.write('{\n');
#         modelfile.write('    version     2.0;\n');
#         modelfile.write('    format      ascii;\n');
#         modelfile.write('    class       dictionary;\n');
#         modelfile.write('    object      blockMeshDict;\n');
#         modelfile.write('}\n');
#         modelfile.write('// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //\n');
#         modelfile.write('\n');
#         modelfile.write('convertToMeters %10.8f;\n',1);
#         modelfile.write('\n');
#         modelfile.write('vertices\n');
#         modelfile.write('(\n');
#         modelfile.write('(%10.8f %10.8f %10.8f)\n',0,0,0);%0
#         modelfile.write('(%10.8f %10.8f %10.8f)\n',0,det,0);%1
#         modelfile.write('(%10.8f %10.8f %10.8f)\n',0,5*det,0);%2
#
#         modelfile.write('(%10.8f %10.8f %10.8f)\n',0.03,0,0);%3
#         modelfile.write('(%10.8f %10.8f %10.8f)\n',0.03,det,0);%4
#         modelfile.write('(%10.8f %10.8f %10.8f)\n',0.03,5*det,0);%5
#
#
#         modelfile.write('(%10.8f %10.8f %10.8f)\n',0,0,0.0001);%6
#         modelfile.write('(%10.8f %10.8f %10.8f)\n',0,det,0.0001);%7
#         modelfile.write('(%10.8f %10.8f %10.8f)\n',0,5*det,0.0001);%8
#
#         modelfile.write('(%10.8f %10.8f %10.8f)\n',0.03,0,0.0001);%9
#         modelfile.write('(%10.8f %10.8f %10.8f)\n',0.03,det,0.0001);%10
#         modelfile.write('(%10.8f %10.8f %10.8f)\n',0.03,5*det,0.0001);%11
#
#
#         modelfile.write(');\n');
#
#         modelfile.write('blocks \n');
#         modelfile.write('(\n');
#
#         modelfile.write('     hex (0 3 4 1 6 9 10 7) (100 20 1) simpleGrading (1 1 1)\n');
#         modelfile.write('     hex (1 4 5 2 7 10 11 8) (100 80 1) simpleGrading (1 1 1)\n');
#
#
#
#         modelfile.write(');\n');
#         modelfile.write('\n');
#
#
#
#         modelfile.write('edges \n');
#         modelfile.write('(\n');
#
#         modelfile.write('spline 0 3\n');%固定边
#         modelfile.write('(\n');
#         for i=1:n
#             modelfile.write( '( %10.8f %10.8f %10.8f) \n',curve1(i,:));
#         end
#         modelfile.write(')\n');
#
#         modelfile.write('spline 1 4\n');%气液边界
#         modelfile.write('(\n');
#         for i=1:n
#             modelfile.write( '( %10.8f %10.8f %10.8f) \n',curve2(i,:));
#         end
#         modelfile.write(')\n');
#         modelfile.write('spline 2 5\n');%气相边界
#         modelfile.write('(\n');
#         for i=1:n
#             modelfile.write( '( %10.8f %10.8f %10.8f) \n',curve3(i,:));
#         end
#         modelfile.write(')\n');
#         modelfile.write('spline 6 9\n');
#         modelfile.write('(\n');
#         for i=1:n
#             modelfile.write( '( %10.8f %10.8f %10.8f) \n',curve1z(i,:));
#         end
#         modelfile.write(')\n');
#         modelfile.write('spline 7 10\n');
#         modelfile.write('(\n');
#         for i=1:n
#             modelfile.write( '( %10.8f %10.8f %10.8f) \n',curve2z(i,:));
#         end
#         modelfile.write(')\n');
#         modelfile.write('spline 8 11\n');
#         modelfile.write('(\n');
#         for i=1:n
#             modelfile.write( '( %10.8f %10.8f %10.8f) \n',curve3z(i,:));
#         end
#         modelfile.write(')\n');
#
#
#         modelfile.write(');\n');
#
#         modelfile.write('\n');
#         modelfile.write('patches \n');
#
#         modelfile.write('(\n');
#
#         modelfile.write('    patch liquidinlet\n');
#         modelfile.write('    (\n');
#         modelfile.write('        (0 1 7 6)\n');
#         modelfile.write('    )\n');
#
#         modelfile.write('    patch liquidoutlet\n');
#         modelfile.write('    (\n');
#         modelfile.write('        (3 4 10 9)\n');
#
#         modelfile.write('    )\n');
#
#         modelfile.write('    wall fixedwall\n');
#         modelfile.write('    (\n');
#         modelfile.write('        (0 3 9 6)\n');
#         modelfile.write('    )\n');
#
#         modelfile.write('    patch airinlet\n');
#         modelfile.write('    (\n');
#         modelfile.write('        (1 2 8 7)\n');
#         modelfile.write('    )\n');
#
#         modelfile.write('    patch airoutlet\n');
#         modelfile.write('    (\n');
#         modelfile.write('        (4 5 11 10)\n');
#
#         modelfile.write('    )\n');
#
#         modelfile.write('    patch airatmosphere\n');
#         modelfile.write('    (\n');
#         modelfile.write('        (2 5 11 8)\n');
#         modelfile.write('    )\n');
#
#         modelfile.write('    empty frontAndBackPlanes\n');
#         modelfile.write('    (\n');
#         modelfile.write('        (0 3 4 1)\n');
#         modelfile.write('        (1 4 5 2)\n');
#
#         modelfile.write('    )\n');
#
#         modelfile.write(');\n');
#         modelfile.write('mergePatchPairs\n');
#         modelfile.write('(\n');
#
#         modelfile.write(');\n');
#         modelfile.write('// ************************************************************************* //\n');
