import globalvar as gv


def writesample(sampleLocation):
    with open(sampleLocation, 'r') as readmodel:
        lines = readmodel.readlines()
    lines[25] = '    start (%10.8f %10.8f 0);\n' % (gv.L_in + 3 / 2 * gv.L, -gv.A)  # 提取第二个波波谷
    lines[26] = '    end (%10.8f -0.00032128 0);\n' % (gv.L_in + 3 / 2 * gv.L) # 第二个参数由alpha0.5处得到
    lines.insert(21,'    bottom\n')
    lines.insert(22,'  {\n')
    lines.insert(23,'    type uniform;\n')
    lines.insert(24,'    axis xyz;\n')
    lines.insert(25,'    start (%10.8f %10.8f 0);\n' % (gv.L_in + 5 / 4 * gv.L, -gv.A) ) # 提取第二个波波谷
    lines.insert(26,'    end (%10.8f 0 0);\n' % (gv.L_in + 7 / 4 * gv.L) )# 第二个参数由alpha0.5处得到
    lines.insert(27,'    nPoints 10000;\n')
    lines.insert(28,'  }\n')
    with open(sampleLocation, 'w') as writemodel:
        writemodel.writelines(lines)
