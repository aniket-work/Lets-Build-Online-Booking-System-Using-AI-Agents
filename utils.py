import streamlit as st
import datetime
from logger import setup_logger

logger = setup_logger(__name__)

def initialize_session_state():
    if 'appointments' not in st.session_state:
        st.session_state.appointments = []
        logger.debug("Initialized empty appointments list in session state")

def process_appointments():
    logger.debug(f"Appointments in session state: {st.session_state.appointments}")
    for appointment in st.session_state.appointments:
        logger.debug(f"Processing appointment: {appointment}")
        st.write(f"Debug: Processing appointment: {appointment}")
        st.write(
            f"{appointment['name']} - {appointment['type']} on {appointment['time'].strftime('%B %d, %Y at %I:%M %p')}")

    if not st.session_state.appointments:
        st.write("No appointments scheduled.")
        logger.debug("No appointments found in session state")

def add_manual_appointment(person_name, appointment_type, appointment_date, appointment_time):
    new_appointment = {
        "name": person_name,
        "type": appointment_type,
        "time": datetime.datetime.combine(appointment_date, appointment_time)
    }
    st.session_state.appointments.append(new_appointment)
    logger.debug(f"Manually added appointment: {new_appointment}")