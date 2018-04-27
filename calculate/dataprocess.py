import csv
import os
import sys

import math


def yintensity_bogu(re, ang, A, L, wnum, structure, L_in, niandu, density, sigma):
    path = os.path.join('postProcessing', 'sets', '0.5', 'velocity_U.xy')
    newnamepath = os.path.join('postProcessing', 'sets', '0.5', 'velocity_U')
    if os.path.exists(path) and not os.path.exists(newnamepath):
        os.rename(path, newnamepath)
    if not os.path.exists('../../../yintensity_bogu.csv'):
        with open('../../../yintensity_bogu.csv', 'w', newline='') as yintensity_bogu:
            csv_writer = csv.writer(yintensity_bogu, dialect='excel')
            csv_writer.writerow(
                ['re', 'ang', 'A', 'L', 'wnum', 'structure', 'yintensity_bogu', ' niandu', 'density', 'sigma'])

    with open('../../../yintensity_bogu.csv', 'a', newline='') as yintensity_bogu:
        csv_writer = csv.writer(yintensity_bogu, dialect='excel')
        with open(newnamepath, 'r') as water_constant:
            lines = water_constant.readlines()
        count = 0
        sumt = 0
        for line in lines:
            hang = line.split(" ")
            yintensity_bogu = abs(float(hang[2]))
            sumt += yintensity_bogu
            count += 1
        ys = sumt / count
        csv_writer.writerow([re, ang, A, L, wnum, structure, ys, niandu, density, sigma])


def yintensity_surface(re, ang, A, L, wnum, structure, L_in, niandu, density, sigma):
    path = os.path.join('postProcessing', 'surfaces', '0.5', 'U_constantIso.raw')
    newnamepath = os.path.join('postProcessing', 'surfaces', '0.5', 'U_constantIso')
    if os.path.exists(path) and not os.path.exists(newnamepath):
        os.rename(path, newnamepath)
    if not os.path.exists('../../../yintensity_surface.csv'):
        with open('../../../yintensity_surface.csv', 'w', newline='') as yintensity_surface:
            csv_writer = csv.writer(yintensity_surface, dialect='excel')
            csv_writer.writerow(
                ['re', 'ang', 'A', 'L', 'wnum', 'structure', 'yintensity_surface', 'niandu', 'density', 'sigma'])
    with open('../../../yintensity_surface.csv', 'a', newline='') as yintensity_surface:
        csv_writer = csv.writer(yintensity_surface, dialect='excel')
        newnamepath = os.path.join('postProcessing', 'surfaces', '0.5', 'U_constantIso')
        with open(newnamepath, 'r') as water_constant:
            lines = water_constant.readlines()
        lines = lines[2:-1]
        count = 0
        sumt = 0
        for line in lines:
            hang = line.split(" ")
            x = float(hang[0])
            yintensity_surface = abs(float(hang[4]))
            if float(L_in) + float(L) <= x <= float(L_in) + 2 * float(L):
                sumt += yintensity_surface
                count += 1
        ys = sumt / count
        csv_writer.writerow([re, ang, A, L, wnum, structure, ys, niandu, density, sigma])


def yspeed(re, ang, A, L, wnum, structure, L_in, niandu, density, sigma):
    path = os.path.join('postProcessing', 'surfaces', '0.5', 'U_constantIso.raw')
    newnamepath = os.path.join('postProcessing', 'surfaces', '0.5', 'U_constantIso')
    if os.path.exists(path) and not os.path.exists(newnamepath):
        os.rename(path, newnamepath)
    if not os.path.exists('../../../yspeed.csv'):
        with open('../../../yspeed.csv', 'w', newline='') as yspeed:
            csv_writer = csv.writer(yspeed, dialect='excel')
            csv_writer.writerow(['re', 'ang', 'A', 'L', 'wnum', 'structure', 'yspeed', 'niandu', 'density', 'sigma'])
    with open('../../../yspeed.csv', 'a', newline='') as yspeed:
        csv_writer = csv.writer(yspeed, dialect='excel')
        newnamepath = os.path.join('postProcessing', 'surfaces', '0.5', 'U_constantIso')
        with open(newnamepath, 'r') as water_constant:
            lines = water_constant.readlines()
        lines = lines[2:-1]
        count = 0
        sumt = 0
        for line in lines:
            hang = line.split(" ")
            x = float(hang[0])
            yspeed = float(hang[4])
            if abs(float(L_in) + float(L) / 2 - x) / x <= 0.003:
                sumt += yspeed
                count += 1
        ys = sumt / count
        csv_writer.writerow([re, ang, A, L, wnum, structure, ys, niandu, density, sigma])


