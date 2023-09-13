# Artificial Intelligence (feat.CS-188n)

Searching
## 暴力：DFS&BFS
- 数据结构
  - 搜索是非线性的，因此需要数据结构来储存过程信息
  - DFS——到底回退——栈，BFS——顺序的同步前进——队列
- python 实现
```python
    class BFS:

```
  
## UCS(uniform cost search)
- 当解法有成本，路径有加权时，DFS和BFS找到的解的顺序是随机的，不能直接找到最优解
- 自然的想法——成本优先
  - 每次把一定成本可以到达的点全部取到，作为可能解路径的一部分，一点点增加成本范围；
  - 而如果在更高的成本达到了曾经达到过的点，则高成本的路径就不需要再考虑了，从而减少搜索次数
- 算法完毕，找到的一定是最优解
- 局限性：
  - 解是有限距离内的才可搜到（本质上是因为仍是暴力搜索）
  - 边权必须是正的，否则点的成本排序可能与搜索的顺序不同
  - 单向的，没有利用目标的信息
- 实现
  - priority queue
    - 维护“一次achievable”的点列，以其成本维持优先队列，每次纳入第一个点到已知路径集
    - 题外话，优先队列不一定是严格单调(维护需要O(n))，只需要保证首项最小——最小堆，O(logn)
- 
  ```python
  ``` 
## 有信息搜索（informed search）
- 人类看地图找路的时候，首先是既看起点，也看是不是这条路会离目标越来越远，可否借用
  - ps.但人类在迷宫上就没有地图上智慧，这是地图的性质，我们能否度量？
- 启发 heuristic
  - 用一个启发函数衡量“离目标距离”，但这个距离也需要算法计算
  - 这里我们先假设这个启发估计是已知的
- 贪心搜索
  - 仍是从起点出发，这次我们利用信息直接去我们能到达的点中距离目标最近的点，不断迭代
  - 问题：
    - 没有考虑去那个点的代价
    - 估计不一定准
    - 这样一定对吗——很可能某一步选错了（譬如某一条边权非常大，但对应的点距离目标很近，加起来仍是不划算），之后所有的选择都是这个错误的子树中，最终还需要返回重新搜；而且我们不知道搜出来的是不是最小的
- A*
  - 为了解决上面的问题，那就必须把该加起来的加起来，从而试图保证准确性和稳定性
  - 从起点出发，把每个可达点的值标记为 从起点到达这个点的累计（最小）权g+这个点的启发距离h
    - $f(n)=g(n)+h(n)$
    - 本质不是在排列点，而是在排列此刻已知路径上可选择发展的下一步中最小的
  - 仍然维持优先队列，直到目标被移除优先队列，那权值可知。想知道路径就可以记录每一个点的最小权路径的父节点，从目标反查即可
  - 特点：
    - 如果启发完全准确，理论上一定是对的（可以反证）
    - 是给盲目的UCS加上了目标点“方向”的信息，从而减少了向其他方向不必要的搜索
    - 启发估计如果不准确，那可以导致搜到的结果并不是最好的
- 可接受启发admissible：
  - 假设启发全是0，没有信息，那回到UCS，结果不会错但算法结束会更慢
  - 假设启发是大于真实距离的，而且和真实距离有出入，可能出现一个本应下一步被搜到的点，因为被赋予了较大的假距离，而停滞在了优先队列的深处
    - 导致搜索长期在迷失错误的子树，降低效率
    - 可能导致搜索在错误的子树里走到目标，得到错误的结果
    - 问：怎么保证至少结果不要错？
  - 可接受的：
    - 要求$ 0\leq h(n)\leq {h}^{*}(n) $，其中${h}^{*}(n)$是真实的代价
    - WHY？：
      - 我们需要证明，终点目标A一定被最优的路径下搜索到，在算法里体现为，A的所有最优路径前序节点一定在A之前离开队列，这样A就不会被非最优的路径搜索到
      - 反证法：假设我们以非最优的路径搜索到B点，B点下A是achievable的，则此时:$$f(b)\geq g(b) ,since: h(b)\geq 0$$则此时，$f(a)=g(a)$即为非最优路径的总代价；
      而对于A的最优路径前序节点中，进入了优先队列但还没被排出的点x（易知一定存在，即本应走的那条岔路），$$f(x)=g(x)+h(x)\leq g(x)+h^{*}(x)$$即小于最优路径的总代价，那么x应该比A先出队列；
      递归地，所有A的最优路径前序节点都会在A之前出队列，那么A一定以最优路径被搜索到
    - A*比UCS好：更多信息，有方向性
    - 问题：在图中搜索时，可能产生在搜索进行时，由于搜出了新的点，一个已经被搜到过的点的g值降低了，此时需要将其重新放入优先队列再次排出，并记录新的g值以及父节点，以得到正确的搜索顺序
      - 这会导致需要的存储空间上升，运算量一定程度上升
      - 避免这种现象，需要保证启发是一致的consistency：对任意边的两端点，其启发值差不能大于边权

