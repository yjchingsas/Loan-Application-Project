import settings_b1317393_c264_41eb_9e5c_986d501f5582
dm_pklname = '_1H3TZJO257GBCD9E09DRHLI76_PKL.pickle'
dm_class_input = ["Delinquencies","DerogatoryMarks","Inquiries","JobType"]
dm_interval_input = ["CredLineAge","CredLines","DebtIncRatio","HomeValue","Income","LoanRequest" ,"LoanToValue","YearsOnJob"]

import pickle
import numpy as np
import pandas as pd

# Load pickle file objects
with open(settings_b1317393_c264_41eb_9e5c_986d501f5582.pickle_path + '/' + dm_pklname, 'rb') as f:
    imputer = pickle.load(f)
    ohe = pickle.load(f)
    model = pickle.load(f)

def score_method(Delinquencies, DerogatoryMarks, Inquiries, JobType, CredLineAge, CredLines, DebtIncRatio, LoanRequest, HomeValue, Income, LoanToValue, YearsOnJob):
    "Output: P_Default0, P_Default1, I_Default"

    # Create single row dataframe
    record = pd.DataFrame([[Delinquencies, DerogatoryMarks, Inquiries, JobType, CredLineAge, CredLines, DebtIncRatio, LoanRequest, HomeValue, Income, LoanToValue, YearsOnJob]],\
             columns=['Delinquencies', 'DerogatoryMarks', 'JobType', 'Inquiries', 'CredLineAge', 'CredLines', 'DebtIncRatio', 'LoanRequest', 'HomeValue', 'Income', 'LoanToValue', 'YearsOnJob'])

    dm_class_input = ["Delinquencies", "DerogatoryMarks", "Inquiries", "JobType"]
    dm_interval_input = ["CredLineAge","CredLines","DebtIncRatio","HomeValue","Income","LoanRequest" ,"LoanToValue","YearsOnJob"]

    # Impute interval missing values to median if needed
    rec_intv = record[dm_interval_input]
    rec_intv_imp = imputer.transform(rec_intv)

    # One-hot encode class inputs, unknown levels are set to all 0s
    rec_class = record[dm_class_input].applymap(str)
    rec_class_ohe = ohe.transform(rec_class).toarray()

    # Score data passed to this method
    rec = np.concatenate((rec_intv_imp, rec_class_ohe), axis=1)
    rec_pred_prob = model.predict_proba(rec)
    rec_pred = model.predict(rec)

    return float(rec_pred_prob[0][0]), float(rec_pred_prob[0][1]), str(float(rec_pred[0]))
