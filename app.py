import streamlit as st

# ====== Page Configuration ======
st.set_page_config(
    page_title="Web Word Count Analyzer",
    page_icon="📊",
    layout="wide"
)

# ====== Header Section ======
with st.container():
    col1, col2 = st.columns([1, 3])
    with col1:
        st.image("assets/future-group-logo.png", width=150)
    with col2:
        st.title("Web Word Count Analyzer")
        st.caption("Localization Engineering Tool • 2025 • v0.1.0")

# ====== Sidebar ======
with st.sidebar:
    st.header("Developer Info")
    st.subheader("Ahmed Mostafa Saad")
    st.write("""
    - **Position**: Localization Engineering & TMS Support Lead  
    - **Email**: [ahmed.mostafaa@future-group.com](mailto:ahmed.mostafaa@future-group.com)  
    - **Company**: Future Group Translation Services
    """)
    st.divider()

    st.header("Usage Instructions")
    st.write("""
    1. Enter the target website URL  
    2. Configure the crawl settings  
    3. Choose word count strategy  
    4. Start analysis to get reports and page exports
    """)

# ====== Input Section ======
st.header("Analyze Website Word Count")

with st.form("crawl_form"):
    url = st.text_input("Target Website URL", placeholder="https://www.example.com")
    max_depth = st.slider("Crawl Depth", min_value=1, max_value=5, value=3)
    word_count_method = st.selectbox("Word Count Method", [
        "Simple (whitespace split)",
        "Advanced (tokenizer-based)",
        "Trados-like (CAT tool segmentation)"
    ])
    custom_instructions = st.text_area("Custom Instructions (optional)", height=120)
    submitted = st.form_submit_button("
