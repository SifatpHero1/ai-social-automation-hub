import openai
from config import Config

class AIGenerator:
    def __init__(self):
        # যদি আসল API কি না থাকে, তাহলে এরর এড়াতে এটা স্কিপ করবে
        if Config.OPENAI_API_KEY and not Config.OPENAI_API_KEY.startswith("sk-proj-your"):
            self.client = openai.OpenAI(api_key=Config.OPENAI_API_KEY)
        else:
            self.client = None

    def create_post_content(self, topic):
        print(f"🤖 AI: '{topic}' নিয়ে কন্টেন্ট বানাচ্ছে...")
        
        # ডেমো রান করার জন্য ডামি কন্টেন্ট (আসল কি না থাকলে)
        if not self.client:
            return f"AI is revolutionizing {topic}! #AI #Tech #Future"

        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "তুমি একজন সোশ্যাল মিডিয়া এক্সপার্ট।"},
                    {"role": "user", "content": f"'{topic}' নিয়ে একটা ছোট ফেসবুক পোস্ট লিখে দাও। সাথে ৩টা হ্যাশট্যাগ দিবে।"}
                ]
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"AI Error: {e}"