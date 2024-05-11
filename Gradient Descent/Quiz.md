# 小测

## 第一题

梯度下降法是一种算法，用于寻找能使成本函数$J$最小化的参数值$w$和$b$。

重复直到收敛：

$$
w=w-\alpha \frac{\partial J(w,b)}{\partial w} \tag{3}
$$

$$
b=b-\alpha \frac{\partial J(w,b)}{\partial b} \tag{4}
$$

当$\frac{\partial J(w,b)}{\partial w}$是一个负数（比零小），在一个更新步骤后$w$会发生什么？

- [ ] $w$保持不变
- [ ] 判断$w$会增加还是减少是不可能的
- [ ] $w$减少
- [x] $w$增加

## 第二题

对于线性回归，对于变量$b$的更新步骤是什么？

- [ ] b=b-\alpha \frac{1}{m} \sum\limits_{i = 0}^{m-1} (f_{w,b}(x^{(i)}) - y^{(i)})x^{(i)}
- [x] b=b-\alpha \frac{1}{m} \sum\limits_{i = 0}^{m-1} (f_{w,b}(x^{(i)}) - y^{(i)})