import os
from crawler.raw_html_spider import RawHtmlSpider
from zip_utils import zip_html_folder
from excel_report import generate_main_report
from trados_like_report import generate_trados_style_report

# Define paths
html_dir = "html_pages"
zip_path = "exports/html_pages.zip"
main_excel = "reports/main_report.xlsx"
trados_excel = "reports/trados_report.xlsx"

# Simulated example data — replace with actual results from spider
sample_data = [
    {"url": "https://example.com", "status": 200, "saved_to": "html_pages/index.html"},
    {"url": "https://example.com/about", "status": 200, "saved_to": "html_pages/about.html"}
]

# Create reports
generate_main_report(sample_data, main_excel)
generate_trados_style_report(trados_excel)
zip_html_folder(html_dir, zip_path)

# Display download buttons
st.download_button("Download Main Excel Report", open(main_excel, "rb"), file_name="main_report.xlsx")
st.download_button("Download Trados-style Report", open(trados_excel, "rb"), file_name="trados_report.xlsx")
st.download_button("Download All HTML Pages", open(zip_path, "rb"), file_name="html_pages.zip")
