import streamlit as st 
import streamlit.components.v1 as stc 
from eda_app import run_eda_app
from ml_app import run_ml_app
from PIL import Image

html_temp = """
		<div style="background-color:#072227;padding:10px;border-radius:10px">
		<h1 style="color:#35858B;text-align:center;">Early Stage Diabetes Risk Predictor Web App</h1>
		<h4 style="color:#DDDDDD;text-align:center;">Your Personal Sugar Daddy 👅</h4>
		</div>
		"""

def main():
	# st.title("ML Web App with Streamlit")
	stc.html(html_temp)
	st.markdown("<p><TT>Designed and Developed by <a style='text-decoration:none;color:red' target='_blank' href='https://github.com/sasivatsal7122'>B.Sasi Vatsal</a></TT></p>", unsafe_allow_html=True)

	menu = ["Diabetic Diagnosis","EDA","About"]
	st.sidebar.write("1.Select EDA option to see detailed analysis of the datset")
	st.sidebar.write("2.Select Diabetic Diagnosis to use Diabetes Risk Predictor")
	choice = st.sidebar.selectbox("Choose One of the Option",menu)

	if choice == "Home":
		st.subheader("Home")
		st.write("""
			
			This dataset contains the sign and symptoms data of newly diabetic or would be diabetic patient.
			#### Datasource
				- https://archive.ics.uci.edu/ml/datasets/Early+stage+diabetes+risk+prediction+dataset.
			#### App Content
				- EDA Section: Exploratory Data Analysis of Data
				- ML Section: ML Predictor App

			""")
	elif choice == "EDA":
		run_eda_app()
	elif choice == "Diabetic Diagnosis":
		run_ml_app()
	else:
		image = Image.open()

if __name__ == '__main__':
	main()