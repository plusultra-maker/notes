import numpy as np
import matplotlib.pyplot as plt

# 给出的数据
X = np.array([0, 2, 3])
Y = np.array([1, 1, 4])

# 计算回归系数 w 和截距 b
w, b = np.polyfit(X, Y, 1)

# 绘制回归曲线图像
plt.scatter(X, Y, color='blue')
plt.plot(X, w*X+b, color='red')
plt.title('Linear Regression')
plt.xlabel('X')
plt.ylabel('Y')
plt.savefig('myplot.png')
plt.show()

print('w-6/7 =', w-6/7)
print('b =', b-4/7)
