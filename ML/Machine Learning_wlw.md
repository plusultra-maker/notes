# L1 introduction
## history
- Neural Networks
  - XOR problem
  - BP&DP
- VC Theory
- PAC learning

# L2 Concentration Inequalities
- Markov Inequality
  - 一阶矩
  - $$ P(|X| \geq \epsilon) \leq \frac{E[|X|]}{\epsilon}$$
- Chebyshev Inequality
  - 二阶矩  
  - $$P(|X-\mu| \geq \epsilon) \leq \frac{Var(X)}{\epsilon^2}$$
- even better with more information
  - 更高阶矩:k次方和一次方的不等是等价的
  - $$P(|X-\mu| \geq \epsilon) \leq \frac{E[(X-\mu)^k]}{\epsilon^k}$$？
  - 如果我们知道所有阶矩的信息，我们能做什么
- Moment Generating Function
  - $$E[e^{tX}]=\sum_{k=0}^{\infty} \frac{E[X^k]}{k!}t^k$$
  - （视作关于t的函数进行展开）
- so use $E[e^{tX}]$ to describe $P(x \geq k )$
  - $$P(X \geq k) \leq \inf_{t \geq 0} \frac{E[e^{tX}]}{e^{tk}}$$ (inf means the smallest value)
  - Chernoff inequality
- Concentration Inequalities
  - from chebyshev (e.g. Benoulli)
  - $$P(|\frac{1}{n}\sum_{i=1}^n X_i - \mu| \geq \epsilon) \leq \frac{Var(X)}{n\epsilon^2}$$
  - the question is , is $\frac{1}{n}$ the best we can do?
  - C.L.T tells us that $e^{-O(X)}$ 
- somehow mentioned Entropy
  - use binary encode
  - def:
  - relative entropy(KL divergence)
    - $$D(p||q)=\sum_{x \in X} p(x)log\frac{p(x)}{q(x)}$$
    - $$D(p||q) \geq 0$$
    - $$D(p||q)=0 \iff p=q$$
- can we use chernoff inequality on benoulli?
  - $$P(|\frac{1}{n}\sum_{i=1}^n X_i - \mu| \geq \epsilon) \leq e^{-nD_{KL}(\mu+\epsilon||\mu)}$$
  - Chernoff bound
- what if we only have X's expectation, x in [0,1], ex=p
- more, many x in different ex=p_i p_i's E=p,how?

# L3 Concentration Inequalities cont.
- x in different ex=p_i p_i's E=p
  - 独立，但不同分布,不能直接写成n次方
  - $E(e^{t\Sigma(X_i)}) = \prod_{i=1}^n E(e^{tX_i})$ 由于Jensen不等式，这个值一定小于等于$E(e^{tX_i})^n$