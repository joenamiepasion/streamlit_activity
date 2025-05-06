import streamlit as st

st.title("💻 San Pedro College")
st.subheader("Empowering Minds through Technology")
st.caption("🇵🇭 Republic of the Philippines")

st.markdown("---")

st.sidebar.header("🧭 Navigation Panel")
selected_topic = st.sidebar.selectbox(
    "Choose a topic",
    ("Computer Networks", "Operating Systems")
)

show_details = st.sidebar.checkbox("Show technical insights")

st.header(f"Topic: {selected_topic}")

tab1, tab2 = st.tabs(["Overview", "Core Concepts"])

with tab1:
    st.subheader("Overview")

    if selected_topic == "Computer Networks":
        st.write("""
        Computer Networks refer to interconnected computing devices that can exchange data and resources.
        They enable communication via wired or wireless technologies using protocols like TCP/IP.
        """)
    else:
        st.write("""
        Operating Systems (OS) manage hardware and software resources of a computer.
        It provides essential services such as process management, memory handling, and file operations.
        """)

# Key Concepts Tab
with tab2:
    st.subheader("Core Concepts")

    col1, col2 = st.columns(2)

    with col1:
        if selected_topic == "Computer Networks":
            with st.expander("🌐 IP Addressing"):
                st.write("IP addressing allows each device in a network to be uniquely identified for communication.")

            with st.expander("🔁 Routing and Switching"):
                st.write("Routing directs data across networks, while switching connects devices within the same network.")

        else:
            with st.expander("🧠 Process Management"):
                st.write("The OS manages processes by allocating CPU time, managing threads, and synchronizing tasks.")

            with st.expander("💾 Memory Management"):
                st.write("Handles allocation and deallocation of RAM, using techniques like paging and segmentation.")

    with col2:
        if selected_topic == "Computer Networks":
            with st.expander("📡 Network Protocols"):
                st.write("Protocols like TCP, UDP, and HTTP govern how data is formatted, transmitted, and received.")

            with st.expander("🔐 Network Security"):
                st.write("Secures data transmission using firewalls, encryption, and secure communication protocols.")
        else:
            with st.expander("📂 File Systems"):
                st.write("File systems organize data on storage devices and manage access permissions.")

            with st.expander("👤 User Interfaces"):
                st.write("Operating systems offer CLI or GUI interfaces for user interaction with system components.")

# Optional Details
if show_details:
    st.markdown("---")
    st.subheader("🧾 Technical Insights")

    if selected_topic == "Computer Networks":
        st.write("""
        A typical network setup includes routers, switches, and servers, communicating via standard protocols.
        Understanding the OSI model (Layered architecture) is essential for troubleshooting and network design.
        """)
    else:
        st.write("""
        Operating Systems handle multitasking using scheduling algorithms like Round Robin and Priority Scheduling.
        They also ensure resource isolation and security through user permission controls and system calls.
        """)
