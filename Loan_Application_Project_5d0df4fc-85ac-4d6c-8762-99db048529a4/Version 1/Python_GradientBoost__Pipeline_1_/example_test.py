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

print(score_record(87.37,164.52,85.97,"",43.02,183.69,103.14,78.21,3.90,52.46,191.21,44.58))
