#GAMES105

##Math
1. matrix representation
2. Euler
3. Quaternions
   - rules
   - Understanding
     - 最重要的就是旋转的想法
   - application in 3D rotation
## Forward Kinematics
1. from characters to skeleton
   - rigid bones
   - using joint to connect,bones can rotate,but not separate
   - how to perform the orientation of bones with joints connecting as a chain, meaning the leading end will influence after end----forward kinematics
2. a chain（mechanical arm）
   - 记录每段臂的坐标系（基底）矩阵表示$Q_i=I$
   - 末端n发生旋转，则利用旋转矩阵每个臂矩阵$Q_n=R_n$[^1] 
    [^1]:这里旋转矩阵$R_n$的含义是，如果一个向量在$Q_n$下的坐标表示为$a_n$，则在空间系下其坐标表示是$a^*=R_na_n$；因此在表达坐标系旋转时是右乘，这样作用在坐标上的顺序才是对的。
   - 旋转的传递，表现在坐标上是左乘旋转矩阵，则在基底上就是右乘：$$Q_i=Q_{i-1}R_i$$
   - 进一步，臂是轻杆，有长度$l_i$，那么就可以表示关节的坐标
   - 很明显的，关节位置$p_{i+1}=p_{i}+Q_il_i$
   - 则已知一个点在$Q_i$下的坐标表示$x_i$,计算其在父关节系的坐标表示$$x_{i-1}=l_{i-1}+R_ix_i$$
3. chain to character
   - a tree:由root发展出结果，root可以根据需要任取
     - 不能是图（人身上无环）
   - 现实里 关节的旋转不是$4\pi$立体角的,有些是限制在平面内，有些限制在半球
   - DoF(自由度) 1or2or3
   - 角度限制 
   - 存储，BVH文件
## Inverse Problems
对直观的描述和调整一个人体来说，直接操作某个臂or关节达到某位置，希望能自动解出其他关节的位置或臂的角度，是更自然的思路；因为现实中我们的目标更多是末端动作：推拉抓……，而如何屈伸肌肉转关节来实现，这是不用思考就自然发生的，我们期望复现这一逻辑。
1. 
     
   