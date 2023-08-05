"""
Created on Sat Aug  5 14:03:35 2023

@author: raosa
"""
import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models

diabetes_model = pickle.load(open('C:/Users/raosa/Desktop/MULTI/saved models/diabetes_model.sav', 'rb'))
lung_cancer_model =pickle.load(open('C:/Users/raosa/Desktop/MULTI/saved models/lung_cancer_model.sav','rb'))
parkinsons_model = pickle.load(open('C:/Users/raosa/Desktop/MULTI/saved models/parkinsons_model.sav', 'rb'))
kidney1_model = pickle.load(open('C:/Users/raosa/Desktop/MULTI/saved models/kidney_model.sav', 'rb'))
heart_attack_model=pickle.load(open('C:/Users/raosa/Desktop/MULTI/saved models/heart_attack_model.sav', 'rb'))



# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('MULTI-DISEASE PREDICTION FOR TOMMOROW\'S WORLD',
                          ['Diabetes Prediction',
                           'Lung cancer Prediction',
                           'Parkinsons Prediction','Chronic kidney disease','Heart attack prediction'],
                          icons=['activity','lungs','person','meta','heart'],
                          default_index=0)
    
    
# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    
    # page title
    st.title('Diabetes Prediction using ML')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        
    with col2:
        Glucose = st.text_input('Glucose Level')
    
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    
    with col2:
        Insulin = st.text_input('Insulin Level')
    
    with col3:
        BMI = st.text_input('BMI value')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    
    with col2:
        Age = st.text_input('Age of the Person')
    
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        if (diab_prediction[0] == 1):
           diab_diagnosis = '''Oh no! The person is diabetic. Manage your diabetes ABCs.
           Follow your diabetes meal plan.\n Make physical activity part of your routine.\n Take your medicine.\n Check your blood glucose levels.
           Monitor your blood sugar.'''

        else:
          diab_diagnosis = 'The person is not diabetic'
        
    st.success(diab_diagnosis)
    
if (selected == 'Lung cancer Prediction'):

    st.title('Lung Cancer Prediction using ML')
    
    # Getting the input data from the user
    col1, col2, col3= st.columns(3)
    
    with col1:
        GENDER = st.text_input('Gender')
    
    with col2:
        AGE = st.text_input('Age of the Person')
    
    with col3:
        SMOKING = st.text_input('Smoking')
    
    with col1:
        YELLOW_FINGERS = st.text_input('Yellow Fingers')
    
    with col2:
        ANXIETY = st.text_input('Anxiety')
    
    with col3:
        PEER_PRESSURE = st.text_input('Peer Pressure')
    
    with col1:
        CHRONIC_DISEASE = st.text_input('Chronic Disease')
    
    with col2:
        FATIGUE = st.text_input('Fatigue')
    
    with col3:
        ALLERGY	= st.text_input('Allergy')
    
    with col1:
        WHEEZING =st.text_input('Wheezing')
        
    with col2:
        ALCOHOL_CONSUMING = st.text_input("Alchol")
    
    with col3:
        COUGHING =st.text_input("Coughing")
    
    with col1:
        SHORTNESS_OF_BREATH = st.text_input('Shortness_of_breath') 
    
    with col2:
        SWALLOWING_DIFFICULTY = st.text_input('Swallowing difficulty')
    
    with col3:
        CHEST_PAIN = st.text_input('Chest pain')
        
        

    lung_cancer_diagnosis = ''
    

    if st.button('Lung Cancer Test Result'):
        lung_cancer_prediction = lung_cancer_model.predict([[GENDER,AGE,SMOKING,YELLOW_FINGERS,ANXIETY,PEER_PRESSURE,CHRONIC_DISEASE,FATIGUE,ALLERGY,WHEEZING,ALCOHOL_CONSUMING,COUGHING,SHORTNESS_OF_BREATH,SWALLOWING_DIFFICULTY,CHEST_PAIN]])
        if lung_cancer_prediction[0] == 1:
            lung_cancer_diagnosis = 'The person has lung cancer'
        else:
            lung_cancer_diagnosis = 'The person does not have lung cancer'
        
    st.success(lung_cancer_diagnosis)