def eddyposition(re, ang, A, L, wnum, structure, L_in, niandu, density, sigma):
    if not os.path.exists('../../../eddyposition.csv'):
        with open('../../../eddyposition.csv', 'w', newline='') as eddyposition:
            csv_writer = csv.writer(eddyposition, dialect='excel')
            csv_writer.writerow(
                ['re', 'ang', 'A', 'L', 'wnum', 'structure', 'eddyposition', 'niandu', 'density', 'sigma'])
    with open('../../../eddyposition.csv', 'a', newline='') as eddyposition:
        csv_writer = csv.writer(eddyposition, dialect='excel')
        newnamepath = os.path.join('postProcessing', 'sets', '0.5', 'bottom_U.xy')
        with open(newnamepath, 'r') as water_constant:
            lines = water_constant.readlines()
        xs = 100
        for line in lines:
            hang = line.split(" ")
            x = float(hang[0])
            y = float(hang[1])
            xspeed = float(hang[3])
            yspeed = float(hang[4])
            if abs(xspeed) < abs(xs) and xspeed != 0 and yspeed < 0:
                xs, xp = xspeed, x

        print('eddy position: ' + str(xp))
        csv_writer.writerow([re, ang, A, L, wnum, structure, xp, niandu, density, sigma])


def simple_eddyp(A=0.001, L=0.01, L_in=0.01):
    import os, subprocess
    dirs = os.listdir()
    for dir in dirs:
        if os.path.isdir(dir):
            os.chdir(dir)
            sampleLocation = os.path.join('system', 'sampleDict')
            with open(sampleLocation, 'r') as readmodel:
                lines = readmodel.readlines()
            lines.insert(21, '    bottom\n')
            lines.insert(22, '  {\n')
            lines.insert(23, '    type uniform;\n')
            lines.insert(24, '    axis xyz;\n')
            lines.insert(25, '    start (%10.8f %10.8f 0);\n' % (L_in + 5 / 4 * L, -A))  # 提取第二个波波谷
            lines.insert(26, '    end (%10.8f 0 0);\n' % (L_in + 7 / 4 * L))  # 第二个参数由alpha0.5处得到
            lines.insert(27, '    nPoints 10000;\n')
            lines.insert(28, '  }\n')
            with open(sampleLocation, 'w') as writemodel:
                writemodel.writelines(lines)
            subprocess.call(['rm', 'log.sample'])
            subprocess.call(['sample'])
            eddyposition(dir, 1, A, L, 1, 1, L_in, 1, 1, 1)
            os.chdir(os.path.pardir)


def yspeed_abs(re, ang, A, L, wnum, structure, L_in, niandu, density, sigma):
    path = os.path.join('postProcessing', 'surfaces', '0.5', 'U_constantIso.raw')
    newnamepath = os.path.join('postProcessing', 'surfaces', '0.5', 'U_constantIso')
    if os.path.exists(path) and not os.path.exists(newnamepath):
        os.rename(path, newnamepath)
    if not os.path.exists('../../../yspeed_abs.csv'):
        with open('../../../yspeed_abs.csv', 'w', newline='') as yspeed_abs:
            csv_writer = csv.writer(yspeed_abs, dialect='excel')
            csv_writer.writerow(
                ['re', 'ang', 'A', 'L', 'wnum', 'structure', 'yspeed_abs', 'niandu', 'density', 'sigma'])
    with open('../../../yspeed_abs.csv', 'a', newline='') as yspeed_abs:
        csv_writer = csv.writer(yspeed_abs, dialect='excel')
        newnamepath = os.path.join('postProcessing', 'surfaces', '0.5', 'U_constantIso')
        with open(newnamepath, 'r') as water_constant:
            lines = water_constant.readlines()
        lines = lines[2:-1]
        count = 0
        sumt = 0
        for line in lines:
            hang = line.split(" ")
            x = float(hang[0])
            yspeed_abs = abs(float(hang[4]))
            if abs(float(L_in) + float(L) / 2 - x) / x <= 0.003:
                sumt += yspeed_abs
                count += 1
        ys = sumt / count
        csv_writer.writerow([re, ang, A, L, wnum, structure, ys, niandu, density, sigma])


