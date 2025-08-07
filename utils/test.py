import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x = [1, 2, 3]  # Tọa độ x của các điểm
y = [4, 5, 6]  # Tọa độ y
z = [7, 8, 9]  # Tọa độ z
ax.scatter(x, y, z, c='r', marker='o')  # Vẽ các điểm
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()