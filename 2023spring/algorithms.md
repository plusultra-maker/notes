# 算分
## Tips in General
- 设计算法，要有描述，有核心的模型与思路，边界条件（初末），记得给出复杂度
- 

## 数学基础
- 函数渐进界
  - 一堆符号和意义
    - 主要就是不高于O，等于$\Theta$
  - 判断表达式的阶数和排序
    - >$log(n!)=nlog(n)$ stirling公式
    - 指数大于任何级别的多项式大于任何的logn多项式
  - 求和方法
    - 求和公式
    - 积分近似：1/k求和约等于ln(n)
- 递推方程求解
  - 主定理
    - 条件：a>=1,b>1
      - 第一类：f(n)较小，低于$n^{log_ba-\epsilon}$,则递归项为主，$T(n)=\Theta n^{log_ba}$,注意这里函数的阶数是紧的
      - 第二类：恰好完全同阶，则T还需再乘logn
      - 第三：f(n)较大，高于+\epsilon阶，且f满足$af(n/b) \leq  cf(n)$,大概表现了f倾向于规模递增，因此可以放缩，得到T与f同阶
    - 分类，注意f(n)中的logn系数可能导致无法被分类，必须手动递归树求解
    - 注意第三类（f(n)占大头），有附加条件$af(n/b)\leq cf(n)$

  - 递归树
    - 主定理用不了，就递归树展开：
    - 树的部分是递归，展开到边界为叶子，附加项列一旁，每行对应不同的总附加值，附加项相加得到总值
    - 转换为附加项求和问题，求和总数可以放大到最深层数，按规律求和
  - 迭代归纳
    - 直接代入，展开，找到展开式的规律

## 分治
1. 基本思路
   - 分开为数个子问题，子问题与原问题自相似，分别求解并归并的递归实现
   - 给出子问题的终结情况；给出结合的方法；从而写出复杂度的递归式
2. 分治的优化
   - 通过复用子问题的结论，减少需要求解的子问题个数or规模，从而减少分支数
   - 预处理，将归并需要的复杂度尽量移除递归过程，从而减少不断迭代的归并项，降低总复杂度
3. 分治的应用
   - 二分搜索
     - 要求：有界性（有界可分），单调性（可以验证是否符合条件，且一次性排除一半（一部分）不可能的情况）
     - logn
   - 二分归并排序
     - 合并需要线性时间
     - nlogn
   - 芯片测试
     - 通过一种方案无损的降低问题空间，每个操作最多一次，O(n)
   - 矩阵乘法
     - 典型的减少子问题个数
   - 最近邻
     - 分子问题，设计代价小的结合方式
   - 快排
     - 最坏O(n^2),平均O(nlogn)
   - Select(第k小)
     - 算法的基本思想是选择一个基准元素，将数组中所有小于基准元素的元素放在左边，大于等于基准元素的元素放在右边。此时，如果基准元素的下标刚好是k-1，则基准元素就是第k小的元素；否则，我们就在左半部分或右半部分中递归地执行同样的操作，直到找到第k小的元素。
     - 平均意义下，线性复杂度
4. Tips:
   - 
## DP（参考cs170）
- 基本思路
   - 通常为优化问题,要求满足优化原则，即最优决策的子序列也是子问题的最优决策
   - 要求：优化性质当问题可以被分解为子问题，且子问题可以
- To start with:Shortest paths in dags(directed acyclic graphs )
   - 在这种无环的图中，我们可以写为拓扑排序，线性的，只有向右的路径
     - which means 如果我们有了某个点v的所有左边点的$dist(u)$，我们可以很简单的求出$dist(v)$
     > $$dist(v) = min_{(u,v)∈E}{dist(u) + l(u, v)}$$
   - 所以只要我们有了这些子问题的解，就可以轻易的得到distv的解，这些问题嵌套着
   - 只要从小的从最开始的$dist(s)=0$开始解，则一步步就可以累积的把所有问题求完（有点像分治，但这里没有分这一步，结构是自然的，我们只需要逐步治而合
   - 在更普遍的问题里，dags is implicit，我们必须找到子问题与总问题的联系，并且将子问题递归到最简单的问题去：
      > Its nodes are the subproblems we define, and its edges are the dependencies between the subproblems:
- An example: Longest increasing subsequences
   - 最大的递增子序列，同样显示了有向性（无环），如果一个解子序列是最大的，那也就意味着以其倒数第二个点为终点的序列也是局部最大的，因此仍可以把大问题拆成一系列子问题的解的竞争，从而递归。
   - To myself:注意，子问题的解是局部最大的，不代表一定会选择这个子问题，例如：
      ```
         1，2，3，5，8，6，7
      ```
      这其中12358是局部最大的，12356也是，但因为最后是7，所有12358不构成7的子问题，因此不会被选中，这说明子问题的解是子问题的事情，只需要在子问题下是最值，而不需要考虑和其邻居的关系（不需要考虑为什么要选这个点为子问题）；而权衡如何从众多子问题中，选出并计算总问题的解，这是那个递归方程需要处理的问题。
   - Recursion? No, thanks.(unread)
     - 递推方程的建立不一定指向递归算法，因为递归会导致重复的计算相同的子问题，因为子问题是后出现的，所以很难复用
     - 使用从前至后的遍历，以表格形式存储函数的值
