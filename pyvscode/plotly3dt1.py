import plotly.graph_objects as go
import numpy as np
 
# 生成示例数据
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)
z = np.sin(np.sqrt(x**2 + y**2))
 
# 创建3D曲面图
fig = go.Figure(data=[go.Surface(z=z, x=x, y=y)])
 
# 添加标题和标签
fig.update_layout(title='3D Surface Plot', scene=dict(xaxis_title='X-axis', yaxis_title='Y-axis', zaxis_title='Z-axis'))
 
# 显示图表
fig.show()