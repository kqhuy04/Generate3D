import sympy as sp
import regex as re
from utils import Utils

with open(r'inputs.txt', 'r', encoding = 'utf-8') as file:
    commands = file.read().split('\n')
if len(commands) > 0:
    points = []
    for command in commands:
        value = [item.strip() for item in re.split(r':|,', command)]
        if value[0] == 'hình chóp':
            if len(value[2]) == 4:
                points.append(Point(value[1], 0, 0, 1))
                points.append(Point(value[2][0], 1, 1, 0))
                points.append(Point(value[2][1], -1, 1, 0))
                points.append(Point(value[2][2], -1, -1, 0))
                points.append(Point(value[2][3], 1, -1, 0))
            elif len(value[2]) == 3:
                points.append(Point(value[1], 0, 0, 2))
                points.append(Point(value[2][0], 0, 0, 0))
                points.append(Point(value[2][1], 4, 0, 0))
                points.append(Point(value[2][2], 2, 3, 0))
        if value[0] == 'vuông góc':
            if len(value[1]) == 2 and len(value[2]) == 3:
                if (Utils.isIn(value[1][0], value[2])):
                    
                elif (Utils.isIn(value[1][0], value[2])):


                

