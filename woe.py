# -*- coding: utf-8 -*-  
""" 
Created on Thu Jul 26 22:53:48 2018 
@author: ykp 
"""  
import pandas as pd  
import numpy as np  
import copy  
  
def myfind(x,y):  
    return [ a for a in range(len(y)) if y[a] == x]  
  
def WOE_ykp( x,y ):  
    n1 = len(y) # 总个数  
    n2 = sum(y) # 违约总个数  
    out = dict()  
    out_2 = dict()  
    leibie = list(set(x))  
    for i in leibie:  
        #print(i)  
        index_ykp = myfind(i,x)  
        n_i_all = len(index_ykp)  
        temp_sum = 0  
        for j in index_ykp:  
            temp_sum = temp_sum+y[j] # 第j类别的违约个数  
        if temp_sum==0 and n_i_all==temp_sum:  
            out[i] = -np.log(((temp_sum+1)/(n_i_all-temp_sum+1))/(n2/(n1-n2)))  
        elif temp_sum!=0 and n_i_all==temp_sum:  
            out[i] = -np.log(((temp_sum)/(n_i_all-temp_sum+1))/(n2/(n1-n2)))  
        elif temp_sum==0 and n_i_all!=temp_sum:  
            out[i] = -np.log(((temp_sum+1)/(n_i_all-temp_sum))/(n2/(n1-n2)))  
        else:  
            out[i] = -np.log(((temp_sum)/(n_i_all-temp_sum))/(n2/(n1-n2)))  
        #temp_i_1 = map(lambda (a,b):a*b, zip(l1,l2))  
        # out[i] = np.log(((temp_sum+1)/(n_i_all-temp_sum+1))/((n2+1)/(n1-n2+1))) if (n1-n2)==0 or (n_i_all-temp_sum)==0 or n2==0 or temp_sum==0 else np.log((temp_sum+1/(n_i_all-temp_sum))/(n2+1/(n1-n2)))   
    am_ykp = sorted(out, key= lambda k: out[k])  
    min_ykp = out[am_ykp[0]]  
    max_ykp = out[am_ykp[len(am_ykp)-1]]  
    minus_ykp = max_ykp-min_ykp  
    for i in leibie:  
        out_2[i] = (out[i]-min_ykp)/minus_ykp # 负向指标打分公式，woe数值越大,标准化后越应该等于0  
    return out,out_2  
  
path_in = 'C:/Users/308-11/Desktop/'  
data = pd.read_excel(path_in+'定性指标输入样例.xlsx',sheetname = 'Sheet1', header=0, index_col =None)  
  
data_copy_or = copy.deepcopy(data)  
data_copy_st = copy.deepcopy(data)  
woe=dict(dict())  
woe_01=dict(dict())  
woe_output = dict()  
woe_output_1 = dict()  
woe_output_2 = dict()  
name = list(data.columns)  
for i in name[1:len(name)]:  
    woe[i],woe_01[i] = WOE_ykp(data[i],data[name[len(name)-1]]) # woe_01为标准化打分结果  
    data_copy_or[i] = data_copy_or[i].replace(list(woe[i].keys()),list(woe[i].values()))  
    data_copy_st[i] = data_copy_st[i].replace(list(woe_01[i].keys()),list(woe_01[i].values()))  
    woe_output_1[i] = pd.DataFrame.from_dict(woe[i],orient='index').T  
    woe_output_2[i] = pd.DataFrame.from_dict(woe_01[i],orient='index').T  
    woe_output[i] = woe_output_1[i].append(woe_output_2[i])  
# 结果输出  
writer = pd.ExcelWriter(path_in+'定性指标输出结果-WOE.xlsx')  
data.to_excel(excel_writer=writer, sheet_name = '1.原始数据', columns = name,index=None)  
data_copy_or.to_excel(excel_writer=writer, sheet_name = '2.woe原始值对应填补', columns = name,index=None)  
data_copy_st.to_excel(excel_writer=writer, sheet_name = '3.woe标准化值对应填补', columns = name,index=None)  
temp = 3  
for i in name[1:len(name)-1]:  
    woe_output[i].to_excel(excel_writer=writer, sheet_name = str(temp+1)+'.'+str(i),index=None)  
    temp = temp+1  
writer.save()