## CSP问题 
- 我们此前处理的问题称为 计划问题，特点是给出某种最优的方案（存在目标函数）。下面我们讨论CSP问题，目的是给出满足约束的解（identification problem）
- CSP factors
  - 变量 一系列变量构成解
  - 定义域
  - 约束
- 问题：
  - 更多的结构，指数级的复杂度，NP-hard————化为搜索问题，并尝试降低搜索损耗
  - 抽象化为一个constraint graph，可以发现图是稀疏还是密集，是不是树形结构，这样可以针对性的开发算法
  - 如何搜索，如何减少浪费，如何尽早发现错误
## CSP解法：
- 最传统的搜索逻辑：backtracking回溯，一种基于dfs的搜索
  1. 手动确定一个搜索的顺序（本质上是把图约化为树）
  2. 对于下一个未确定的变量或需要被更改的变量，只能用 没有用过的且不与之前元素冲突的值，如果不存在，则回溯到上一层，重复。直到找到解，或回溯到根节点无可用值。
- Filtering 过滤 [Note3](https://inst.eecs.berkeley.edu/~cs188/fa22/assets/notes/cs188-fa22-note03.pdf)
  - forward checking:通过一些机制来提前缩小未分配变量的定义域，从而减少分支数（即不去试错而直接剔除）
  - arc consistency:
    - 想法是当在一个给定的条件发生时（例如出现了新的变量赋值），此时可以直接通过图和约束检查那些待分配的变量（forward）,如果出现了必然导致矛盾的取值，则直接将剔出其定义域。
    - 实现：
      1. 首先，先将所有待分配的变量中，所有会与已分配变量直接矛盾的值剔除。
      2. 把所有constraint化为双箭头(arc)，维护一个由箭头组成的队列Q。
      3. 当从Q中移除一个i->j的箭头时，检查i上是否有值可能使得j无值可选；如果有，则从i的定义域剔出该值，并把所有未被赋值的点k且k->i的箭头重新放回Q中——意义是i的选项减小了，需要重新判断是否导致有新的k值使得i中无值可选。
      4. 直到Q空——没有可剔除的值，继续赋值搜索；发现某些点的没有值可选，要回溯。
    - AC-3 algorithm 
    - 特点：
      - 提前利用了约束的关系，从而有信息的剔除了一些值，减少了试错回溯的次数
      - 但判断的过程需要大量计算，需要权衡
      - 思想来自于k-consistency,即k-1的节点的任何子集都需要使得k节点有值可选。我们这里k=2。
- Ordering 顺序
  - 显然，我们的搜索需要确定点or选值的顺序，可以针对此进行优化
  - Minimum Remaining Values 
    - 优先选择剩余可选值较少的点来分配（比较直觉）
  - Least Constraining Value
    - 选值尽量选会导致更少的剔除的值（更有可能是解），但这需要额外的计算（比如arc consistency）
- Structure
  - exploit the structure to improve your solving strategy
  - 树形约束，约束中无环，则可以将复杂度降为$O(nd^2)$
    - 方法：
      - 随意选一个根节点，将其他节点排列为拓扑排序，只使用单向的arc（显然满足单向就必然满足双向）
      - 从后向前做arc consistancy排除（从后向前保证了不需要重复再添加arc）
      - 只要排除后的每个点都有选项，那从根向后必然可以一次搜到一个解
    - 这里的主要代价只在arc consistancy中，且是单向的:$f(d)*O(n)$
  - 类（reasonably close to）树形结构
    - cutset conditioning(割集调节)
    - 通过寻找一个图里的最小点集使得割去该集后，剩下的结构为树形，可以沿用前述方法
    - 复杂度$O(d^c(n−c)d^2)$,其中c为割集大小，显然有较小的割集的图更适宜用
- Local Search
  - heuristic启发式：用一个函数表达与解的距离，比如目前违反的constraint数
  - 初始随机分配解，之后每次变动一个变量使得违反的约束总数减少，直到为0
  - 总时间代价不会随n而爆炸，对于randomly generated CSP？友好
  - 缺点：
    - 计算时间与${numbers of constraionts}/{numbers of variables}$相关，可能存在一个很高的峰
    - 不完备：随机出来的；suboptimal：很可能陷在局部里，找到极值而非最值
    - 典型的例子是 maximize or minimize an objective function，对于这类最优化问题我们介绍三种算法：__hill-climbing, simulated annealing and genetic algorithms__
- Hill-Climbing Search
  - 基于贪心，向目前所处的地方邻域的更高处进行
    - 缺点：incomplete 陷于局部最大，或陷于高原，且在到达"shoulders"的时候会很慢
  - stochastic hill-climbing 随机上爬
    - selects an action randomly among the uphill move
  - Random-Restart hill-climbing 随机起点,多次试验取极值，trivially complete
- Simulated Annealing Search 模拟退火
  - 随机跳向下一个点,计算目标值变化$\Delta$
    - if $\Delta >0$ 则更新
    - else 则按$e^{\Delta /T}$概率更新
    - 其中T是一个随着跳的次数变多逐渐下降的温度函数（退火）
    > If temperature is decreased slowly enough then the simulated annealing algorithm will reach the global maximum with probability approaching 1.
- Genetic Algorithms 遗传算法
  - a variant of local beam search：模拟遗传过程
    - 用一个序列表示变量的取值，初始随机出一些序列，并按目标函数的值降序排列
    - 按这些值相关的概率，抽出一些对来配对(fitness function)
    - 在这些对上随机取断点(selection),再交叉换位（crossover）生成新的序列
    - 最后这些新序列的某些位置按一定几率变异，从而得到新的一组序列，并重复
  - 通过更高概率交叉优质的基因，从而得到取值更高的序列，适用于较大的解集空间，较多的变量，很快的得到优质解

## SAT问题：
- “布尔可满足性问题”：给定一个布尔表达式，是否存在一组布尔变量的取值使得该表达式的值为真。
- 部分CSP问题可以形式化为SAT问题（变量的取值只有0or1，或转化为bool变量描述），例如N皇后
- 针对SAT问题的DPLL算法：
  - 把整个表达式转化为合取范式，即子句内为并，子句间为交，这样发现子句错则整体错，快速发现错误早回溯
- CDCL算法：矛盾指引的子句学习（[conflict-driven clause learning](https://cse442-17f.github.io/Conflict-Driven-Clause-Learning/)）算法 
  - 在CDCL算法中，每当DPLL算法导致矛盾时，算法会分析矛盾的原因，并将其表示为一个称为矛盾子句的新子句 learning！
  - Boolean Constraint Propagation:在实现DPLL算法时，面对一个CNF formula, 一种优化是去找unit clause，也就是子句中只有一个变量没确定，且这个变量可以决定子句的对错（换句话说，其他的子变量都是false），此时则可以直接定此变量为真，继续搜索，从而快速剪掉变量为假的分支；此过程可以迭代直到没有unit clause，从而恢复普通搜索直到下一个unit clause出现
  - CDCL的核心是，当在搜索的过程中，如果我们发现当某些变量的特定值组合必然会（通过BCP）引领到false的话，可能说明这些变量可以被写为新的子句，同时我们直接回溯到新子句保护的变量的最后一个分叉，利用新子句去以新的顺序搜索，会避免DPLL算法中出现的不断的陷入这个implicit clause造成的conflict中
  - So how to learn?:可以在BCP发生时构建一个implication graph,去揭示哪些变量的哪个取值，通过哪个子句，会必然的引向false。highlevelly，我们通过指向false结果的有向边反推，则如果存在某个极小的节点簇使得false结果的所有祖父节点都【只】来自这个节点（且所有的子过程都是BCP的），则这个节点簇的取值可以构成一个新的clause。（而这种思想可能不止用于Bool变量的搜索）
  - 可以看链接中的一个Sudoku例子

## GAMES [Note5]
- adversaries involved
  - 我们初始时不确定竞争者会如何选择来对抗我们，需要新算法
- adversarial search problems classification
  - actions have deterministic or stochastic (probabilistic) outcomes
  - numbers of players
  - zero-sum(零和) or not
- deterministic zero-sum games
  - 确定性的结果（什么意思）
  - 零和：两方的利益总和为0，敌增我减，无法合作引申为所有对立问题
  - eg. 一方想最大化某个值，另一方试图最小化
    - 跳棋checkers:可解的问题 任何残局的解是确定的
    - chess:Deep Blue 
      - >use extremely sophisticated methods to evaluate over 200 million positions per second
  - 如何通过计算发展一个strategy or policy
- Minimax
  - motivationg assumption激励假设：对手总是做对我们最坏的选择
    - we maximize it,they minimize it.
  - 先从没有敌人阻碍的情形，建立：state value(the optimal score attainable by the agent which controls that state) 和 terminal utility（一个pacman例子，pacman在一维上左右游走，在尽可能少的步数下吃到豆子）
    - terminal utility 指的就是游戏有个总结的状态，在终结时我的某个utility即terminal utility，使其最大化是我的目标
    - 而其他我从初始状态开始可能到达的状态下，从此状态开始，接下来能实现的最大terminal utility(即这个状态变化子树内的最优值)，称为该状态的state value
    - 这就是一种启发函数，我们从后向前递推的判断：在状态a下向哪边走的state function更优，哪边就是更优的选择
  - 现在引入敌人ghost：
    - ghost的出现会使得状态树变为交替的层结构，两者交替做选择
    - 我们注意到整个过程是确定的，即如果后面的state value已知那么理性人agent会从后向前分析出每一步每个人的选择，那这是不存在博弈的。比如如例子中在进行1回合后的state value是可见的，那么后动的ghost选择必定分别是其中值更小的，那先动的pacman的两种选择的值也是确定的。
    > being wisely, Pacman is forced to hedge his bets and counterintuitively move away.
    - 回到公式，递归关系此时必须是一步之内的，下一步的人的选择确定了，即state value确定了，这一步的人才能有效选择
    - Hence，计算value的顺序应当是树的后序遍历(postorder traversal)
- Alpha-Beta Pruning
  - Minimax简单直接有效，但很慢，很多时候我们搜不完整个树 
  - 优化：alpha-beta 剪枝，怎么剪
    > Conceptually, alpha-beta pruning is this: if you’re trying to determine the value of a node n by looking at its successors, stop looking as soon as you know that n’s value can at best equal the optimal value of n’s parent.
  - 简单的说，由于第0层要最大子值，而子值的选取方式是子的子值中的最小值，如果子值一计算完成为a，子值2的第一个子就小于a，那子值2的值必定也小于a，对于父来说子值2一定不会被选取，那么就不必计算了，可以直接剪掉
    - 这一特性直接来自于game tree的minimax交替特点，普通的树是不行的
  - 有时能带来相同代价下增加很多层的搜索，是一种优化，但并不能直接解决问题，因为我们目前的逻辑还是要从terminal state向前搜(which)
- Evaluation Functions
  - 没办法从结束计算，那自然我们想象设计一个启发函数，能只用几步后的信息做判断，从而减少运算深度和时间。那就需要把几步后的情况定为终结，并为他们选择尽量有用的evaluation function,让agent的选择仍尽量最优
  - 一种常见的构造：特性(feature)的线性组合：$$Eval(s) = w_1 f_1(s) +w_2 f_2(s) +...+w_n f_n(s)$$
    - feature是从一个状态里我们可能直接提取的量化的值，例如象棋中剩余的各类棋子的个数，围棋的目等等，特性通常是很多方面的，可以写为一个向量，从而基于其重要性来加权求和
  - 其他的：nonlinear evaluation functions based on neural networks are very common in Reinforcement Learning applications. 
  - 记住Evaluation function的目的是尽量让我们做更多更优的选择，并应以此Tuning我们的function
- Expectimax
  - minimax针对最优敌人优化，有时候我们会面对随机敌人
  - 则改变minimizer返回的utility为某个random性质的数学期望，成为expected utility
    - 我们可以任意的设定概率分布以满足模型的需求（面对无限智能的敌人，那就是mininum的概率为1）
- MCTS
  - ideas:
    - Evaluation by rollouts: From state s play many times using a policy (e.g. random) and count wins/losses.
    - Selective search: explore parts of the tree, without constraints on the horizon, that will improve decision at the root.
  - 改进：
    - 我们不想平均的随机的搜索所有步骤，如果短时间内发现某个方向胜率很低，那应该更多的去花时间检验其他方向中哪个更好
    - 同时，在表现相近的方向中，如果有测试次数很少的方向，那其表现的可信度较低方程较大，我们更倾向于花时间在它身上去确认其表现
    - UCB：trade-off between “promising" and “uncertain’
      -  表达式：
   - UCT algorithm:
     - 4-step cycle
     -  
  - lab.feedback:
    - simulation中，通常在走一定步数内无法到达WinorLose,需要以演化后状态的启发函数返回，从而达到类似胜率的效果
    - 可以用启发式前进代替随机模拟，同时UCB也可以掺杂启发函数，从而更有方向性地搜索
      - 但一定要保留一定的随机性，否则一些不完善的启发函数会使agent被困在某个状态里（比如一个迷宫的死胡同）不断stop
    - 很难设计出一个针对所有可能的情况都良好的、易于实现而便于计算的启发函数，总是存在人脑无法预测到的错误情况
      - 更好的启发函数设计：机器学习
 - General Games
   - maybe not zero-sum:更广泛的博弈问题
     - multi-agent utilities
     - 每个人有每个人的utility，每个人只关心自己的utility并做出决策
     - 但事实上，这如果每个人有更高的智能，他们会发现他们的决策影响着后人的决策从而反馈回他们自己的utility，那或许他们就不是在自己的layer上选择max那么简单，这需要更多的计算来实现

## 机器学习基础
- in a word: data&output-->program
- 一些分类：
- 学习方式：
  - 监督学习模型：这类模型的训练数据包含输入和输出的配对，即已知每个输入应该对应什么输出。例如，分类问题和回归问题都可以通过监督学习来解决。

  - 无监督学习模型：这类模型的训练数据只包含输入数据，没有输出数据。无监督学习的目标通常是发现数据的内在结构，例如聚类和降维等问题。

  - 半监督学习模型：这类模型的训练数据包含一部分输入和输出的配对，以及一部分只包含输入的数据。半监督学习旨在利用未标记数据来提高模型的性能。

  - 强化学习模型：这类模型是基于智能体（agent）与环境进行交互的学习方式，强化学习的目标是通过智能体与环境的交互来学习最佳的行为策略。
- 接下来我们看一下按目的分类的模型
### 判别式模型
- 基本目标：构建一个包含参数的函数作为模型，将输入映射到一个数值或类别上（统称为label）
  - 学习过程：通过调整参数来拟合到训练数据上
    - 如果需要映射到连续值上，则为回归
    - 离散值则为分类
  - 评估：
    - 在训练集上学习，去降低训练集上的误差
    - 在测试集中测试，想要同样得到可以接受的误差，从而证明有泛化能力，避免过拟合
- k近邻算法
  - 不用训练，只是拿着训练集，看测试输入的周围最近的k个训练样本中更多的标签，来预测测试样本的标签
  - 一个例子是判断一个地点属于哪一个国家，看它离的近的点中哪个国家更多即可；
  - 但缺点：
    - 需要样本间的边界较为“平直”
    - 在更多模态的问题上，距离很难定义
    - 同时在高维下，距离的差别变得诡异，维度越高点更倾向于分布在边界而非近处，距离很难衡量真正意义的“样本接近”
  - k-NN是典型的非参数模型，没有参数参与，纯粹依靠原始的训练集
  - 而对应的是参数模型，通过训练合适的参数来拟合训练集，生成参数模型，去预测新的输入
- 线性回归
  - 线性模型：$f(x)=w^Tx+b$；w的分量构成每个维度的权重，b为整体的偏置
  - 评估误差：损失函数
    - 平方损失函数，所有点的预测值与真值的差值的平方求平均值（最小二乘法）
    - 最小化该函数，需要一些方法改变参数的方法
  - 梯度下降；沿着梯度反方向以超参数$\alpha$的幅度改变参数向量，从而减少误差值，直到无法再下降（下降足够缓慢）
    - 问题：可能陷入局部最小值而无法到达全局最小值
    - 但如果目标函数是凸函数就一定能这样找到最小值（凸函数不会有两个低谷），这就是凸优化问题；线性回归问题恰好是凸函数（Hessian半正定），因此可以梯度下降
    - 同时注意选择合适的超参数$\alpha$，保证下降搜索的速率足够快但不会因为幅度过大而不断错过最低点
- Empirical Risk Minimization (ERM)
  - 线性回归是ERM的代表
  - 经验风险最小化框架：确定模型，确定损失函数，调节模型参数以最小化损失（通常可以采用梯度下降）
  - 区别只是模型和损失的选取和定义
  - 而对于分类问题，一个难点在于没有数值，也就没有了距离和排序，应该如何建立模型和损失函数
- 逻辑回归
  - 对于分类问题，首先是二分类问题，能不能用类似的思路
  - 沿用Loss Function模型：含参的初等函数通常值域是实数域，需要映射到二分类中(def y= 1or-1)，因此引入$sign(f(x))$，以0为界限分到两类中
    - 误差函数：问题出现了，如果我们直接去求差得到误差求和：零一损失，这样会导致得到的是阶跃函数，无法梯度下降
  - 对于分类问题，差值是没有意义的，预测只有正确与否，那么预测一种分类的概率更有价值
    - 通俗的说，模型告诉我们一个输入有多大概率属于某一类，这样可以检查训练集中我们猜的有多对，显然对于正确的label，更高的概率预测是好于较低的概率预测的，这种可操作空间是以0为界的sign函数做不到的
  - 最大似然估计：使用概率论的工具，我们认为这是这种分类是一种概率事件，即对于任意输入，输出遵循一种概率分布，这里则是一个二元分布列$$p(y|x;\theta)$$其中参数$\theta$控制对于输入x，输出各个y的概率。通过建立这种分布模型，可以带入训练集，如果假设训练样本间独立，那么要求带入所有正确label的概率乘积最大是自然的；为了计算上的方便，通常转化化为对数求和最大化要求。
    - 常用的概率模型：把线性模型的R值域用sigmoid函数映射到[0,1]上，作为正类的概率；同时$y=\pm 1$保证了概率都可以写为$p=\sigma(y*f(x))$的形式，帮助化简
    - 得到形如$$\min \frac{1}{n} \sum(log(1+e^{-y_i(w^Tx_i+b)}))$$的要求，又回到了类似最小化损失函数的形式，因此这个对数损失函数被称为交叉熵损失
  - 交叉熵损失同时满足：
    - 是零一损失的上界
    - 连续可微凸函数
    - 最小化的同时，也达到了最小化零一损失的目的
    这种损失函数称为替代损失函数。同样的，把零一损失放大为一种线性函数的做法也是构造一种替代损失函数。
  - 逻辑回归训练
    - 梯度下降：发现梯度有$1-p$项，说明p接近1，拟合充分时，梯度很小
- 多分类问题
## 神经网络
