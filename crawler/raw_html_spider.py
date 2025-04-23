import scrapy
from urllib.parse import urlparse
import os

class RawHtmlSpider(scrapy.Spider):
    name = "raw_html"
    custom_settings = {
        "LOG_ENABLED": True,
        "DEPTH_LIMIT": 3,
        "DOWNLOAD_DELAY": 1,
        "ROBOTSTXT_OBEY": True,
    }

    def __init__(self, start_url=None, output_dir="downloaded_pages", *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.start_urls = [start_url]
        self.allowed_domains = [urlparse(start_url).netloc]
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def parse(self, response):
        parsed_url = urlparse(response.url)
        path = parsed_url.path.strip("/").replace("/", "_") or "index"
        filename = f"{parsed_url.netloc}_{path}.html"

        full_path = os.path.join(self.output_dir, filename)
        with open(full_path, "wb") as f:
            f.write(response.body)

        yield {"url": response.url, "status": response.status, "saved_to": full_path}

        # Follow only internal links
        for href in response.css("a::attr(href)").getall():
            absolute_url = response.urljoin(href)
            if self.should_follow(absolute_url):
                yield scrapy.Request(url=absolute_url, callback=self.parse)

    def should_follow(self, url):
        parsed = urlparse(url)
        is_same_domain = parsed.netloc == self.allowed_domains[0]
        is_not_media = not parsed.path.lower().endswith((".pdf", ".jpg", ".png", ".zip", ".mp4", ".svg", ".webp"))
        return is_same_domain and is_not_media
