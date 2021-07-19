'''Program to know whether the patient have all the severe symptoms or not'''
import pandas as pd
import numpy as np
data = pd.read_csv("corona_sym.csv")
concepts = np.array(data)[:,:-1]
target = np.array(data)[:,-1]

def train(con, tar):
    '''Find s algarithm to get specific hypothesis'''
    for i, val in enumerate(tar):
        if val == 'no':
            specific_h = con[i].copy()
            break

    for i, val in enumerate(con):
        if tar[i] == 'no':
            length=len(specific_h)
            for hypo_atr in range(length):
                if val[hypo_atr] != specific_h[hypo_atr]:
                    specific_h[hypo_atr] = '?'
                else:
                    pass
    return specific_h

ref_list=train(concepts,target)

def test_input():
    '''taking inputs from user'''
    enter_list=[]
    print("Please give all the asked information",end=" ")
    print("to know whether you have all the corona symptoms or not?")
    print("Enter \"yes\" or \"no\" for the following question")
    print("Do you have head ache?")
    enter_list.append(input())
    print("Do you have Shortness of breath?")
    enter_list.append(input())
    print("Do you have tiredness?")
    enter_list.append(input())
    print("Do you have continuous cough?")
    enter_list.append(input())
    print("Do you have fever?")
    enter_list.append(input())
    print("Do you feel loss of taste?")
    enter_list.append(input())
    print("Do you feel loss of smell?")
    enter_list.append(input())
    print("Do you have muscles pain?")
    enter_list.append(input())
    return enter_list

def check_sym(r_std , test):
    '''comparing symptoms with most common symptoms'''
    for k, i in enumerate(r_std):
        if i == '?':
            test[k] = r_std[k]
    flg = 0
    for sym_char in range(len(r_std)):
        if REF[sym_char] == test[sym_char]:
            flg=0
        else:
            flg = 1
            break
    return flg

Test = test_input()
REF = ref_list.tolist()
RES = check_sym(REF, Test)
if RES == 1:
    print("You have severe symptoms of corona,Test yourself")
else:
    print("You don't have any severe symptoms of corona")
