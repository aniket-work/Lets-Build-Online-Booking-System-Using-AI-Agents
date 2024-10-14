import streamlit as st
from agent import receive_message_from_caller, CONVERSATION
from langchain_core.messages import HumanMessage
from config import AppConfig
from logger import setup_logger
from utils import initialize_session_state, process_appointments

logger = setup_logger(__name__)


def main():
    config = AppConfig()
    initialize_session_state()

    st.set_page_config(layout="wide")
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Appointment Manager")
        for message in CONVERSATION:
            if isinstance(message, HumanMessage):
                st.chat_message("user").write(message.content)
            else:
                st.chat_message("assistant").write(message.content)

        user_input = st.chat_input("Type message here")
        if user_input:
            logger.debug(f"Received user input: {user_input}")
            receive_message_from_caller(user_input)
            st.rerun()

    with col2:
        st.header("Backend Trace")
        st.write("Debug: Session State Contents")
        st.write(st.session_state)

        st.write("Debug: Appointments List")
        st.write(st.session_state.appointments)

        process_appointments()

        # Add a form to manually create an appointment
        st.subheader("Create Appointment")
        with st.form("appointment_form"):
            person_name = st.text_input("Name")
            appointment_type = st.text_input("Appointment Type")
            appointment_date = st.date_input("Date")
            appointment_time = st.time_input("Time")
            submit_button = st.form_submit_button("Add Appointment")

            if submit_button:
                utils.add_manual_appointment(person_name, appointment_type, appointment_date, appointment_time)
                st.rerun()


if __name__ == "__main__":
    main()