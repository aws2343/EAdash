import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder

st.set_page_config(page_title="Employee Attrition Dashboard", layout="wide")

st.title("📊 Employee Attrition Analytics Dashboard")
st.markdown("This dashboard provides in-depth insights into employee attrition to support strategic HR decisions.")

# Load data
df = pd.read_csv("EA.csv")

# Label Encoding for Attrition (if needed)
if df['Attrition'].dtype != 'int64':
    le = LabelEncoder()
    df['Attrition'] = le.fit_transform(df['Attrition'])

# Sidebar Filters
st.sidebar.header("Filter the data:")

# Example Filters
departments = st.sidebar.multiselect("Select Department(s):", options=df['Department'].unique(), default=df['Department'].unique())
genders = st.sidebar.multiselect("Select Gender(s):", options=df['Gender'].unique(), default=df['Gender'].unique())
ages = st.sidebar.slider("Select Age Range:", int(df['Age'].min()), int(df['Age'].max()), (25, 50))

# Apply filters
filtered_df = df[(df['Department'].isin(departments)) &
                 (df['Gender'].isin(genders)) &
                 (df['Age'] >= ages[0]) & (df['Age'] <= ages[1])]

# Tabs for Macro and Micro Analysis
tab1, tab2 = st.tabs(["📈 Macro-Level Insights", "🔍 Micro-Level Employee Views"])

with tab1:
    st.header("📌 Key Metrics")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Employees", len(filtered_df))
    col2.metric("Attrition Count", int(filtered_df['Attrition'].sum()))
    col3.metric("Attrition Rate (%)", round(filtered_df['Attrition'].mean() * 100, 2))

    st.subheader("1. Attrition by Department")
    st.caption("This shows how attrition is distributed across departments.")
    fig1 = px.histogram(filtered_df, x="Department", color="Attrition", barmode="group")
    st.plotly_chart(fig1, use_container_width=True)

    st.subheader("2. Age Distribution")
    st.caption("Age-wise count of employees with attrition overlay.")
    fig2 = px.histogram(filtered_df, x="Age", color="Attrition", nbins=30, marginal="rug")
    st.plotly_chart(fig2, use_container_width=True)

    st.subheader("3. Gender vs Attrition")
    st.caption("This explores attrition trends by gender.")
    fig3 = px.histogram(filtered_df, x="Gender", color="Attrition", barmode="group")
    st.plotly_chart(fig3, use_container_width=True)

    st.subheader("4. Monthly Income Distribution")
    st.caption("Income distribution among current and former employees.")
    fig4 = px.box(filtered_df, x="Attrition", y="MonthlyIncome", color="Attrition")
    st.plotly_chart(fig4, use_container_width=True)

    st.subheader("5. Job Role vs Attrition")
    st.caption("Which job roles have the most attrition?")
    fig5 = px.histogram(filtered_df, x="JobRole", color="Attrition", barmode="group")
    st.plotly_chart(fig5, use_container_width=True)

    st.subheader("6. Heatmap of Correlation")
    st.caption("This visualizes correlation between numerical features and attrition.")
    corr = filtered_df.select_dtypes(include='number').corr()
    fig6, ax6 = plt.subplots(figsize=(10, 6))
    sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", ax=ax6)
    st.pyplot(fig6)

with tab2:
    st.header("🔍 Employee-Level Details")
    st.caption("Use dropdowns to drill down to individual employee records.")

    selected_emp = st.selectbox("Select an Employee ID:", df['EmployeeNumber'])
    emp_info = df[df['EmployeeNumber'] == selected_emp]
    st.write(emp_info.T)

    st.subheader("7. Education vs Attrition")
    st.caption("Exploring attrition across education levels.")
    fig7 = px.histogram(filtered_df, x="EducationField", color="Attrition", barmode="group")
    st.plotly_chart(fig7, use_container_width=True)

    st.subheader("8. Years at Company vs Attrition")
    fig8 = px.box(filtered_df, x="Attrition", y="YearsAtCompany", color="Attrition")
    st.plotly_chart(fig8, use_container_width=True)

    st.subheader("9. Overtime vs Attrition")
    if "OverTime" in df.columns:
        fig9 = px.histogram(filtered_df, x="OverTime", color="Attrition", barmode="group")
        st.plotly_chart(fig9, use_container_width=True)

    st.subheader("10. Performance Rating")
    if "PerformanceRating" in df.columns:
        fig10 = px.box(filtered_df, x="Attrition", y="PerformanceRating", color="Attrition")
        st.plotly_chart(fig10, use_container_width=True)

# Add more charts (up to 20+) in this format using st.subheader(), fig = px/plt, st.plotly_chart/st.pyplot

st.markdown("---")
st.caption("Dashboard created for XYZ Company – HR Analytics Team")
