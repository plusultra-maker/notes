# Question
```
给出渐进意义下尽可能小的 Gaussian tail bound，即尽可能小的 f(t) 使得：
P(X >= t) <= f(t)
X 是服从标准正态分布的随机变量
```
# Answer
由于X服从标准正态分布，所以其期望为0，方差为1，即$E[X]=0,Var(X)=1$。
那么由chernoff inequality可知：
$$P(X \geq k) \leq \inf_{ t\geq 0} \frac{E[e^{tX}]}{e^{tk}}$$