import os
import os.path
import sys

sys.path.append('/models/resources/viya/b1317393-c264-41eb-9e5c-986d501f5582/')

import _1h3tzjo257gbcd9e09drhli76

import settings_b1317393_c264_41eb_9e5c_986d501f5582

settings_b1317393_c264_41eb_9e5c_986d501f5582.pickle_path = '/models/resources/viya/b1317393-c264-41eb-9e5c-986d501f5582/'

def score_record(Delinquencies,DerogatoryMarks,Inquiries,JobType,CredLineAge,CredLines,DebtIncRatio,LoanRequest,HomeValue,Income,LoanToValue,YearsOnJob):
    "Output: P_Default0,P_Default1,I_Default"
    return _1h3tzjo257gbcd9e09drhli76.score_method(Delinquencies,DerogatoryMarks,Inquiries,JobType,CredLineAge,CredLines,DebtIncRatio,LoanRequest,HomeValue,Income,LoanToValue,YearsOnJob)

print(score_record(14.20,155.73,111.31,"",20.73,186.01,181.01,26.61,78.94,29.21,5.14,100.91))
