import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Artem Sychov")
    content = """
    Result-oriented Engineering Manager with 19+ years of experience.
    Excel in building offshore and onsite teams, deep practical knowledge in
    leadership and motivation. Extensive experience in R&D,
    Product Development, Engineering, QC, and a full delivery cycle.
    """
    st.info(content)

content2 = """
Below you can find some of the apps I have built in Python. Feel free to contact me!
"""
st.write(content2)