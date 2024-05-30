'''
### in terminal (cmd (should be default)):

# create new environment called env_streamlit
conda create -n env_streamlit python

# activate new environment
conda activate env_streamlit

# install packages:
pip install ipykernel    # for jupyter notebook in vs code (cant use .ipynb without)
pip install streamlit

# check list of installed packages in env_streamlit environment
pip list

### in jupyter notebook
manually select env_streamlit kernel in top right
'''

#####################
# Start of app code #
#####################

# Import Streamlit
import streamlit as st

# Title of your app
st.title('My First Streamlit App')

# Add some text
st.write('Welcome to my first Streamlit app!')

# Add a slider
age = st.slider('Select your age', 0, 100, 25)

# Display the selected age
st.write(f'Your selected age: {age}')

###################
# End of app code #
###################

# Run the following in cmd terminal
# streamlit run c:/Users/crudek/Github/streamlit/practice/my_first_app.py