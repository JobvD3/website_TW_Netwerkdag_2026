"""
Here you will find the functions that make the Fonty Toegepaste Wiskunde Netwerkdag website work
"""
import pandas as pd
import streamlit as st


def information_student(student_name, student_year):
    """
    This function will make a schedule from the data in website_tw_nd.xlsx

    args:
        student_name: Is the name of the selected student.

        student_year: Is the year that the selected student is in.
    
    Returns:
        The schedule of the selected student on the website
    """
    df = pd.read_excel("website_tw_nd.xlsx", sheet_name="students")

    df_student = df.loc[(df.name == student_name) & (df.year == student_year)]

    if len(df_student.index) < 1:
        st.error("Student not found")
    
    else:
        student = df_student.iloc[0]

        if student.year in [1,2]:
            with st.container(border=True):
                st.write("Walk in:")
                st.write("10:30")

            with st.container(border=True):
                st.write("Start-event:")
                st.write("11:00")

            with st.container(border=True):
                st.write(f"Speed date with {student.speed_date1}:")
                st.write("11:20")

            with st.container(border=True):
                st.write(f"Speed date with {student.speed_date2}:")
                st.write("11:40")

            with st.container(border=True):
                st.write(f"Speed date with {student.speed_date3}:")
                st.write("12:10")

            with st.container(border=True):
                st.write("Break:")
                st.write("12:20")

            with st.container(border=True):
                st.write(f"Speed date with {student.speed_date4}:")
                st.write("12:40")
            if student.year == 1:
                with st.container(border=True):
                    st.write("Importance of Networking Presentation:")
                    st.write("12:50")

                with st.container(border=True):
                    st.write("Company market:")
                    st.write("13:10")
            
            else:
                with st.container(border=True):
                    st.write("Company market:")
                    st.write("12:50")

            with st.container(border=True):
                st.write(f"speed date with {student.speed_date5} & pitches:")
                st.write("13:30")
            with st.container(border=True):
                st.write("End of event:")
                st.write("13:50")

        else:
            with st.container(border=True):
                st.write("Walk in:")
                st.write("15:10")

            with st.container(border=True):
                st.write("Introduction:")
                st.write("15:20")

            with st.container(border=True):
                st.write(f"Speed date with {student.speed_date_late1}:")
                st.write("15:35")

            with st.container(border=True):
                st.write(f"Speed date with {student.speed_date_late2}:")
                st.write("15:50")

            with st.container(border=True):
                st.write(f"Speed date with {student.speed_date_late3}:")
                st.write("16:05")