def simple_averagethickness(A=0.001, L=0.01, L_in=0.01):
    import os, subprocess
    dirs = os.listdir()
    for dir in dirs:
        if os.path.isdir(dir):
            os.chdir(dir)
            averagethickness(dir, 1, A, L, 1, 1, L_in, 1, 1, 1)
            os.chdir(os.path.pardir)


def simple_surfacelength(A=0.001, L=0.01, L_in=0.01):
    import os, subprocess
    dirs = os.listdir()
    for dir in dirs:
        if os.path.isdir(dir) and dir.startswith('r'):
            os.chdir(dir)
            surfacelength2(dir, 1, A, L, 1, 1, L_in, 1, 1, 1)
            os.chdir(os.path.pardir)


def surfacelength2(re, ang, A, L, wnum, structure, L_in, niandu, density, sigma):
    if not os.path.exists('../../../surfacelength.csv'):
        with open('../../../surfacelength.csv', 'w', newline='') as fuzhi:
            csv_writer = csv.writer(fuzhi, dialect='excel')
            csv_writer.writerow(
                ['re', 'ang', 'A', 'L', 'wnum', 'structure', 'surfacelength', 'niandu', 'density', 'sigma'])
    with open('../../../surfacelength.csv', 'a', newline='') as fuzhi:
        csv_writer = csv.writer(fuzhi, dialect='excel')
        newnamepath = os.path.join('postProcessing', 'surfaces', '0.5', 'alpha.water_constantIso')
        with open(newnamepath, 'r') as water_constant:
            lines = water_constant.readlines()
        length = 0
        dots = []
        for line in lines:
            hang = line.split(" ")
            x = float(hang[0])
            y = float(hang[1])
            if float(L_in) <= x <= float(L_in) + 5 * float(L):
                dots.append([x, y])
        dots = sorted(dots, key=lambda dot: dot[0])
        for i in range(0, len(dots) - 1):
            length += math.sqrt(
                (dots[i][0] - dots[i + 1][0]) * (dots[i][0] - dots[i + 1][0]) + (dots[i][1] - dots[i + 1][1]) * (
                dots[i][1] - dots[i + 1][1]))
        csv_writer.writerow([re, ang, A, L, wnum, structure, length, niandu, density, sigma])


def surfacelength(re, ang, A, L, wnum, structure, L_in, niandu, density, sigma):
    if not os.path.exists('../../../surfacelength.csv'):
        with open('../../../surfacelength.csv', 'w', newline='') as fuzhi:
            csv_writer = csv.writer(fuzhi, dialect='excel')
            csv_writer.writerow(
                ['re', 'ang', 'A', 'L', 'wnum', 'structure', 'surfacelength', 'niandu', 'density', 'sigma'])
    with open('../../../surfacelength.csv', 'a', newline='') as fuzhi:
        csv_writer = csv.writer(fuzhi, dialect='excel')
        newnamepath = os.path.join('postProcessing', 'surfaces', '0.5', 'alpha.water_constantIso')
        with open(newnamepath, 'r') as water_constant:
            lines = water_constant.readlines()
        length = 0
        dots = []
        for line in lines:
            hang = line.split(" ")
            x = float(hang[0])
            y = float(hang[1])
            if float(L_in) + float(L) <= x <= float(L_in) + 4 * float(L):
                dots.append([x, y])
        dots = sorted(dots, key=lambda dot: dot[0])
        for i in range(0, len(dots) - 1):
            length += math.sqrt(
                (dots[i][0] - dots[i + 1][0]) * (dots[i][0] - dots[i + 1][0]) + (dots[i][1] - dots[i + 1][1]) * (
                dots[i][1] - dots[i + 1][1]))
        csv_writer.writerow([re, ang, A, L, wnum, structure, length, niandu, density, sigma])


