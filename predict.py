# *** New Model: Removing "import pickle" and Creating a New Model***
import numpy as np
# Explanation of code change (Lawrence): One of the significant changes includes the replacement of the .pkl file/"pickle", with a new model class that has been called "MockModel", which can be seen a few lines below. This is because we were receiving an error message in regard to the file.  

def predict_readmission(
    Gender, Admission_Type, Diagnosis, Num_Lab_Procedures,
    Num_Medications, Num_Outpatient_Visits, Num_Inpatient_Visits,
    Num_Emergency_Visits, Num_Diagnoses, A1C_Result
):
    # Mock model logic
    class MockModel:
        def predict(self, data):
            # Explanation of code change (Lawrence): Prediction rule: Readmission likely if inpatient visits >= 2 and A1C is abnormal. This is a relatively simple rule that can be used within the predict function. Also, it allows for a more predictable outcome based on what is input by the user. Here, index 6 represents the amount of inpatient visits, while 9 is the A1C result.
            if data[0][6] >= 2 and data[0][9] == 0:
                return [1]
            return [0]

    model = MockModel()

    data = np.array([[
        Gender, Admission_Type, Diagnosis, Num_Lab_Procedures,
        Num_Medications, Num_Outpatient_Visits, Num_Inpatient_Visits,
        Num_Emergency_Visits, Num_Diagnoses, A1C_Result
    ]])

    prediction = model.predict(data)
    return prediction[0]


# ==== Input Section ====

selected_gender = input("Select a Gender (Female, Male, Other): ")
Gender = {"Female": 0, "Male": 1}.get(selected_gender, 2)

selected_admission_type = input("Select an Admission Type (Emergency, Urgent, Elective): ")
Admission_Type = {"Emergency": 1, "Urgent": 2}.get(selected_admission_type, 0)

selected_diagnosis = input("Select a Diagnosis (Heart Disease, Diabetes, Injury, Infection): ")
Diagnosis = {"Heart Disease": 1, "Diabetes": 0, "Injury": 3}.get(selected_diagnosis, 2)

Num_Lab_Procedures = int(input("Select a Number of Lab Procedures (1-99): "))
Num_Medications = int(input("Select a Number of Medications (1-35): "))
Num_Outpatient_Visits = int(input("Select a Number of Outpatient Visits (0-4): "))
Num_Inpatient_Visits = int(input("Select a Number of Inpatient Visits (0-4): "))
Num_Emergency_Visits = int(input("Select a Number of Emergency Visits (0-4): "))
Num_Diagnoses = int(input("Select a Number of Diagnoses (1-9): "))

A1C = input("Select an A1C Result (Normal, Abnormal): ")
A1C_Result = 1 if A1C == "Normal" else 0

# ==== Prediction ====

admission = predict_readmission(
    Gender, Admission_Type, Diagnosis, Num_Lab_Procedures,
    Num_Medications, Num_Outpatient_Visits, Num_Inpatient_Visits,
    Num_Emergency_Visits, Num_Diagnoses, A1C_Result
)

# ==== Output ====

if admission == 1:
    print("Readmission is Required")
else:
    print("Readmission is Not Required")
# *** Diet Added: "Diet" has been added as a new input parameter ***

import numpy as np

# Explanation of code change (Lawrence): Diet variable is now a part of the predict_readmission() function 
def predict_readmission(
    Gender, Admission_Type, Diagnosis, Num_Lab_Procedures,
    Num_Medications, Num_Outpatient_Visits, Num_Inpatient_Visits,
    Num_Emergency_Visits, Num_Diagnoses, A1C_Result, Diet
):
    # Mock model logic
    class MockModel:
        def predict(self, data):
            # Simulated prediction: readmission likely if inpatient visits >= 2 or diet is "Regular"
            # Explanation of code change (Lawrence): The highest index is now 10 for this model (as Diet has been added). The code is now saying that if the patient has 2 or more inpatient visits or is on a regular diet, they have a higher likelihood of being readmitted. 
            if data[0][6] >= 2 or data[0][10] == 0:  # 0 represents "Regular" diet
                return [1]
            return [0]

    model = MockModel()

    data = np.array([[
        Gender, Admission_Type, Diagnosis, Num_Lab_Procedures,
        Num_Medications, Num_Outpatient_Visits, Num_Inpatient_Visits,
        Num_Emergency_Visits, Num_Diagnoses, A1C_Result, Diet
    ]])

    prediction = model.predict(data)
    return prediction[0]


# ==== Input Section ====

selected_gender = input("Select a Gender (Female, Male, Other): ")
Gender = {"Female": 0, "Male": 1}.get(selected_gender, 2)

selected_admission_type = input("Select an Admission Type (Emergency, Urgent, Elective): ")
Admission_Type = {"Emergency": 1, "Urgent": 2}.get(selected_admission_type, 0)

selected_diagnosis = input("Select a Diagnosis (Heart Disease, Diabetes, Injury, Infection): ")
Diagnosis = {"Heart Disease": 1, "Diabetes": 0, "Injury": 3}.get(selected_diagnosis, 2)

Num_Lab_Procedures = int(input("Select a Number of Lab Procedures (1-99): "))
Num_Medications = int(input("Select a Number of Medications (1-35): "))
Num_Outpatient_Visits = int(input("Select a Number of Outpatient Visits (0-4): "))
Num_Inpatient_Visits = int(input("Select a Number of Inpatient Visits (0-4): "))
Num_Emergency_Visits = int(input("Select a Number of Emergency Visits (0-4): "))
Num_Diagnoses = int(input("Select a Number of Diagnoses (1-9): "))

