import matplotlib.pyplot as plt
from matplotlib import font_manager
# 设置支持中文和符号的字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False
import numpy as np
import json

# 从文件读取数据（假设数据为JSON格式）
with open('car.json', 'r', encoding='utf-8') as f:
    data = json.load(f)  # 直接解析为Python对象（列表/字典）

# 后续操作（如遍历数据）
for car in data:
    # 从price_range字段解析价格区间
    price_range = car['price_range'].replace('万', '')  # 去掉"万"字
    price_low, price_high = price_range.split('-')     # 分割价格区间
    print(f"车型: {car['model']}, 价格区间: {price_low}-{price_high}万")

models = []
min_prices = []
max_prices = []
brand_colors = []  # 按品牌分配颜色

# 只处理一次数据，移除重复的处理循环
for car in data:
    # 提取价格范围并转换为浮点数
    price_range = car["price_range"].replace("万", "")  # 去掉"万"字
    low, high = price_range.split("-")                  # 分割价格区间
    models.append(car["model"])
    min_prices.append(float(low))
    max_prices.append(float(high))

    # 按品牌分配颜色
    if "华晨宝马" in car["brand"]:
        brand_colors.append("dodgerblue")
    elif "宝马(进口)" in car["brand"]:
        brand_colors.append("darkorange")
    else:  # 宝马M系列
        brand_colors.append("crimson")

# 按最低价排序（需要在排序前确保数据一一对应）
# 创建索引排序
sorted_idx = np.argsort(min_prices)

# 应用排序到所有相关列表
models_sorted = [models[i] for i in sorted_idx]
min_prices_sorted = [min_prices[i] for i in sorted_idx]
max_prices_sorted = [max_prices[i] for i in sorted_idx]
brand_colors_sorted = [brand_colors[i] for i in sorted_idx]

# 创建图表
plt.figure(figsize=(12, 10), dpi=100)

# 绘制价格区间条
for i, (model, low, high, color) in enumerate(zip(models_sorted, min_prices_sorted, max_prices_sorted, brand_colors_sorted)):
    plt.hlines(y=i, xmin=low, xmax=high,
               colors=color, lw=8, alpha=0.7)
    # 添加价格标签
    plt.text(low, i, f"¥{low}万", ha="right", va="center", fontsize=9)
    plt.text(high, i, f"¥{high}万", ha="left", va="center", fontsize=9)

# 添加品牌图例
from matplotlib.lines import Line2D
legend_elements = [
    Line2D([0], [0], color="dodgerblue", lw=4, label="华晨宝马"),
    Line2D([0], [0], color="darkorange", lw=4, label="宝马(进口)"),
    Line2D([0], [0], color="crimson", lw=4, label="宝马M系列")
]

# 设置图表样式
plt.title("宝马各车型价格区间分布 (2025)", fontsize=14, pad=20)
plt.yticks(range(len(models_sorted)), models_sorted, fontsize=10)
plt.xticks(np.arange(0, 350, 50), fontsize=9)
plt.xlabel("价格 (人民币/万)", fontsize=12)
plt.grid(axis="x", linestyle="--", alpha=0.3)
plt.legend(handles=legend_elements, loc="lower right")
plt.margins(y=0.05, x=0.02)

plt.tight_layout()
plt.savefig("bmw_price_ranges.png", bbox_inches="tight")
plt.show()
