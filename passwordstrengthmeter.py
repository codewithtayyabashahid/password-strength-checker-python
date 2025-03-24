#build a password strength meter with python & streamlit

import streamlit as st
import re

#page styling
st.set_page_config(page_title="Password Strength Checker by Tayyaba Shahid", page_icon="🔐",layout="centered")

#styling with css
st.markdown("""
<style>
            .main {text-align: center;}
            .stTextInput {width: 60% !important; margin: auto;}
            .stButton button { width: 50%; background-color:rgb(0, 0, 0); color: white; font-size: 18px; }
            .stButton button:hover { background-color: white; }
                </style>
            """, unsafe_allow_html=True)

#Page title and desription
st.title( "🔐 Password Strength Checker")
st.write("🔍Check your password strength with this simple tool")

#function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []
    
    #check length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌Weak: Password is less than 8 characters")
        
    #check for uppercase and lowercase
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("❌Weak: Password does not contain both uppercase and lowercase letters")
        
    #check for numbers
    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("❌Weak: Password should include one number (0-9)")
        
    #check for special characters
    if re.search(r'[!@#$%^&*(),.?":{}<>|]', password):
        score += 1
    else:
        feedback.append("❌Weak: Password should include one special character (e.g . , ! @ # $ % ^ & * ())")
        
    ##display password strength results 
    if score >= 5:
        st.success("🔑 Strong Password")
    elif score >= 3:
        st.warning("🔑 Medium Password")
    else:
        st.error("❌ Weak Password . Follow suggestions to improve it.")

        #feedback 
        if feedback:
            with st.expander("🔍 improve your password"):
                for item in feedback:
                    st.write(item)
password = st.text_input("Enter your password", type="password" ,help="password should be at least 8 characters long and contain both uppercase and lowercase letters, numbers, and special characters")

#BUTTON WORKING
if st.button("Check Password Strength"):
    if password:
        check_password_strength(password)
    else:
        st.warning(" ⚠️ Please enter a password to check its strength")
