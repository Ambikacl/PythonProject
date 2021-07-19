'''Program to know whether the patient have all the severe symptoms or not'''
import pandas as pd
import numpy as np
import functions as f

data = pd.read_csv("corona_sym.csv")
concepts = np.array(data)[:,:-1]
target = np.array(data)[:,-1]

ref_list=f.train(concepts,target)

Test = f.test_input()
REF = ref_list.tolist()
RES = f.check_sym(REF, Test)
if RES == 1:
    print("You have severe symptoms of corona,Test yourself")
else:
    print("You don't have any severe symptoms of corona")
