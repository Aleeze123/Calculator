import streamlit as st

def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Cannot divide by zero!"
    else:
        return "Invalid operator!"

# Streamlit UI
st.title("Aleeza Calculator")

num1 = st.number_input("Enter first number", value=0)
num2 = st.number_input("Enter second number", value=0)
operator = st.selectbox("Choose operator", ['+', '-', '*', '/'])

if st.button("Calculate"):
    result = calculate(num1, num2, operator)
    st.write(f"The result is: {result}")


