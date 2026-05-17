import streamlit as st
from datetime import date

st.set_page_config(
    page_title="Agent Horizon",
    page_icon="🌅",
    layout="wide"
)

st.title("🌅 Agent Horizon")
st.caption("The living year-scale calendar for AI agents")

# Sidebar
with st.sidebar:
    st.header("Builder Program")
    st.write("**Current Week:** 0 / 36")
    st.progress(0)
    st.selectbox("Difficulty Tier", ["Explorer", "Builder", "Pathfinder"], index=1)

# Main content
col1, col2 = st.columns([2, 1])

with col1:
    st.success("✅ Project skeleton is ready!")
    st.markdown("### Welcome to Week 0 - Builder Foundations")
    if st.button("🚀 Start Onboarding Week", type="primary"):
        st.balloons()
        st.info("Week 0 would load here with safety frameworks, journal setup, etc.")

with col2:
    st.info("**Program Status**")
    st.write("Start Date: 2026-09-01")
    st.write("Projected End: 2027-05-15")
    st.write("Status: **Active**")

st.divider()
st.caption("Built with Agent Horizon • Local-first & Private")