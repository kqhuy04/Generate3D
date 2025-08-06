import numpy as np

class Utils:
    def __init__(self):
        pass
    def distance(A, B):
        return round(((A.x - B.x) ** 2 + (A.y - B.y) ** 2 + (A.z - B.z) ** 2) ** 0.5 * 100) / 100
    def isIn(name, list):
        for item in list:
            if (item.name == name):
                return True  
        return False    
    def getNormalVector(A, B, C):
        D = np.array([[A.x, A.y, A.z],
                      [B.x, B.y, B.z],
                      [C.x, C.y, C.z]])
        E = np.array([1, 1, 1])
        F = np.linalg.solve(D, E)
        return [round(i * 100) / 100 for i in list(F)]


        