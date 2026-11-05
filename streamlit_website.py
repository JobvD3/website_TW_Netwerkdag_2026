"""
This is the website for the Fontys Toegepaste Wiskunde Netwerkdag 2026.
Op deze website kunnen studenten en bedrijven vinden waar ze moeten zijn.
"""
import streamlit as st

#Setup
if "student_company" not in st.session_state:
    st.session_state.student_company = None


#Sidebar
with st.sidebar:
    if st.session_state.student_company == None:
        student_company = st.selectbox(label="Are you a student or a company?",
                                        options=["Student", "Company"],
                                        index=None,
                                        placeholder="Please make a choice")
        if student_company == "Student":
            name = st.text_input(label="What is your name?")
            year = st.selectbox(label="What year are you in?",
                                options=[1,2,3,4],
                                index= None,
                                placeholder="Please select your year")
        elif student_company == "Company":
            name = st.text_input(label="What is your company name?")
            year = None

        if "name" in locals():
            st.session_state.student_company = [student_company, name, year]