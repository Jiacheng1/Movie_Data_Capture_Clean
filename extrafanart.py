import os
import sys
import re

# 获取文件夹路径作为命令行参数
if len(sys.argv) != 2:
    print("请提供文件夹路径作为参数。")
    sys.exit(1)

folder_path = sys.argv[1]

# 检查文件夹路径是否存在
if not os.path.isdir(folder_path):
    print(f"指定的路径 '{folder_path}' 不是一个有效的文件夹。")
    sys.exit(1)

# 获取文件夹中的所有文件名
files = [f for f in os.listdir(folder_path) if f.startswith('extrafanart-') and f.endswith('.jpg')]
# files = [f for f in os.listdir(folder_path)]

# 按文件名排序
# files.sort()

# 使用正则表达式提取数字并按数字排序
files.sort(key=lambda f: int(re.search(r'(\d+)', f).group(1)))

# for file in files:
#     print(file)

# 删除 extrafanart-1.jpg
if len(files) > 0:
    os.remove(os.path.join(folder_path, files[0]))
    print(f"已删除 '{files[0]}'")

# 重命名文件
for i in range(1, len(files)):
    old_name = files[i]
    new_name = f'extrafanart-{i}.jpg'
    os.rename(os.path.join(folder_path, old_name), os.path.join(folder_path, new_name))
    print(f"已将 '{old_name}' 改为 '{new_name}'")

print("操作完成。")
