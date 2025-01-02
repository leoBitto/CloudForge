import streamlit as st
from authentication import require_auth

st.set_page_config(
    page_title="Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

def render_sidebar():
    with st.sidebar:
        st.title("Menu")
        st.write(f"👤 {st.session_state.user['username']}")
        st.write(f"🔑 Gruppi: {', '.join(st.session_state.user['groups'])}")
        
        st.header("Navigation")
        return st.radio("Seleziona sezione:", ["Dashboard", "Analisi", "Impostazioni"])


@require_auth
def main():
    menu_choice = render_sidebar()
    st.title(f"📊 {menu_choice}")
    
    if menu_choice == "Dashboard":
        col1, col2 = st.columns(2)
        with col1:
            with st.container():
                st.subheader("Card 1")
                st.write("Contenuto")
        with col2:
            with st.container():
                st.subheader("Card 2")
                st.write("Contenuto")
    elif menu_choice == "Analisi":
        st.write("Sezione Analisi")
    elif menu_choice == "Impostazioni":
        render_settings()


if __name__ == "__main__":
    main()