A1C = input("Select an A1C Result (Normal, Abnormal): ")
A1C_Result = 1 if A1C == "Normal" else 0

# ==== New Diet Input ====
# Explanation of code change (Lawrence): A new input has been created. There are five diet types below, with "Regular" (which is assigned the value "0") being the default if nothing is input by the user.
selected_diet = input("Select a Diet (Regular, Renal, Cardiac, Diabetic, Low Sodium): ")
Diet = {
    "Regular": 0,
    "Renal": 1,
    "Cardiac": 2,
    "Diabetic": 3,
    "Low Sodium": 4
}.get(selected_diet, 0)  # Default to "Regular" if unknown

# ==== Prediction ====

admission = predict_readmission(
    Gender, Admission_Type, Diagnosis, Num_Lab_Procedures,
    Num_Medications, Num_Outpatient_Visits, Num_Inpatient_Visits,
    Num_Emergency_Visits, Num_Diagnoses, A1C_Result, Diet
)

# ==== Output ====

if admission == 1:
    print("Readmission is Required")
else:
    print("Readmission is Not Required")

# ***Prediction based on 3 conditions: Number of inpatient visits is greater than or equal to two, A1C is abnormal, or they are on a regular diet.***
import numpy as np

# Prediction function with 3 conditions
def predict_readmission(
    Gender, Admission_Type, Diagnosis, Num_Lab_Procedures,
    Num_Medications, Num_Outpatient_Visits, Num_Inpatient_Visits,
    Num_Emergency_Visits, Num_Diagnoses, A1C_Result, Diet
):
# Explanation of code change (Lawrence): The change below improves readability by assigning the names that represents each value (and their indices).
    class MockModel:
        def predict(self, data):
            inpatient_visits = data[0][6]
            diet = data[0][10]
            a1c = data[0][9]
# Explanation of code change (Lawrence): The three predictors from the previous two codes are now combined here. Unlike in those codes, this one has all three of them at once, contributing to a slightly more complex prediction rule. 
            # Predict readmission if any one condition is true
            if inpatient_visits >= 2 or diet == 0 or a1c == 0:
                return [1]
            return [0]

    model = MockModel()

    data = np.array([[
        Gender, Admission_Type, Diagnosis, Num_Lab_Procedures,
        Num_Medications, Num_Outpatient_Visits, Num_Inpatient_Visits,
        Num_Emergency_Visits, Num_Diagnoses, A1C_Result, Diet
    ]])

    prediction = model.predict(data)
    return prediction[0]


# ==== Input Section ====

selected_gender = input("Select a Gender (Female, Male, Other): ")
Gender = {"Female": 0, "Male": 1}.get(selected_gender, 2)

selected_admission_type = input("Select an Admission Type (Emergency, Urgent, Elective): ")
Admission_Type = {"Emergency": 1, "Urgent": 2}.get(selected_admission_type, 0)

selected_diagnosis = input("Select a Diagnosis (Heart Disease, Diabetes, Injury, Infection): ")
Diagnosis = {"Heart Disease": 1, "Diabetes": 0, "Injury": 3}.get(selected_diagnosis, 2)

Num_Lab_Procedures = int(input("Select a Number of Lab Procedures (1-99): "))
Num_Medications = int(input("Select a Number of Medications (1-35): "))
Num_Outpatient_Visits = int(input("Select a Number of Outpatient Visits (0-4): "))
Num_Inpatient_Visits = int(input("Select a Number of Inpatient Visits (0-4): "))
Num_Emergency_Visits = int(input("Select a Number of Emergency Visits (0-4): "))
Num_Diagnoses = int(input("Select a Number of Diagnoses (1-9): "))

A1C = input("Select an A1C Result (Normal, Abnormal): ")
A1C_Result = 1 if A1C == "Normal" else 0

selected_diet = input("Select a Diet (Regular, Renal, Cardiac, Diabetic, Low Sodium): ")
Diet = {
    "Regular": 0,
    "Renal": 1,
    "Cardiac": 2,
    "Diabetic": 3,
    "Low Sodium": 4
}.get(selected_diet, 0)  # Default to "Regular" if invalid

# ==== Prediction ====

admission = predict_readmission(
    Gender, Admission_Type, Diagnosis, Num_Lab_Procedures,
    Num_Medications, Num_Outpatient_Visits, Num_Inpatient_Visits,
    Num_Emergency_Visits, Num_Diagnoses, A1C_Result, Diet
)

# ==== Output ====

if admission == 1:
    print("Readmission is Required")
else:
    print("Readmission is Not Required")

# ***Prediction: Readmission if A1c is abnormal. Prioritize A1C over the other conditions***
import numpy as np

# Prediction function
def predict_readmission(
    Gender, Admission_Type, Diagnosis, Num_Lab_Procedures,
    Num_Medications, Num_Outpatient_Visits, Num_Inpatient_Visits,
    Num_Emergency_Visits, Num_Diagnoses, A1C_Result, Diet
):
    class MockModel:
        def predict(self, data):
            inpatient_visits = data[0][6]
            a1c = data[0][9]
            diet = data[0][10]
            # Explanation of code change (Lawrence): This block of code below is going to check whether or not A1C is normal, and if it is, then all other variables are ignored. This model assumes that a normal A1C equates to a low risk, thereby justifying a no readmission statement to be returned.   
            # Rule: If A1C is normal, there is no readmission regardless of the other factors
            if a1c == 1:
                return [0]
            elif inpatient_visits >= 2 or diet == 0:
                return [1]
            else:
                return [0]

    model = MockModel()

    data = np.array([[
        Gender, Admission_Type, Diagnosis, Num_Lab_Procedures,
        Num_Medications, Num_Outpatient_Visits, Num_Inpatient_Visits,
        Num_Emergency_Visits, Num_Diagnoses, A1C_Result, Diet
    ]])

    prediction = model.predict(data)
    return prediction[0]


