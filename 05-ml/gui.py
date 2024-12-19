import streamlit as st
import pickle

with open('./output/random_forest_penguin.pickle', 'rb') as rf_pickle:
    rfc = pickle.load(rf_pickle)

with open('./output/output_penguin.pickle', 'rb') as map_pickle:
    unique_penguin_mapping = pickle.load(map_pickle)



island = st.selectbox("Penguin Island", options=["Biscoe", "Dream", "Torgerson"])
sex = st.selectbox("Sex", options=["Female", "Male"])
bill_length = st.number_input("Bill Length (mm)", min_value=0)
bill_depth = st.number_input("Bill Depth (mm)", min_value=0)
flipper_length = st.number_input("Flipper Length (mm)", min_value=0)
body_mass = st.number_input("Body Mass (g)", min_value=0)
user_inputs = [island, sex, bill_length, bill_depth, flipper_length, body_mass]
st.write(f"""the user inputs are {user_inputs}""".format())
