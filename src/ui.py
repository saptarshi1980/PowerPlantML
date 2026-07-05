"""
Reusable UI Components
"""

import streamlit as st


def page_header(title, description):
    """
    Display a consistent page header.
    """

    st.title(title)
    st.markdown(description)
    st.divider()


def show_footer():

    st.divider()

    st.caption(
        "PowerPlantML • AI Decision Support System"
    )


def kpi_card(label, value):

    st.metric(
        label=label,
        value=value
    )


def success(message):

    st.success(message)


def error(message):

    st.error(message)