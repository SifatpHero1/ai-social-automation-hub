from modules.ai_generator import AIGenerator
from modules.seo_analyzer import SEOAnalyzer
from modules.social_poster import SocialPoster

def main():
    print("=========================================")
    print("   AI Social Automation Hub Started 🚀   ")
    print("=========================================\n")

    # অবজেক্ট তৈরি
    ai = AIGenerator()
    seo = SEOAnalyzer()
    social = SocialPoster()

    topic = "AI Integration in Modern Business"
    website_url = "https://google.com"

    # ধাপ ১: AI কন্টেন্ট 
    print("--- ধাপ ১: কন্টেন্ট তৈরি ---")
    generated_content = ai.create_post_content(topic)
    print(f"AI এর তৈরি কন্টেন্ট:\n{generated_content}\n")

    # ধাপ ২: SEO চেক
    print("--- ধাপ ২: SEO অ্যানালাইসিস ---")
    seo_report = seo.check_website(website_url)
    print(f"SEO রিপোর্ট: {seo_report}\n")

    # ধাপ ৩: সোশ্যাল মিডিয়া পোস্টিং
    print("--- ধাপ ৩: সোশ্যাল মিডিয়া পোস্টিং ---")
    social.post_to_facebook(generated_content)
    social.post_to_tiktok(generated_content)

    print("\n=========================================")
    print("   সব কাজ সফলভাবে সম্পন্ন হয়েছে! 🎉    ")
    print("=========================================")

if __name__ == "__main__":
    main()