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

print(score_record(65.45,167.83,161.56,"",57.46,162.94,161.61,24.35,143.00,54.78,103.22,96.70))
