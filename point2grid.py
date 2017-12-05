# -*- coding: utf-8 -*-
import decimal

def imax(ilist):
    return ilist[0] if (ilist[0] > ilist[1]) else ilist[1]

def imin(ilist):
    return ilist[0] if (ilist[0] < ilist[1]) else ilist[1]

def iround(input):
    return ((int)(input / 0.001)) / 1000.0

def remainder(input):
    return (input * 100) % 1 == 0

def getlist(point1, point2):
    """
    return grid_id list between 2 point line
    :param point1: 
    :param point2: 
    :return: grid_id list
            e.g.  ['111.245,22.655','111.255,22.655']
    """
    grid = 0.001
    halfgrid = grid / 2
    x1 = point1[0]  # halfgrid
    x2 = point2[0]  # 0.018
    y1 = point1[1]  # 0.0075
    y2 = point2[1]  # 0.0075

    ilist = []
    ilist.append(str(iround(x1) + halfgrid) + "," + str(iround(y1) + halfgrid))
    if str(iround(x2) + halfgrid) + "," + str(iround(y2) + halfgrid) not in ilist:
        ilist.append(str(iround(x2) + halfgrid) + "," + str(iround(y2) + halfgrid))
    if (x1 == x2 and x1 % grid == 0):
        i = iround(imin([y1, y2]))
        while (i <= iround(imax([y1, y2]))):
            if str(iround(x1) + halfgrid) + "," + str(i + halfgrid) not in ilist:
                ilist.append(str(iround(x1) + halfgrid) + "," + str(i + halfgrid))
            if str(iround(x1) - halfgrid) + "," + str(i + halfgrid) not in ilist:
                ilist.append(str(iround(x1) - halfgrid) + "," + str(i + halfgrid))
            i = i + grid
    else:
        if (iround(x1) == iround(x2)):
            i = iround(imin([y1, y2]))
            while (i < iround(imax([y1, y2]))):
                if str(iround(x1) + halfgrid) + "," + str(i + halfgrid) not in ilist:
                    ilist.append(str(iround(x1) + halfgrid) + "," + str(i + halfgrid))
                i = i + grid
        else:
            i = iround(imin([x1, x2]))
            while (i < iround(imax([x1, x2]))):
                i = i + grid
                i = ((int)(i / 0.001)) / 1000.0
                y = (y2 - y1) / (x2 - x1) * (i - x1) + y1
                if (y % grid == 0):
                    if ((y2 - y1) / (x2 - x1) > 0):
                        if str(i - halfgrid) + "," + str(iround(y) - halfgrid) not in ilist:
                            ilist.append(str(i - halfgrid) + "," + str(iround(y) - halfgrid))
                        if str(i + halfgrid) + "," + str(iround(y) + halfgrid) not in ilist:
                            ilist.append(str(i + halfgrid) + "," + str(iround(y) + halfgrid))
                    if ((y2 - y1) / (x2 - x1) < 0):
                        if str(i - halfgrid) + "," + str(iround(y) + halfgrid) not in ilist:
                            ilist.append(str(i - halfgrid) + "," + str(iround(y) + halfgrid))
                        if str(i + halfgrid) + "," + str(iround(y) + halfgrid) not in ilist:
                            ilist.append(str(i + halfgrid) + "," + str(iround(y) - halfgrid))
                else:
                    if str(i - halfgrid) + "," + str(iround(y) + halfgrid) not in ilist:
                        ilist.append(str(i - halfgrid) + "," + str(iround(y) + halfgrid))
                    if str(i + halfgrid) + "," + str(iround(y) + halfgrid) not in ilist:
                        ilist.append(str(i + halfgrid) + "," + str(iround(y) + halfgrid))

            i = iround(imin([y1, y2]))
            while (i < iround(imax([y1, y2]))):
                i = i + grid
                i = ((int)(i / 0.001)) / 1000.0
                x = (x2 - x1) / (y2 - y1) * (i - y1) + x1
                if (x % grid == 0):
                    if ((y2 - y1) / (x2 - x1) > 0):
                        if str(iround(x) + halfgrid) + "," + str(i + halfgrid) not in ilist:
                            ilist.append(str(iround(x) + halfgrid) + "," + str(i + halfgrid))
                        if str(iround(x) - halfgrid) + "," + str(i - halfgrid) not in ilist:
                            ilist.append(str(iround(x) - halfgrid) + "," + str(i - halfgrid))
                    if ((y2 - y1) / (x2 - x1) < 0):
                        if str(iround(x) + halfgrid) + "," + str(i - halfgrid) not in ilist:
                            ilist.append(str(iround(x) + halfgrid) + "," + str(i - halfgrid))
                        if str(iround(x) - halfgrid) + "," + str(i + halfgrid) not in ilist:
                            ilist.append(str(iround(x) - halfgrid) + "," + str(i + halfgrid))
                else:
                    if str(iround(x) + halfgrid) + "," + str(i + halfgrid) not in ilist:
                        ilist.append(str(iround(x) + halfgrid) + "," + str(i + halfgrid))
                    if str(iround(x) + halfgrid) + "," + str(i - halfgrid) not in ilist:
                        ilist.append(str(iround(x) + halfgrid) + "," + str(i - halfgrid))
    return ilist
