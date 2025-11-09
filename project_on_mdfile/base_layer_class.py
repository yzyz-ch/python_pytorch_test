import numpy as np


def standardize_data(input_data):
    """
    数据标准化函数：将list/dict输入转换为标准化后的numpy数组（均值=0，方差=1）
    Args:
        input_data (list/dict): 输入数据
            - list格式：单特征时为一维列表（如[1,2,3]），多特征时为二维列表（如[[1,2],[3,4]]）
            - dict格式：key为特征名，value为该特征的所有样本（如{"height":[160,170],"weight":[50,60]}）
    Returns:
        np.ndarray: 标准化后的数组，shape=(样本数, 特征数)
    """
    # 步骤1：将输入转换为numpy数组（统一维度为2D：样本数×特征数）
    if isinstance(input_data, dict):
        # dict → 提取values并转换为2D数组（每个value是一个特征的所有样本）
        data = np.array(list(input_data.values())).T  # 转置后为 (样本数, 特征数)
    elif isinstance(input_data, list):
        # list → 转换为numpy数组，确保是2D（避免一维数组处理出错）
        data = np.array(input_data)
        if data.ndim == 1:  # 一维列表（单特征）→ 扩展为2D
            data = data.reshape(-1, 1)
    else:
        raise TypeError("输入仅支持list或dict类型")

    # 步骤2：计算均值和标准差（按特征维度计算，axis=0）
    mean = np.mean(data, axis=0, keepdims=True)  # keepdims=True保持维度一致，方便广播
    std = np.std(data, axis=0, keepdims=True)

    # 步骤3：标准化（避免标准差为0时除以0）
    std = np.where(std == 0, 1e-8, std)  # 标准差为0时替换为极小值
    standardized_data = (data - mean) / std

    return standardized_data


# ------------------- 测试代码 -------------------
if __name__ == "__main__":
    # 测试1：输入list（单特征）
    list_input1 = [1, 2, 3, 4, 5]
    result1 = standardize_data(list_input1)
    print("测试1（list单特征）：")
    print(f"原始数据：{list_input1}")
    print(f"标准化后：\n{result1.round(4)}")
    print(f"标准化后均值：{np.mean(result1).round(4)}（应接近0）")
    print(f"标准化后方差：{np.var(result1).round(4)}（应接近1）\n")

    # 测试2：输入list（多特征）
    list_input2 = [[1, 50], [2, 60], [3, 70], [4, 80]]  # 2个特征，4个样本
    result2 = standardize_data(list_input2)
    print("测试2（list多特征）：")
    print(f"原始数据：{list_input2}")
    print(f"标准化后：\n{result2.round(4)}")
    print(f"各特征均值：{np.mean(result2, axis=0).round(4)}（应接近[0,0]）")
    print(f"各特征方差：{np.var(result2, axis=0).round(4)}（应接近[1,1]）\n")

    # 测试3：输入dict（多特征）
    dict_input = {"height": [160, 170, 180, 190], "weight": [50, 60, 70, 80]}
    result3 = standardize_data(dict_input)
    print("测试3（dict多特征）：")
    print(f"原始数据：{dict_input}")
    print(f"标准化后：\n{result3.round(4)}")