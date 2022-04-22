import streamlit as st 
import joblib
import os
import numpy as np

attrib_info = """
#### Attribute Information:
    - Age 1.20-65
    - Sex 1. Male, 2.Female
    - Polyuria 1.Yes, 2.No.
    - Polydipsia 1.Yes, 2.No.
    - sudden weight loss 1.Yes, 2.No.
    - weakness 1.Yes, 2.No.
    - Polyphagia 1.Yes, 2.No.
    - Genital thrush 1.Yes, 2.No.
    - visual blurring 1.Yes, 2.No.
    - Itching 1.Yes, 2.No.
    - Irritability 1.Yes, 2.No.
    - delayed healing 1.Yes, 2.No.
    - partial paresis 1.Yes, 2.No.
    - muscle stiness 1.Yes, 2.No.
    - Alopecia 1.Yes, 2.No.
    - Obesity 1.Yes, 2.No.
    - Class 1.Positive, 2.Negative.

"""
label_dict = {"No":0,"Yes":1}
gender_map = {"Female":0,"Male":1}
target_label_map = {"Negative":0,"Positive":1}

['age', 'gender', 'polyuria', 'polydipsia', 'sudden_weight_loss',
       'weakness', 'polyphagia', 'genital_thrush', 'visual_blurring',
       'itching', 'irritability', 'delayed_healing', 'partial_paresis',
       'muscle_stiffness', 'alopecia', 'obesity', 'class']


def get_fvalue(val):
	feature_dict = {"No":0,"Yes":1}
	for key,value in feature_dict.items():
		if val == key:
			return value 

def get_value(val,my_dict):
	for key,value in my_dict.items():
		if val == key:
			return value 



# Load ML Models
@st.cache
def load_model(model_file):
	loaded_model = joblib.load(open(os.path.join(model_file),"rb"))
	return loaded_model


def run_ml_app():
	st.subheader("Machine Learning Section")
	loaded_model = load_model("models/logistic_regression_model_diabetes_21_oct_2020.pkl")

	with st.beta_expander("Attributes Info"):
		st.markdown(attrib_info,unsafe_allow_html=True)

	# Layout
	col1,col2 = st.beta_columns(2)

	with col1:
		age = st.number_input("Age",10,100)
		gender = st.radio("Gender",("Female","Male"))
		polyuria = st.radio("Polyuria",["No","Yes"])
		polydipsia = st.radio("Polydipsia",["No","Yes"]) 
		sudden_weight_loss = st.selectbox("Sudden_weight_loss",["No","Yes"])
		weakness = st.radio("weakness",["No","Yes"]) 
		polyphagia = st.radio("polyphagia",["No","Yes"]) 
		genital_thrush = st.selectbox("Genital_thrush",["No","Yes"]) 
		
	
	with col2:
		visual_blurring = st.selectbox("Visual_blurring",["No","Yes"])
		itching = st.radio("itching",["No","Yes"]) 
		irritability = st.radio("irritability",["No","Yes"]) 
		delayed_healing = st.radio("delayed_healing",["No","Yes"]) 
		partial_paresis = st.selectbox("Partial_paresis",["No","Yes"])
		muscle_stiffness = st.radio("muscle_stiffness",["No","Yes"]) 
		alopecia = st.radio("alopecia",["No","Yes"]) 
		obesity = st.select_slider("obesity",["No","Yes"]) 

	with st.beta_expander("Your Selected Options"):
		result = {'age':age,
		'gender':gender,
		'polyuria':polyuria,
		'polydipsia':polydipsia,
		'sudden_weight_loss':sudden_weight_loss,
		'weakness':weakness,
		'polyphagia':polyphagia,
		'genital_thrush':genital_thrush,
		'visual_blurring':visual_blurring,
		'itching':itching,
		'irritability':irritability,
		'delayed_healing':delayed_healing,
		'partial_paresis':partial_paresis,
		'muscle_stiffness':muscle_stiffness,
		'alopecia':alopecia,
		'obesity':obesity}
		st.write(result)
		encoded_result = []
		for i in result.values():
			if type(i) == int:
				encoded_result.append(i)
			elif i in ["Female","Male"]:
				res = get_value(i,gender_map)
				encoded_result.append(res)
			else:
				encoded_result.append(get_fvalue(i))


		# st.write(encoded_result)
	with st.beta_expander("Prediction Results"):
		single_sample = np.array(encoded_result).reshape(1,-1)

		
		prediction = loaded_model.predict(single_sample)
		pred_prob = loaded_model.predict_proba(single_sample)
		st.write(prediction)
		if prediction == 1:
			st.warning("Positive Risk-{}".format(prediction[0]))
			pred_probability_score = {"Negative DM":pred_prob[0][0]*100,"Positive DM":pred_prob[0][1]*100}
			st.subheader("Prediction Probability Score")
			st.json(pred_probability_score)
		else:
			st.success("Negative Risk-{}".format(prediction[0]))
			pred_probability_score = {"Negative DM":pred_prob[0][0]*100,"Positive DM":pred_prob[0][1]*100}
			st.subheader("Prediction Probability Score")
			st.json(pred_probability_score)

