import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="Slotted ALOHA Simulator",
    page_icon="📡",
    layout="wide"
)

# Title and description
st.title("📡 Slotted ALOHA Protocol Simulator")
st.markdown("""
This simulator demonstrates the **Slotted ALOHA** protocol, a random access protocol 
where time is divided into slots and nodes can only transmit at the beginning of a slot.
""")

# Sidebar for input controls
st.sidebar.header("Simulation Parameters")

num_nodes = st.sidebar.slider(
    "Number of Nodes",
    min_value=2,
    max_value=50,
    value=10,
    help="Number of nodes competing for channel access"
)

transmission_prob = st.sidebar.slider(
    "Transmission Probability (p)",
    min_value=0.01,
    max_value=1.0,
    value=0.3,
    step=0.01,
    help="Probability that a node will attempt to transmit in a given slot"
)

num_slots = st.sidebar.slider(
    "Number of Time Slots",
    min_value=100,
    max_value=5000,
    value=1000,
    step=100,
    help="Total number of time slots to simulate"
)

# Run simulation button
run_simulation = st.sidebar.button("Run Simulation", type="primary")

# Slotted ALOHA simulation logic
def simulate_slotted_aloha(num_nodes, p, num_slots):
    """
    Simulate Slotted ALOHA protocol
    
    Returns:
    - slots_data: List of tuples (slot_number, num_transmissions, status)
    - statistics: Dictionary with overall statistics
    """
    slots_data = []
    successful_transmissions = 0
    collisions = 0
    idle_slots = 0
    
    for slot in range(num_slots):
        # Each node decides to transmit with probability p
        transmitting_nodes = np.random.random(num_nodes) < p
        num_transmissions = np.sum(transmitting_nodes)
        
        if num_transmissions == 0:
            status = "Idle"
            idle_slots += 1
        elif num_transmissions == 1:
            status = "Success"
            successful_transmissions += 1
        else:
            status = "Collision"
            collisions += 1
        
        slots_data.append((slot, num_transmissions, status))
    
    # Calculate throughput (successful transmissions per slot)
    throughput = successful_transmissions / num_slots
    
    # Theoretical maximum throughput for Slotted ALOHA is 1/e ≈ 0.368
    theoretical_max = 1 / np.e
    
    # Calculate offered load (G = N * p)
    offered_load = num_nodes * p
    
    statistics = {
        "successful": successful_transmissions,
        "collisions": collisions,
        "idle": idle_slots,
        "throughput": throughput,
        "theoretical_max": theoretical_max,
        "offered_load": offered_load,
        "efficiency": (throughput / theoretical_max) * 100
    }
    
    return slots_data, statistics

# Theoretical throughput curve
def get_theoretical_throughput(G_values):
    """Calculate theoretical throughput: S = G * e^(-G)"""
    return G_values * np.exp(-G_values)

