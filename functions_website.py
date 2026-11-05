"""
Here you will find the functions that make the Fonty Toegepaste Wiskunde Netwerkdag website work
"""
import pandas as pd
import streamlit as st


def information_student(student_name, student_year):
    """
    This function will make a schedule from the data in website_tw_nd.xlsx.

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

        activity, time = st.columns([3,1], border=True)

        if student.year in [1,2]:
            activity.write("Walk in:")
            time.write("10:30")
            activity.write("Start-event:")
            time.write("11:00")
            activity.write(f"Speed date with {student.speed_date1}:")
            time.write("11:20")
            activity.write(f"Speed date with {student.speed_date2}:")
            time.write("11:40")
            activity.write(f"Speed date with {student.speed_date3}:")
            time.write("12:10")
            activity.write("Break:")
            time.write("12:20")
            activity.write(f"Speed date with {student.speed_date4}:")
            time.write("12:40")
            if student.year == 1:
                activity.write("Importance of Networking Presentation:")
                time.write("12:50")
                activity.write("Company market:")
                time.write("13:10")
            else:
                activity.write("Company market:")
                time.write("12:50")
            activity.write(f"speed date with {student.speed_date5} & pitches:")
            time.write("13:30")
            activity.write("End of event:")
            time.write("13:50")

        else:
            activity.write("Walk in:------------------------------------------15:10")
            activity.write("Introduction:-------------------------------------15:20")
            activity.write(f"Speed date with {student.speed_date_late1}:------15:35")
            activity.write(f"Speed date with {student.speed_date_late2}:------15:35")
            activity.write(f"Speed date with {student.speed_date_late3}:------15:35")
            activity.write(f"Speed date with {student.speed_date_late4}:------15:35")

def information_company(company_name):
    """
    This function will make a schedule from the data in website_tw_nd.xlsx.
    
    args:
        company_name: Is the name of the selected company.
    
    Returns:
        The schedule of the selected company on the website
    """
    df = pd.read_excel("website_tw_nd.xlsx", sheet_name="companys")

    df_company = df.loc[df.name == company_name].iloc[0]

    if len(df_company.index) < 1:
        st.error("Company not found")
    
    else:
        company = df_company.iloc[0]

        if company.first == 1 and company.second == 1:
            st.write("Setting up:---------------------------------------10:30")
            st.write("Start of event:-----------------------------------11:00")
            st.write(f"Speed date with {company.speed_date1}:-----------11:20")
            st.write(f"Speed date with {company.speed_date2}:-----------11:40")
            st.write(f"Speed date with {company.speed_date3}:-----------12:10")
            st.write("Break:--------------------------------------------12:20")
            st.write(f"Speed date with {company.speed_date4}:-----------12:40")
            st.write("Company market:-----------------------------------12:50")
            st.write(f"speed date with {company.speed_date5}:-----------13:30")
            st.write("End of first halve:-------------------------------13:50")

            st.write("Break with Lunch:---------------------------------14:00")

            st.write("Walk in 3th & 4th years students:-----------------15:10")
            st.write("Introduction second halve:------------------------15:20")
            st.write(f"Speed date with {company.speed_date_late1}:------15:35")
            st.write(f"Speed date with {company.speed_date_late2}:------15:35")
            st.write(f"Speed date with {company.speed_date_late3}:------15:35")
            st.write(f"Speed date with {company.speed_date_late4}:------15:35")
            st.write("Borrel:-------------------------------------------16:30")
            st.write("End of event:-------------------------------------17:30")


        elif company.first == 1 and company.second != 1:
            st.write("Setting up:---------------------------------------10:30")
            st.write("Start of event:-----------------------------------11:00")
            st.write(f"Speed date with {company.speed_date1}:           11:20")
            st.write(f"Speed date with {company.speed_date2}:           11:40")
            st.write(f"Speed date with {company.speed_date3}:           12:10")
            st.write("Break:                                            12:20")
            st.write(f"Speed date with {company.speed_date4}:           12:40")
            st.write("Company market:                                   12:50")
            st.write(f"speed date with {company.speed_date5}:           13:30")
            st.write("End of event:                                     13:50")

        elif company.first != 1 and company.second == 1:
            st.write("Setting up:                                       14:30")
            st.write("Walk in 3th & 4th years students:                 15:10")
            st.write("Introduction second halve:                        15:20")
            st.write(f"Speed date with {company.speed_date_late1}:      15:35")
            st.write(f"Speed date with {company.speed_date_late2}:      15:35")
            st.write(f"Speed date with {company.speed_date_late3}:      15:35")
            st.write(f"Speed date with {company.speed_date_late4}:      15:35")
            st.write("Borrel:                                           16:30")
            st.write("End of event:                                     17:30")


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