# ==== User Input Section ====

selected_gender = input("Select a Gender (Female, Male, Other): ").strip()
Gender = {"Female": 0, "Male": 1}.get(selected_gender, 2)

selected_admission_type = input("Select an Admission Type (Emergency, Urgent, Elective): ").strip()
Admission_Type = {"Emergency": 1, "Urgent": 2}.get(selected_admission_type, 0)

selected_diagnosis = input("Select a Diagnosis (Heart Disease, Diabetes, Injury, Infection): ").strip()
Diagnosis = {"Heart Disease": 1, "Diabetes": 0, "Injury": 3}.get(selected_diagnosis, 2)

Num_Lab_Procedures = int(input("Select a Number of Lab Procedures (1-99): "))
Num_Medications = int(input("Select a Number of Medications (1-35): "))
Num_Outpatient_Visits = int(input("Select a Number of Outpatient Visits (0-4): "))
Num_Inpatient_Visits = int(input("Select a Number of Inpatient Visits (0-4): "))
Num_Emergency_Visits = int(input("Select a Number of Emergency Visits (0-4): "))
Num_Diagnoses = int(input("Select a Number of Diagnoses (1-9): "))

A1C = input("Select an A1C Result (Normal, Abnormal): ").strip()
A1C_Result = 1 if A1C.lower() == "normal" else 0

selected_diet = input("Select a Diet (Regular, Renal, Cardiac, Diabetic, Low Sodium): ").strip()
Diet = {
    "Regular": 0,
    "Renal": 1,
    "Cardiac": 2,
    "Diabetic": 3,
    "Low Sodium": 4
}.get(selected_diet, 0)  # Defaults to Regular if input is blank or invalid

# ==== Prediction ====

admission = predict_readmission(
    Gender, Admission_Type, Diagnosis, Num_Lab_Procedures,
    Num_Medications, Num_Outpatient_Visits, Num_Inpatient_Visits,
    Num_Emergency_Visits, Num_Diagnoses, A1C_Result, Diet
)

# ==== Output ====

if admission == 1:
    print("Readmission is Required")
else:
    print("Readmission is Not Required")

# ***Prediction with BMI added, along with weight (kilos) and height (meters) by extension***
import numpy as np

# Prediction function with BMI
def predict_readmission(
    Gender, Admission_Type, Diagnosis, Num_Lab_Procedures,
    Num_Medications, Num_Outpatient_Visits, Num_Inpatient_Visits,
    Num_Emergency_Visits, Num_Diagnoses, A1C_Result, Diet, BMI
):
    class MockModel:
        def predict(self, data):
            inpatient_visits = data[0][6]
            a1c = data[0][9]
            diet = data[0][10]
            bmi = data[0][11]
            # Explanation of code change (Lawrence): Readmission is required if BMI is 30 or more, as the BMI is now within the obese range. 
            # Logic:
            # If A1C is normal → no readmission
            if a1c == 1:
                return [0]
            # If BMI is 30 or more → readmission required
            elif bmi >= 30:
                return [1]
            # If inpatient visits are high or diet is regular
            elif inpatient_visits >= 2 or diet == 0:
                return [1]
            else:
                return [0]

    model = MockModel()

    data = np.array([[
        Gender, Admission_Type, Diagnosis, Num_Lab_Procedures,
        Num_Medications, Num_Outpatient_Visits, Num_Inpatient_Visits,
        Num_Emergency_Visits, Num_Diagnoses, A1C_Result, Diet, BMI
    ]])

    prediction = model.predict(data)
    return prediction[0]


# ==== User Input Section ====

selected_gender = input("Select a Gender (Female, Male, Other): ").strip()
Gender = {"Female": 0, "Male": 1}.get(selected_gender, 2)

selected_admission_type = input("Select an Admission Type (Emergency, Urgent, Elective): ").strip()
Admission_Type = {"Emergency": 1, "Urgent": 2}.get(selected_admission_type, 0)

selected_diagnosis = input("Select a Diagnosis (Heart Disease, Diabetes, Injury, Infection): ").strip()
Diagnosis = {"Heart Disease": 1, "Diabetes": 0, "Injury": 3}.get(selected_diagnosis, 2)

Num_Lab_Procedures = int(input("Select a Number of Lab Procedures (1-99): "))
Num_Medications = int(input("Select a Number of Medications (1-35): "))
Num_Outpatient_Visits = int(input("Select a Number of Outpatient Visits (0-4): "))
Num_Inpatient_Visits = int(input("Select a Number of Inpatient Visits (0-4): "))
Num_Emergency_Visits = int(input("Select a Number of Emergency Visits (0-4): "))
Num_Diagnoses = int(input("Select a Number of Diagnoses (1-9): "))

A1C = input("Select an A1C Result (Normal, Abnormal): ").strip()
A1C_Result = 1 if A1C.lower() == "normal" else 0

selected_diet = input("Select a Diet (Regular, Renal, Cardiac, Diabetic, Low Sodium): ").strip()
Diet = {
    "Regular": 0,
    "Renal": 1,
    "Cardiac": 2,
    "Diabetic": 3,
    "Low Sodium": 4
}.get(selected_diet, 0)  # Default to Regular if blank/invalid

