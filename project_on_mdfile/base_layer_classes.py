import numpy as np


class LinearLayer:
    """
    基础线性层类：模拟PyTorch的nn.Linear，实现 y = x @ w + b 的线性变换
    包含：权重初始化、前向计算（支持激活函数）
    """

    def __init__(self, in_features, out_features, activation=None):
        """
        初始化线性层
        Args:
            in_features (int): 输入特征数（如输入x的shape=(样本数, in_features)）
            out_features (int): 输出特征数（如输出y的shape=(样本数, out_features)）
            activation (str, optional): 激活函数，支持"relu"或None（无激活）. Defaults to None.
        """
        self.in_features = in_features
        self.out_features = out_features
        self.activation = activation  # 激活函数类型

        # 步骤1：初始化权重和偏置（遵循模型训练的常规初始化逻辑）
        # 权重w：shape=(in_features, out_features)，用正态分布初始化（均值0，方差1/√in_features，避免梯度爆炸）
        self.w = np.random.normal(loc=0.0, scale=np.sqrt(1 / in_features), size=(in_features, out_features))
        # 偏置b：shape=(1, out_features)，初始化为0
        self.b = np.zeros(shape=(1, out_features))

    def forward(self, x):
        """
        前向计算：输入x → 线性变换 → 激活函数 → 输出y
        Args:
            x (np.ndarray): 输入数据，shape=(样本数, in_features)
        Returns:
            np.ndarray: 输出数据，shape=(样本数, out_features)
        """
        # 步骤1：线性变换（矩阵乘法 + 偏置）
        linear_output = np.matmul(x, self.w) + self.b  # 等价于 x @ self.w + self.b

        # 步骤2：激活函数（可选）
        if self.activation == "relu":
            # ReLU激活：max(0, x)，缓解梯度消失
            output = np.maximum(0, linear_output)
        else:
            # 无激活函数（直接返回线性输出）
            output = linear_output

        return output


# ------------------- 测试代码 -------------------
if __name__ == "__main__":
    # 测试：创建一个输入特征数=2、输出特征数=3的线性层（带ReLU激活）
    layer = LinearLayer(in_features=2, out_features=3, activation="relu")

    # 构造输入数据（4个样本，每个样本2个特征）
    x = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
    print(f"输入数据shape：{x.shape}")
    print(f"权重w shape：{layer.w.shape}")
    print(f"偏置b shape：{layer.b.shape}\n")

    # 前向计算
    y = layer.forward(x)
    print("前向计算输出：")
    print(f"输出shape：{y.shape}（应等于(4,3)）")
    print(f"输出值：\n{y.round(4)}")
    print(f"ReLU激活后无负值：{np.all(y >= 0)}（应返回True）")