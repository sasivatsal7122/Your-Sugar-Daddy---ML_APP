import streamlit as st 
import streamlit.components.v1 as stc 
from eda_app import run_eda_app
from ml_app import run_ml_app

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

	menu = ["Home","EDA","ML","About"]
	choice = st.sidebar.selectbox("Menu",menu)

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
	elif choice == "ML":
		run_ml_app()
	else:
		pass

if __name__ == '__main__':
	main()