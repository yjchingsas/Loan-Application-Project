import settings
dm_pklname = '_DJ5N7WG1NE74BJO4LN9LUR5FZ_PKL.pickle'
dm_class_input = ["Delinquencies","DerogatoryMarks","Inquiries","JobType"]
dm_interval_input = ["CredLineAge","CredLines","DebtIncRatio","HomeValue","Income","LoanRequest" ,"LoanToValue","YearsOnJob"]

import pickle
import numpy as np
import pandas as pd

with open(settings.pickle_path + '/' + dm_pklname, 'rb') as f:
    ohe = pickle.load(f)
    model = pickle.load(f)

def score_method(Delinquencies, DerogatoryMarks, Inquiries, JobType, CredLineAge, CredLines, DebtIncRatio, LoanRequest, HomeValue, Income, LoanToValue, YearsOnJob):
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
