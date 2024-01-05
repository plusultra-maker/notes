# L1 introduction
## history
- Neural Networks
  - XOR problem
  - BP&DP
- VC Theory
- PAC learning

# L2 Concentration Inequalities
## single random variable
- Markov Inequality
  - 一阶矩
  - $$ P(|X| \geq \epsilon) \leq \frac{E[|X|]}{\epsilon}$$
- Chebyshev Inequality
  - 二阶矩  
  - $$P(|X-\mu| \geq \epsilon) \leq \frac{Var(X)}{\epsilon^2}$$
  - 总结一下，更多的information，更好的bound
- even better with more information
  - 更高阶矩:k次方和一次方的不等是等价的
  - $$P(|X-\mu| \geq \epsilon) \leq \frac{E[(X-\mu)^k]}{\epsilon^k}$$？
  - 如果我们知道所有阶矩的信息，我们能做什么
- Moment Generating Function
  - 引入一个变量t，来描述所以阶矩的信息，并可以找出最强的bound
  - 首先 如何描述这些阶矩的信息
  - $$E[e^{tX}]=\sum_{k=0}^{\infty} \frac{E[X^k]}{k!}t^k$$
  - （视作关于t的函数进行展开）
  - 从而我们把直接用t来指出t阶矩，换为用E$e^{tX}$以及t的任意性来利用这无穷多的信息，且其形式更简单，t连续可导
- so use $E[e^{tX}]$ to describe $P(x \geq k )$
  - $$P(X \geq k) \leq \inf_{t \geq 0} \frac{E[e^{tX}]}{e^{tk}}$$ (inf means the smallest value)
  - Chernoff inequality
  - 一个相当好的bound
## Concentration Inequalities (multiple random variable)
- Concentration Inequalities
  - 我们就想知道，1000次抛硬币，正面朝上的次数是多少是可以相信的，即平均值以多快的速度收敛到期望值，这是大数定理、中心极限定理都没有回答的问题
  - from chebyshev (e.g. Benoulli)
  - $$P(|\frac{1}{n}\sum_{i=1}^n X_i - \mu| \geq \epsilon) \leq \frac{Var(X)}{n\epsilon^2}$$
  - the question is , is $\frac{1}{n}$ the best we can do?
  - C.L.T lead us to Gaussian tail probability that might tell us that $e^{-O(X)}$ is a possible better form
  - C.L.T 指出了整个分布趋近于高斯分布，利用了整个分布的信息，而chebyshev只利用了期望和方差的信息，所以我们应该学着利用更多的信息来得到更好的bound，就像上面的Chernoff inequality
- somehow mentioned Entropy (Pre-knowledge)
  - use binary encode
  - Entropy
    - $$H(X)=-\sum_{x \in X} p(x) \log_{2}{p(x)}$$
    - $$H(X) \geq 0$$
    - $$H(X)=0 \iff p(x)=1$$
    - 代表了对于一个分布是p(x)的随机变量，我们需要多少bit的编码长度来表示它
  - relative entropy(KL divergence)
    - 有两个随机变量的分布p(x)和q(x)，描述其差异，仍是bit的长度
    - $$D(p||q)=\sum_{x \in X} p(x)log\frac{p(x)}{q(x)}$$
    - $$D(p||q) \geq 0$$
    - $$D(p||q)=0 \iff p=q$$
- can we use chernoff inequality on benoulli?
  - $$P(|\frac{1}{n}\sum_{i=1}^n X_i - \mu| \geq \epsilon) \leq e^{-nD_{KL}(\mu+\epsilon||\mu)}$$
  - Chernoff bound
- what if we only have X's expectation, x in [0,1], ex=p
  - still
- more, many x in different ex=p_i p_i's E=p,how?

# L3
- more on Chernoff bound
  - independent, $x_i \in [0,1]$, $E[x_i]=p_i$, 有 $\Sigma p_i=p$
    - use Jansen's inequality, the same as Chernoff bound
  - additive Chernoff bound
    - 改写为 $$P(\frac{1}{n}\sum_{i=1}^n X_i - p \geq \epsilon) \leq e^{-nD_{KL}(p+\epsilon||p)} \leq e^{-2n \epsilon^2}$$
    - 这样与p无关，是一个广泛的性质
  - 随机变量的Concentration究竟是如何发生的，其程度与什么相关——尾部收敛速度
  - Hoeffding Ineq:
    - 对于多个随机变量，独立，其只需满足对于每个随机变量$X_i$，其取值范围在$[a_i,b_i]$之间，即可得到其平均值的Concentration Inequality
    - $$P(|\frac{1}{n}\sum_{i=1}^n X_i - \mu| \geq \epsilon) \leq e^{\frac{-2n^2\epsilon^2 }{\sum_i(b_i-a_i)^2}}$$
    - 说明只需要有界而不需要其具体分布，就可以表现出一定的concentration
- Draw with/without replacement
  - Setting:
    - Assume $a_1,a_2,...,a_N \in [0,1]$
    - Randomly draw $X_1,X_2,...,X_n$ from $a_1,a_2,...,a_N$
  - with replacement  
    - 每次draw是完全一样的，X_i是独立且同分布的Bernoulli随机变量，其p就是$a_i$中1的比例，由前述有concentration
  - without replacement
    - 直观的想，without 会使结果更加concentrated，因为每次draw都会明确使得剩下的a_i的比例朝已知的方向变化，即降低了不确定性
  - 计算：
    - 记$X_i$为第i次draw with的结果，$Y_i$为第i次draw without的结果
    - 则证明$Y_i$更加concentrated，只需证明 
    - $$对于任意t有E[e^{t\Sigma Y_i}] \leq E[e^{t\Sigma X_i}] $$ 
    - 对$t$做taylor expansion:
      $$ E[e^{t\Sigma X_i}] = 1+t*E[\Sigma X_i]+t^2*E[\Sigma_{ij} X_iX_j]+...$$
      $$ E[e^{t\Sigma Y_i}] = 1+t*E[\Sigma Y_i]+t^2*E[\Sigma_{ij} Y_iY_j]+...$$
    - 对于0阶和1阶，显然相等（不涉及相关性）
    - 对于2阶以上，如二阶，$E[\Sigma_{ij} Y_iY_j]$即$Y_i=1,Y_j=1$的概率，而由于without replacement，出现一个1后，下一个1的概率就会降低，所以$E[\Sigma_{ij} Y_iY_j] \leq E[\Sigma_{ij} X_iX_j]$，更高阶是类似的
    - 因此，$E[e^{t\Sigma Y_i}] \leq E[e^{t\Sigma X_i}]$，即without replacement更加concentrated
    - 在之后Generation中有用
