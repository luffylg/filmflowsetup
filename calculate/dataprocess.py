import csv
import os
import sys
def yintensity_surface(re, ang, A, L, wnum, structure, L_in):
    path = os.path.join('postProcessing', 'surfaces', '0.5', 'U_constantIso.raw')
    newnamepath = os.path.join('postProcessing', 'surfaces', '0.5', 'U_constantIso')
    if os.path.exists(path) and not os.path.exists(newnamepath):
        os.rename(path, newnamepath)
    if not os.path.exists('../../../yintensity_surface.csv'):
        with open('../../../yintensity_surface.csv', 'w', newline='') as yintensity_surface:
            csv_writer = csv.writer(yintensity_surface, dialect='excel')
            csv_writer.writerow(['re', 'ang', 'A', 'L', 'wnum', 'structure', 'yintensity_surface'])
    else:
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
            csv_writer.writerow([re, ang, A, L, wnum, structure, ys])


def yspeed(re, ang, A, L, wnum, structure, L_in):
    path = os.path.join('postProcessing', 'surfaces', '0.5', 'U_constantIso.raw')
    newnamepath = os.path.join('postProcessing', 'surfaces', '0.5', 'U_constantIso')
    if os.path.exists(path) and not os.path.exists(newnamepath):
        os.rename(path, newnamepath)
    if not os.path.exists('../../../yspeed.csv'):
        with open('../../../yspeed.csv', 'w', newline='') as yspeed:
            csv_writer = csv.writer(yspeed, dialect='excel')
            csv_writer.writerow(['re', 'ang', 'A', 'L', 'wnum', 'structure', 'yspeed'])
    else:
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
                if abs(float(L_in) + float(L) / 2 - x) / x <= 0.002:
                    sumt += yspeed
                    count += 1
            ys = sumt / count
            csv_writer.writerow([re, ang, A, L, wnum, structure, ys])


def fuzhi(re, ang, A, L, wnum, structure, L_in):
    if not os.path.exists('../../../fuzhi.csv'):
        with open('../../../fuzhi.csv', 'w', newline='') as fuzhi:
            csv_writer = csv.writer(fuzhi, dialect='excel')
            csv_writer.writerow(['re', 'ang', 'A', 'L', 'wnum', 'structure', 'fuzhi'])
    else:
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
            csv_writer.writerow([re, ang, A, L, wnum, structure, fz])


if __name__ == '__main__':
    if len(sys.argv) == 9:
        type = sys.argv[1]
        re = sys.argv[2]
        ang = sys.argv[3]
        A = sys.argv[4]
        L = sys.argv[5]
        wnum = sys.argv[6]
        structure = sys.argv[7]
        L_in = sys.argv[8]
        if type == 'fuzhi':
            fuzhi(re, ang, A, L, wnum, structure, L_in)
        if type == 'yspeed':
            yspeed(re, ang, A, L, wnum, structure, L_in)
        if type == 'yintensity_surface':
            yintensity_surface(re, ang, A, L, wnum, structure, L_in)
