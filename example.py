import streamlit as st 
import pandas as pd 

st.write('I love cats')
file = st.file_uploader('Put your csv here')

try:
	df = pd.read_csv(file)
except:
	st.write('Please load your csv file')
else:
	if st.checkbox('See all dataframe'):
		st.write(df)
	if st.checkbox('Filter dataframe'):
		n_rows = st.number_input('How many lines do you want to see?',min_value= 1,step=1)
		selected_columns = df.columns
		selected_columns = st.multiselect('What columns do you want?', selected_columns)
		if st.button('Preview'):
			if len(selected_columns) ==0:
				st.write(df.head(n_rows))
			else:
				st.write(df.head(n_rows)[selected_columns])
				st.balloons()