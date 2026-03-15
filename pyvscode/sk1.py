# 导入必要的库
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文字体
plt.rcParams['axes.unicode_minus'] = False    # 正常显示负号
# 创建一些数据
# 假设我们有一些关于房子面积（平方英尺）的数据
# 以及对应的房价（万美元）
# 这里我们使用numpy来创建模拟数据
X = np.array([[150], [200], [250], [300], [350], [400], [600]])
y = np.array([1, 1.5, 2, 2.5, 3, 3.5, 5])

# 将数据集分为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 创建线性回归模型
model = LinearRegression()

# 训练模型
model.fit(X_train, y_train)

# 使用模型进行预测
y_pred = model.predict(X_test)

# 输出模型的参数
print("斜率: ", model.coef_)
print("截距: ", model.intercept_)

# 绘制结果
plt.scatter(X, y, color='blue', label='真实数据')
plt.scatter(X_test, y_pred, color='red', label='预测数据')
plt.plot(X, model.predict(X), color='green', linewidth=2, label='回归线')
plt.xlabel('面积（平方英尺）')
plt.ylabel('价格（万美元）')
plt.title('房子面积与价格的线性回归')
plt.legend()
plt.show()
input("按任意键退出...")