import numpy as np
from .Point import Point
import matplotlib.pyplot as plt

class Utils:
    def __init__(self):
        pass
    def distance(A: Point, B: Point):
        return round(((A.x - B.x) ** 2 + (A.y - B.y) ** 2 + (A.z - B.z) ** 2) ** 0.5 * 100) / 100
    def getPoint(name: str, list: list):
        for item in list:
            if (item.name == name):
                return item
        return None
    def getNormalVector(A: Point, B: Point, C: Point):
        if ((A.x == 0 and B.X == 0 and C.x == 0) or
            (A.y == 0 and B.y == 0 and C.y == 0) or
            (A.z == 0 and B.z == 0 and C.z == 0)):
            return [0, 0, 0]
        D = np.array([[A.x, A.y, A.z],
                      [B.x, B.y, B.z],
                      [C.x, C.y, C.z]])
        E = np.array([1, 1, 1])
        F = np.linalg.solve(D, E)
        return [round(i * 100) / 100 for i in list(F)]
    def toCoordinate(A: Point):
        return [A.x, A.y, A.z]
    def draw(points: list, edges: list):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        
        # Extract coordinates and plot points
        x = [point.x for point in points]  # Tọa độ x
        y = [point.y for point in points]  # Tọa độ y
        z = [point.z for point in points]  # Tọa độ z
        ax.scatter(x, y, z, c='r', marker='o')  # Vẽ các điểm
        
        # Add labels for each point
        for point in points:
            ax.text(point.x, point.y, point.z, point.name, size=10, zorder=1, color='k')  # Thêm nhãn
        
        # Draw line segments between specified point pairs
        for point1, point2 in edges:
            ax.plot(
                [point1.x, point2.x],  # x coordinates of the two points
                [point1.y, point2.y],  # y coordinates
                [point1.z, point2.z],  # z coordinates
                'b-',  # Blue line with solid style
                linewidth=1
            )
        
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.set_axis_off()
        def update_view(event):
            if event.inaxes == ax:
                elev = ax.elev
                azim = ax.azim
                print(f"Góc nhìn hiện tại - Elevation: {elev:.1f}°, Azimuth: {azim:.1f}°")
                
                # Tính toán tọa độ góc nhìn gần đúng (camera position)
                distance = 10  # Khoảng cách từ tâm, bạn có thể điều chỉnh
                x_center = np.mean(x)
                y_center = np.mean(y)
                z_center = np.mean(z)
                
                # Chuyển đổi từ góc sang tọa độ
                theta = np.radians(azim)  # Góc quay quanh trục z
                phi = np.radians(90 - elev)  # Góc nâng (chuyển đổi để phù hợp với hệ tọa độ cầu)
                
                x_cam = x_center + distance * np.sin(phi) * np.cos(theta)
                y_cam = y_center + distance * np.sin(phi) * np.sin(theta)
                z_cam = z_center + distance * np.cos(phi)
                
                print(f"Tọa độ góc nhìn gần đúng: ({x_cam:.1f}, {y_cam:.1f}, {z_cam:.1f})")
    
        fig.canvas.mpl_connect('motion_notify_event', update_view)
        plt.show()


        