# ==== BMI Input and Calculation ====
# Explanation of code change (Lawrence): Here, the user will input their height and weight, which will then determine the BMI below. The formula of BMI = weight_kg / (height_meters raised to the 2nd power) below will be used to determine the BMI category of the user. It is important to note that we are using the metric system formula, and not the imperial system one.
height_meters = float(input("Enter height in meters (e.g., 1.75): "))
weight_kg = float(input("Enter weight in kilograms (e.g., 70): "))

BMI = weight_kg / (height_meters ** 2)

# ==== BMI Classification ====
# Explanation of code change (Lawrence): Below is a block of code that determines the BMI, which will then classify an individual as underweight, normal weight, etc.
if BMI < 18.5:
    bmi_category = "Underweight"
elif 18.5 <= BMI < 24.9:
    bmi_category = "Normal weight"
elif 25 <= BMI < 29.9:
    bmi_category = "Overweight"
elif 30 <= BMI < 34.9:
    bmi_category = "Obesity (Class 1)"
elif 35 <= BMI < 39.9:
    bmi_category = "Severe Obesity (Class 2)"
else:
    bmi_category = "Morbid Obesity (Class 3)"

print(f"BMI: {BMI:.2f} - Category: {bmi_category}")

# ==== Prediction ====

admission = predict_readmission(
    Gender, Admission_Type, Diagnosis, Num_Lab_Procedures,
    Num_Medications, Num_Outpatient_Visits, Num_Inpatient_Visits,
    Num_Emergency_Visits, Num_Diagnoses, A1C_Result, Diet, BMI
)

# ==== Output ====

if admission == 1:
    print("Readmission is Required")
else:
    print("Readmission is Not Required")

# ***Prediction with Blood Glucose added as a condition for admission with BMI***
def calculate_bmi(weight, height):
    """Function to calculate BMI based on weight and height."""
    bmi = weight / (height ** 2)
    return bmi

def predict_readmission(Gender, Admission_Type, Diagnosis, Num_Lab_Procedures,
                        Num_Medications, Num_Outpatient_Visits, Num_Inpatient_Visits,
                        Num_Emergency_Visits, Num_Diagnoses, A1C_Result, Blood_Glucose, BMI):
    # Explanation of code change (Lawrence): If blood glucose is outside of the safe range (greater than or equal to 180 and less than or equal to 60), readmission is required. This because a blood glucose that is too low is the result of hypoglycemia, and one that is too high is hyperglycemia.
    # Check for blood glucose level conditions
    if Blood_Glucose <= 60 or Blood_Glucose >= 180:
        return 1  # Readmission is required

    # Check for BMI conditions
    if BMI >= 30:
        return 1  # Readmission is required

    # Check A1C
    if A1C_Result == 0:
        return 1  # Readmission required

    return 0  # No readmission required

# ==== User Input Section ====

selected_gender = input("Select a Gender (Female, Male, Other): ").strip()
Gender = {"Female": 0, "Male": 1}.get(selected_gender, 2)

selected_admission_type = input("Select an Admission Type (Emergency, Urgent, Elective): ").strip()
Admission_Type = {"Emergency": 1, "Urgent": 2}.get(selected_admission_type, 0)

selected_diagnosis = input("Select a Diagnosis (Heart Disease, Diabetes, Injury, Infection): ").strip()
Diagnosis = {"Heart Disease": 1, "Diabetes": 0, "Injury": 3}.get(selected_diagnosis, 2)

Num_Lab_Procedures = int(input("Select a Number of Lab Procedures (1-99): "))
Num_Medications = int(input("Select a Number of Medications (1-35): "))
Num_Outpatient_Visits = int(input("Select a Number of Outpatient Visits (0-4): "))
Num_Inpatient_Visits = int(input("Select a Number of Inpatient Visits (0-4): "))
Num_Emergency_Visits = int(input("Select a Number of Emergency Visits (0-4): "))
Num_Diagnoses = int(input("Select a Number of Diagnoses (1-9): "))

A1C = input("Select an A1C Result (Normal, Abnormal): ").strip()
A1C_Result = 1 if A1C.lower() == "normal" else 0

Diet = input("Select a Diet (Regular, Renal, Cardiac, Diabetic, Low Sodium): ").strip()
# Explanation of code change (Lawrence): Below, the patient will input their blood glucose levels. This is required, as otherwise, there will be no way to know whether or not a patient's blood glucose levels are normal.
Blood_Glucose = int(input("Enter the Blood Glucose Level (mg/dL): "))

# BMI Calculation
height = float(input("Enter height in meters (e.g., 1.75): "))
weight = float(input("Enter weight in kilograms (e.g., 70): "))
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

# ==== Prediction ====
admission = predict_readmission(Gender, Admission_Type, Diagnosis, Num_Lab_Procedures,
                                Num_Medications, Num_Outpatient_Visits, Num_Inpatient_Visits,
                                Num_Emergency_Visits, Num_Diagnoses, A1C_Result,
                                Blood_Glucose, BMI)

# ==== Output ====
if admission == 1:
    print("Readmission is Required")
else:
    print("Readmission is Not Required")

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



## ***Readmission based on 2 risk factors A1C and Blood Glucose level***

def calculate_bmi(weight, height):
    """Function to calculate BMI based on weight and height."""
    bmi = weight / (height ** 2)
    return bmi


