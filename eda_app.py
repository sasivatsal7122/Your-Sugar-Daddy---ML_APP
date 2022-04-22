import streamlit as st 
import pandas as pd 

# Data Viz Pkgs
import matplotlib.pyplot as plt 
import matplotlib
matplotlib.use('Agg')
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

	submenu = st.sidebar.selectbox("SubMenu",["Descriptive","Plots"])
	if submenu == "Descriptive":
		
		st.dataframe(df)

		with st.beta_expander("Data Types Summary"):
			st.dataframe(df.dtypes)

		with st.beta_expander("Descriptive Summary"):
			st.dataframe(df_clean.describe())

		with st.beta_expander("Gender Distribution"):
			st.dataframe(df['Gender'].value_counts())

		with st.beta_expander("Class Distribution"):
			st.dataframe(df['class'].value_counts())
	else:
		st.subheader("Plots")

		# Layouts
		col1,col2 = st.beta_columns([2,1])
		with col1:
			with st.beta_expander("Dist Plot of Gender"):
				# fig = plt.figure()
				# sns.countplot(df['Gender'])
				# st.pyplot(fig)

				gen_df = df['Gender'].value_counts().to_frame()
				gen_df = gen_df.reset_index()
				gen_df.columns = ['Gender Type','Counts']
				# st.dataframe(gen_df)
				p01 = px.pie(gen_df,names='Gender Type',values='Counts')
				st.plotly_chart(p01,use_container_width=True)

			with st.beta_expander("Dist Plot of Class"):
				fig = plt.figure()
				sns.countplot(df['class'])
				st.pyplot(fig)





		with col2:
			with st.beta_expander("Gender Distribution"):
				st.dataframe(df['Gender'].value_counts())

			with st.beta_expander("Class Distribution"):
				st.dataframe(df['class'].value_counts())
			

		with st.beta_expander("Frequency Dist Plot of Age"):
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

		with st.beta_expander("Outlier Detection Plot"):
			# outlier_df = 
			fig = plt.figure()
			sns.boxplot(df['Age'])
			st.pyplot(fig)

			p3 = px.box(df,x='Age',color='Gender')
			st.plotly_chart(p3)

		with st.beta_expander("Correlation Plot"):
			corr_matrix = df_clean.corr()
			fig = plt.figure(figsize=(20,10))
			sns.heatmap(corr_matrix,annot=True)
			st.pyplot(fig)

			p3 = px.imshow(corr_matrix)
			st.plotly_chart(p3)


	







