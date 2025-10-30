# Slotted ALOHA Protocol Simulator

This project is an interactive web application built with **Streamlit** to simulate and visualize the Slotted ALOHA random access protocol.

It allows you to adjust parameters like the number of nodes (N) and their transmission probability (p) to instantly see how they affect network performance. This tool is perfect for students and engineers who want to visualize the trade-offs between network load and throughput.


*(Note: Make sure your screenshot files are in the same directory as the README or update the paths!)*

## ✨ Features

* **Interactive Controls:** Use sliders to set the **Number of Nodes (N)** and **Transmission Probability (p)**.
* **Real-time Calculations:** Instantly see the **Offered Load ($G = N \times p$)** and the resulting **Throughput (S)**.
* **Performance vs. Theory:** The "Throughput vs Offered Load" graph plots your simulation's result (red dot) against the theoretical Slotted ALOHA performance curve ($S = G \times e^{-G}$). It also highlights the theoretical maximum throughput (green star) at $G=1$.
* **Detailed Visualizations:**
    * **Time Slot Distribution:** A pie chart breaking down the simulation into **Successful**, **Collision**, and **Idle** slots.
    * **Transmission Activity Timeline:** A bar chart that visualizes the status of the first 100 time slots, clearly showing where collisions occurred.
* **Complete Statistics:** Get a full summary of simulation parameters and performance metrics, including total collisions, successes, and efficiency.

## 💡 The Theory

This simulator demonstrates the core concept of Slotted ALOHA:

* Time is divided into discrete **slots**.
* Nodes can only begin transmitting at the start of a slot.
* A **Success** occurs if *exactly one* node transmits in a slot.
* A **Collision** occurs if *two or more* nodes transmit in the same slot.
* An **Idle** slot occurs if *zero* nodes transmit.

The simulation proves the theory that the maximum possible throughput is $1/e \approx 0.368$ (or 36.8%), which happens only when the offered load $G=1$.

## 🚀 How to Run This Project

Follow these steps to set up and run the simulator on your local machine.

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/slotted-aloha-simulator.git](https://github.com/your-username/slotted-aloha-simulator.git)
    cd slotted-aloha-simulator
    ```

2.  **Create and activate a virtual environment:**
    *(This is a best practice to keep dependencies isolated)*
    ```bash
    # Create the virtual environment
    python3 -m venv venv

    # Activate it (on macOS/Linux)
    source venv/bin/activate

    # (On Windows, use: .\venv\Scripts\activate)
    ```

3.  **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Streamlit app:**
    ```bash
    streamlit run app.py
    ```
    *(If your main Python file is named differently, like `main.py`, use that name instead.)*

    Streamlit will automatically open the simulator in your default web browser.

## 🛠️ Technologies Used

* **Python**
* **Streamlit** - For the interactive web app UI
* **NumPy** - For efficient numerical calculations
* **Pandas** - For data structuring
* **Matplotlib** / **Altair** - For plotting the graphs

## Authors

* Katyayni Aarya
* Suyesha Saha