def predict_readmission(Gender, Admission_Type, Diagnosis, Num_Lab_Procedures,Num_Medications, Num_Outpatient_Visits, Num_Inpatient_Visits,
                        Num_Emergency_Visits, Num_Diagnoses, A1C_Result, Blood_Glucose):
    
    # Readmission logic only based on A1C and Blood Glucose
    if Blood_Glucose <= 60 or Blood_Glucose >= 180:
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

# A1C percentage input
A1C_value = float(input("Enter A1C percentage (e.g., 5.6): "))
if A1C_value < 5.7:
    A1C_Result = "Normal"
elif A1C_value < 6.4:
    A1C_Result = "Prediabetes"
else:
    A1C_Result = "Abnormal"
print(f"A1C Category: {A1C_Result}")

# Diet (for reference, not used in logic yet)
Diet = input("Select a Diet (Regular, Renal, Cardiac, Diabetic, Low Sodium): ")

# Blood glucose input
Blood_Glucose = int(input("Enter the Blood Glucose Level (mg/dL): "))

# Height and weight for BMI
height = float(input("Enter height in meters (e.g., 1.75): "))
weight = float(input("Enter weight in kilograms (e.g., 70): "))

# Calculate BMI
BMI = calculate_bmi(weight, height)
print(f"BMI: {BMI:.2f}")

# BMI Category + Advisory
if BMI < 18.5:
    print("BMI Category: Underweight")
    print("Advisory: Being underweight may impact recovery. Please consult a doctor.")
elif BMI < 25:
    print("BMI Category: Normal")
elif BMI < 30:
    print("BMI Category: Overweight")
elif BMI < 35:
    print("BMI Category: Obese")
    print("Advisory: Consider speaking with your doctor about a healthy weight plan.")
else:
    print("BMI Category: Severely Obese (Class 3)")
    print("Advisory: Your BMI suggests severe obesity. Please consult your doctor for guidance.")

# Final prediction based on selected risk factors
admission = predict_readmission(Gender, Admission_Type, Diagnosis, Num_Lab_Procedures, Num_Medications,
                                Num_Outpatient_Visits, Num_Inpatient_Visits, Num_Emergency_Visits,
                                Num_Diagnoses, A1C_Result, Blood_Glucose)

# Final result
if admission == 1:
    print("Readmission is Required")
else:
    print("Readmission is Not Required")


# ***Prediction with Diagnosis changed to trigger readmission***
# *** Diagnosis list changed to reflect high risk diagnosis ***

def calculate_bmi(weight, height):
    """Function to calculate BMI based on weight and height."""
    return weight / (height ** 2)


def predict_readmission(Gender, Admission_Type, Diagnosis, Num_Lab_Procedures,Num_Medications, Num_Outpatient_Visits, Num_Inpatient_Visits,
                        Num_Emergency_Visits, Num_Diagnoses, A1C_Result, Blood_Glucose):

    high_risk_diagnoses = ["DKA", "HHS", "Severe Hypoglycemia", "Heart Failure","Acute Renal Failure", "Chronic Renal Failure",
        "Infections", "Uncontrolled Diabetes"]

    if Diagnosis in high_risk_diagnoses:
        return 1  # Readmission required due to critical condition

    if Blood_Glucose <= 60 or Blood_Glucose >= 180:
        return 1  # Readmission required due to blood glucose level

    if A1C_Result == "Abnormal":
        return 1  # Readmission required due to high A1C

    return 0  # No readmission required

#  Collect inputs from the user
Selected_gender = input("Select a Gender (Female, Male, Other): ")
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

# Diagnosis input with specific conditions
Selected_Diagnosis = input("Select a Diagnosis (DKA, HHS, Severe Hypoglycemia, Heart Failure, "
    "Acute Renal Failure, Chronic Renal Failure, Infections, Uncontrolled Diabetes, Other): ")

high_risk_diagnoses = ["DKA", "HHS", "Severe Hypoglycemia", "Heart Failure",
    "Acute Renal Failure", "Chronic Renal Failure","Infections", "Uncontrolled Diabetes"]

if Selected_Diagnosis in high_risk_diagnoses:
    print(" Critical Condition Detected: This condition often requires readmission.")

Num_Lab_Procedures = int(input("Select a Number of Lab Procedures (1-99): "))
Num_Medications = int(input("Select a Number of Medications (1-35): "))
Num_Outpatient_Visits = int(input("Select a Number of Outpatient Visits (0-4): "))
Num_Inpatient_Visits = int(input("Select a Number of Inpatient Visits (0-4): "))
Num_Emergency_Visits = int(input("Select a Number of Emergency Visits (0-4): "))
Num_Diagnoses = int(input("Select a Number of Diagnoses (1-9): "))

#  A1C percentage input
A1C_value = float(input("Enter A1C percentage (e.g., 5.6): "))
if A1C_value < 5.7:
    A1C_Result = "Normal"
elif A1C_value < 6.4:
    A1C_Result = "Prediabetes"
else:
    A1C_Result = "Abnormal"
print(f"A1C Category: {A1C_Result}")

#  Diet input (currently not used in logic)
Diet = input("Select a Diet (Regular, Renal, Cardiac, Diabetic, Low Sodium): ")

#  Blood glucose level
Blood_Glucose = int(input("Enter the Blood Glucose Level (mg/dL): "))

#  Height and weight for BMI
height = float(input("Enter height in meters (e.g., 1.75): "))
weight = float(input("Enter weight in kilograms (e.g., 70): "))

BMI = calculate_bmi(weight, height)
print(f"BMI: {BMI:.2f}")

