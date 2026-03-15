
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# 设置中文字体和解决负号显示问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 加载示例数据集
tips = sns.load_dataset("tips")
iris = sns.load_dataset("iris")

def scatter_plot_example():
    """散点图示例"""
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=tips, x="total_bill", y="tip", hue="day", style="time")
    plt.title("餐厅小费数据散点图")
    plt.xlabel("总账单金额")
    plt.ylabel("小费金额")
    plt.show()

def line_plot_example():
    """折线图示例"""
    plt.figure(figsize=(10, 6))
    # 创建时间序列数据
    dates = pd.date_range('2023-01-01', periods=100, freq='D')
    values = np.cumsum(np.random.randn(100)) + 100
    data = pd.DataFrame({'date': dates, 'value': values})
    
    sns.lineplot(data=data, x="date", y="value")
    plt.title("时间序列折线图")
    plt.xlabel("日期")
    plt.ylabel("数值")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def bar_plot_example():
    """条形图示例"""
    plt.figure(figsize=(10, 6))
    sns.barplot(data=tips, x="day", y="total_bill", hue="sex", errorbar=None)
    plt.title("不同日期和性别平均账单金额")
    plt.xlabel("日期")
    plt.ylabel("平均账单金额")
    plt.show()

def histogram_example():
    """直方图示例"""
    plt.figure(figsize=(10, 6))
    sns.histplot(data=tips, x="total_bill", kde=True, bins=30)
    plt.title("账单金额分布直方图")
    plt.xlabel("账单金额")
    plt.ylabel("频次")
    plt.show()

def box_plot_example():
    """箱线图示例"""
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=tips, x="day", y="total_bill", hue="smoker")
    plt.title("不同日期吸烟情况账单金额箱线图")
    plt.xlabel("日期")
    plt.ylabel("账单金额")
    plt.show()

def heatmap_example():
    # 加载iris数据集
    iris = sns.load_dataset('iris')
    
    # 使用numeric_only=True参数计算相关性矩阵
    corr_matrix = iris.corr(numeric_only=True)
    
    # 绘制热力图
    plt.figure(figsize=(8, 6))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0)
    plt.title('Iris数据集特征相关性热力图')
    plt.tight_layout()
    plt.show()

def regression_plot_example():
    """回归图示例"""
    plt.figure(figsize=(10, 6))
    sns.regplot(data=tips, x="total_bill", y="tip")
    plt.title("账单金额与小费金额回归分析")
    plt.xlabel("账单金额")
    plt.ylabel("小费金额")
    plt.show()

def violin_plot_example():
    """小提琴图示例"""
    plt.figure(figsize=(10, 6))
    sns.violinplot(data=tips, x="day", y="total_bill", hue="sex", split=True)
    plt.title("不同日期和性别账单金额分布小提琴图")
    plt.xlabel("日期")
    plt.ylabel("账单金额")
    plt.show()

def pair_plot_example():
    """配对图示例"""
    plt.figure(figsize=(12, 10))
    sns.pairplot(iris, hue="species")
    plt.suptitle("鸢尾花特征配对图", y=1.02)
    plt.show()

def main():
    """主函数，依次执行各个示例"""
    print("开始展示Seaborn各种图表示例...")
    
    scatter_plot_example()
    line_plot_example()
    bar_plot_example()
    histogram_example()
    box_plot_example()
    heatmap_example()
    regression_plot_example()
    violin_plot_example()
    pair_plot_example()
    
    print("所有示例展示完毕！")

if __name__ == "__main__":
    main()
