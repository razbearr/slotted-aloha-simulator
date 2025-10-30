import streamlit as st

# --------------------- PAGE CONFIG ---------------------
st.set_page_config(
    page_title="Computer Networks Simulator Dashboard",
    page_icon="🌐",
    layout="centered"
)

# --------------------- MAIN HEADER ---------------------
st.title("Computer Networks Protocol Simulators")

st.markdown("""
Welcome to the **Computer Networks Simulation Dashboard**.  
This application demonstrates key **medium access control (MAC)** protocols used in network communication.
""")

st.divider()

# --------------------- PROJECT DETAILS ---------------------
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    ### 👩‍💻 Developed By:
    **Suyesha Saha & Katyayni Aarya**  
    Department of Computer Science  
    Vellore Institute Of Technology
    """)

with col2:
    st.markdown("""
    ### 🧪 Course:
    **Computer Networks**  
    Academic Year: 2025  
    Instructor: *Swaminathan A*
    """)

st.divider()

# --------------------- AVAILABLE SIMULATORS ---------------------
st.subheader("Available Protocol Simulators")

st.markdown("""
**1️⃣ Slotted ALOHA Simulator**  
Explore the random access protocol that divides time into discrete slots.  
- Analyze idle, successful, and collision slots  
- Visualize throughput vs offered load  
- Download simulation data for analysis  
""")

st.markdown("""
**2️⃣ CSMA & CSMA/CD Simulator**  
Simulate the Carrier Sense Multiple Access protocols with collision detection and backoff.  
- Compare 1-persistent, non-persistent, and p-persistent variants  
- Visualize channel activity, collisions, and efficiency  
- Export comparison results for reporting  
""")

st.divider()

# --------------------- FOOTER ---------------------
st.caption("Developed with Streamlit | Computer Networks Protocol Simulators © 2025")