- Edit distance
   - Greedy algorithms build up a solution piece by piece, always choosing the next piece that offers the most obvious and immediate benefit.
   - And prove that's right by induction.
   - Mini

- Knapsack

- 0-1背包问题
  - 

- Tips
  - 先做离散的分割，使得最优解具有递推的性质
    - 有时不是一个显性的值的最优化问题，可能是可行性问题，但我们可以通过设计F={0,1}的递归函数来转化为最优化问题（有1则1）
  - 要有初始边界条件(i=1),和结束界限
  - 构建目标函数注意，有时候有两个变量有时候有一个，但变量一定是离散的，有限多个，才能建立函数值表储存结果
  - 注意计算的过程是否可以优化
  - 有时候DP复杂度是有两个参数（分别代表迭代项和某种属性项）决定的，因此表达式应该包含两个参数

## Greedy
- 思路：
  - 以某种规则，正向的选择第一步的最优方案；
  - 完成第一步选择后，问题转换为相似的问题，再次重复上一步；直到完成所有选择。
  - 一定要保证每步的最优方案（即对应的决策规律）唯一的指向全局的最优情况
- 应用
  - 最小生成树
    - prim 不断囊括
    - Krus 取全局最短边
  - 最短路径
    - Dijkstra 搜索
- Tips
  - 比较明显的问题，用数学归纳法证明
  - 每当解答出于直觉，或对小范围成立时（补充题1），如果不方便直接进行递推和归纳，那考虑使用交换论证
     - 注意交换论证中，一定要证明解空间的所有解都可以通过这一交换方案转化为贪心方案，且转化过程优化结果
  - 通过预处理，降低每次贪心选择的复杂度 
  - 对任何问题都应该优先考虑贪心，直到发现其不具有贪心的性质（矛盾）
## backtracking
- 思路
  - 家里决策空间，通常可以是一个向量；根据一些遍历策略进行树搜索
  - 建立一个分支界限，进行剪枝，如果还有最大化要求，引入代价函数
    - 要求有后效性，即已确定的变量违反了规则即可剪枝，后面的任何选择都救不回来
    - 代价函数应为子树中所有可能解对应的目标函数值的上界（因此向下搜索代价函数总不会增大，满足后效性）
    - 可存储界函数，存储当前搜索到的最大目标值，如果搜到的代价函数已经小于界函数，则可以剪枝
- Tips:
  - 回溯与DP: DP通常是基于两个变量的一个表，而回溯是基于向量的一个树，因此 他们的复杂度是基于不同维度的，回溯只与迭代数有关，而DP还与属性有关
  - 回溯对应的解空间很大，且没有太多逻辑，因此最坏复杂度很高

## linear programming
- 模型的一般形式
  - 目标函数和目标方向
  - 约束条件：线性不等式
  - 非负条件
  - 自由变量 无所谓非负
  - 可行解，可行域；最优解，最优值
- 标准形
  - 目标为min
  - 约束全部为等式，非线性项大于0
  - 所有变量要求非负
