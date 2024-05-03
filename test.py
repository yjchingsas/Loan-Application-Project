import pickle
import numpy as np
import pandas as pd

# Load pickle file objects
with open('Loan_Application_Project_MM_e64e0df0-7986-4dff-93d1-4da08b6b931d/Version 1/scikit-learn_RandomForest/rf_V3_11_5.pkl', 'rb') as f:
    imputer = pickle.load(f)
    ohe = pickle.load(f)
    model = pickle.load(f)

def score_method(DELINQUENCIES, DEROGATORYMARKS, INQUIRIES, CREDLINEAGE, CREDLINES, DEBTINCRATIO, LOANREQUEST, HOMEVALUE, INCOME, LOANTOVALUE, YEARSONJOB):
    "Output: P_DEFAULT0, P_DEFAULT1, I_DEFAULT"

    # Create single row dataframe
    record = pd.DataFrame([[DELINQUENCIES, DEROGATORYMARKS, INQUIRIES, CREDLINEAGE, CREDLINES, DEBTINCRATIO, LOANREQUEST, HOMEVALUE, INCOME, LOANTOVALUE, YEARSONJOB]],\
             columns=['DELINQUENCIES', 'DEROGATORYMARKS', 'INQUIRIES', 'CREDLINEAGE', 'CREDLINES', 'DEBTINCRATIO', 'LOANREQUEST', 'HOMEVALUE', 'INCOME', 'LOANTOVALUE', 'YEARSONJOB'])

    dm_class_input = ["DELINQUENCIES", "DEROGATORYMARKS", "INQUIRIES"]
    dm_interval_input = ["CREDLINEAGE","CREDLINES","DEBTINCRATIO","HOMEVALUE","INCOME","LOANREQUEST" ,"LOANTOVALUE","YEARSONJOB"]

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

def test_function_is_tuple():
    assert type(score_method(14.20,155.73,111.31,20.73,186.01,181.01,26.61,78.94,29.21,5.14,100.91)) is tuple

def test_output_scores():
    assert score_method(14.20,155.73,111.31,20.73,186.01,181.01,26.61,78.94,29.21,5.14,100.91)[0] + score_method(14.20,155.73,111.31,20.73,186.01,181.01,26.61,78.94,29.21,5.14,100.91)[1] == 1.0

def test_output_result():
    assert type(score_method(14.20,155.73,111.31,20.73,186.01,181.01,26.61,78.94,29.21,5.14,100.91)[2]) is str