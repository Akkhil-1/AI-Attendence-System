# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return render_template('index.html')

# if __name__ == '__main__':
#     app.run(debug=True, port=5002)

import streamlit as st 

from src.screens.home_screen import home_screen
from src.screens.student_screen import student_screen
from src.screens.teacher_screen import teacher_screen

def main():
    if 'login_type' not in st.session_state:
        st.session_state['login_type'] = None    # initialize
        
    match st.session_state['login_type'] :
        case 'teacher':
            teacher_screen()
        
        case 'student':
            student_screen()
        
        case None:
            home_screen()

main()