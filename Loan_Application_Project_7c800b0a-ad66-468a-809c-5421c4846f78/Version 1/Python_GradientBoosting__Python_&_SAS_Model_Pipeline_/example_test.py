import os
import os.path
import sys

sys.path.append('/models/resources/viya/18a81ad7-db11-4470-8a0b-fc3d807efce2/')

import _dj5n7wg1ne74bjo4ln9lur5fz

import settings_18a81ad7_db11_4470_8a0b_fc3d807efce2

settings_18a81ad7_db11_4470_8a0b_fc3d807efce2.pickle_path = '/models/resources/viya/18a81ad7-db11-4470-8a0b-fc3d807efce2/'

def score_record(Delinquencies,DerogatoryMarks,Inquiries,JobType,CredLineAge,CredLines,DebtIncRatio,LoanRequest,HomeValue,Income,LoanToValue,YearsOnJob):
    "Output: P_Default0,P_Default1,I_Default"
    return _dj5n7wg1ne74bjo4ln9lur5fz.score_method(Delinquencies,DerogatoryMarks,Inquiries,JobType,CredLineAge,CredLines,DebtIncRatio,LoanRequest,HomeValue,Income,LoanToValue,YearsOnJob)

print(score_record(117.17,137.71,26.64,"",167.65,186.61,177.16,197.1,116.13,156.33,64.27,112.49))
