import pandas as pd

# 读取Excel文件
file_path = 'coffee_sales.xlsx'
df = pd.read_excel(file_path)

# 查看数据的前几行
print("原始数据：")
print(df.head())

# 计算每天的总销售数量
daily_sales = df.groupby('销售日期')['销售数量'].sum().reset_index()
daily_sales.columns = ['销售日期', '总销售数量']

# 计算每种商品的总销售数量
product_sales = df.groupby('商品名称')['销售数量'].sum().reset_index()
product_sales.columns = ['商品名称', '总销售数量']

# 找出最畅销的商品
most_sold_product = product_sales.loc[product_sales['总销售数量'].idxmax()]

# 输出结果
print("\n每天的总销售数量：")
print(daily_sales)

print("\n每种商品的总销售数量：")
print(product_sales)

print("\n最畅销的商品：")
print(most_sold_product)

# 将结果写入新的Excel文件
with pd.ExcelWriter('coffee_sales_analysis.xlsx', engine='openpyxl') as writer:
    daily_sales.to_excel(writer, sheet_name='每天总销售', index=False)
    product_sales.to_excel(writer, sheet_name='每种商品总销售', index=False)
    most_sold_product.to_excel(writer, sheet_name='最畅销商品', index=False)

print("\n分析结果已保存到 'coffee_sales_analysis.xlsx'")
