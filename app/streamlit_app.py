import streamlit as st
import os
import subprocess
import time
from reports.excel_report import generate_main_report
from reports.trados_like_report import generate_trados_style_report
from utils.zip_utils import zip_html_folder

# Paths
html_dir = "html_pages"
zip_path = "exports/html_pages.zip"
main_excel = "reports/main_report.xlsx"
trados_excel = "reports/trados_report.xlsx"

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
    submitted = st.form_submit_button("Start Analysis")

# ====== Execution ======
if submitted and url:
    st.info("Crawling in progress... Please wait.")
    
    if os.path.exists(html_dir):
        for f in os.listdir(html_dir):
            os.remove(os.path.join(html_dir, f))
    else:
        os.makedirs(html_dir)

    try:
        subprocess.run([
            "scrapy",
            "runspider",
            "crawler/raw_html_spider.py",
            "-a", f"start_url={url}",
            "-a", f"output_dir={html_dir}"
        ], check=True)
        time.sleep(2)
        st.success("Crawling completed.")
    except Exception as e:
        st.error(f"Scrapy failed: {str(e)}")

    html_files = []
    for file in os.listdir(html_dir):
        if file.endswith(".html"):
            html_files.append({
                "url": f"[inferred from {file}]",
                "status": 200,
                "saved_to": os.path.join(html_dir, file)
            })

    generate_main_report(html_files, main_excel)
    generate_trados_style_report(trados_excel)
    zip_html_folder(html_dir, zip_path)

    st.success("Reports and ZIP archive are ready.")

    st.download_button("Download Main Excel Report", open(main_excel, "rb"), file_name="main_report.xlsx")
    st.download_button("Download Trados-style Report", open(trados_excel, "rb"), file_name="trados_report.xlsx")
    st.download_button("Download HTML Pages ZIP", open(zip_path, "rb"), file_name="html_pages.zip")
