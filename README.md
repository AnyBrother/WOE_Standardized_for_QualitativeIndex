# WOE_Standardized_for_QualitativeIndex
This is the python codes (v3.6) for Standardized the Qualitative Index based on WOE score.

# 代码操作说明
 1. 在"定性指标输入样例.xlsx"中,保证第1列为序号，最后一列为0/1的违约状态，中间列均是待转化的定性指标(其中的空值要用"空"来填补,不能空着).
 2. 将"woe.py"中第44行路径修改为该py文件所在的路径,如`$ path_in = 'C:/Users/308-11/Desktop/'   $`.
 
 3. 执行woe.py代码, 输出的结果显示在"定性指标输出结果-WOE.xlsx"中.
 
 · WOE标准化打分原理,详见word文件"woe原理说明.doc".
