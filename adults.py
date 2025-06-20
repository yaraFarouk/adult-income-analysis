
import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(layout= 'wide', page_title= 'adults EDA', page_icon= '✨')

page = st.sidebar.radio('Pages', ['Dataset','Univariate Analysis', 'Bivariate Analysis', 'Multivariate Analysis'])
adults = pd.read_csv('adult.csv')
if page == 'Dataset':
    st.dataframe(adults)
    st.title("Adult Income Dataset - Project Overview")

    st.markdown("""
    ### 📄 Dataset Description

    The **Adult Income Dataset** is extracted from the 1994 U.S. Census database.  
    It is commonly used to predict whether an individual's annual income exceeds \$50K, based on demographic and employment-related attributes.

---

### 🔍 Features Included:

- **age**: Age of the individual (in years)
- **workclass**: Type of employment (e.g., Private, Self-emp, Government)
- **fnlwgt**: Final weight – represents how many people the record represents
- **education**: Highest level of education completed
- **education.num**: Numeric representation of education
- **marital.status**: Marital status (e.g., Married, Divorced, Never-married)
- **occupation**: Job type (e.g., Tech-support, Sales)
- **relationship**: Relationship status within household
- **race**: Race category (e.g., White, Black, Asian)
- **sex**: Gender (Male/Female)
- **capital.gain**: Income from capital gains
- **capital.loss**: Loss from capital investments
- **hours.per.week**: Total working hours per week
- **native.country**: Country of origin
- **income**: Target variable – whether income is >50K or <=50K

---

### 🎯 Objective

The goal of this project is to analyze and visualize demographic and employment patterns to predict income level, and understand key features that influence high earnings.

  """)
elif page == 'Univariate Analysis':
    question = st.selectbox('Select Question', ['What is the distribution of age in the dataset?','What percentage of individuals earn more than $50K?','What is the distribution of hours worked per week?'])
    if question == 'What is the distribution of age in the dataset?':
        st.plotly_chart(px.histogram(data_frame= adults, x= 'age', color= 'income', title= 'Age Distribution by Income'))
    elif question == 'What percentage of individuals earn more than $50K?':
        st.plotly_chart(px.pie(data_frame= adults, names= 'income', title= 'Income Distribution'))
    elif question == 'What is the distribution of hours worked per week?':
        st.plotly_chart(px.box(adults,x = 'hours.per.week',title= ' Hours Worked Per Week Distribution'))

elif page == 'Bivariate Analysis':
    question = st.selectbox('Select Question', ['Is there a relationship between education level and income?','Does income distribution vary by gender?','Do individuals who work more hours tend to earn more?'])
    if question == 'Is there a relationship between education level and income?':
        st.plotly_chart(px.histogram(data_frame= adults, x= 'education', color= 'income',barmode='group', title= 'Education Number Distribution by Income'))
    elif question == 'Does income distribution vary by gender?':
        st.plotly_chart(px.histogram(data_frame= adults, x= 'sex', color= 'income',barmode='group', title= 'Income by Gender'))
    elif question == 'Do individuals who work more hours tend to earn more?':
        st.plotly_chart(px.box(adults, x='income', y='hours.per.week', color='income', title='Hours per Week by Income Level'))
    
elif page == 'Multivariate Analysis':
    question = st.selectbox('Select Question',['How do education level and gender together affect income?','Does the relationship between age and income differ by gender?','How do education level and working hours together influence income?'])
    if question == 'How do education level and gender together affect income?':
        st.plotly_chart(px.histogram(data_frame= adults, x= 'education', color= 'income',barmode='group',facet_col='sex', title= 'Income by Education and Gender'))

    elif question == 'Does the relationship between age and income differ by gender?':
        st.plotly_chart(px.histogram(adults, x='age', color='income',facet_col='sex', title='Age Distribution by Income and Gender'))

    elif question == 'How do education level and working hours together influence income?':
        st.plotly_chart(px.scatter(adults, x='hours.per.week', y='education.num', color='income',title='Income by Hours Worked and Education Level',))

