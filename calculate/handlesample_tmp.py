import os
import sys


def writesample(filename, ypostion):
    di = os.path.join('system', 'sampleDict')
    print("sampling " + di)
    with open(di, 'r') as readmodel:
        lines = readmodel.readlines()

    height = float(filename.split('h')[1])/1000
    # lines[26] = lines[26].replace('-0.00032128', str("%10.8f" % float(ypostion)))  # 第二个参数由alpha0.5处得到

    # 临时处理
    lines[25] = '    start (%10.8f %10.8f 0);\n' % (0.025, -height)  # 提取第二个波波谷
    lines[26] = '    end (%10.8f %10.8f 0);\n' % (0.025, float(ypostion))  # 第二个参数由alpha0.5处得到

    with open(di, 'w') as writemodel:
        writemodel.writelines(lines)


if __name__ == '__main__':
    if len(sys.argv) == 3:
        location = sys.argv[1]
        yposition_interface = sys.argv[2]
        writesample(location, yposition_interface)
