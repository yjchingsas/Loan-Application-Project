import os
import os.path
import sys

sys.path.append('/models/resources/viya/4136b5c6-4c03-46cd-b46c-852c63462643/')

import _56liklgygp1yokc3m2xxt7y6h

import settings_4136b5c6_4c03_46cd_b46c_852c63462643

settings_4136b5c6_4c03_46cd_b46c_852c63462643.pickle_path = '/models/resources/viya/4136b5c6-4c03-46cd-b46c-852c63462643/'

def score_record(Delinquencies,DerogatoryMarks,Inquiries,JobType,CredLineAge,CredLines,DebtIncRatio,LoanRequest,HomeValue,Income,LoanToValue,YearsOnJob):
    "Output: P_Default0,P_Default1,I_Default"
    return _56liklgygp1yokc3m2xxt7y6h.score_method(Delinquencies,DerogatoryMarks,Inquiries,JobType,CredLineAge,CredLines,DebtIncRatio,LoanRequest,HomeValue,Income,LoanToValue,YearsOnJob)

print(score_record(23.29,170.67,31.44,"",175.42,189.33,164.70,34.98,161.67,179.11,137.30,161.58))
