# 数据库HW CH7 关系规范化
> 喻勃洋 2000011483 21级信科
## 问答：
1. 一个全是主属性的关系模式肯定可以达到3NF,因为没有非主属性。未必是BCNF。
2. 一个全码的关系模式最高可以达到BCNF。因为全码下任何属性集的函数依赖都要么是平凡的，要么是依赖于整个候选码。
3. 任何一个二目关系模式 R(A,B) 一定属于BCNF。 显然，如果存在非平凡的函数依赖 A->B 或 B->A，那么A或B就是候选码，R就是BCNF的。
4. 不一定，如ppt中的STC关系模式中如果sno是候选码，那么这个单候选码的3NF就不是BCNF的。
5. 一定是2NF的，因为单属性候选码说明所有主属性一定就是码，因此一定是完全函数依赖。但不一定是3NF，因为不影响存在传递函数依赖，如ppt中的S_D。
6. 其关系是，利用多值依赖可以指导我们进行无损分解。如果一个关系模式具有多值依赖 X→→Y，可以将分解(X,Y) 和 (X,Z−Y)，这种分解是无损连接的。
7. 其只选择不符合BCNF条件的依赖进行分解，保证分解是无损的。因为分解这样的中级码，可以保证原关系的所有函数依赖都能在分解后的关系中找到。
8. 因为不在Fmin中的依赖已经被去除了，且此时满足X→A,且XA=U, 因此类比前问的二目关系模式，至少是3NF的。

## 题目一
1. 候选码：$AB, AC$
2. 范式：1NF,2NF,不满足3NF（例如B->D）
3. 
   - 无损连接分解：$BD,ACE$；（有很多种解）
   - 保持函数依赖分解3NF：{ABC,AB->C},{ACB,AC->B},{BD,B->D},{CDE,CD->E},{CEB,CE->B}

## 题目二
$$F_S={AB→D,BC→D,D→A}$$

## 题目三
其候选码有$BG,BC$
先得到保持函数依赖分解3NF:
{BGC,BG->C}, {GF,G->F}, {CH,C->H}, {CG,C->G}, {FD,F->D}
有$BG,BC \subseteq BGC$，因此保持无损连接

## 题目四
首先A->BCD,而B->->C,即给出一个B，可以唯一的确定一组C，而与A，D无关;而唯一的A可以确定唯一的B，C，D，这说明给出一个B只能对应一个C，如果对应多个C则需要每个A和此B都对应这多个C，与A->BCD矛盾，因此B->C也是函数依赖。因此这不是3NF，最高是2NF。同时B也不是码，因此也不是4NF。

## 题目五
关系代数：
1. 投影 A 和 B：
   $$ R_1 = \pi_{A,B}(r) $$

2. 投影 A 和 C：
   $$ R_2 = \pi_{A,C}(r) $$

3. 自然连接 AB 和 AC：
   $$ R_3 = R_1 \bowtie R_2 $$

4. 比较：
   如果 $$ R_3 \subseteq r $$ ，则 $$ A \rightarrow\rightarrow B $$ 成立。

sql：
~~~sql
#投影AB AC
CREATE TABLE AB_combinations AS
SELECT DISTINCT A, B
FROM r;

CREATE TABLE AC_combinations AS
SELECT DISTINCT A, C
FROM r;


CREATE TABLE ABC_combinations AS
SELECT AB.A, AB.B, AC.C
FROM AB_combinations AB
JOIN AC_combinations AC ON AB.A = AC.A;

SELECT * FROM ABC_combinations
EXCEPT
SELECT * FROM r;
~~~


## 题目六
原：{ABCD→E，E→D，A→B，AC→D}
{AC→E，A→B，AC→D}