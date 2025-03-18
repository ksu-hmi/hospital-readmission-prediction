import numpy as np
import pickle

def predict_readmission(Gender, Admission_Type, Diagnosis, Num_Lab_Procedures,
                        Num_Medications, Num_Outpatient_Visits, Num_Inpatient_Visits,
                        Num_Emergency_Visits, Num_Diagnoses, A1C_Result):

    # Load the model
    with open("Readmission_Model.pkl", "rb") as m:
        model = pickle.load(m)
    
    # Prepare data for prediction
    data = np.array([[Gender, Admission_Type, Diagnosis, Num_Lab_Procedures,
                      Num_Medications, Num_Outpatient_Visits, Num_Inpatient_Visits,
                      Num_Emergency_Visits, Num_Diagnoses, A1C_Result]])
    
    # Predict and return the result
    prediction = model.predict(data)
    out = prediction[0]
    return out 


# Collect inputs from the user
selected_gender = input("Select a Gender (Female, Male, Other): ")
if selected_gender == "Female":
    Gender = 0
elif selected_gender == "Male":
    Gender = 1
else:
    Gender = 2

Selected_Admission_Type = input("Select an Admission Type (Emergency, Urgent, Elective): ")
if Selected_Admission_Type == "Emergency":
    Admission_Type = 1
elif Selected_Admission_Type == "Urgent":
    Admission_Type = 2
else:
    Admission_Type = 0

Selected_Diagnosis = input("Select a Diagnosis (Heart Disease, Diabetes, Injury, Infection): ")
if Selected_Diagnosis == "Heart Disease":
    Diagnosis = 1
elif Selected_Diagnosis == "Diabetes":
    Diagnosis = 0
elif Selected_Diagnosis == "Injury":
    Diagnosis = 3
else:
    Diagnosis = 2

Num_Lab_Procedures = int(input("Select a Number of Lab Procedures (1-99): "))
Num_Medications = int(input("Select a Number of Medications (1-35): "))
Num_Outpatient_Visits = int(input("Select a Number of Outpatient Visits (0-4): "))
Num_Inpatient_Visits = int(input("Select a Number of Inpatient Visits (0-4): "))
Num_Emergency_Visits = int(input("Select a Number of Emergency Visits (0-4): "))
Num_Diagnoses = int(input("Select a Number of Diagnoses (1-9): "))

A1C = input("Select an A1C Result (Normal, Abnormal): ")
if A1C == "Normal":
    A1C_Result = 1
else:
    A1C_Result = 0

# Prediction based on the inputs
admission = predict_readmission(Gender, Admission_Type, Diagnosis, Num_Lab_Procedures, 
                                Num_Medications, Num_Outpatient_Visits, Num_Inpatient_Visits, 
                                Num_Emergency_Visits, Num_Diagnoses, A1C_Result)

# Display the result
if admission == 1:
    print("Readmission is Required")
else:
    print("Readmission is Not Required")
