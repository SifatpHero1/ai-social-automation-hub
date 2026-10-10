class SocialPoster:
    def post_to_facebook(self, message):
        print("📘 Facebook: পোস্ট পাবলিশ করা হচ্ছে...")
        # এখানে পরে আসল Facebook API কোড বসবে
        print(f"✅ সফল হয়েছে! পোস্ট: {message[:30]}...")
        return {"status": "success", "platform": "Facebook"}

    def post_to_tiktok(self, message):
        print("🎵 TikTok: কন্টেন্ট আপলোড করা হচ্ছে...")
        # এখানে পরে আসল TikTok API কোড বসবে
        print(f"✅ সফল হয়েছে! পোস্ট: {message[:30]}...")
        return {"status": "success", "platform": "TikTok"}