import streamlit as st  # pip install streamlit
import pandas as pd  # pip install pandas
import seaborn as sns  #pip install seaborn
from matplotlib import pyplot as plt  #pip install matplotlib


# Setting Page Titles
st.set_page_config(page_title='Excel Data Visualisation')
st.title('Employee Attrition Data Visualisation 📈')
st.subheader('Feed me with your Excel file')


#Uploading data
uploaded_file = st.file_uploader('Choose a XLSX file', type='xlsx')
if uploaded_file:
    st.markdown('---')
    df = pd.read_excel(uploaded_file, engine='openpyxl')

    #Selecting Specific Categorical Variables
    groupby_column = st.selectbox(
        'Which Categorical Variable would you like to analyse?',
        ('BusinessTravel', 'Department', 'Education', 'EducationField','EnvironmentSatisfaction', 
        'Gender', 'JobRole', 'JobSatisfaction', 'MaritalStatus', 'OverTime', 'PerformanceRating', 
        'Attrition'),
    )

    # Here we plot the simple graph 
    st.subheader(f'Graph showing the distribution of {groupby_column}')
    fig = sns.catplot(df, x=groupby_column, kind="count", palette="ch:start=.2,rot=-.3") #shrink = 0.8)
    st.pyplot(fig)


    # Here we plot the relationship between Attrition and the selected categorical variables
    st.subheader(f'Relationship between Attrition and {groupby_column}')
    fig1 = sns.displot(df,x=groupby_column, hue="Attrition", multiple="dodge", shrink=0.8)
    st.pyplot(fig1)


    # Here we create a selector for continuous variables
    groupby_cont_column = st.selectbox(
        'Which Continuous Variables would you like to analyse?',
        ('Age', 'CostOfHiring', 'MonthlySalary', 'NumCompaniesWorked', 'TotalWorkingYears',
        'TrainingTimesLastYear', 'YearsAtCompany', 'YearsSinceLastPromotion'),
    )
    

    # Here we plot the relationship between Attrition and the selected continuous variables
    st.subheader(f'Relationship between Attrition and {groupby_cont_column}')
    fig2 = sns.catplot(df, kind="box", y=groupby_cont_column, x="Attrition") #hue="Attrition")
    st.pyplot(fig2)
