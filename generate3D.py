import sympy as sp
import regex as re
from utils.Utils import Utils
from utils.Point import Point

with open(r'inputs.txt', 'r', encoding='utf-8') as file:
    commands = file.read().split('\n')

if len(commands) > 0:
    points = []
    edges = []
    for command in commands:
        value = [item.strip() for item in re.split(r':|,', command)]
        print(value)
        if value[0] == 'hình chóp':
            if len(value[2]) == 4:
                S = Point(value[1], 0, 0, 2)
                A = Point(value[2][0], 1, 1, 1)
                B = Point(value[2][1], -1, 1, 1)
                C = Point(value[2][2], -1, -1, 1)
                D = Point(value[2][3], 1, -1, 1)
                points.append(S)  # Đỉnh chóp S
                points.append(A)  # A
                points.append(B)  # B
                points.append(C)  # C
                points.append(D)  # D
                edges.append([S, A])
                edges.append([S, B])
                edges.append([S, C])
                edges.append([S, D])
                edges.append([A, B])
                edges.append([B, C])
                edges.append([C, D])
                edges.append([D, A])

            elif len(value[2]) == 3:
                S = Point(value[1], 0, 0, 3)
                A = Point(value[2][0], 0, 0, 1)
                B = Point(value[2][1], 4, 0, 1)
                C = Point(value[2][2], 2, 3, 1)
                points.append(S)  # Đỉnh chóp S
                points.append(A)  # A
                points.append(B)  # B
                points.append(C)  # C
                edges.append([S, A])
                edges.append([S, B])
                edges.append([S, C])
                edges.append([A, B])
                edges.append([B, C])
                edges.append([C, A])

        elif value[0] == 'vuông góc':
            if len(value[1]) == 2:
                A, B, C = Utils.getNormalVector(
                    Utils.getPoint(value[2][0], points),
                    Utils.getPoint(value[2][1], points),
                    Utils.getPoint(value[2][2], points)
                )
                fpoint = Utils.getPoint(value[1][0], points)
                spoint = Utils.getPoint(value[1][1], points)
                distance = Utils.distance(fpoint, spoint)
                if value[1][0] in value[2]:
                    spoint.x = A * distance + fpoint.x
                    spoint.y = B * distance + fpoint.y
                    spoint.z = C * distance + fpoint.z
                elif value[1][1] in value[2]:
                    fpoint.x = A * distance + spoint.x
                    fpoint.y = B * distance + spoint.y
                    fpoint.z = C * distance + spoint.z
        elif value[0] == 'tam giác vuông':
            A = Utils.getPoint(value[1][0], points)
            B = Utils.getPoint(value[1][1], points)
            C = Utils.getPoint(value[1][2], points)
            if value[2] == A.name:  # Góc vuông tại A
                C.x = A.x
                C.y = B.y
            elif value[2] == B.name:  # Góc vuông tại B
                C.x = B.x
                C.y = A.y
            elif value[2] == C.name:  # Góc vuông tại C
                B.x = C.x
                B.y = A.y
        elif value[0] == 'tam giác cân':
            A = Utils.getPoint(value[1][0], points)
            B = Utils.getPoint(value[1][1], points)
            C = Utils.getPoint(value[1][2], points)
            if value[2] == A.name:  # Cân tại A
                C.x = A.x
                C.y = -B.y
            elif value[2] == B.name:  # Cân tại B
                C.x = B.x
                C.y = -A.y
            elif value[2] == C.name:  # Cân tại C
                A.x = C.x
                A.y = -B.y
        elif value[0] == 'tam giác đều':
            A = Utils.getPoint(value[1][0], points)
            B = Utils.getPoint(value[1][1], points)
            C = Utils.getPoint(value[1][2], points)
            # Đặt tọa độ sao cho AB = BC = CA
            B.x = A.x + 1
            B.y = A.y
            C.x = A.x + 0.5
            C.y = A.y + sp.sqrt(3) / 2
        elif value[0] == 'tam giác vuông cân':
            A = Utils.getPoint(value[1][0], points)
            B = Utils.getPoint(value[1][1], points)
            C = Utils.getPoint(value[1][2], points)
            if value[2] == A.name:  # Vuông cân tại A
                B.x = A.x + 1
                B.y = A.y
                C.x = A.x
                C.y = A.y + 1
            elif value[2] == B.name:  # Vuông cân tại B
                A.x = B.x + 1
                A.y = B.y
                C.x = B.x
                C.y = B.y + 1
            elif value[2] == C.name:  # Vuông cân tại C
                A.x = C.x + 1
                A.y = C.y
                B.x = C.x
                B.y = C.y + 1
        elif value[0] == 'độ dài':
            A = Utils.getPoint(value[1][0], points)
            B = Utils.getPoint(value[1][1], points)
            length = float(value[2])
            current_distance = Utils.distance(A, B)
            if current_distance != 0:
                scale = length / current_distance
                B.x = A.x + (B.x - A.x) * scale
                B.y = A.y + (B.y - A.y) * scale
                B.z = A.z + (B.z - A.z) * scale
        elif value[0] == 'tỷ lệ':
            A = Utils.getPoint(value[1][0], points)
            B = Utils.getPoint(value[1][1], points)
            C = Utils.getPoint(value[1][2], points)
            ratio = float(value[2])
            # AB/AC = ratio
            C.x = A.x + (B.x - A.x) / ratio
            C.y = A.y + (B.y - A.y) / ratio
            C.z = A.z + (B.z - A.z) / ratio
        elif value[0] == 'hình chữ nhật':
            A = Utils.getPoint(value[1][0], points)
            B = Utils.getPoint(value[1][1], points)
            C = Utils.getPoint(value[1][2], points)
            D = Utils.getPoint(value[1][3], points)
            # Đảm bảo AB vuông góc với AD, AB = CD, AD = BC
            C.x = B.x + (A.x - D.x)
            C.y = B.y + (A.y - D.y)
            C.z = B.z + (A.z - D.z)
        elif value[0] == 'hình thoi':
            A = Utils.getPoint(value[1][0], points)
            B = Utils.getPoint(value[1][1], points)
            C = Utils.getPoint(value[1][2], points)
            D = Utils.getPoint(value[1][3], points)
            # AB = BC = CD = DA
            mid_AC_x = (A.x + C.x) / 2
            mid_AC_y = (A.y + C.y) / 2
            mid_AC_z = (A.z + C.z) / 2
            mid_BD_x = (B.x + D.x) / 2
            mid_BD_y = (B.y + D.y) / 2
            mid_BD_z = (B.z + D.z) / 2
            D.x = 2 * mid_AC_x - B.x
            D.y = 2 * mid_AC_y - B.y
            D.z = 2 * mid_AC_z - B.z
        elif value[0] == 'hình chiếu':
            S = Utils.getPoint(value[1], points)
            H = Utils.getPoint(value[3], points)
            plane_points = [Utils.getPoint(p, points) for p in value[2]]
            A, B, C = Utils.getNormalVector(plane_points[0], plane_points[1], plane_points[2])
            t = sp.Symbol('t')
            eq1 = A * (S.x + t * (H.x - S.x)) + B * (S.y + t * (H.y - S.y)) + C * (S.z + t * (H.z - S.z))
            t_val = sp.solve(eq1, t)[0]
            H.x = S.x + t_val * (H.x - S.x)
            H.y = S.y + t_val * (H.y - S.y)
            H.z = S.z + t_val * (H.z - S.z)
        elif value[0] == 'trung điểm':
            M = Utils.getPoint(value[2], points)
            A = Utils.getPoint(value[1][0], points)
            B = Utils.getPoint(value[1][1], points)
            M.x = (A.x + B.x) / 2
            M.y = (A.y + B.y) / 2
            M.z = (A.z + B.z) / 2
        elif value[0] == 'góc':
            A = Utils.getPoint(value[1][0], points)
            B = Utils.getPoint(value[1][1], points)
            C = Utils.getPoint(value[1][2], points)
            angle = float(value[2]) * sp.pi / 180  # Chuyển đổi sang radian
            # Tính vector AB và BC
            AB = [B.x - A.x, B.y - A.y, B.z - A.z]
            BC = [C.x - B.x, C.y - B.y, C.z - B.z]
            # Tính tích vô hướng và điều chỉnh tọa độ C
            dot_product = sum(a * b for a, b in zip(AB, BC))
            mag_AB = Utils.distance(A, B)
            mag_BC = Utils.distance(B, C)
            cos_angle = sp.cos(angle)
            t = sp.Symbol('t')
            eq = dot_product - mag_AB * mag_BC * cos_angle
            C.x = B.x + (C.x - B.x) * t
            C.y = B.y + (C.y - B.y) * t
            C.z = B.z + (C.z - B.z) * t
            t_val = sp.solve(eq.subs({C.x: B.x + (C.x - B.x) * t, C.y: B.y + (C.y - B.y) * t, C.z: B.z + (C.z - B.z) * t}), t)
            if t_val:
                t_val = t_val[0]
                C.x = B.x + (C.x - B.x) * t_val
                C.y = B.y + (C.y - B.y) * t_val
                C.z = B.z + (C.z - B.z) * t_val
    Utils.draw(points, edges)
