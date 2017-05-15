import globalvar as gv


def writesample(sampleLocation):
    with open(sampleLocation, 'r') as readmodel:
        lines = readmodel.readlines()
    lines[25] = '    start (%10.8f %10.8f 0);\n' % (gv.L_in + 3 / 2 * gv.L, -gv.A)  # 提取第二个波波谷
    lines[26] = '    end (%10.8f -0.00032128 0);\n' % (gv.L_in + 3 / 2 * gv.L) # 第二个参数由alpha0.5处得到
    with open(sampleLocation, 'w') as writemodel:
        writemodel.writelines(lines)
