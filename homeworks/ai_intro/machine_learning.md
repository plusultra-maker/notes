---
title: "机器学习作业"
date: 2023-04-18
author: "喻勃洋"
---

# ai引论 课后练习-3 机器学习
> 喻勃洋 2000011483
## 题目一
平方损失函数
$$Loss=\frac{1}{3}\sum_{i=1}^{3} (w x_i+b-y_i)^2$$
$$
\begin{aligned}
    &\frac{\partial L}{\partial w}= 2(w\bar{x^2}+b\bar{x}-\bar{xy})=0 \\
    &\frac{\partial L}{\partial b}= 2(w\bar{x}+b-\bar{y})=0 \\
\end{aligned}
$$
代入数据：
$$
\begin{aligned}
    \Rightarrow \, w&=\frac{6}{7}   \\
    b&=\frac{4}{7}
\end{aligned}
$$
可以作图：
<img src="myplot.png" alt="My Plot" class="center">
<br>

## 题目2
### 1)
仍有正类概率为线性模型f(x)叠加sigmoid函数的映射
$$p(y=1|x;\theta)=\sigma(f(x))$$
负类则为补值：
$$p(y=0|x;\theta)=1-\sigma(f(x))=\sigma(-f(x))$$
### 2)
以题目给的方式将两者表示为同一形式
$$p(y=y_i|x)=(\sigma(f(x_i)))^{y_i}(\sigma(-f(x_i)))^{1-y_i}$$
做最大对数似然：
$$
\begin{aligned}
&\max_{w,b}\sum_{i=1}^{n}log[(\sigma(f(x_i)))^{y_i}(\sigma(-f(x_i)))^{1-y_i}] \\
=&\max_{w,b}\sum_{i=1}^{n} y_ilog[\sigma(f(x))]+(1-y_i)log[\sigma(-f(x_i))] \\
=&\max_{w,b}-\sum_{i=1}^{n} y_ilog[1+e^{-(w^Tx_i+b)}]+(1-y_i)log[1+e^{+(w^Tx_i+b)}] \\
\end{aligned}
$$
写成最小化平均损失函数的形式:
$$
\min_{w,b}\frac{1}{n}\sum_{i=1}^{n} y_ilog[1+e^{-(w^Tx_i+b)}]+(1-y_i)log[1+e^{+(w^Tx_i+b)}]
$$
  
<br>

## 题目3
### 1)
先计算属性A的熵：
$$
H(D_A)=-\frac{6}{9}\log_2\frac{6}{9}-\frac{3}{9}\log_2\frac{3}{9}=0.9183
$$
再计算属性A的增益：
D的熵：
$$
H(D)=-\frac{6}{9}\log_2\frac{6}{9}-\frac{3}{9}\log_2\frac{3}{9}=0.9183
$$
分类后的熵：
$$
H(D_A)=\frac{3}{9}(0)+\frac{6}{9}(-\frac{3}{6}\log_2\frac{3}{6}-\frac{3}{6}\log_2\frac{3}{6})=0.6667
$$
gain ratio A:
$$
g_R(D,A)=\frac{H(D)-H(D_A)}{H(D_A)}=0.274
$$

### 2)
```bash
            A=1/0
          /       \
         /         \
     C=1/0        [-1,-1,-1]
 [-1,-1,-1,1,1,1]
       /    \       
      /      \     
  B=1/0      [1] 
[-1,-1,-1,1,1]
    /   \        
   /     \     
[-1,-1]  [-1,1,1]           

```
因此 $x_*=[1,1,1]$对应标签y=-1

<br>

## 题目4
### 1)
$$
\begin{aligned}
a_i&=\frac{e^{z_i}}{\sum_k e^{z_k}}  \\
\frac{\partial L}{\partial z_i}&=\sum_j \frac{\partial L}{\partial a_j} \frac{\partial a_j}{\partial z_i} \\
if \: i\neq j:& \\
\frac{\partial a_j}{\partial z_i}&= -\frac{e^{z_j+z_i}}{(\sum_k e^{z_k})^2} \\
if \: i=j: &\\
\frac{\partial a_j}{\partial z_i}&=-\frac{(\sum_{k\neq i}e^{z_k})e^{z_i}}{(\sum_k e^{z_k})^2}\\
\\
\therefore \frac{\partial L}{\partial z_i}
&= \frac{e^{z_i}}{(\sum_k e^{z_k})^2}
(\frac{\partial L}{\partial a_i}\sum_{j\neq i} e^{z_j}-
\sum_{j\neq i} \frac{\partial L}{\partial a_j}e^{z_j}) \\
&= a_i(\frac{\partial L}{\partial a_i} \sum_{j\neq i} a_j-\sum_{j\neq i} \frac{\partial L}{\partial a_j}a_j)\\
&=a_i\sum_{j\neq i}(\frac{\partial L}{\partial a_i}-\frac{\partial L}{\partial a_j})a_j
\end{aligned}
$$

### 2)

$$
\begin{aligned}
a_i&=ln\frac{e^{z_i}}{\sum_k e^{z_k}}  \\
\frac{\partial L}{\partial z_i}&=\sum_j \frac{\partial L}{\partial a_j} \frac{\partial a_j}{\partial z_i} \\
if \: i\neq j:& \\
\frac{\partial a_j}{\partial z_i}&= -\frac{e^{z_j}}{\sum_k e^{z_k}} \\
if \: i=j: &\\
\frac{\partial a_j}{\partial z_i}&=-\frac{(\sum_{k\neq i}e^{z_k})}{\sum_k e^{z_k}}\\
\\
\therefore \frac{\partial L}{\partial z_i}
&= \frac{1}{\sum_k e^{z_k}}
(\frac{\partial L}{\partial a_i}\sum_{j\neq i} e^{z_j}-
\sum_{j\neq i} \frac{\partial L}{\partial a_j}e^{z_j}) \\
&= \frac{\partial L}{\partial a_i} \sum_{j\neq i} a_j-\sum_{j\neq i} \frac{\partial L}{\partial a_j}a_j\\
&=\sum_{j\neq i}(\frac{\partial L}{\partial a_i}-\frac{\partial L}{\partial a_j})a_j
\end{aligned}
$$