import requests
from bs4 import BeautifulSoup

class SEOAnalyzer:
    def check_website(self, url):
        print(f"🔍 SEO: '{url}' চেক করা হচ্ছে...")
        
        try:
            response = requests.get(url, timeout=5)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            title = soup.find('title')
            title_text = title.get_text().strip() if title else "নেই"
            
            meta = soup.find('meta', attrs={'name': 'description'})
            meta_text = meta['content'].strip() if meta and meta.get('content') else "নেই"

            return {
                "url": url,
                "title": title_text,
                "meta_description": meta_text,
                "status": "সফলভাবে চেক হয়েছে"
            }
        except Exception as e:
            return {"error": str(e)}