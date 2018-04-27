import csv
import os
import sys

import math


def surfacesudu(re):
    path = os.path.join('postProcessing', 'surfaces', '0.5', 'U_constantIso.raw')
    newnamepath = os.path.join('postProcessing', 'surfaces', '0.5', 'U_constantIso')
    if os.path.exists(path) and not os.path.exists(newnamepath):
        os.rename(path, newnamepath)
    if not os.path.exists('../../../surfacesudu.csv'):
        with open('../../../surfacesudu.csv', 'w', newline='') as surfacesudu:
            csv_writer = csv.writer(surfacesudu, dialect='excel')
            csv_writer.writerow(['re', 'x','y','xs','ys'])
    with open('../../../surfacesudu.csv', 'a', newline='') as surfacesudu:
        csv_writer = csv.writer(surfacesudu, dialect='excel')
        with open(newnamepath, 'r') as water_constant:
            lines = water_constant.readlines()
        lines = lines[2:-1]
        for line in lines:
            hang = line.split(" ")
            x = float(hang[0])
            y = float(hang[1])
            xs = float(hang[3])
            ys=float(hang[4])
            csv_writer.writerow([re, x,y,xs,ys])

def houduspeed(re):
    path = os.path.join('postProcessing', 'sets', '0.5', 'velocity_U.xy')
    newnamepath = os.path.join('postProcessing', 'sets', '0.5', 'velocity_U')
    if os.path.exists(path) and not os.path.exists(newnamepath):
        os.rename(path, newnamepath)
    if not os.path.exists('../../../houduspeed.csv'):
        with open('../../../houduspeed.csv', 'w', newline='') as houduspeed:
            csv_writer = csv.writer(houduspeed, dialect='excel')
            csv_writer.writerow(['re', 'y','xs','ys'])
    with open('../../../houduspeed.csv', 'a', newline='') as houduspeed:
        csv_writer = csv.writer(houduspeed, dialect='excel')
        with open(newnamepath, 'r') as water_constant:
            lines = water_constant.readlines()
        for line in lines:
            hang = line.split(" ")
            y = float(hang[0])
            xs = float(hang[1])
            ys=float(hang[2])
            csv_writer.writerow([re,y,xs,ys])


if __name__ == '__main__':
    import os,subprocess
    dirs = os.listdir()
    for dir in dirs:
        if os.path.isdir(dir):
            os.chdir(dir)
            surfacesudu(dir)
            houduspeed(dir)
            os.chdir(os.path.pardir)