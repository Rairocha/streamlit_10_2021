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

html_temp='<div class='tableauPlaceholder' id='viz1631288342567' style='position: relative'><noscript><a href='#'><img alt='Story 1 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;6Y&#47;6YTXFY7Y5&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='path' value='shared&#47;6YTXFY7Y5' /> <param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;6Y&#47;6YTXFY7Y5&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='pt-BR' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1631288342567');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='1369px';vizElement.style.height='854px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>'
st.components.v1.html(html_temp, width=1200, height=1000)