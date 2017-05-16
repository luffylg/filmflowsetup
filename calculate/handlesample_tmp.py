import os
import sys


def getyposition(xposition):
    path = os.path.join('postProcessing', 'surfaces', '0.5', 'alpha.water_constantIso.raw')
    newnamepath = os.path.join('postProcessing', 'surfaces', '0.5', 'alpha.water_constantIso')
    if os.path.exists(path):
        os.rename(path, newnamepath)
    with open(newnamepath, 'r') as water_constant:
        lines = water_constant.readlines()
    lines = lines[2:-1]
    xpos = 10000
    ypos = 10000
    for line in lines:
        hang = line.split(" ")
        x = float(hang[0])
        y = float(hang[1])
        if abs(x - xposition) < xpos:
            xpos = abs(x - xposition)
            xfinal = x
            ypos = y
    with open(newnamepath, 'w') as water_constant2:
        print("x:%10.8f y:%10.8f" % (xfinal, ypos))
        water_constant2.writelines(lines)
    return ypos


def writesample(filename, xpos):
    di = os.path.join('system', 'sampleDict')
    print("sampling " + filename)
    with open(di, 'r') as readmodel:
        lines = readmodel.readlines()

    height = float(filename.split('h')[1]) / 1000
    # lines[26] = lines[26].replace('-0.00032128', str("%10.8f" % float(yposition)))  # 第二个参数由alpha0.5处得到

    # 临时处理
    lines[25] = '    start (%10.8f %10.8f 0);\n' % (0.025, -height)  # 提取第二个波波谷
    yposition = getyposition(xpos)
    lines[26] = '    end (%10.8f %10.8f 0);\n' % (0.025, float(yposition))  # 第二个参数由alpha0.5处得到

    with open(di, 'w') as writemodel:
        writemodel.writelines(lines)


if __name__ == '__main__':
    if len(sys.argv) == 3:
        location = sys.argv[1]
        writesample(location, float(sys.argv[2]))
