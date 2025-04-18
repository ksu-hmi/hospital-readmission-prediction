# **Target Users**
- Healthcare Providers: To identify and support high-risk diabetic patients.
- Patients: To receive more personalized care and avoid unplanned readmissions.

# **Tools & Technologies**
- Python, Jupyter Notebooks                                                                                                          - -
- GitHub for collaboration and version control

# **Original Project Info (Retained Below for Reference)** Lawrence (Larry706)

# **Hospital Readmission Prediction**  

## **Overview**  
This project predicts hospital readmissions within 30 days of discharge and analyzes A1C levels for diabetes patients. The goal is to help healthcare professionals identify high-risk patients and optimize treatment plans.  

## **Project Structure**  
```
hospital-readmission-prediction
│── data
│   ├── hospital_readmissions.csv
│── A1C_Model.ipynb
│── A1C_Model.pkl
│── Readmitted_Model.ipynb
│── Readmission_Model.pkl
│── Replacing_A1C.ipynb
│── predict.py
│── requirements.txt
│── README.md
```
- **A1C_Model.ipynb** - Machine learning model for A1C analysis.  
- **Readmitted_Model.ipynb** - Predictive model for hospital readmissions.  
- **Replacing_A1C.ipynb** - Data preprocessing and feature engineering for A1C.  
- **predict.py** - Script to test the trained model.  
- **hospital_readmissions.csv** - Initial dataset for model training.  
- **Readmission_Model.pkl** - Trained readmission prediction model.  
- **A1C_Model.pkl** - Trained A1C analysis model.  

## **Installation**  
1. Clone the repository:  
   ```bash
   git clone https://github.com/KaushikBiswalXD/hospital-readmission-prediction.git
   cd hospital-readmission-prediction
   ```
2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```

## **Training the Model**  
Run the Jupyter Notebooks in the following order:  
1. `Replacing_A1C.ipynb` - Preprocesses A1C data.  
2. `A1C_Model.ipynb` - Builds and evaluates the A1C model.  
3. `Readmitted_Model.ipynb` - Trains and tests the readmission prediction model.  
4. The trained model is saved as **Readmission_Model.pkl**.  

## **Using the Trained Model**  
Once the model is trained, you can test it by running:  
```bash
python predict.py
```
This script collects user input, loads `Readmission_Model.pkl`, and predicts whether a patient will require readmission.  

## **Technologies Used**  
- Python (pandas, numpy, scikit-learn)  
- Jupyter Notebook  
- Machine Learning (Logistic Regression, Random Forest, etc.)  
## Contributing  
If you'd like to contribute:  
1. Fork the repository.  
2. Create a new branch: `git checkout -b feature-branch`  
3. Commit changes: `git commit -m "Added new feature"`  
4. Push to GitHub: `git push origin feature-branch`  
5. Open a pull request.  

---

## License  
This project is for educational purposes. Feel free to use and modify it.  
