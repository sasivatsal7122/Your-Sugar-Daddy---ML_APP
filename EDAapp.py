import streamlit as st 
import pandas as pd 

import matplotlib.pyplot as plt 
import seaborn as sns
import plotly.express as px 


@st.cache
def load_data(data):
	df = pd.read_csv(data)
	return df


def run_eda_app():
	st.subheader("EDA Section")
	df = load_data("data/diabetes_data_upload.csv")
	df_clean = load_data("data/diabetes_data_upload_clean.csv")
	freq_df = load_data("data/freqdist_of_age_data.csv")
	
	st.sidebar.text("Choose Option of Your liking : ")
	submenu = st.sidebar.selectbox("SubMenu",["Descriptive","Plots"])
	if submenu == "Descriptive":
		
		st.dataframe(df)

		with st.expander("Descriptive Summary"):
			st.dataframe(df_clean.describe())

		with st.expander("Gender Distribution"):
			st.dataframe(df['Gender'].value_counts())

		with st.expander("Class Distribution"):
			st.dataframe(df['class'].value_counts())
	else:
		st.subheader("Plots")

		col1,col2 = st.columns([2,1])
		with col1:
			with st.expander("Dist Plot of Gender"):
				
				fig = plt.figure()
				sns.countplot(df['Gender'])
				st.pyplot(fig)

				gen_df = df['Gender'].value_counts().to_frame()
				gen_df = gen_df.reset_index()
				gen_df.columns = ['Gender Type','Counts']
				st.dataframe(gen_df)
				p01 = px.pie(gen_df,names='Gender Type',values='Counts')
				st.plotly_chart(p01,use_container_width=True)

			with st.expander("Dist Plot of Class"):
				fig = plt.figure()
				sns.countplot(df['class'])
				st.pyplot(fig)

		with col2:
			with st.expander("Gender Distribution"):
				st.dataframe(df['Gender'].value_counts())

			with st.expander("Class Distribution"):
				st.dataframe(df['class'].value_counts())
			

		with st.expander("Frequency Dist Plot of Age"):
			# fig,ax = plt.subplots()
			# ax.bar(freq_df['Age'],freq_df['count'])
			# plt.ylabel('Counts')
			# plt.title('Frequency Count of Age')
			# plt.xticks(rotation=45)
			# st.pyplot(fig)

			p = px.bar(freq_df,x='Age',y='count')
			st.plotly_chart(p)

			p2 = px.line(freq_df,x='Age',y='count')
			st.plotly_chart(p2)

		with st.expander("Outlier Detection Plot"):
			# fig = plt.figure()
			# sns.boxplot(df['Age'])
			# st.pyplot(fig)

			p3 = px.box(df,x='Age',color='Gender')
			st.plotly_chart(p3)

		with st.expander("Correlation Plot"):
			corr_matrix = df_clean.corr()
			fig = plt.figure(figsize=(20,10))
			sns.heatmap(corr_matrix,annot=True)
			st.pyplot(fig)

			p3 = px.imshow(corr_matrix)
			st.plotly_chart(p3)


	