#  BMI Category + Advisory
if BMI < 18.5:
    print("BMI Category: Underweight")
    print(" Advisory: Being underweight may impact recovery. Please consult a doctor.")
elif BMI < 25:
    print("BMI Category: Normal")
elif BMI < 30:
    print("BMI Category: Overweight")
elif BMI < 35:
    print("BMI Category: Obese")
    print(" Advisory: Consider speaking with your doctor about a healthy weight plan.")
else:
    print("BMI Category: Severely Obese (Class 3)")
    print(" Advisory: Your BMI suggests severe obesity. Please consult your doctor for guidance.")

# Predict readmission
admission = predict_readmission(Gender, Admission_Type, Selected_Diagnosis, Num_Lab_Procedures,
                                Num_Medications, Num_Outpatient_Visits, Num_Inpatient_Visits,
                                Num_Emergency_Visits, Num_Diagnoses, A1C_Result, Blood_Glucose)

#  Final output
if admission == 1:
    print("Readmission is Required")
else:
    print("Readmission is Not Required")


## *** Risk Score added to the model***
## *** A1C, Blood Glucose and Diagnosis determine the readmission prediction ***
def calculate_bmi(weight, height):
    return weight / (height ** 2)

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal"
    elif 25 <= bmi < 30:
        return "Overweight"
    elif 30 <= bmi < 35:
        return "Obese"
    else:
        return "Severely Obese (Class 3)"

def predict_readmission(Gender, Admission_Type, Diagnosis, Num_Lab_Procedures,
                        Num_Medications, Num_Outpatient_Visits, Num_Inpatient_Visits,
                        Num_Emergency_Visits, Num_Diagnoses, A1C_Value,
                        Blood_Glucose, Diet, Height, Weight):

    risk_score = 0
    reasons = []

    # Diagnosis check (case-insensitive)
    high_risk_diagnoses = ["dka", "hhs", "severe hypoglycemia", "heart failure",
        "acute renal failure", "chronic renal failure", "infections", "uncontrolled diabetes"]
    if Diagnosis.lower() in high_risk_diagnoses:
        risk_score += 1
        reasons.append("High-risk medical condition (e.g., DKA, HHS, Severe Hypoglycemia, etc.)")

    # A1C check

    if A1C_Value >= 6.4:
        risk_score += 1
        reasons.append(f"Abnormal A1C (≥ 6.4%) - A1C: {A1C_Value}%")
    elif 5.7 <= A1C_Value < 6.4:
        reasons.append(f"Prediabetes A1C (5.7–6.3%) - A1C: {A1C_Value}%")
    else:
        reasons.append(f"Normal A1C (< 5.7%) - A1C: {A1C_Value}%")

    # Blood glucose check
    if Blood_Glucose <= 60:
        risk_score += 1
        reasons.append(f"Low blood glucose (≤ 60 mg/dL) - Blood Glucose: {Blood_Glucose} mg/dL")
    elif Blood_Glucose > 180:
        risk_score += 1
        reasons.append(f"High blood glucose (> 180 mg/dL) - Blood Glucose: {Blood_Glucose} mg/dL")
    else:
        reasons.append(f"Normal blood glucose (70–140 mg/dL) - Blood Glucose: {Blood_Glucose} mg/dL")

    # Calculate BMI
    bmi = calculate_bmi(Weight, Height)
    bmi_category = classify_bmi(bmi)

    # Determine final decision
    if risk_score >= 3:
        status = "Readmission is Required"
    elif risk_score >= 1:
        status = "Monitor Patient Closely"
    else:
        status = "Readmission is Not Required"

    # Output section
    print(f"\nBMI: {bmi:.2f}")
    print(f"BMI Category: {bmi_category}")
    if bmi >= 30:
        print("Advisory: Consider speaking with your doctor about a healthy weight plan.")

    # Reason explanation in a sentence
    print(f"\nReadmission is required due to: {', '.join(reasons)}")
    print(f"\nRisk Score: {risk_score}")
    print(f"Final Decision: {status}")

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

Selected_Diagnosis = input("Select a Diagnosis (DKA, HHS, Severe Hypoglycemia, Heart Failure, Acute Renal Failure, Chronic Renal Failure, Infections, Uncontrolled Diabetes, Other): ")
if Selected_Diagnosis.lower() in ["dka", "hhs", "severe hypoglycemia", "heart failure", "acute renal failure", "chronic renal failure", "infections", "uncontrolled diabetes"]:
    Diagnosis = Selected_Diagnosis.lower()
else:
    Diagnosis = "Other"

Num_Lab_Procedures = int(input("Select a Number of Lab Procedures (1-99): "))
Num_Medications = int(input("Select a Number of Medications (1-35): "))
Num_Outpatient_Visits = int(input("Select a Number of Outpatient Visits (0-4): "))
Num_Inpatient_Visits = int(input("Select a Number of Inpatient Visits (0-4): "))
Num_Emergency_Visits = int(input("Select a Number of Emergency Visits (0-4): "))
Num_Diagnoses = int(input("Select a Number of Diagnoses (1-9): "))

A1C_Value = float(input("Enter A1C percentage (e.g., 5.6): "))

Diet = input("Select a Diet (Regular, Renal, Cardiac, Diabetic, Low Sodium): ")

Blood_Glucose = int(input("Enter the Blood Glucose Level (mg/dL): "))

Height = float(input("Enter height in meters (e.g., 1.75): "))
Weight = float(input("Enter weight in kilograms (e.g., 70): "))