# Parkinson's Prediction Page
if (selected == "Parkinsons Prediction"):
    
    # page title
    st.title("Parkinson's Disease Prediction using ML")
    
    col1, col2, col3, col4, col5 = st.columns(5)  
    
    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
        
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')
        
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')
        
    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')
        
    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
        
    with col1:
        RAP = st.text_input('MDVP:RAP')
        
    with col2:
        PPQ = st.text_input('MDVP:PPQ')
        
    with col3:
        DDP = st.text_input('Jitter:DDP')
        
    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')
        
    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
        
    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')
        
    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')
        
    with col3:
        APQ = st.text_input('MDVP:APQ')
        
    with col4:
        DDA = st.text_input('Shimmer:DDA')
        
    with col5:
        NHR = st.text_input('NHR')
        
    with col1:
        HNR = st.text_input('HNR')
        
    with col2:
        RPDE = st.text_input('RPDE')
        
    with col3:
        DFA = st.text_input('DFA')
        
    with col4:
        spread1 = st.text_input('spread1')
        
    with col5:
        spread2 = st.text_input('spread2')
        
    with col1:
        D2 = st.text_input('D2')
        
    with col2:
        PPE = st.text_input('PPE')
        
    
    
    # code for Prediction
    parkinsons_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          
        
        if (parkinsons_prediction[0] == 1):
          parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
          parkinsons_diagnosis = "The person does not have Parkinson's disease"
        
    st.success(parkinsons_diagnosis)
    

# Diabetes Prediction Page
if (selected == 'Chronic kidney disease'):
    
    # page title
    st.title('Chronic kidney disease Prediction using ML')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Bp = st.text_input('blood Pressuure')
        
    with col2:
        Sg = st.text_input('Sg')
    
    with col3:
        Al = st.text_input('Al')
    
    with col1:
        Su = st.text_input('Su')
    
    with col2:
        Rbc = st.text_input('red blood cells')
    
    with col3:
        Bu = st.text_input('Bu')
    
    with col1:
        Sc = st.text_input('sc')
    
    with col2:
        Sod = st.text_input('Sod')
        
    with col3:
         Pot = st.text_input('Pot')
         
    with col1:
        Hemo = st.text_input('Heamoglobin')
        
    with col2:
        Wbcc = st.text_input('Wbc')   
        
    with col3:
         Rbcc = st.text_input('Rbcc')
         
    with col1:
        Htn = st.text_input('htn')
    
    
    # code for Prediction
    chronic_kidney_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Chronic Kideny Test Result'):
        chronic_prediction = kidney1_model.predict([[Bp	,Sg	,Al,Su,Rbc,Bu,Sc,Sod,Pot,Hemo,Wbcc,Rbcc,Htn]])
        
        if (chronic_prediction[0] == 0):
          chronic_kidney_diagnosis = 'The person has chances of chronic kidney disease'
        else:
          chronic_kidney_diagnosis = 'Hurray! you are safe , the person has less chance of chronic kidney disease'
        
    st.success(chronic_kidney_diagnosis)


# Diabetes Prediction Page
if (selected == 'Heart attack prediction'):
    
    # page title
    st.title('Heart attack Prediction using ML')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('age')
        
    with col2:
        sex = st.text_input('sex')
    
    with col3:
         cp= st.text_input('cp')
    
    with col1:
        trtbps = st.text_input('trtbps')
    
    with col2:
        chol= st.text_input('chol')
    
    with col3:
        fbs = st.text_input('fbs')
    
    with col1:
         restecg = st.text_input('ecg')
    
    with col2:
        thalachh = st.text_input('thalachh')
        
    with col3:
         exng = st.text_input('exng')
         
    with col1:
        oldpeak = st.text_input('oldpeak')
        
    with col2:
        slp= st.text_input('slp')   
        
    with col3:
         caa= st.text_input('caa')
         
    with col1:
        thall = st.text_input('thall')
    
    
    # code for Prediction
    heart_attack_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('heart attack Test Result'):
        attack_prediction = heart_attack_model.predict([[age,sex,cp,trtbps,chol,fbs,restecg,thalachh,exng,oldpeak,slp,caa,thall	]])
        
        if (attack_prediction[0] == 1):
          heart_attack_diagnosis = 'ohoo! you are in trouble! the person has higher chances of getting heart attack'
        else:
          heart_attack_diagnosis = 'Hurray! you are safe , the person has lesser chance of heart attack'
        
    st.success(heart_attack_diagnosis)
