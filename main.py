import os
import glob
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

plt.rcParams['font.family'] = 'SimSun'
# 指定图片文件夹路径
image_folder = r"E:\DataSet\FG-NET\pai\Images"

# 创建空字典用于存储分类统计结果
classification = {1}

# 获取图片文件名列表
image_files = glob.glob(os.path.join(image_folder, "*.jpg"))  # 包含 "/path/to/images" 文件夹下所有以 ".jpg" 结尾的文件路径 返回图片名称的列表

total_images = len(image_files)
# 遍历图片文件列表
for image_file in image_files:
    # 获取文件名的后两位字符
    category = image_file[-6:-4]  # 假设文件名形如 "image01.jpg"，需要根据实际情况修改索引范围

    # 检查字典中是否已存在该分类标识的键
    if category in classification:
        # 如果存在，将对应的值加一
        classification[category] += 1
    else:
        # 如果不存在，将该分类标识作为新的键，并设置值为 1
        classification[category] = 1


#
# # 输出分类统计结果
# for category, count in classification.items():
#     print(f"分类 {category}: {count} 个")


int_classification = {}



# 遍历原字典
for key, value in classification.items():
    # 将键从字符串类型转换为整数类型，并将对应的值存储到新字典中
    int_key = int(key)
    int_classification[int_key] = value

sort_classification = dict(sorted(int_classification.items(), key=lambda x: int(x[0]))) # 升序排序
for key, value in sort_classification.items():
    print(f"key:{key}, value:{value}")
print(total_images)
print(int_classification)
print(sort_classification)
a = list(sort_classification.keys())
b = list(sort_classification.values())
print("键列表:", a)
print("值列表:", b)
i = len(sort_classification)
output = ("建的个数: {}".format(i))
print(output)
 # 按照年龄进行排序制图
p = plt.bar(a, b, width=0.5)
plt.bar_label(p, label_type="edge")
for j in range(len(p)):
    if b[j] < (total_images/i):
        p[j].set_color('black')

plt.xlabel('年龄')
plt.ylabel('图片个数')
plt.title("数据集统计")

plt.plot(a, b, marker='.', linestyle='-', color='red', label='折现')
plt.axhline(total_images/i, color='blue', linestyle='--', label='平均线')# 绘制水平线

plt.xticks(range(16, 78, 2)) # 让每个横坐标都显示
plt.legend() # 在左上角将lable显示出来，图例
plt.show()


bd = sorted(int_classification.items(), key=lambda x: int(x[1]), reverse=True)
print(bd)
a1 = list(bd.keys())
b1 = list(bd.values())
print(a1, b1)