# Prediction based on the inputs
predict_readmission(Gender, Admission_Type, Diagnosis, Num_Lab_Procedures, 
                    Num_Medications, Num_Outpatient_Visits, Num_Inpatient_Visits, 
                    Num_Emergency_Visits, Num_Diagnoses, A1C_Value, Blood_Glucose, 
                    Diet, Height, Weight)



### *** Age added to the model but not a risk factor ***

def calculate_bmi(weight, height):
    return weight / (height ** 2)

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal"
    elif 25 <= bmi < 30:
        return "Overweight"
    elif 30 <= bmi < 35:
        return "Obese"
    else:
        return "Severely Obese (Class 3)"

def predict_readmission(Age, Gender, Admission_Type, Diagnosis, Num_Lab_Procedures, Num_Medications, Num_Outpatient_Visits, Num_Inpatient_Visits,
                        Num_Emergency_Visits, Num_Diagnoses, A1C_Value, Blood_Glucose, Diet, Height, Weight):

    risk_score = 0
    reasons = []

    # Diagnosis check

    high_risk_diagnoses = [
        "dka", "hhs", "severe hypoglycemia", "heart failure",
        "acute renal failure", "chronic renal failure",
        "infections", "uncontrolled diabetes"]
    if Diagnosis.lower() in high_risk_diagnoses:
        risk_score += 1
        reasons.append(f"High-risk diagnosis ({Diagnosis.title()})")

    # A1C check
    if A1C_Value >= 6.4:
        risk_score += 1
        reasons.append(f"Abnormal A1C (≥ 6.4%) - A1C: {A1C_Value}%")
    elif 5.7 <= A1C_Value < 6.4:
        reasons.append(f"Prediabetes A1C (5.7–6.3%) - A1C: {A1C_Value}%")
    else:
        reasons.append(f"Normal A1C (< 5.7%) - A1C: {A1C_Value}%")

    # Blood glucose check
    if Blood_Glucose <= 60:
        risk_score += 1
        reasons.append(f"Low blood glucose (≤ 60 mg/dL) - Blood Glucose: {Blood_Glucose} mg/dL")
    elif Blood_Glucose > 180:
        risk_score += 1
        reasons.append(f"High blood glucose (> 180 mg/dL) - Blood Glucose: {Blood_Glucose} mg/dL")
    else:
        reasons.append(f"Normal blood glucose (70–140 mg/dL) - Blood Glucose: {Blood_Glucose} mg/dL")

    # Calculate BMI

    bmi = calculate_bmi(Weight, Height)
    bmi_category = classify_bmi(bmi)

    # Final readmission decision
    if risk_score >= 3:
        status = "Readmission is Required"
    elif risk_score >= 1:
        status = "Monitor Patient Closely"
    else:
        status = "Readmission is Not Required"

    # Output

    print(f"\nPatient Age: {Age}")
    print(f"BMI: {bmi:.2f}")
    print(f"BMI Category: {bmi_category}")
    if bmi >= 30:
        print("Advisory: Consider speaking with your doctor about a healthy weight plan.")

    print("\nReason(s) considered:")
    for reason in reasons:
        print(f"- {reason}")

    print(f"\nRisk Score: {risk_score}")
    print(f"Final Decision: {status}")

# Collect inputs from the user

Age = int(input("Enter Age: "))

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

Selected_Diagnosis = input("Select a Diagnosis (DKA, HHS, Severe Hypoglycemia, Heart Failure, Acute Renal Failure, Chronic Renal Failure, Infections, Uncontrolled Diabetes, Other): ")
if Selected_Diagnosis.lower() in ["dka", "hhs", "severe hypoglycemia", "heart failure", "acute renal failure", "chronic renal failure", "infections", "uncontrolled diabetes"]:
    Diagnosis = Selected_Diagnosis.lower()
else:
    Diagnosis = "Other"

Num_Lab_Procedures = int(input("Select a Number of Lab Procedures (1-99): "))
Num_Medications = int(input("Select a Number of Medications (1-35): "))
Num_Outpatient_Visits = int(input("Select a Number of Outpatient Visits (0-4): "))
Num_Inpatient_Visits = int(input("Select a Number of Inpatient Visits (0-4): "))
Num_Emergency_Visits = int(input("Select a Number of Emergency Visits (0-4): "))
Num_Diagnoses = int(input("Select a Number of Diagnoses (1-9): "))

A1C_Value = float(input("Enter A1C percentage (e.g., 5.6): "))
Diet = input("Select a Diet (Regular, Renal, Cardiac, Diabetic, Low Sodium): ")
Blood_Glucose = int(input("Enter the Blood Glucose Level (mg/dL): "))
Height = float(input("Enter height in meters (e.g., 1.75): "))
Weight = float(input("Enter weight in kilograms (e.g., 70): "))

# Predict

predict_readmission(Age, Gender, Admission_Type, Diagnosis, Num_Lab_Procedures, Num_Medications, Num_Outpatient_Visits, Num_Inpatient_Visits, 
                    Num_Emergency_Visits, Num_Diagnoses, A1C_Value, Blood_Glucose, Diet, Height, Weight)



## **** Medication adherence added to the model ****

