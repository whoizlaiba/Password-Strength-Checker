import streamlit as st
import re

# 🎨 Custom CSS for styling
st.markdown("""
    <style>
        /* Title styling */
        .css-1d391kg {
            color: #4caf50;
            font-size: 36px;
            font-weight: bold;
            text-align: center;
        }

        /* Description styling */
        .css-1q8b0bq {
            font-size: 18px;
            color: #333;
            line-height: 1.5;
            text-align: center;
        }

        /* Input field styling */
        .stTextInput input {
            font-size: 18px;
            color: #333;
            padding: 10px;
            border-radius: 8px;
            border: 2px solid #4caf50;
        }

        /* Button styling */
        .stButton>button {
            background-color: #4caf50;
            color: white;
            border-radius: 10px;
            padding: 10px 20px;
            border: none;
            font-size: 18px;
            cursor: pointer;
        }

        .stButton>button:hover {
            background-color: #45a049;
        }

        /* Success message styling */
        .stAlert.stSuccess {
            background-color: #388e3c;
            color: white;
            font-size: 18px;
            border-radius: 8px;
            padding: 12px;
        }

        /* Warning message styling */
        .stAlert.stWarning {
            background-color: #ff9800;
            color: white;
            font-size: 18px;
            border-radius: 8px;
            padding: 12px;
        }

        /* Error message styling */
        .stAlert.stError {
            background-color: #d32f2f;
            color: white;
            font-size: 18px;
            border-radius: 8px;
            padding: 12px;
        }

        /* Footer styling */
        .css-1ynkhrd {
            font-size: 14px;
            color: #777;
            text-align: center;
            padding: 10px;
        }

        /* Info box styling */
        .stInfo {
            background-color: #f1f1f1;
            border-left: 4px solid #2196f3;
            padding: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# 🎉 Title
st.title("🔐 **Ultimate Password Strength Checker**")

# 🏷️ Input Field
password = st.text_input("🔑 **Enter your password:**", type="password")

# 🔍 Password Strength Check
def check_password_strength(password):
    score = 0
    feedback = []

    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ **Password should be at least 8 characters long.**")

    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ **Include both uppercase and lowercase letters.**")

    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ **Add at least one number (0-9).**")

    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ **Include at least one special character (!@#$%^&*).**")

    return score, feedback


# ✅ Button to Check Password
if st.button("🔍 **Check Password Strength**"):
    if password:
        score, feedback = check_password_strength(password)

        st.subheader("🔒 **Password Strength Result:**")

        if score == 4:
            st.success("✅ **Strong Password! Your password is secure.**")
        elif score == 3:
            st.warning("⚠️ **Moderate Password - Consider adding more security features.**")
        else:
            st.error("❌ **Weak Password - Improve it using the suggestions below.**")

        if feedback:
            st.info("💡 **Suggestions to improve your password:**")
            for tip in feedback:
                st.write(tip)
    else:
        st.error("🚨 **Please enter a password to check.**")

# 📝 Description
st.markdown("""
**Welcome to the Ultimate Password Strength Checker!**  
**Ensure your password is secure by checking:**
- ✅ **Length**
- ✅ **Upper & Lowercase letters**
- ✅ **Numbers**
- ✅ **Special Characters**

 ⚡ **Improve your online security by creating strong passwords!** 
""")
