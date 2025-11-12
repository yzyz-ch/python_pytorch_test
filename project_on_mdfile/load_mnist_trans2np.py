import pandas as pd
import numpy as np
import struct
import gzip  # 导入处理gzip压缩文件的模块
import os


def read_mnist_labels(file_path):
    """
    读取MNIST二进制标签文件（支持.gz压缩），转换为numpy数组
    Args:
        file_path (str): 标签文件路径（可以是.gz压缩文件）
    Returns:
        np.ndarray: 标签数组，shape=(样本数,)
    """
    # 检查文件是否存在
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"文件不存在: {file_path}")

    # 判断文件是否为.gz压缩文件，并选择相应的打开方式
    open_func = gzip.open if file_path.endswith('.gz') else open

    with open_func(file_path, 'rb') as f:
        # 解析头部（前8字节）：魔法数 + 样本数
        magic_number, num_labels = struct.unpack('>II', f.read(8))

        # 验证文件格式
        if magic_number != 2049:
            raise ValueError("不是有效的MNIST标签文件（魔法数不匹配）")

        # 读取所有标签数据
        labels = np.fromfile(f, dtype=np.uint8)

    # 用pandas转换（可选步骤，用于熟悉pandas操作）
    labels_series = pd.Series(labels)
    labels_np = labels_series.to_numpy()

    return labels_np


# ------------------- 测试代码 -------------------
if __name__ == "__main__":
    # 定义你的MNIST标签文件路径（使用.gz压缩文件）

    print(os.getcwd())
    label_file_name = "train-labels-idx1-ubyte.gz"
    label_file_path = os.path.join("./dataest/MNIST/", label_file_name)

    try:
        # 读取标签
        labels = read_mnist_labels(label_file_path)

        # 打印结果
        print(f"成功读取标签文件: {label_file_path}")
        print(f"标签数组形状: {labels.shape}")
        print(f"前10个标签: {labels[:10]}")
        print(f"标签数据类型: {labels.dtype}")

    except FileNotFoundError as e:
        print(f"\n错误: {e}")
        print("请确保你的MNIST数据集文件存放在正确的路径下: ./dataset/MNIST/")
        print("你可以从 http://yann.lecun.com/exdb/mnist/ 下载数据集")
    except Exception as e:
        print(f"\n读取失败: {str(e)}")