# 小测

## 第一题

在本系列讲座中，“成本”和“损失”具有不同的含义。哪一个适用于单个训练示例？

- [x] 损失
- [ ] 成本
- [ ] 损失和成本
- [ ] 既不是损失也不是成本

## 第二题

简化的损失函数

$$
\begin{equation}
loss(f_{\mathbf{w},b}(\mathbf{x}^{(i)}),y^{(i)})=\begin{cases}
-\log\left(f_{\mathbf{w},b}\left(\mathbf{x}^{(i)}\right)\right)&\text{if $y^{(i)}=1$}\\
-\log\left(1-f_{\mathbf{w},b}\left(\mathbf{x}^{(i)}\right)\right)&\text{if $y^{(i)}=0$}
\end{cases}
\end{equation}
$$

$$loss(f_{\mathbf{w},b}(\mathbf{x}^{(i)}), y^{(i)})=(-y^{(i)}\log\left(f_{\mathbf{w},b}\left(\mathbf{x}^{(i)}\right)
\right)-\left(1-y^{(i)}\right)\log\left(1-f_{\mathbf{w},b}\left( \mathbf{x}^{(i)}\right)\right)$$

对于简化的损失函数，如果标签$y^{(i)}=0$，那么这个表达式简化为什么？

$$-\log\left(1-f_{\mathbf{w},b}\left(\mathbf{x}^{(i)}\right)\right)$$