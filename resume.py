import streamlit as st

st.title("WELCOME")
st.write("MY RESUME")

st.header("About Me")
st.write("Hello! My Name is Jenifer.I'm studying in kgisl institute of technology,In the department of CSBS")
st.write("Iam sure thet this resume will give a clesr outline of me ")

st.subheader("Contact Information")
st.write("Email:abchbu@gmail.com")
st.write("Moblie no:9867540351")
st.write("Address:245A,cccc Nagar,aaa")
info={"Institution name:[ABC School','Kg college]"}
st.dataframe(info)
st.write("My skills :Java,Python,C++,HTML")
        