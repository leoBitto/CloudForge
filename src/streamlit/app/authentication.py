import streamlit as st
import requests
from functools import wraps

def require_auth(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'sessionid' not in st.context.cookies:
            st.error("Effettua il login")
            return False
        
        response = requests.post(
            'http://django-app:8000/auth/api/verify-session/',
            json={'sessionid': st.context.cookies['sessionid']}
        )
        
        if response.status_code == 200:
            user_data = response.json()
            st.session_state.user = user_data['user']
            return func(*args, **kwargs)
        else:
            st.error("Sessione non valida")
            return False
    return wrapper