'''Program to know whether the patient have all the severe symptoms or not
based on 1)headache  2)shortness of breath 3)tiredness 4)continuous cough
5)fever  6)loss of taste 7)loss of smell 8)muscles pain'''
import pandas as pd
import numpy as np
import functions as f

def test_fun():
    '''1 for test yourself and 0 for vaccinate yourself'''
    assert f.check_sym(REF, testcase1) == 1
    assert f.check_sym(REF, testcase2) == 1
    assert f.check_sym(REF, testcase3) == 0
    assert f.check_sym(REF, testcase4) == 0

data = pd.read_csv("corona_sym.csv")
concepts = np.array(data)[:,:-1]
target = np.array(data)[:,-1]

ref_list=f.train(concepts,target)
REF = ref_list.tolist()

testcase1 = ['no', 'yes', 'no', 'yes', 'no', 'yes', 'yes', 'no']
testcase2 = ['no', 'no', 'no', 'no', 'no', 'yes', 'yes', 'no']
testcase3 = ['yes', 'no', 'yes', 'no', 'no', 'no', 'no', 'yes']
testcase4 = ['no', 'no', 'no', 'no', 'no', 'no', 'no', 'no']

test_fun()
