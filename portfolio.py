import streamlit as st

# Portfolio title and description
st.title("My Streamlit Portfolio")
st.write("""
Welcome to my portfolio! Below are some of the projects I've worked on. 
Click on the project links to explore them interactively.
""")

# Dictionary of projects
projects = {
    "Loan Approval Prediction": "https://pe372hvim2k9vuccfq7kre.streamlit.app/",
    "Customer Churn Prediction": "projects/churn_prediction/app.py",
    "House Price Prediction": "projects/house_price/app.py",
}

# Display project links
for project_name, project_path in projects.items():
    st.write(f"### [{project_name}](/{project_path})")

# Note: Adjust the paths according to your project structure.