def averagethickness(re, ang, A, L, wnum, structure, L_in, niandu, density, sigma):
    if not os.path.exists('../../../averagethickness.csv'):
        with open('../../../averagethickness.csv', 'w', newline='') as fuzhi:
            csv_writer = csv.writer(fuzhi, dialect='excel')
            csv_writer.writerow(
                ['re', 'ang', 'A', 'L', 'wnum', 'structure', 'averagethickness', 'niandu', 'density', 'sigma'])
    with open('../../../averagethickness.csv', 'a', newline='') as fuzhi:
        csv_writer = csv.writer(fuzhi, dialect='excel')
        newnamepath = os.path.join('postProcessing', 'surfaces', '0.5', 'alpha.water_constantIso')
        with open(newnamepath, 'r') as water_constant:
            lines = water_constant.readlines()
        ysum = 0
        count = 0
        for line in lines:
            hang = line.split(" ")
            x = float(hang[0])
            y = float(hang[1])
            if float(L_in) + float(L) <= x <= float(L_in) + 4 * float(L):
                # if float(L_in) + float(L) + float(L)/4 <= x <= float(L_in) + 2 * float(L)-float(L)/4:
                #     ysum = ysum + y + A
                # else:
                ysum += y
                count += 1
        averagethickness = ysum / count
        csv_writer.writerow([re, ang, A, L, wnum, structure, averagethickness, niandu, density, sigma])


def fuzhi(re, ang, A, L, wnum, structure, L_in, niandu, density, sigma):
    if not os.path.exists('../../../fuzhi.csv'):
        with open('../../../fuzhi.csv', 'w', newline='') as fuzhi:
            csv_writer = csv.writer(fuzhi, dialect='excel')
            csv_writer.writerow(['re', 'ang', 'A', 'L', 'wnum', 'structure', 'fuzhi', 'niandu', 'density', 'sigma'])
    with open('../../../fuzhi.csv', 'a', newline='') as fuzhi:
        csv_writer = csv.writer(fuzhi, dialect='excel')
        newnamepath = os.path.join('postProcessing', 'surfaces', '0.5', 'alpha.water_constantIso')
        with open(newnamepath, 'r') as water_constant:
            lines = water_constant.readlines()
        maxval = -1000
        minval = 1000
        for line in lines:
            hang = line.split(" ")
            x = float(hang[0])
            y = float(hang[1])
            if float(L_in) + float(L) <= x <= float(L_in) + 2 * float(L):
                minval = min(minval, y)
                maxval = max(maxval, y)
        fz = maxval - minval
        csv_writer.writerow([re, ang, A, L, wnum, structure, fz, niandu, density, sigma])


if __name__ == '__main__':
    if len(sys.argv) == 12:
        type = sys.argv[1]
        re = sys.argv[2]
        ang = sys.argv[3]
        A = sys.argv[4]
        L = sys.argv[5]
        wnum = sys.argv[6]
        structure = sys.argv[7]
        L_in = sys.argv[8]
        niandu = sys.argv[9]
        density = sys.argv[10]
        sigma = sys.argv[11]
        if type == 'fuzhi':
            fuzhi(re, ang, A, L, wnum, structure, L_in, niandu, density, sigma)
        if type == 'yspeed':
            yspeed(re, ang, A, L, wnum, structure, L_in, niandu, density, sigma)
        if type == 'yspeedabs':
            yspeed_abs(re, ang, A, L, wnum, structure, L_in, niandu, density, sigma)
        if type == 'yintensity_surface':
            yintensity_surface(re, ang, A, L, wnum, structure, L_in, niandu, density, sigma)
        if type == 'yintensity_bogu':
            yintensity_bogu(re, ang, A, L, wnum, structure, L_in, niandu, density, sigma)
        if type == 'eddyposition':
            eddyposition(re, ang, A, L, wnum, structure, L_in, niandu, density, sigma)
        if type == 'averagethickness':
            averagethickness(re, ang, A, L, wnum, structure, L_in, niandu, density, sigma)
        if type == 'surfacelength':
            surfacelength(re, ang, A, L, wnum, structure, L_in, niandu, density, sigma)
    else:
        simple_surfacelength()
