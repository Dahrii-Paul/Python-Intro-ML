import numpy as np
import pandas as pd
from pandas import Series, DataFrame
from numpy.random import *


seq = "ATGCGGCATTAT"
score_df = df


# split seq 
def split_n(text, n):
    return [ text[i:i+n] for i in range(len(text)-(n-1)) ]

# calcurate values in given sequence
def col_val(sequence,dataframe,start):
    vl = 0
    num = start
#    print(seqs[start])
    
    for nc in sequence[start]: 
        point = 4
        if nc == "A":
            point = 0
        elif nc == "T":
            point = 1
        elif nc == "G":
            point = 2
        elif nc == "C":
            point = 3
    
        vl += df.iloc[point,num]
        num += 1
    return vl


# split seq by 5
splited = split_n(seq,5)

# calcurate values in each splited sequence
vls = []
vls = [col_val(splited,score_df,times) for times in range(len(splited))]

# Save results as dataframe
seq_df = pd.DataFrame({"start_from":range(len(splited)),
                       "sequence":splited,
                       "value":vls},
                      columns=["start_from","sequence","value"])

seq_df
