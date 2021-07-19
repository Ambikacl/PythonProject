'''Program to know whether the patient have all the severe symptoms or not
based on 1)headache  2)shortness of breath 3)tiredness 4)continuous cough
5)fever  6)loss of taste 7)loss of smell 8)muscles pain'''
import pandas as pd
import numpy as np

testcase1 = ['no', 'yes', 'no', 'yes', 'no', 'yes', 'yes', 'no']
testcase2 = ['no', 'no', 'no', 'no', 'no', 'yes', 'yes', 'no']
testcase3 = ['yes', 'no', 'yes', 'no', 'no', 'no', 'no', 'yes']
testcase4 = ['no', 'no', 'no', 'no', 'no', 'no', 'no', 'no']


data = pd.read_csv("corona_sym.csv")
concepts = np.array(data)[:,:-1]
target = np.array(data)[:,-1]

def train(con, tar):
    '''Find s algarithm to get specific hypothesis of a given data'''
    for i, val in enumerate(tar):
        if val == 'no':
            specific_h = con[i].copy()
            break

    for i, val in enumerate(con):
        if tar[i] == 'no':
            length=len(specific_h)
            for hyp_atr in range(length):
                if val[hyp_atr] != specific_h[hyp_atr]:
                    specific_h[hyp_atr] = '?'
                else:
                    pass
    return specific_h

ref_list=train(concepts,target)

def check_sym(r_std , test):
    '''comparing symptoms with most common symptoms'''
    for k, i in enumerate(r_std):
        if i == '?':
            test[k] = r_std[k]
    length=len(r_std)
    for sym_char in range(length):
        if check_list[sym_char] == test[sym_char]:
            flag = 0
        else:
            flag = 1
            break
    return flag

check_list = ref_list.tolist()

def test_fun():
    '''1 for test yourself and 0 for vaccinate yourself'''
    assert check_sym(check_list, testcase1) == 1
    assert check_sym(check_list, testcase2) == 1
    assert check_sym(check_list, testcase3) == 0
    assert check_sym(check_list, testcase4) == 0