def information_company(company_name):
    """
    This function will make a schedule from the data in website_tw_nd.xlsx.
    
    args:
        company_name: Is the name of the selected company.
    
    Returns:
        The schedule of the selected company on the website
    """
    df = pd.read_excel("website_tw_nd.xlsx", sheet_name="companys")

    df_company = df.loc[df.name == company_name]

    if len(df_company.index) < 1:
        st.error("Company not found")
    
    else:
        company = df_company.iloc[0]


        if company.first == 1 and company.second == 1:
            with st.container(border=True):
                st.write("Setting up:")
                st.write("10:30")

            with st.container(border=True):
                st.write("Start of event:")
                st.write("11:00")

            with st.container(border=True):
                st.write(f"Speed date with {company.speed_date1}:")
                st.write("11:20")

            with st.container(border=True):
                st.write(f"Speed date with {company.speed_date2}:")
                st.write("11:40")

            with st.container(border=True):
                st.write(f"Speed date with {company.speed_date3}:")
                st.write("12:10")

            with st.container(border=True):
                st.write("Break:")
                st.write("12:20")

            with st.container(border=True):
                st.write(f"Speed date with {company.speed_date4}:")
                st.write("12:40")

            with st.container(border=True):
                st.write("Company market:")
                st.write("12:50")

            with st.container(border=True):
                st.write(f"speed date with {company.speed_date5}:")
                st.write("13:30")

            with st.container(border=True):
                st.write("End of first halve:")
                st.write("13:50")

            with st.container(border=True):
                st.write("Break with Lunch:")
                st.write("14:00")

            with st.container(border=True):
                st.write("Walk in 3th & 4th years students:")
                st.write("15:10")

            with st.container(border=True):
                st.write("Introduction second halve:")
                st.write("15:20")

            with st.container(border=True):
                st.write(f"Speed date with {company.speed_date_late1}:")
                st.write("15:35")

            with st.container(border=True):
                st.write(f"Speed date with {company.speed_date_late2}:")
                st.write("15:50")

            with st.container(border=True):
                st.write(f"Speed date with {company.speed_date_late3}:")
                st.write("16:05")

            with st.container(border=True):
                st.write("Borrel:")
                st.write("16:30")

            with st.container(border=True):
                st.write("End of event:")
                st.write("17:30")


        elif company.first == 1 and company.second != 1:
            with st.container(border=True):
                st.write("Setting up:")
                st.write("10:30")

            with st.container(border=True):
                st.write("Start of event:")
                st.write("11:00")

            with st.container(border=True):
                st.write(f"Speed date with {company.speed_date1}:")
                st.write("11:20")

            with st.container(border=True):
                st.write(f"Speed date with {company.speed_date2}:")
                st.write("11:40")

            with st.container(border=True):
                st.write(f"Speed date with {company.speed_date3}:")
                st.write("12:10")

            with st.container(border=True):
                st.write("Break:")
                st.write("12:20")

            with st.container(border=True):
                st.write(f"Speed date with {company.speed_date4}:")
                st.write("12:40")

            with st.container(border=True):
                st.write("Company market:")
                st.write("12:50")

            with st.container(border=True):
                st.write(f"speed date with {company.speed_date5}:")
                st.write("13:30")

            with st.container(border=True):
                st.write("End of event:")
                st.write("13:50")

        elif company.first != 1 and company.second == 1:
            with st.container(border=True):
                st.write("Setting up:")
                st.write("14:30")

            with st.container(border=True):
                st.write("Walk in 3th & 4th years students:")
                st.write("15:10")

            with st.container(border=True):
                st.write("Introduction second halve:")
                st.write("15:20")

            with st.container(border=True):
                st.write(f"Speed date with {company.speed_date_late1}:")
                st.write("15:35")

            with st.container(border=True):
                st.write(f"Speed date with {company.speed_date_late2}:")
                st.write("15:50")

            with st.container(border=True):
                st.write(f"Speed date with {company.speed_date_late3}:")
                st.write("16:05")

            with st.container(border=True):
                st.write("Borrel:")
                st.write("16:30")

            with st.container(border=True):
                st.write("End of event:")
                st.write("17:30")


def information_event(student_company, name, year):
    """
    This function will make a schedule from the data in website_tw_nd.xlsx.
    
    args:
        student_company: Is it a company or a student

        name: Is the name of the selected company or student.

        year: Is the year that the student is in, None for companys
    
    Returns:
        The schedule of the selected company or student on the website
    """

    if student_company == "Student":
        information_student(name.lower(), int(year))
    elif student_company == "Company":
        information_company(name.lower())
    else:
        st.error("Something went wrong please fill your acount information in again.")

def company_information():
    """
    This function will make a callabel element in streamlit where students can find information about a company
    
    Returns:
        Streamlit code to show information about the requested company
    """
    df = pd.read_excel("Networking Day 2026 Applied Mathematics - Company Registration.xlsx")

    df = df.iloc[:, [6,7]]
    df.columns = ["name", "information"]

    company = st.selectbox(label="Please select the company that you want to know more about",
                           options=df["name"],
                           index=None,
                           placeholder="Pleace choose a company")

    if company != None:
        st.title(company)

        st.write(df["information"].loc[df["name"] == company].iloc[0])
