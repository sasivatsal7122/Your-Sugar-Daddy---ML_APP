import streamlit as st 
import streamlit.components.v1 as stc 
from eda_app import run_eda_app
from ml_app import run_ml_app
from PIL import Image
import webbrowser

html_temp = """
		<div style="background-color:#35858B;padding:10px;border-radius:10px">
		<h1 style="color:#AEFEFF;text-align:center;">Early Stage Diabetes Risk Predictor Web App</h1>
		<h2 style="color:#064663;text-align:center;">Your Personal Sugar Daddy 👅</h2>
		</div>
		"""

def main():
	st.set_page_config(page_title="Your Sugar Daddy",page_icon='🍫',layout="wide")
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
		image = Image.open('preview/dp.jpg')
		col1,col2 = st.columns([1,2])
		with col1:
  			st.image(image)
		
		with col2:
			st.markdown("<h1> Hey There <span style = 'display: block;'> I'm Sasi Vatsal</span> </h1>",unsafe_allow_html=True)
			st.markdown("<h5>Python - Data Science - Machine Learning Developer<h5>",unsafe_allow_html=True)
			st.write("A Self- motivated, Inquisitive, energetic computer science engineering student skilled in leadership, with a strong foundation in math, logic, and cross-platform coding with proven and tested engineering, management, marketing skills Seeking a challenging role at a reputed organization to utilize my skills usefully and effectievely")
			
			st.text("Connect With ME : ")
			github = st.button("Visit My Github")
			linkedin = st.button("Visit My Linkedin")
			if github:
				webbrowser.open('https://github.com/sasivatsal7122')
			if linkedin:
				webbrowser.open('https://www.linkedin.com/in/sasi-vatsal-606195215/')

if __name__ == '__main__':
	main()