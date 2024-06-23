# 数据库HW3 关系代数
> 喻勃洋 2000011483 21级信科
## Q1
1. 求同时向位于北京和天津的工程供应了零件的供应商的供应商名
$$ 
\pi_{S.Sname}(\sigma_{J.CITY=Beijing \wedge J.JNO=SPJ.JNO \wedge SPJ.SNO=S.SNO}  (J\times SPJ \times S)) \\
\cup \ \pi_{S.Sname}(\sigma_{J.CITY=Tianjin \wedge J.JNO=SPJ.JNO \wedge SPJ.SNO=S.SNO}  (J\times SPJ \times S))
$$
2. 求向和自己位于相同城市的工程供应零件的供应商的供应商号
$$ \pi_{S.SNO}(\sigma_{J.CITY=S.CITY \wedge J.JNO=SPJ.JNO \wedge SPJ.SNO=S.SNO}  (J\times SPJ \times S))$$
3. 求只向和自己位于不同城市的工程供应零件的供应商的供应商号
$$ \pi_{S.SNO}(S) -\pi_{S.SNO}(\sigma_{J.CITY= S.CITY \wedge J.JNO=SPJ.JNO \wedge SPJ.SNO=S.SNO}  (J\times SPJ \times S))$$
4. 求向所有位于北京的工程都供应了零件的供应商的供应商号
$$ \pi_{SPJ.SNO,J.JNO}(\sigma_{SPJ.JNO=J.JNO}(SPJ\times \sigma_{CITY=Beijing}(J))) \div \pi_{J.JNO}(\sigma_{CITY=Beijing}(J))$$
5. 求价格最高的零件的零件号
$$ \pi_{PNO}(\sigma_{PRICE=max(PRICE)}(P))$$

## Q2
1. 求至少选修了c1和c2课程的学生
$$ \pi_{SNO}(\sigma_{CNO=c1}(SC)) \cap \pi_{SNO}(\sigma_{CNO=c2}(SC))$$
2. #pass
3. 求选修了所有s1同学所修课程的学生
$$ \pi_{SNO,CNO}(SC) \div \pi_{CNO}(\sigma_{SNO=s1}(SC))$$
4. 求其选修课程被s1同学所修课程完全包含的学生
$$ \pi_{SNO}(SC) \\- \pi_{SNO}(\sigma_{SC.CNO=T.CNO}(SC \times \rho_T(\pi_{CNO}(SC)-\pi_{CNO}(\sigma_{SNO=s1}(SC)))))$$
5. 求和s1同学所修课程完全不同的学生
$$ \pi_{SNO}(SC) - \pi_{SC.SNO}(\sigma_{T.SNO=s1 \wedge SC.CNO=T.CNO}(SC\times \rho_T(SC)))$$

## Q3
1. 对于关系R(A, B)，用关系代数来检验A是否取值唯一。
$$ \sigma_{R.A=T.A \wedge R.B\neq T.B}(R \times \rho_T(R)) = \emptyset$$
2. 对于关系R(A, B, C)，用关系代数来检验A是否取值唯一。
$$ \sigma_{R.A=T.A \wedge R.B\neq T.B}(R \times \rho_T(R)) = \emptyset \\
\wedge \ \sigma_{R.A=T.A \wedge R.C\neq T.C}(R \times \rho_T(R)) = \emptyset$$


## Q4
- 元组关系演算：
  1. 求同时选修了c1和c2课程的学生
    $$ \{ s | \exist t \in SC ( t[cno]=c1 \wedge s[sno]=t[sno])\} \\ 
    \cap \ \{ s | \exist t \in SC ( t[cno]=c2 \wedge s[sno]=t[sno])\}$$
  2. 求选修c1课程成绩比s1同学的该门课程成绩高的学生
    $$ \{ s | \exist t \in SC \ \exist r \in SC ( t[cno]=c1 \wedge r[cno]=c1 \wedge r[sno]=s1 \\
    \wedge t[grade] > r[grade] \wedge s[sno]=t[sno]) \}$$
- 域关系演算
  1. 求同时选修了c1和c2课程的学生
    $$ \{ sno | \exist grade( <sno,c1,grade> \in SC)\} \\
   \cap \ \{ sno | \exist grade( <sno,c2,grade> \in SC)\}$$
  2. 求选修c1课程成绩比s1同学的该门课程成绩高的学生
    $$ \{ sno | \exist grade1,grade2 \  ( grade1>grade2 \wedge <sno,c1,grade1> \in SC \wedge <s1,c1,grade2> \in SC)\}$$