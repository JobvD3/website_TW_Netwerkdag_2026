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
        confirm = False
        
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
            if st.button(label="Confirm choices"):
                confirm = True
        elif student_company == "Company":
            name = st.text_input(label="What is your company name?")
            year = False
            if st.button(label="Confirm choices"):
                confirm = True

        if ("name" in locals()) and (year != None):
            st.session_state.student_company = [student_company, name, year]

    elif st.session_state.student_company[0] == "Student":
        st.write("Student name:", st.session_state.student_company[1])
        st.write("School year:", st.session_state.student_company[2])

    elif st.session_state.student_company[0] == "Company":
        st.write("Company name:", st.session_state.student_company[1])

    else:
        st.session_state.student_company = None