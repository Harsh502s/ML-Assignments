# Creating a web app using Streamlit and Deploying it to Streamlit Cloud

# Path: Notebooks\ML Deploy.ipynb

# Importing libraries

import streamlit as st
import pickle


# Loading the pickle file

with open(r"C:\Users\ds12\College\ML-Assignments\Notebooks\model.pkl", "rb") as f:
    model = pickle.load(f)
    pass

# Taking input of features from the user and storing it in a variable

# Taking pclass as input from the as selectbox

pclass = st.selectbox("Passenger Class", ["1", "2", "3"])

# Taking age as input from the user as a slider

age = st.slider("Age", 0, 100)

# Taking sibsp as input from the user in integer form

sibsp = st.slider("Siblings/Spouses Aboard", 0, 10)

# Taking parch as input from the user in integer form

parch = st.slider("Parents/Children Aboard", 0, 10)

# Taking fare as input from the user in integer form

fare = st.number_input("Fare")

# Taking input of sex_Male from the user in the form of 0 and 1

gender = st.selectbox("Sex", ["Male", "Female"])

if gender == "Male":
    sex_Male = 1
else:
    sex_Male = 0

# Taking input of embarked_C from the user in the form of 0 and 1

embarked_C = st.selectbox("Embarked_C", ["0", "1"])

# Taking input of embarked_Q from the user in the form of 0 and 1

embarked_Q = st.selectbox("Embarked_Q", ["0", "1"])

# Taking input of embarked_S from the user in the form of 0 and 1

embarked_S = st.selectbox("Embarked_S", ["0", "1"])

# Creating a button to predict the output

if st.button("Predict"):
    ypred = model.predict(
        [
            [
                pclass,
                age,
                sibsp,
                parch,
                fare,
                sex_Male,
                embarked_C,
                embarked_Q,
                embarked_S,
            ]
        ]
    )
    # Printing the output

    if ypred == 0:
        st.write("The passenger did not survive")
    else:
        st.write("The passenger survived")
