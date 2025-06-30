import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from sklearn.preprocessing import LabelEncoder

st.set_page_config(page_title="Employee Attrition Dashboard", layout="wide")
st.title("📊 Employee Attrition Dashboard")
st.markdown("This interactive dashboard provides key insights for HR leadership to monitor and analyze employee attrition patterns across the organization.")

# Load data
df = pd.read_csv("EA.csv")

# Encode 'Attrition' if it's categorical
if df['Attrition'].dtype == 'object':
    le = LabelEncoder()
    df['Attrition'] = le.fit_transform(df['Attrition'])

# Sidebar filters
st.sidebar.header("Filter Options")
departments = st.sidebar.multiselect("Department", options=df['Department'].unique(), default=df['Department'].unique())
genders = st.sidebar.multiselect("Gender", options=df['Gender'].unique(), default=df['Gender'].unique())
ages = st.sidebar.slider("Age Range", int(df['Age'].min()), int(df['Age'].max()), (25, 50))

filtered_df = df[
    (df['Department'].isin(departments)) &
    (df['Gender'].isin(genders)) &
    (df['Age'].between(ages[0], ages[1]))
]

# Tabs
tab1, tab2 = st.tabs(["📈 Overview", "🔍 Detailed Analysis"])

with tab1:
    st.header("Overview Metrics and Visualizations")

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Employees", len(filtered_df))
    col2.metric("Attrition Count", int(filtered_df['Attrition'].sum()))
    col3.metric("Attrition Rate (%)", round(filtered_df['Attrition'].mean() * 100, 2))

    # 1. Attrition by Department
    st.subheader("1. Attrition by Department")
    st.caption("Shows which departments have the highest attrition counts.")
    fig1 = px.histogram(filtered_df, x="Department", color="Attrition", barmode="group")
    st.plotly_chart(fig1, use_container_width=True)

    # 2. Age Distribution
    st.subheader("2. Age Distribution with Attrition")
    fig2 = px.histogram(filtered_df, x="Age", color="Attrition", nbins=30)
    st.plotly_chart(fig2, use_container_width=True)

    # 3. Gender and Attrition
    st.subheader("3. Attrition by Gender")
    fig3 = px.histogram(filtered_df, x="Gender", color="Attrition", barmode="group")
    st.plotly_chart(fig3, use_container_width=True)

    # 4. Monthly Income Distribution
    st.subheader("4. Monthly Income Distribution")
    fig4 = px.box(filtered_df, x="Attrition", y="MonthlyIncome", color="Attrition")
    st.plotly_chart(fig4, use_container_width=True)

    # 5. Job Role and Attrition
    st.subheader("5. Job Role vs Attrition")
    fig5 = px.histogram(filtered_df, x="JobRole", color="Attrition", barmode="group")
    st.plotly_chart(fig5, use_container_width=True)

    # 6. Education Field and Attrition
    st.subheader("6. Education Field and Attrition")
    fig6 = px.histogram(filtered_df, x="EducationField", color="Attrition", barmode="group")
    st.plotly_chart(fig6, use_container_width=True)

    # 7. Years at Company
    st.subheader("7. Years at Company vs Attrition")
    fig7 = px.box(filtered_df, x="Attrition", y="YearsAtCompany", color="Attrition")
    st.plotly_chart(fig7, use_container_width=True)

    # 8. Environment Satisfaction
    st.subheader("8. Environment Satisfaction")
    fig8 = px.histogram(filtered_df, x="EnvironmentSatisfaction", color="Attrition", barmode="group")
    st.plotly_chart(fig8, use_container_width=True)

    # 9. Work-Life Balance
    st.subheader("9. Work-Life Balance and Attrition")
    fig9 = px.histogram(filtered_df, x="WorkLifeBalance", color="Attrition", barmode="group")
    st.plotly_chart(fig9, use_container_width=True)

    # 10. OverTime vs Attrition
    if 'OverTime' in df.columns:
        st.subheader("10. OverTime and Attrition")
        fig10 = px.histogram(filtered_df, x="OverTime", color="Attrition", barmode="group")
        st.plotly_chart(fig10, use_container_width=True)

with tab2:
    st.header("Micro-Level Exploration")

    # 11. Heatmap
    st.subheader("11. Correlation Heatmap")
    st.caption("Shows correlation between numerical variables and attrition.")
    corr = filtered_df.select_dtypes(include='number').corr()
    fig11, ax11 = plt.subplots(figsize=(12, 8))
    sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f", ax=ax11)
    st.pyplot(fig11)

    # 12. Marital Status and Attrition
    st.subheader("12. Marital Status")
    fig12 = px.histogram(filtered_df, x="MaritalStatus", color="Attrition", barmode="group")
    st.plotly_chart(fig12, use_container_width=True)

    # 13. Distance From Home
    st.subheader("13. Distance From Home")
    fig13 = px.box(filtered_df, x="Attrition", y="DistanceFromHome", color="Attrition")
    st.plotly_chart(fig13, use_container_width=True)

    # 14. Years With Current Manager
    st.subheader("14. Years With Current Manager")
    fig14 = px.box(filtered_df, x="Attrition", y="YearsWithCurrManager", color="Attrition")
    st.plotly_chart(fig14, use_container_width=True)

    # 15. Num Companies Worked
    st.subheader("15. Number of Companies Worked")
    fig15 = px.histogram(filtered_df, x="NumCompaniesWorked", color="Attrition", barmode="group")
    st.plotly_chart(fig15, use_container_width=True)

    # 16. Total Working Years
    st.subheader("16. Total Working Years")
    fig16 = px.box(filtered_df, x="Attrition", y="TotalWorkingYears", color="Attrition")
    st.plotly_chart(fig16, use_container_width=True)

    # 17. Job Level
    st.subheader("17. Job Level")
    fig17 = px.histogram(filtered_df, x="JobLevel", color="Attrition", barmode="group")
    st.plotly_chart(fig17, use_container_width=True)

    # 18. Training Times Last Year
    st.subheader("18. Training Times Last Year")
    fig18 = px.histogram(filtered_df, x="TrainingTimesLastYear", color="Attrition", barmode="group")
    st.plotly_chart(fig18, use_container_width=True)

    # 19. Relationship Satisfaction
    st.subheader("19. Relationship Satisfaction")
    fig19 = px.histogram(filtered_df, x="RelationshipSatisfaction", color="Attrition", barmode="group")
    st.plotly_chart(fig19, use_container_width=True)

    # 20. Hourly Rate
    if "HourlyRate" in df.columns:
        st.subheader("20. Hourly Rate")
        fig20 = px.box(filtered_df, x="Attrition", y="HourlyRate", color="Attrition")
        st.plotly_chart(fig20, use_container_width=True)

st.markdown("---")
st.caption("Dashboard created for XYZ HR Leadership • Powered by Streamlit")


### ✅ requirements.txt

```txt
streamlit
pandas
matplotlib
seaborn
plotly