- 化为标准型
  - max -> min
  - 把b_i<0的式子两边变号，使得所有约束都有b_i>=0
  - 引入非负的松弛（剩余）变量，把不等式变为等式
  - 把自由变量$x_j->x_j^{'}-x_j^{''}$，后两者大于零
  - 这样就得到了可能有更多变量参与的标准形，接下来只需要研究标准形的性质即可
  - 实际上全是等式也给我们提供了用矩阵表示的便利性
- 标准形的可行解
  - 找到系数矩阵A$(r_A=m)$的m个线性无关向量，构成一组基B，则对应的变量为基变量
  - 令非基变量全为0，则基变量必然有唯一解$x_B=B^-1b$，称为基本解；
  - 检验如果基本解满足非负约束，则为基本可行解，对应的基为可行基
- 基本解的性质定理：
  - 有可行解，必有基本可行解（即必然可以通过满足约束的变化使得一些变量为0，这是线性方程组的性质）
  - 有最优解，必存在一个基本可行解是最优解（实际上即将“优化目标函数为最优”写为一个新的约束方程，则新的方程组有可行解，则必有满足最优条件的基本可行解）
- 单纯形法：
  - 基本思路：从一个可行解移动到一个具有更好目标函数值的相邻可行解（其实这是几乎所有最优化算法的基础）
    - 每个标准形的一组基选择对应着唯一的解，如果解可行，则对应着唯一的可行值，只要找到符合最优条件的可行值或证明没有满足最优条件的可行值，那就完全的解决了此问题（由定理2）
    - 因此此法把一个多维度的连续性问题转换为了一个组合数范围的离散问题，从而易于求解
    - 接下来的问题是：什么是最优条件；更简单的说，什么样的基变量变化可以降低目标函数值
  - 最优性检验：
    - 通过矩阵推导，可以在任意个给定的可行基B以及对应目标值z_0的基础上,得到:
      $$
      \begin{aligned}
      z=&c^Tx \\
      =&z_0+(c^T-c_{B}^T B^{-1} A)x \\
      从而记 \ 
      \lambda^T=&c^T-c_{B}^T B^{-1} A \ 为检验数 \\
      z=& z_0+\lambda^Tx \\
      \end{aligned}
      $$
    - 这样可以检验其他解（尤其是相邻解）相对此解是否更优（值更小）
    - 对于检验数，由于当x为对应B的变量取值时，所有非基变量都为0，而基变量都>0；
    - 同时将基变量项拆解可知，基变量对应的检验数必为0，因此x不变时，该差值自然为0
    - 这条性质告诉我们，原来的基变量如何取值不影响此差值，故只要我让一个检验数<0的非基变量变为非0，则目标值必然减小，这一推论告诉我们两件事：
      1. 检验数全部大于0，则原x是最优解
      2. 如果存在一个变量的检验数小于0，且$B^{-1} A$对应该值的列向量所有值都<=0，那么让此变量变得任意大于0，基变量组都仍有可行解，且差值可以任意减至负无穷，可以任意说明不存在最优解。
  - 替换策略：
    - 则如果存在检验值小于0且不满足上述2的非基变量，选取其中检验数绝对值最大的，选择任意基变量与之替换
    - 但为了保证替换后的基变量组仍有可行解，需要$B'^{-1}$的基变量系数大于0，则选取选定非基变量下，所有当前系数矩阵>0的项中 与非线性项比值最小的即可
    - 同时还可能写出检验数的变换，第j个变量的检验数$\lambda_j$的变化量为$-\lambda_k \alpha_{lj}/\alpha_{lk}$,即得到新的检验数；
      - 由于前面的条件，$\lambda_k<0$,以及$alpha_{lk}>0$,因此只需要考虑那些$\alpha_{lj}<0$或原$\lambda_j<0$的项，他们的检验数可能变化之后仍是负的
  - 单纯形表：注意化为标准型的min情况再来列表，$\lambda$的计算可以传递
- 对偶性
  - 有一个原始的max线性规划，则存在一个对偶的min线性规划，其形式是系数矩阵做转置，非线性项向量与目标函数系数向量互换，约束变为大于等于，并添加合适的变量数量
  - 如果给出的原规划存在大于等于或等于约束，则通过拆分和变号，全部转为原始形式，再做对偶，完成之后再化简
    - 可以推出一个对偶规划的一般形式，值得注意的是对偶后变量为任意的数量对应着对偶前的等式数量，对偶后的等式数量对应原规划中取值为任意的变量的数量；这两种东西都出现在靠后的序号
  - 对偶的性质：
    1. 原始规划的值总是小于对偶规划的值，证明即矩阵的结合律
    2. 当两值相等时，两不等式均取等，均达到最优解
    3. 一规划存在最优解，则两规划都有最优解，且最优值相等（即1的推论）
- 整数规划
  - 特点：要求一些特定的变量只能是整数取值
  - 分支限界：
    - 首先先去掉所有整数要求，求出最优解
    - 如果恰好满足整数要求，则结束
    - 否则选出某个不满足整数要求的变量最优解a，分支为加入小于a的下取整的规划，和大于a的上取整的规划，分别求解
    - 从而实现分支搜索，直到搜索到所有最优解满足整数要求的规划，比较这些叶子的最优值得到根的最优值
    - 优化：可以维护一个当前最优值的界，当子树的搜索已经必然劣于当前最优值了，则不必再搜下去了
  - 这样的方式可以将整数的取值搜索问题，简化为只发生在边界可行解上的线性规划解法，这样在近似意义上可以减少搜索空间
  

## Amortized Analysis
- 概念
  - 平摊分析不同于传统的最坏情况或平均情况分析，因为它考虑了一组操作的总体代价，而不仅仅是单个操作的代价。
- 聚集分析
  - 由于算法总是在一个客体上连续的运行，而一系列的操作前后之间是有联系和限制的，因而一组操作的总代价不是简单的单个操作的倍数，我们需要考虑操作间的联系
  - 在一些情形中，即使任何一步操作最差情况下都可以有很高的代价，但由于一些限制这些最坏操作发生的次数一定很小，那么它们的代价可以被平摊到其他操作上
  - 而这些时候，通常我们很难求出每一步出现多高代价的概率分布，但我们知道总体我们至多要完成哪些操作，所以总运行时间有一个紧的上界，从而求平均得到平摊时间
    - 这不是一种概率意义上的平均，而是一种分摊意义上的平均
    - 聚集分析不在乎具体的操作（通常跑完一个算法可能会用到好几种操作），只在乎总体的代价与总体的次数
- 记账法
  - 我们为不同的操作赋予一些假设代价，可能高于或低于实际代价。
  - 如果高于实际代价，就把差值当作存款存起来，可以存放到被操作的数据结构中的某些对象上
  - 这样当其他操作再次操作这些对象时，如果我们分配的代价不能满足它们的实际代价，那就利用对象上存的钱去填补这个空缺；而如果存放的机制设计的好，那可以得到某种不变性，保证总能找到存款去补偿
  - 如果所有操作都进行完毕我们总是能保证不欠钱，那就是一个正确的假设，而总假设的代价就是总真实代价的上界
    - 如果不能，则需要重新考虑假设代价与分配机制
- 势能法
  - 把记账法的思路抽象化一些，更朴实的存款策略是以一个数据结构的状态的函数去标注，称为势函数
  - 我们定义每一步的平摊代价是真实代价加势函数的增加值，类似物理中的输入的能量等于损耗加势能变化
  - $$a_i=c_i+\Phi(D_i)-\Phi(D_{i-1})$$
  - 这样 只要势函数满足末态势能高于初态，则说明平摊代价是合理的，其和是真实代价的和的上界
  - 总结：记账法和势能法都是类似的主动获得单个操作的平摊代价，而通常这些代价是常数阶的，这就说明总代价也只是总操作次数阶的，这就是平摊分析的价值，通过平摊而避免被罕见的大代价操作影响总代价估计，得到更合理的上界
- 实例：动态表
- Tips：
  - 势能函数法通常是最直接的方法，势能函数的构造往往也对应着数据结构与操作逻辑的某种性质，形式上与构造记账法的分摊存款是类似的，包括当操作逻辑本身带有数值的性质，可以很好的融合到势能函数中；但由于不用考虑过多的细节，只需计算差值，是比记账法更简洁的
  - 因此构造势能函数要考虑数据结构的结构特性与操作逻辑的特点（尤其是那些代价可能很大的操作）

## 网络流
### 最大流
- 问题的起源： Shipping oil
  - 表现流的运输网络：
    - 有向
    - 承载能力有上限
    - 不能存储，要满足流的连续性原理
    - >注意这与物理意义上的流不同，水流等的流量是速度和截面的函数，但我们这里相当于规定了速度为1，故不总能满足截面的上界
- 最大流
  - 基本假设：
    - $G=(V,E)\, s,t\in V c_e>0$ （不妨假设s只出，t只进，便于后面讨论）
    - 对所有边e:$0\leq f_e \leq c_e$
    - 对于所有非s,t的点u:$$\sum_{(w,u)\in E}f_wu=\sum_{(u,z)\in E}f_uz $$ flow is conserved
    - 定义 $size(f)=\sum_{(s,u)\in E}f_su$
  - 综上假设，可以看出线性约束+线性目标函数——线性规划问题
  - 因此我们可以很简单的用单纯形法求解
- 能更进一步吗？
  - 思考单纯形法的本质
    - 在约束规定的区域内，在边界上跑（改变变量的值），且要求变化之后的目标函数值增大，直到找到使目标函数最大的位置
  - 所以实际上单纯形法在最大流中的操作
    - 从无流开始
    - 重复的寻找$s\rightarrow t\:$的通路(how?)，并在其上加上最大可能的flow，作为一次优化
  - 每次添加新的$s\rightarrow t\:$通路 需要满足什么要求呢
    - 目前全图已经有了一个flow的分配：$f_{uv}$，可以维护一个$G^f=(V,E^f)$来储存
    - 对于找到的通路的每个边$u\rightarrow v\:$，如果符合有向，则最多能添加$c_{uv}-f_{uv}$的flow
    - 而如果与本来的有向相反，则可以用来抵消一部分原来的flow，故给出最多$f_{vu}$的flow
    - figure7.5
    - 以此规律，我们得到了一个每条边有确定上限的通路，则显然添加的最大flow为最小的边上限
    - 添加flow后，要更新$G^f$，从而迭代的寻找下一个优化
    - 图
- 最优化条件？（A certificate of optimality）
  - 为什么我们认为我们算法的终止即是最优解
  - 单纯形法的终止：
    - 在当下，我们再也找不到任何一种变换使得目标函数更优
    - 其来源是约束方程与目标函数的关系
  - 观察网络流的直观上限
    - 对于任何将s,t分开的分割L和R，跨越分割的$R\rightarrow L\:$的线的总和的最大流的上界（但不总是紧的）,记为$capacity(L,R)$
    - 图
  - 何时是紧的上界
    - 算法终止————无$s\rightarrow t\:$通路————从s能走到的点中没有t
    - 因此可以以此来做一个分割，所有从s能走到的点为L，其余的点为R
    - 故，任何从L到R的边都是满的，任何从R到L的边都是0
    - 图
    - 故，此时有$size(f)=capacity(L,R)$
      - 此上界即为紧的上界，此解即为最优解
    - 有定理：
      - 最小的分割上界即为最大流的最大值
      - >Max-flow min-cut theorem The size of the maximum flow in a network equals the capacity of the smallest (s,t)-cut.
    - 例题（18年期末）：
      - >如果 f 是最大流，那么不存在关于 f 的 s-t 增广链。（√）
- 算法效率
  - 简单分析
    - 每次搜索到一个通路：$O(\left|E\right|)$
    - 总共的迭代次数：
      - 假设边都是整数的承载量，且最大值为C，则最大流的上界总是小于$C\left|E\right|$
      - 且每次找到新通路我们至少增添了1的总流量
    - 因此总复杂度在$O(C{\left|E\right|}^{2})$
  - 这是紧的吗
    - C可能很大，边值可能都很大，如果能一次添加很大的流量，则迭代次数可以降低
  - 通路的搜索策略
    - 看一个例子
    - 图
    - 我们尽量寻找可能的最大流量来作为迭代——贪心
      1. 用Dijkstra的变式算法来解出，图中具有最大流量的通路
      2. 最大流的最大值总是小于图中最多$\left|E\right|$条边的和
      3. 以每次都取最大流量的通路来迭代，迭代次数的上限为$O(\left|E\right|logF)$,$F$是最大流的结果
    - 证明：每次贪心至少可以减少$\frac{F_{last}}{\left|E\right|}$
      - 因此$F_t\leq F(1-\frac{1}{E})^t<F(e^{-1/k})^t=Fe^{-t/k}$
- Dinic算法
  - 更快

### 最小费用流

### 最大流算法的应用
- 带需求的流通
  - 将最大流问题扩展为多个起点(S)和终点(T)，每个点都固定的需求$d_v$（需求为负则构成供给）
    - 问：是否存在可行流通
  - 问题的特性：
    - 流不凭空出现，不凭空消失：总需求的代数和为0：$$\sum_{v\in T}d_v=\sum_{v\in S}-d_v$$
    - 因此可以可以想象为流从一个地方s\*发给S，再从T汇集到一个地方t\*，且每条对应线路的上限为$|d_v|$，只要供满即满足需求
  - 解决：
    - 如上所述，添加超节点s\*,t\*,并按要求连接所有收发点，构成G'的最大流问题
    - 可以有引理：G中存在一个带需求${d_v}$的可行流通，当且仅当G'的最大流为D
    - 图1
- 运输问题 (Hitchcock问题)
  - 将最小费用流问题扩展为多个起点(S)和终点(T)，每个点都固定的供给$a_i$或需求$b_i$，如何安排使得总运费最小
  - 与“带需求的流通”问题高度相似，其关系就如同传统的最大流与最小费用流问题的关系
  - 解决：
    - 添加超节点s\*,t\*,并按每条对应补充线路的容量上限为$a_i或b_i$，费用为0
    - 记$v_0=\sum_i a_i=\sum_j bj$，则所有补充线路全满等价于总流量$v_0$，构成G'的满足流量$v_0$问题
    - 图2
- 二部图的最大匹配
  - 对于给定的二部图G=<A,B,E>，M是其边集的子集，如果M中任意两条边都不相邻，则M为G的一个匹配
    - 通俗的看，即M的选择表示了A B之间的一个单射，每个点只能匹配一个点
    - 问：尽可能多的匹配
  - 增广交错路径
    - 边：匹配即是否属于M；点：饱和即是否已被匹配
    - G 中由匹配边和非匹配边交替构成的路径称为交错路径
    - 起点和终点都是非饱和点的交错路径称为增广交错路径
  - 增广交错路径的特性
    - 起终点异侧，共2m个点：__1,2,...,2m-1,2m__
    - 起终边都是非匹配边,故匹配关系为：__1,(2,3),(4,5),...,(2m-2,2m-1),2m__，共$m-1$对
    - 因此必然可以将此路径上的边和匹配关系改为：__(1,2),(3,4),...,(2m-1,2m)__，共$m$对，使得匹配数增加
    - 图3
    - >引理12设 M 是二部图 G 的一个匹配, P是一条关于M 的增广交错路径, 则$M' = M \oplus E(P)$是一个匹配 且 |M' | = |M| + 1. 
    - >定理8 二部图的匹配是最大匹配当且仅当不存在关于它的增广交错路径
  - 匈牙利算法
    - 从一个初始匹配 M 开始, 每次找一条增广交错路径 P, 令 $M' \leftarrow M \oplus E(P)$, 直到不存在增广交错路径为止. 
    - 复杂度：每次搜索$O(|E|)$,总迭代次数即最大匹配数
  - 与最大流的关系
    - 类比“带需求的流通”，同属于多起点多终点问题，可以添加超起点和超终点，并将所有边的容量设为1（只能通过0或1），_A与B间的边全部为A到B的单向边_
    - 则最大匹配即最大流量
    - 可以看出，一条增广交错路径即一个s-t增广链
    - 因此匈牙利算法即FF算法
- 赋权二部图的匹配
  - 指派问题：完全二部图，给定匹配的权值，求权和最小的匹配
  - 期中考试题目4
  - Kuhn-Munkres Algorithm也即匈牙利算法
    - [KM算法 oi-wiki](https://oi-wiki.org/graph/graph-matching/bigraph-weight-match/#hungarian-algorithmkuhn-munkres-algorithm)
  - 本质上，这种算法与教科书上基于原始-对偶的线性规划算法是一样的
  - 转化为费用流模型
- 图像分割
  - 目标：将一个问题的前景背景分离
  - 图4
  - 最优标记
  - 这个问题从形式上看就很像最小割
    - 想把一部分像素分给前景，一部分像素分给后景，尽量符合事实并且尽量少的分割
    - 也就是在像素间做一个最小割，切断尽可能小的可能性，使得每个元素待在更属于自己的景区里
    - 图5
  - 数学语言：
    - 最大化：$q(A,B)=\sum_{i\in A}a_i+\sum_{j\in B}b_j- \sum_{i,j不同区}p_{ij}$
    - 等价于最小化:$q'(A,B)=\sum_{i\in B}a_i+\sum_{j\in A}b_j+ \sum_{i,j不同区}p_{ij}$
    - 等价于一个最小割问题
    - 
### 一些算法的复杂度结论
- 最大流：
  - FF算法：最朴素的选择规律下，复杂度低于mC步，m是边数，C是所有百年的容量和
  - Dinic算法：构造分层辅助网络AN（辅助网络就是根据现有流修正的可流网络，分层就是按度分成数层，只保留层间网络），不断的求AN的最大流并迭代更新辅助网络，复杂度为n^3
- 最小费用流
  - 辅助网络类似最大流，但注意反向流过的时候是减去费用，故边权取负
  - 最小费用流等价于辅助网络不存在负费用圈
  - 如果已知流量v的最小费用流，则此时辅助网络中的最短路径上加u流量，就得到了u+v的最小费用流
  - Floyd算法：检测负回路是否存在，使用DP，其原理是递推的计算i到j中间经过定点号码不大于k的最短路径，如果存在负回路，那么最短路径会在包含其时缩短，使得d(i,i)<0，复杂度为n^3
  - 因此最小费用流有两种思路：
    - 基于负回路存在性
    - 基于最短路径可加
- 二部图匹配
  - 找最大匹配：匈牙利算法：每次找一条增广交错路径，复杂度为$O(n^3)$
- key
  - 学会如何分配权值构建图满足题意，增添起终点得到基本的最大流或最小费用流

## 问题的复杂度
- 针对问题的复杂度的下界
- 方法：
  - 首先大于问题的读取
  - 对于类似排序的多分支问题，可以考虑决策树，每次计算至多分一次支，那么决策树的深度就是问题的复杂度的下界
  - 通过对输出至少需要的信息量进行分析，对于任意算法给出一种最坏构造，使其至少经历n步才能达到需要的信息量，否则结果不能保证正确。那么n就是问题的复杂度的下界
  - 通过归约为其他问题
- 一些结论
  - 排序问题的下界是nlogn，归并和堆都是最优的，快排平均时间最优
  - 找最大值问题的下界是n-1
  - 找最大最小是3n/2-2 ，通过信息证明
  - 找第二大是锦标赛，n+logn-2
  - select问题的下届

## NP完全性
- P类和NP类：
  - P类：多项式时间内可解决的判定问题
  - NP类：多项式时间内可验证的判定问题
    - 多项式时间验证：存在一个多项式时间算法，给定任何一个真实例，总存在一个猜想t（譬如一个可以证明问题为真的解，需要看问题的具体形式），可以在多项式时间内验证t的存在作为证据，能够说明实例为真（反之亦然）
    - 通俗的说，就是当别人给出判定问题的一种解释，可以在多项式时间内验证这个解释的正确性
  - 注意：这些一定是判定问题，即只有yes和no两种答案
    - 如何是一个组合优化问题，那么就需要用一个界值来转换成判定问题
  - P类是NP类的子集
- 归约
  - 注意我们仍是讨论判定问题，用多项式时间变换更好理解   
  - 有两个判定问题p1和p2，如果p1的每个实例可以在多项式时间内变换到一个p2的实例，且p1的实例为真当且仅当p2的实例为真，则称p1归约到p2，记为p1≤p2
    - 通俗的说，就是所有p1问题都可以被转换为p2问题，因此只要存在p2问题的算法，就可以解决p1问题：说明p2问题难于p1问题
- NP-Complete
  - 如果对于所有NP问题p 都可以归约到一个问题p2，则p2难于所有NP问题，p2为NP-hard问题
  - 如果一个NP-hard问题p2属于NP类，则p2为NP-complete问题
    - 换句话说，NP类中最难的问题就是NP-complete问题
  - 如果想证明一个问题p2为NP-complete，只需要证明：
    - p2属于NP类
    - 任何一个NP问题p1都可以归约到p2；但这个证明往往比较困难
      - 因此通常通过证明某个已知的NP-complete问题p3可以归约到p2，从而证明p2为NP-complete
  - 以上分类也说明，如果证明了任何一个NP-hard的问题是属于P类的，那么就有P=NP
- 一些经典可用的NPC问题：主要了解其描述，来帮助我们判断如何归约到其他问题
  - SAT问题：给定一个布尔表达式（合取式，子句间是交），是否存在一组布尔变量的赋值，使得表达式为真
    - 3-SAT问题：SAT问题的一个特例，表达式中每个子句最多有3个变量
  - 顶点覆盖问题（VC）：给定一个图G和一个整数k，是否存在一个顶点集合，使得这个集合中的顶点数不超过k，且图中每条边都至少有一个端点在这个集合中
    - 注意这个问题是判定问题，有一个整数k参与，而不是优化问题，这样才能归约到其他问题
    - 在归约的过程中，我们也要通过k来把这个问题转化为其他问题的判定问题
  - 团：图G的一个团是一个完全子图，即子图中的任意两个顶点都有一条边相连
    - 最大团问题：给定一个图G和一个整数k，是否存在一个团，使得这个团中的顶点数不少于k
  - 独立集：图G的一个独立集是一个顶点集合，使得这个集合中的顶点数不超过k，且图中任意两个顶点都不相连
    - 最大独立集问题：给定一个图G和一个整数k，是否存在一个独立集，使得这个独立集中的顶点数不少于k
      - 也就是说，最大独立集问题是最大团问题的补问题
  - 哈密顿回路HC：给定一个图G，是否存在一个简单回路，使得这个回路经过图中的每个顶点一次且仅一次
    - 有向图的哈密顿回路：给定一个有向图G，是否存在一个简单回路，使得这个回路经过图中的每个顶点一次且仅一次
  - VC——独立集——团，比较容易归约
  - 有向HC-HC容易归约
  - 货郎问题（TSP）：给定一个图G和一个整数k，是否存在一个简单回路，使得这个回路经过图中的每个顶点一次且仅一次，且回路的长度不超过k
    - 通常货郎问题的图很容易找到很多哈密顿回路，问题在于如何找到尽量短的
    - 注意图中的边可以有权重，因此回路的长度是指回路中所有边的权重之和
    - 满足三角不等式的TSP问题是指其所有边的权重满足三角不等式
  - 恰好覆盖：给定一个集合X和一个集合F，其中F是X的一些子集组成的集合，再给定一个正整数K，证明是否存在一个F的子集C，使得这个集合中的元素数恰好为K，元素间交为空，且这个集合的并集等于X
    - 即F中存在X的恰好覆盖
  - 子集和问题：给定一个整数集合X和一个整数k，证明是否存在一个X的子集C，使得这个集合中的元素数恰好为K，且这个集合的并集等于X
  - 0-1背包问题：即判定是否存在放法达到目标值V
  - 双机调度问题：假设有一组任务，每个任务需要在两台机器上进行处理。每个任务在每台机器上的处理时间是已知的。问题的目标是确定一个任务调度方案，将任务分配给机器，并安排它们的执行顺序，使得所有任务完成所需的总时间最小化。判定问题就给一个整数的界。

## 近似算法
- 近似算法：对于一个优化问题，如果存在一个多项式时间算法，可以在多项式时间内找到一个解，使得这个解的值不超过最优解的值的数倍，则称这个算法为近似算法
  - 对于一个实例：最优解的值为opt与近似算法的解值之比为近似比r，r总是大于等于1，近似算法越好
  - 如果对于所有实例都有ri< r_0,且r_0为常数，则称这个近似算法为r_0-近似算法
  - 分类：
    - 完全可近似问题：对于任何小的e>0 存在其近似比为1+e的近似算法
      - 背包问题
    - 可近似：存在常数比例的近似算法
      - VC，多机调度
    - 不可近似：不存在常数比例的近似算法
      - TSP
- 分析近似比的方法
  - 估计最优解的值，或尝试推导最优解和近似解之间的关系
  - 构造紧实例，证明给出的近似比是紧的
    - 构造实例的方法，有时可以从其近似比的推导中看出，近似比的主要缺陷在哪
- VC
  - MVC算法：添加新边的两端点并删所有已达边 2-近似算法
- 多机调度
  - 即把A分为m个不交的子集，使得max子集内和 最小
  - G-MPS贪心算法，按输入的顺序分配，每次都分配给当前负载最小的
    - 可以看出与输入的顺序很相关
    - 其近似比小于 2-1/m
  - 改进的贪心：
    - 预处理，先按处理时间从大到小排列任务，从头再进行贪心分配（即优先分配大宗）
    - 近似比 3/2-1/2m
- (满足三角不等式的)TSP
  - 满足三角不等式，说明对于货郎来说：他只以想到达某邻城市为目的的话，他一定会选直接去，而不会绕路
  - 最临近法NN:
    - 每次贪心的选择没有到过的最近的城市，直到走完所有城市
    - 其问题很明显在于，有可能走到某一个城市发现，下一步离得近的城市都被走过了，所以必须走一条远的路；算法存在一定的随机性，会导致进行没有规划的反复横跳
    - 其近似比小于 1/2(log2(n)+1)，不是常数近似比
  - 最小生成树MST：
    - 首先求图的最小生成树，再做一次DFS得到树上的欧拉回路，接着选一个点为起点，沿着欧拉回路走，遇到已走过的顶点就跳过，直接走到下一个没走过的点
    - 近似比为2：因为HC本身删去一条边就是一个生成树，而因而最小生成树的边总长总是小于OPT，而我们得到的路径又是不长于2倍的小生成树的边总长
  - 最小权匹配MM：对MST的进一步优化
    - 首先求图的最小生成树T，找到其中奇数度的节点，得到其生成子图H，找到生成子图的最小完美匹配M，则把M加入T后，则该图一定是一个欧拉图，则同MST，在欧拉图上按欧拉回路走并跳过，得到一个哈密顿回路
    - MM的近似比为3/2 : 于MST不同的是，这次在T中的所有边至多被走一次（因为所有dfs回溯的过程都可以被子图的完美匹配上的某些边代替，因此这种走法的总长小于 T中边总长+完美匹配总长；而完美匹配的总长总是小于导出子图的最短HC的总长的一半的（否则不是最短），而导出子图的最短HC总长一定小于全图的最短HC，因为其中三角不等式，抄近路更短。因此总计，MM小于3/2个OPT
    - 要明确3/2是怎么来的
  - 没有约束的货郎问题是不可近似的
- 0-1背包
  - G-KK贪心：
    - 按价值密度从大到小排序，按顺序能装就装，直到遍历完成，得到总价值V；如果检查发现有没放进去的物品中，某个k的价值大于V，就把所有东西倒出来放k
    - 近似比为2：最优解的值小于总重量乘平均密度，那么假设G—KK在第一个没放进去的vl发生时，把vl填进去，其总密度一定最大，故大于最优解，而此时内部已有的物品总价值小于G-kk的最终结果，因此OPT小于G-KK+vl 也就小于2G-KK
  - 含参的多项式时间近似
    - 对于任意e>0为常数，得到常数m=1/e上取整。仍按密度排列。遍历1-m的所有t，检查所有数量为t的子集，只要其能同时放如B中，再使用G_KK
    - 可以证明其近似比为1+e 复杂度我O(n^{1/e+2}),可以认为是可控的多项式算法
  - 伪多项式时间的算法
    - 只虽然复杂度为n的多项式，但又与输入数据的值的范围有关，比如DP就是典型的与数据有关的
  - 完全多项式时间的算法
    - 使用参数e，使其达到近似比1+e,且保证时间复杂度为n和e的多项式
    - 具体的算法是基于e对所有输入数据进行缩小，再在缩小的基础上使用DP，这样可控复杂度，再将最后的解的分配回到原来的数据上，得到值
  
## 随机算法
- Las Vegas型
  - 总是能得到正确解，但是由于算法内有随机性取值，因此复杂度不确定；
    - 我们希望利用概率手段得到其复杂度的期望
  - 随机快速排序
    - 随机选一个元素作为轴，并用其将数组分为三部分，再对大于和小于两部分分别进行排序
    - 由于是分治算法，写出其期望的递归式，上界是2nlnn
  - 随机选择 选第k小
    - 在抽取元素时是随机选取的，仍是有递归性的算法，可以分析其期望复杂度的递归式，并放缩，以证明属于线性复杂度
  - n后的随机放置
    - 即一种在搜索空间中的顺序随机搜索算法，但这样的随机生成是独立的，只能期盼某次生成了好的解，太大的空间则不好用。可以和回溯等确定性算法进行结合，从而改进确定性算法的复杂度

- Monte Carlo型
  - 总是能在多项式时间内得到解，但是解不一定正确，其性能指数是结果的正确率
    - 出错概率小于1/3是有效的MC
  - 主元素测试
    - 随机找一个元素，是主元素就是，不是就输出没有
    - 正是因为主元素的特殊性，使得回答正确率大于1/2
    - 当然如果对正确率有更高的要求，可以根据要求来多测几个元素，以达到期望的正确率
  - 串相等测试
    - 把长串以某种方式生成一个短串，不断判定短串的匹配来判定长串是否相等
    - 用长串生成一个整数，mod一个大素数，把结果转化为短串来匹配
    - 优化就多次执行
  - 模式匹配
    - 就是子串匹配，输出匹配位置或输出不匹配
    - 可以使用基于串相等的随机算法
      - 不断比较X的不同位置的子串和Y是否相等，如果相等则输出，如果全不等则输出不匹配
      - 显然其错误的概率被串匹配算法的错误率决定
  - 素数测试
    - 检测2^(n-1) mod n是否等于1，是则输出素数，否则输出合数 
    - 费马小定理：所有的a不是n的整数倍，a^(n-1) mod n = 1 因此上否定一定正确

## 在线算法
- 在线算法指的是算法在执行过程中，只能看到当前的输入，不能看到未来的输入
  - 与之相对的是离线算法，离线算法可以看到所有的输入，可以根据所有的输入来进行优化
- 竞争比
  - 在线算法的性能指标，是其结果（损耗，越小越好）与离线算法结果之间，对于任意的输入顺序，在线算法的结总是小于等于离线算法的结果*竞争比+一个常数
  - 竞争比大于等于1，越小越好 