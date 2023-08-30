
import pickle
import numpy as np
import pandas as pd

picklepath = "Loan Application Project/unzipped/b1317393-c264-41eb-9e5c-986d501f5582"
dm_pklname = '_56LIKLGYGP1YOKC3M2XXT7Y6H_PKL.pickle'
dm_class_input = ["Delinquencies","DerogatoryMarks","Inquiries","JobType"]
dm_interval_input = ["CredLineAge","CredLines","DebtIncRatio","HomeValue","Income","LoanRequest" ,"LoanToValue","YearsOnJob"]

with open(picklepath+ '/'+ dm_pklname, 'rb') as f:
    ohe = pickle.load(f)
    model = pickle.load(f)

def score_record(Delinquencies, DerogatoryMarks, Inquiries, JobType, CredLineAge, CredLines, DebtIncRatio, LoanRequest, HomeValue, Income, LoanToValue, YearsOnJob):
    "Output: P_Default0, P_Default1, I_Default"

    record = pd.DataFrame([[Delinquencies, DerogatoryMarks, Inquiries, JobType, CredLineAge, CredLines, DebtIncRatio, LoanRequest, HomeValue, Income, LoanToValue, YearsOnJob]],\
             columns=dm_class_input + dm_interval_input)

    rec_intv = record[dm_interval_input]

    rec_class = record[dm_class_input].applymap(str)
    rec_class_ohe = ohe.transform(rec_class).toarray()

    rec = np.concatenate((rec_intv, rec_class_ohe), axis=1)
    rec_pred_prob = model.predict_proba(rec)
    rec_pred = model.predict(rec)

    return float(rec_pred_prob[0][0]), float(rec_pred_prob[0][1]), str(float(rec_pred[0]))

def test_function_is_tuple():
    assert type(score_record(14.20,155.73,111.31,"",20.73,186.01,181.01,26.61,78.94,29.21,5.14,100.91)) is tuple

def test_output_scores():
    assert score_record(14.20,155.73,111.31,"",20.73,186.01,181.01,26.61,78.94,29.21,5.14,100.91)[0] + score_record(14.20,155.73,111.31,"",20.73,186.01,181.01,26.61,78.94,29.21,5.14,100.91)[1] == 1.0

def test_output_result():
    assert type(score_record(14.20,155.73,111.31,"",20.73,186.01,181.01,26.61,78.94,29.21,5.14,100.91)[2]) is str


# import pickle
# import numpy as np
# import pandas as pd

# picklepath = "/home/ssayjc/AFinal_Commit_Projects/A_PROJECTS/Loan-Application-Project/Python_GradientBoost__Pipeline_1_"
# dm_pklname = '_56LIKLGYGP1YOKC3M2XXT7Y6H_PKL.pickle'

# dm_class_input = ["Delinquencies","DerogatoryMarks","Inquiries","JobType"]
# dm_interval_input = ["CredLineAge","CredLines","DebtIncRatio","HomeValue","Income","LoanRequest" ,"LoanToValue","YearsOnJob"]

# with open(picklepath+ '/'+ dm_pklname, 'rb') as f:
#     ohe = pickle.load(f)
#     model = pickle.load(f)

# def score_method(Delinquencies, DerogatoryMarks, Inquiries, JobType, CredLineAge, CredLines, DebtIncRatio, LoanRequest, HomeValue, Income, LoanToValue, YearsOnJob):
#     "Output: P_Default0, P_Default1, I_Default"

#     record = pd.DataFrame([[Delinquencies, DerogatoryMarks, Inquiries, JobType, CredLineAge, CredLines, DebtIncRatio, LoanRequest, HomeValue, Income, LoanToValue, YearsOnJob]],\
#              columns=dm_class_input + dm_interval_input)

#     rec_intv = record[dm_interval_input]

#     rec_class = record[dm_class_input].applymap(str)
#     rec_class_ohe = ohe.transform(rec_class).toarray()

#     rec = np.concatenate((rec_intv, rec_class_ohe), axis=1)
#     rec_pred_prob = model.predict_proba(rec)
#     rec_pred = model.predict(rec)

#     return float(rec_pred_prob[0][0]), float(rec_pred_prob[0][1]), str(float(rec_pred[0]))


# score_record(14.20,155.73,111.31,"",20.73,186.01,181.01,26.61,78.94,29.21,5.14,100.91)