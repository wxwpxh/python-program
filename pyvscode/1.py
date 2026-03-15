# 生成Excel文件

import pandas as pd

# 创建示例数据
data = {
    '商品名称': ['美式咖啡', '拿铁咖啡', '卡布奇诺', '美式咖啡', '拿铁咖啡', '卡布奇诺'],
    '销售数量': [10, 15, 12, 8, 20, 18],
    '销售日期': ['2023-04-01', '2023-04-01', '2023-04-01', '2023-04-02', '2023-04-02', '2023-04-02']
}

# 创建DataFrame
df = pd.DataFrame(data)

# 将DataFrame写入Excel文件
file_path = 'coffee_sales.xlsx'
df.to_excel(file_path, index=False, engine='openpyxl')

print(f"文件已创建: {file_path}")
