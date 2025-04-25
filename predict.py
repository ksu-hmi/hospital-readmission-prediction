# ***Readmission prediction is based on A1C level, BMI and Blood Glucose level***

def calculate_bmi(weight, height):
    """Function to calculate BMI based on weight and height."""
    bmi = weight / (height ** 2)
    return bmi

def predict_readmission(Gender, Admission_Type, Diagnosis, Num_Lab_Procedures,
                        Num_Medications, Num_Outpatient_Visits, Num_Inpatient_Visits,
                        Num_Emergency_Visits, Num_Diagnoses, A1C_Result, Blood_Glucose,
                        BMI):

    # Readmission logic based on risk factors
    if Blood_Glucose <= 60 or Blood_Glucose >= 180:
        return 1  # Readmission is required

    if BMI >= 30:
        return 1  # Readmission is required

    if A1C_Result == "Abnormal":
        return 1  # Readmission is required

    return 0  # No readmission required


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

# A1C Percentage Input
A1C_value = float(input("Enter A1C percentage (e.g., 5.6): "))

if A1C_value < 5.7:
    A1C_Result = "Normal"
elif A1C_value < 6.4:
    A1C_Result = "Prediabetes"
else:
    A1C_Result = "Abnormal"

print(f"A1C Category: {A1C_Result}")

# Diet input (not currently affecting logic, but kept for completeness)
Diet = input("Select a Diet (Regular, Renal, Cardiac, Diabetic, Low Sodium): ")

# **Blood glucose level input**
Blood_Glucose = int(input("Enter the Blood Glucose Level (mg/dL): "))

# **Height and weight for BMI**
height = float(input("Enter height in meters (e.g., 1.75): "))
weight = float(input("Enter weight in kilograms (e.g., 70): "))

# Calculate and categorize BMI
BMI = calculate_bmi(weight, height)
print(f"BMI: {BMI:.2f}")

if BMI < 18.5:
    print("BMI Category: Underweight")
elif BMI < 25:
    print("BMI Category: Normal")
elif BMI < 30:
    print("BMI Category: Overweight")
elif BMI < 35:
    print("BMI Category: Obese")
else:
    print("BMI Category: Severely Obese (Class 3)")

#  Prediction based on all inputs
admission = predict_readmission(Gender, Admission_Type, Diagnosis, Num_Lab_Procedures, 
                                Num_Medications, Num_Outpatient_Visits, Num_Inpatient_Visits, 
                                Num_Emergency_Visits, Num_Diagnoses, A1C_Result, Blood_Glucose, BMI)
#  Final decision
if admission == 1:
    print("Readmission is Required")
else:
    print("Readmission is Not Required")


#***Original code kept for reference***
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