# Main simulation
if run_simulation:
    with st.spinner("Running simulation..."):
        slots_data, stats = simulate_slotted_aloha(num_nodes, transmission_prob, num_slots)
    
    # Display statistics
    st.header("Simulation Results")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            "Throughput (S)",
            f"{stats['throughput']:.4f}",
            help="Successful transmissions per slot"
        )
    
    with col2:
        st.metric(
            "Success Rate",
            f"{(stats['successful']/num_slots)*100:.1f}%"
        )
    
    with col3:
        st.metric(
            "Collision Rate",
            f"{(stats['collisions']/num_slots)*100:.1f}%"
        )
    
    with col4:
        st.metric(
            "Idle Rate",
            f"{(stats['idle']/num_slots)*100:.1f}%"
        )
    
    # Create two columns for charts
    chart_col1, chart_col2 = st.columns(2)
    
    with chart_col1:
        st.subheader("📈 Throughput vs Offered Load")
        
        # Create figure
        fig1, ax1 = plt.subplots(figsize=(8, 6))
        
        # Theoretical curve
        G_range = np.linspace(0, 5, 100)
        S_theoretical = get_theoretical_throughput(G_range)
        ax1.plot(G_range, S_theoretical, 'b-', linewidth=2, label='Theoretical')
        
        # Simulated point
        ax1.plot(stats['offered_load'], stats['throughput'], 'ro', 
                markersize=12, label=f'Simulated (G={stats["offered_load"]:.2f})')
        
        # Mark maximum throughput
        max_G = 1.0
        max_S = 1/np.e
        ax1.plot(max_G, max_S, 'g*', markersize=15, 
                label=f'Maximum (G=1, S={max_S:.3f})')
        
        ax1.set_xlabel('Offered Load (G = N × p)', fontsize=12)
        ax1.set_ylabel('Throughput (S)', fontsize=12)
        ax1.set_title('Slotted ALOHA Performance', fontsize=14, fontweight='bold')
        ax1.grid(True, alpha=0.3)
        ax1.legend()
        ax1.set_xlim(0, 5)
        ax1.set_ylim(0, 0.4)
        
        st.pyplot(fig1)
    
    with chart_col2:
        st.subheader("🥧 Slot Status Distribution")
        
        # Create pie chart
        fig2, ax2 = plt.subplots(figsize=(8, 6))
        
        sizes = [stats['successful'], stats['collisions'], stats['idle']]
        labels = ['Successful', 'Collisions', 'Idle']
        colors = ['#2ecc71', '#e74c3c', '#95a5a6']
        explode = (0.1, 0, 0)
        
        ax2.pie(sizes, explode=explode, labels=labels, colors=colors,
                autopct='%1.1f%%', shadow=True, startangle=90)
        ax2.set_title('Time Slot Distribution', fontsize=14, fontweight='bold')
        
        st.pyplot(fig2)
    
    # Detailed statistics
    st.subheader("Detailed Statistics")
    
    col_a, col_b = st.columns(2)
    
    with col_a:
        st.info(f"""
        **Simulation Parameters:**
        - Number of Nodes: {num_nodes}
        - Transmission Probability: {transmission_prob:.2f}
        - Total Time Slots: {num_slots}
        - Offered Load (G): {stats['offered_load']:.3f}
        """)
    
    with col_b:
        st.success(f"""
        **Performance Metrics:**
        - Successful Transmissions: {stats['successful']}
        - Collisions: {stats['collisions']}
        - Idle Slots: {stats['idle']}
        - Efficiency: {stats['efficiency']:.1f}% of theoretical max
        """)
    
    # Time series chart
    st.subheader("⏱Transmission Activity Over Time (First 100 slots)")
    
    fig3, ax3 = plt.subplots(figsize=(12, 4))
    
    # Show first 100 slots
    display_slots = min(100, num_slots)
    slot_numbers = [s[0] for s in slots_data[:display_slots]]
    num_transmissions = [s[1] for s in slots_data[:display_slots]]
    statuses = [s[2] for s in slots_data[:display_slots]]
    
    # Color code by status
    colors_map = {'Idle': '#95a5a6', 'Success': '#2ecc71', 'Collision': '#e74c3c'}
    bar_colors = [colors_map[status] for status in statuses]
    
    ax3.bar(slot_numbers, num_transmissions, color=bar_colors, alpha=0.7)
    ax3.set_xlabel('Time Slot', fontsize=12)
    ax3.set_ylabel('Number of Transmissions', fontsize=12)
    ax3.set_title('Transmission Activity Timeline', fontsize=14, fontweight='bold')
    ax3.grid(True, alpha=0.3, axis='y')
    
    # Add legend
    from matplotlib.patches import Patch
    legend_elements = [
        Patch(facecolor='#2ecc71', alpha=0.7, label='Success'),
        Patch(facecolor='#e74c3c', alpha=0.7, label='Collision'),
        Patch(facecolor='#95a5a6', alpha=0.7, label='Idle')
    ]
    ax3.legend(handles=legend_elements)
    
    st.pyplot(fig3)
    
    # Download results
    st.subheader("Export Results")
    
    # Create DataFrame
    df = pd.DataFrame(slots_data, columns=['Slot', 'Transmissions', 'Status'])
    csv = df.to_csv(index=False)
    
    st.download_button(
        label="Download Simulation Data (CSV)",
        data=csv,
        file_name=f"aloha_simulation_N{num_nodes}_p{transmission_prob}.csv",
        mime="text/csv"
    )

else:
    # Initial state - show explanation
    st.info("Set your parameters in the sidebar and click **Run Simulation** to start!")
    
    st.header("About Slotted ALOHA")
    
    st.markdown("""
    ### How It Works:
    1. **Time is divided into slots** - Nodes can only transmit at slot boundaries
    2. **Random transmission** - Each node transmits with probability `p` in each slot
    3. **Success condition** - Transmission succeeds only if exactly one node transmits
    4. **Collision** - If multiple nodes transmit simultaneously, all packets collide
    
    ### Key Concepts:
    - **Offered Load (G)**: G = N × p (number of nodes × transmission probability)
    - **Throughput (S)**: Average number of successful transmissions per slot
    - **Maximum Throughput**: S_max = 1/e ≈ 0.368 at G = 1
    
    ### Optimal Performance:
    For maximum throughput, set transmission probability to: **p = 1/N**
    
    This ensures the offered load G = N × (1/N) = 1, achieving maximum throughput!
    """)

# Footer
st.divider()
st.markdown("""
<div style="text-align: center;">
    <p style="font-size: 0.9rem; color: #666;">
        Developed for Computer Networks Project | Slotted ALOHA Protocol Simulator<br>
        Copyright © 2025 Katyayni Aarya and Suyesha Saha.<br>
        All rights reserved.
    </p>
</div>
""", unsafe_allow_html=True)