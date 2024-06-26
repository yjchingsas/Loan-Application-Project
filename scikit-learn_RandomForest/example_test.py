import os
import os.path
import sys

sys.path.append('/models/resources/viya/bb6ea2d6-c061-416a-a872-0de47f74c66d/')

import score_rf2

import settings_bb6ea2d6_c061_416a_a872_0de47f74c66d

settings_bb6ea2d6_c061_416a_a872_0de47f74c66d.pickle_path = '/models/resources/viya/bb6ea2d6-c061-416a-a872-0de47f74c66d/'

def score_record(DELINQUENCIES,DEROGATORYMARKS,INQUIRIES,CREDLINEAGE,CREDLINES,DEBTINCRATIO,LOANREQUEST,HOMEVALUE,INCOME,LOANTOVALUE,YEARSONJOB):
    "Output: P_DEFAULT0,P_DEFAULT1,I_DEFAULT"
    return score_rf2.score_method(DELINQUENCIES,DEROGATORYMARKS,INQUIRIES,CREDLINEAGE,CREDLINES,DEBTINCRATIO,LOANREQUEST,HOMEVALUE,INCOME,LOANTOVALUE,YEARSONJOB)

print(score_record(93.82,1.89,122.80,108.89,140.88,188.00,116.13,133.55,111.19,126.94,38.90))
