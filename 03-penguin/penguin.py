import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Palmer's Penguins")
st.markdown('Use this Streamlit app to make your own scatterplot about penguins!')
selected_species = st.selectbox('What species would you like to visualize?', ['Adelie', 'Gentoo', 'Chinstrap'])
selected_x_var = st.selectbox('What do you want the x variable to be?', ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g'])
selected_y_var = st.selectbox('What about they?', ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g'])

penguins_df = pd.read_csv('./input/penguins.csv')
penguins_df = penguins_df[penguins_df['species'] == selected_species]
st.write(penguins_df)
fig, ax = plt.subplots()
ax = plt.scatter(penguins_df[selected_x_var], penguins_df[selected_y_var])
plt.title(f"Scatterplot of {selected_species} Penguins")
st.pyplot(fig)