def predict_readmission(Age, Gender, Admission_Type, Diagnosis, Num_Lab_Procedures,Num_Medications, Num_Outpatient_Visits, Num_Inpatient_Visits,
                        Num_Emergency_Visits, Num_Diagnoses, A1C_Value, Blood_Glucose, Diet, Height, Weight, Med_Adherence):

    reasons = []  # List to store reasons for readmission
    risk_score = 0  # Tracks overall risk score

    # Dictionary of high-risk conditions
    high_risk_conditions = (("DKA", "Diabetic Ketoacidosis"),("HHS", "Hyperosmolar Hyperglycemic State"),
        ("Severe Hypoglycemia", "Severe drop in blood sugar"), ("Heart Failure", "Chronic heart condition"),
        ("Acute Renal Failure", "Sudden kidney failure"),("Chronic Renal Failure", "Long-term kidney disease"),
        ("Infections", "Various types of infections"),("Uncontrolled Diabetes", "Poorly managed diabetes"))

    # Check for age-related risk
    if Age >= 45:
        risk_score += 1
        reasons.append(f"Age 45 or above may increase the risk of readmission.")

    # Check for admission type
    if Admission_Type == "Emergency":
        risk_score += 1
        reasons.append(f"Emergency admission increases readmission risk.")

    # Check if diagnosis is in high-risk conditions
    for condition in high_risk_conditions:
        if Diagnosis == condition[0]:
            risk_score += 1
            reasons.append(f"Diagnosis of {condition[0]} ({condition[1]}) is a high-risk condition for readmission.")

    # Check A1C value (blood sugar control indicator)
    if A1C_Value >= 6.4:
        risk_score += 1
        reasons.append(f"Abnormal A1C (≥ 6.4%) - A1C: {A1C_Value}%")

    # Check blood glucose levels for abnormal values
    if Blood_Glucose <= 60:
        risk_score += 1
        reasons.append(f"Low blood glucose (≤ 60 mg/dL) - Blood Glucose: {Blood_Glucose} mg/dL")
    elif Blood_Glucose >= 180:
        risk_score += 1
        reasons.append(f"High blood glucose (≥ 180 mg/dL) - Blood Glucose: {Blood_Glucose} mg/dL")

    # Check diet-related risk
    if Diet == "Regular":
        risk_score += 1
        reasons.append(f"Regular diet may increase the risk of readmission.")

    # Store medication adherence information (not affecting risk score)
    if Med_Adherence == "yes":
        reasons.append(f"Patient reports taking medications regularly.")
    else:
        reasons.append(f"Patient reports non-adherence to prescribed medications.")

    # Calculate BMI (Body Mass Index)
    BMI = Weight / (Height ** 2)

    # Categorize BMI status
    if BMI < 18.5:
        BMI_Category = "Underweight"
    elif 18.5 <= BMI < 24.9:
        BMI_Category = "Normal weight"
    elif 25 <= BMI < 29.9:
        BMI_Category = "Overweight"
    else:
        BMI_Category = "Obese"

    # Record BMI information
    reasons.append(f"BMI: {format(BMI, '.2f')} - BMI Category: {BMI_Category}")

    # Determine readmission requirement based on risk score
    if risk_score >= 3:
        return (f"\nReadmission is Required due to:\n"  # Added a newline before the statement
                f"Reason(s) considered:\n"
                + "\n".join([f"- {reason}" for reason in reasons]) + f"\n\n"
                f"Risk Score: {risk_score}\n"
                f"Final Decision: Readmission is Required")
    else:
        return (f"\nReadmission is Not Required due to:\n"  # Added a newline before the statement
                f"Reason(s) considered:\n"
                + "\n".join([f"- {reason}" for reason in reasons]) + f"\n\n"
                f"Risk Score: {risk_score}\n"
                f"Final Decision: Readmission is Not Required")

# Collect inputs from the user
print("Enter patient information below:")

Age = int(input("Enter your age: "))
Gender = input("Select a Gender (Female, Male, Other): ").strip()
Admission_Type = input("Select an Admission Type (Emergency, Urgent, Elective): ").strip()
Diagnosis = input("Select a Diagnosis (DKA, HHS, Severe Hypoglycemia, Heart Failure, Acute Renal Failure, Chronic Renal Failure, Infections, Uncontrolled Diabetes, Other): ").strip()
Num_Lab_Procedures = int(input("Select a Number of Lab Procedures (1-99): "))
Num_Medications = int(input("Select a Number of Medications (1-35): "))
Num_Outpatient_Visits = int(input("Select a Number of Outpatient Visits (0-4): "))
Num_Inpatient_Visits = int(input("Select a Number of Inpatient Visits (0-4): "))
Num_Emergency_Visits = int(input("Select a Number of Emergency Visits (0-4): "))
Num_Diagnoses = int(input("Select a Number of Diagnoses (1-9): "))
A1C_Value = float(input("Enter A1C percentage (e.g., 5.6): "))
Blood_Glucose = int(input("Enter the Blood Glucose Level (mg/dL): "))
Diet = input("Select a Diet (Regular, Renal, Cardiac, Diabetic, Low Sodium): ").strip()
Height = float(input("Enter height in meters (e.g., 1.75): "))
Weight = float(input("Enter weight in kilograms (e.g., 70): "))
Med_Adherence = input("Are you currently taking your prescribed medications regularly? (Yes/No): ").strip().lower()

# Make readmission prediction based on inputs
admission = predict_readmission(Age, Gender, Admission_Type, Diagnosis, Num_Lab_Procedures, Num_Medications, Num_Outpatient_Visits, Num_Inpatient_Visits,
Num_Emergency_Visits, Num_Diagnoses, A1C_Value, Blood_Glucose, Diet, Height, Weight, Med_Adherence)

# Display the result
print(admission)



# ***Original version retained for reference ***
# ***Original code kept for reference***
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
