"""
This is the website for the Fontys Toegepaste Wiskunde Netwerkdag 2026.
Op deze website kunnen studenten en bedrijven vinden waar ze moeten zijn.
"""
import streamlit as st
from functions_website import information_event

#Setup
if "student_company" not in st.session_state:
    st.session_state.student_company = None


#Sidebar
with st.sidebar:
    if st.session_state.student_company == None:
        st.title("Fill in to find information about your networkday")

        confirm = False
        name = None
        year = None

        student_company = st.selectbox(label="Are you a student or a company?",
                                        options=["Student", "Company"],
                                        index=None,
                                        placeholder="Please make a choice")
        if student_company == "Student":
            name = st.text_input(label="What is your name?",
                                 value=None)
            year = st.selectbox(label="What year are you in?",
                                options=["1","2","3","4"],
                                index= None,
                                placeholder="Please select your year")
            if st.button(label="Press twice to confirm your choices"):
                confirm = True

        elif student_company == "Company":
            name = st.text_input(label="What is your company name?",
                                 value=None)
            year = False
            if st.button(label="Press twice to confirm your company"):
                confirm = True

        if (name != None) and (year != None) and (confirm == True):
            st.session_state.student_company = [student_company, name, year]
        elif (name == None) and (year != None) and (confirm == True):
            if student_company == "Student":
                st.error("Please fill in your name")
            elif student_company == "Company":
                st.error("Please fill in your company name")
        elif (name != None) and (year == None) and (confirm == True):
            st.error("Please select the year you're in")
        elif student_company == "Student" and confirm == True:
            st.error("Please fill in your name")
            st.error("Please select the year you're in")
        elif confirm == True:
            st.error("Please fill in your company name")


    elif st.session_state.student_company[0] == "Student":
        st.title("You are")

        st.write("Student name:", st.session_state.student_company[1])
        st.write("School year:", st.session_state.student_company[2])
        if st.button(label="Change account"):
            st.session_state.student_company = None
            st.rerun()

    elif st.session_state.student_company[0] == "Company":
        st.title("Your company is")

        st.write("Company name:", st.session_state.student_company[1])
        if st.button(label="Change account"):
            st.session_state.student_company = None
            st.rerun()

    else:
        st.session_state.student_company = None

    st.title("Applied Mathametics Networkingday 2026")
    if st.session_state.student_company == None:
        st.write("Here you will find your schedule for the Applied Mathametics Networkingday 2026")
        st.header("Please fill in the information in the side bar.")
    else:
        information_event(st.session_state.student_company[0], st.session_state.student_company[1], st.session_state.student_company[2])
