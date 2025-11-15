# Messages Configuration
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
#from CONFIG.config import Config

class Messages(object):
    #######################################################
    # Messages and errors
    #######################################################
    CREDITS_MSG = (
        "<blockquote>🌟 विशेष धन्यवाद प्रायोजक "
        "<a href=\"https://t.me/shazminQ\">mmd</a> को\n"
        "🇮🇹 @downloader_Lumebot\n"
        "</blockquote>"
    )
    TO_USE_MSG = (
        "<i>इस बॉट का उपयोग करने के लिए आपको "
        "<a href=\"https://t.me/LumeTeam\">@LumeTeam</a> को सब्सक्राइब करना होगा</i>\n"
        "चैनल जॉइन करने के बाद, <b>अपना वीडियो लिंक दोबारा भेजें "
        "और बॉट इसे आपके लिए डाउनलोड करेगा</b> ❤️"
    )

    MSG1 = "नमस्ते "
    MSG2 = "यह दूसरा संदेश है. जिसका मतलब है बॉट का अपना संदेश... 😁"
    ERROR1 = "URL लिंक नहीं मिला। कृपया <b>https://</b> या <b>http://</b> के साथ कोई URL दर्ज करें"
    INDEX_ERROR = "आपने मान्य जानकारी नहीं दी। फिर से प्रयास करें..."

    PLAYLIST_HELP_MSG = """
<blockquote expandable>📋 <b>प्लेलिस्ट (yt-dlp)</b>

प्लेलिस्ट डाउनलोड करने के लिए अंत में <code>*start*end</code> रेंज के साथ इसका URL भेजें। उदाहरण: <code>URL*1*5</code>।
या आप <code>/vid FROM-TO URL</code> का उपयोग कर सकते हैं। उदाहरण: <code>/vid 3-7 URL</code>। <code>/audio</code> कमांड के लिए भी काम करता है।

<b>उदाहरण:</b>

🟥 <b>YouTube प्लेलिस्ट से वीडियो रेंज:</b> (🍪 की आवश्यकता)
<code>https://youtu.be/playlist?list=PL...*1*5</code>
(1 से 5 तक के वीडियो डाउनलोड करता है)
🟥 <b>YouTube प्लेलिस्ट से एकल वीडियो:</b> (🍪 की आवश्यकता)
<code>https://youtu.be/playlist?list=PL...*3*3</code>
(केवल तीसरा वीडियो डाउनलोड करता है)

⬛️ <b>TikTok प्रोफाइल:</b> (आपके 🍪 की आवश्यकता)
<code>https://www.tiktok.com/@USERNAME*1*10</code>
(उपयोगकर्ता प्रोफाइल से पहले 10 वीडियो डाउनलोड करता है)

🟪 <b>Instagram कहानियां:</b> (आपके 🍪 की आवश्यकता)
<code>https://www.instagram.com/stories/USERNAME*1*3</code>
(पहली 3 कहानियां डाउनलोड करता है)
<code>https://www.instagram.com/stories/highlights/123...*1*10</code>
(एल्बम से पहली 10 कहानियां डाउनलोड करता है)

🟦 <b>VK वीडियो:</b>
<code>https://vkvideo.ru/@PAGE_NAME*1*3</code>
(उपयोगकर्ता/समूह प्रोफाइल से पहले 3 वीडियो डाउनलोड करता है)

⬛️<b>Rutube चैनल:</b>
<code>https://rutube.ru/channel/CHANNEL_ID/videos*2*4</code>
(चैनल से 2 से 4 तक के वीडियो डाउनलोड करता है)

🟪 <b>Twitch क्लिप्स:</b>
<code>https://www.twitch.tv/USERNAME/clips*1*3</code>
(चैनल से पहले 3 क्लिप्स डाउनलोड करता है)

🟦 <b>Vimeo समूह:</b>
<code>https://vimeo.com/groups/GROUP_NAME/videos*1*2</code>
(समूह से पहले 2 वीडियो डाउनलोड करता है)

🟧 <b>Pornhub मॉडल:</b>
<code>https://www.pornhub.org/model/MODEL_NAME*1*2</code>
(मॉडल प्रोफाइल से पहले 2 वीडियो डाउनलोड करता है)
<code>https://www.pornhub.com/video/search?search=YOUR+PROMPT*1*3</code>
(आपके प्रॉम्प्ट द्वारा खोज परिणामों से पहले 3 वीडियो डाउनलोड करता है)

और इसी तरह...
<a href=\"https://t.me/LumeTeam\">समर्थित साइटों की सूची</a> देखें
</blockquote>

<blockquote expandable>🖼 <b>छवियां (gallery-dl)</b>

कई प्लेटफॉर्म से छवियां/फोटो/एल्बम डाउनलोड करने के लिए <code>/img URL</code> का उपयोग करें।

<b>उदाहरण:</b>
<code>/img https://vk.com/wall-160916577_408508</code>
<code>/img https://2ch.hk/fd/res/1747651.html</code>
<code>/img https://x.com/username/status/1234567890123456789</code>
<code>/img https://imgur.com/a/abc123</code>

<b>रेंज:</b>
<code>/img 11-20 https://example.com/album</code> — आइटम 11..20
<code>/img 11- https://example.com/album</code> — 11 से अंत तक (या बॉट सीमा)

<i>समर्थित प्लेटफॉर्म में vk, 2ch, 35photo, 4chan, 500px, ArtStation, Boosty, Civitai, Cyberdrop, DeviantArt, Discord, Facebook, Fansly, Instagram, Pinterest, Reddit, TikTok, Tumblr, Twitter/X, JoyReactor, आदि शामिल हैं। पूरी सूची:</i>
<a href=\"https://raw.githubusercontent.com/mikf/gallery-dl/refs/heads/master/docs/supportedsites.md\">gallery-dl समर्थित साइटें</a>
</blockquote>
"""
    HELP_MSG = """
<blockquote>🎬 <b>वीडियो डाउनलोड बॉट - सहायता</b>

📥 <b>मूल उपयोग:</b>
• कोई भी लिंक भेजें → बॉट इसे डाउनलोड करता है
  <i>बॉट स्वचालित रूप से yt-dlp के माध्यम से वीडियो और gallery-dl के माध्यम से छवियां डाउनलोड करने की कोशिश करता है।</i>
• <code>/audio URL</code> → ऑडियो निकालें
• <code>/link [quality] URL</code> → प्रत्यक्ष लिंक प्राप्त करें
• <code>/proxy</code> → सभी डाउनलोड के लिए प्रॉक्सी सक्षम/अक्षम करें
• वीडियो पर टेक्स्ट के साथ जवाब दें → कैप्शन बदलें

📋 <b>प्लेलिस्ट और रेंज:</b>
• <code>URL*1*5</code> → वीडियो 1-5 डाउनलोड करें
• <code>/vid 3-7 URL</code> → <code>URL*3*7</code> बन जाता है

🍪 <b>कुकीज़ और निजी:</b>
• निजी वीडियो के लिए *.txt कुकी अपलोड करें
• <code>/cookie [service]</code> → कुकीज़ डाउनलोड करें (youtube/tiktok/x/custom)
• <code>/cookie youtube 1</code> → इंडेक्स द्वारा स्रोत चुनें (1–N)
• <code>/cookies_from_browser</code> → ब्राउज़र से निकालें
• <code>/check_cookie</code> → कुकी सत्यापित करें
• <code>/save_as_cookie</code> → टेक्स्ट को कुकी के रूप में सहेजें

🧹 <b>सफाई:</b>
• <code>/clean</code> → केवल मीडिया फाइलें
• <code>/clean all</code> → सब कुछ
• <code>/clean cookies/logs/tags/format/split/mediainfo/sub/keyboard</code>

⚙️ <b>सेटिंग्स:</b>
• <code>/settings</code> → सेटिंग्स मेनू
• <code>/format</code> → गुणवत्ता और प्रारूप
• <code>/split</code> → वीडियो को भागों में विभाजित करें
• <code>/mediainfo on/off</code> → मीडिया जानकारी
• <code>/nsfw on/off</code> → NSFW धुंधलापन
• <code>/tags</code> → सहेजे गए टैग देखें
• <code>/sub on/off</code> → उपशीर्षक
• <code>/keyboard</code> → कीबोर्ड (OFF/1x3/2x3)

🏷️ <b>टैग:</b>
• URL के बाद <code>#tag1#tag2</code> जोड़ें
• टैग कैप्शन में दिखाई देते हैं
• <code>/tags</code> → सभी टैग देखें

🔗 <b>प्रत्यक्ष लिंक:</b>
• <code>/link URL</code> → सर्वोत्तम गुणवत्ता
• <code>/link [144-4320]/720p/1080p/4k/8k URL</code> → विशिष्ट गुणवत्ता

⚙️ <b>त्वरित कमांड:</b>
• <code>/format [144-4320]/720p/1080p/4k/8k/best/ask/id 134</code> → गुणवत्ता सेट करें
• <code>/keyboard off/1x3/2x3/full</code> → कीबोर्ड लेआउट
• <code>/split 100mb-2000mb</code> → भाग आकार बदलें
• <code>/subs off/ru/en auto</code> → उपशीर्षक भाषा
• <code>/list URL</code> → उपलब्ध प्रारूपों की सूची
• <code>/mediainfo on/off</code> → मीडिया जानकारी चालू/बंद
• <code>/proxy on/off</code> → सभी डाउनलोड के लिए प्रॉक्सी सक्षम/अक्षम करें

📊 <b>जानकारी:</b>
• <code>/usage</code> → डाउनलोड इतिहास
• <code>/search</code> → @vid के माध्यम से इनलाइन खोज

🖼 <b>छवियां:</b>
• <code>URL</code> → छवि URL डाउनलोड करें
• <code>/img URL</code> → URL से छवियां डाउनलोड करें
• <code>/img 11-20 URL</code> → विशिष्ट रेंज डाउनलोड करें
• <code>/img 11- URL</code> → 11वें से अंत तक डाउनलोड करें

👨💻 <i>चैनल:</i> <a href="https://t.me/LumeTeam">@LumeTeam</a>
</blockquote>
    """
    
    # Version 1.0.0 - Добавлен SAVE_AS_COOKIE_HINT для подсказки по /save_as_cookie
    SAVE_AS_COOKIE_HINT = (
        "बस अपनी कुकी को <b><u>cookie.txt</u></b> के रूप में सहेजें और इसे बॉट को दस्तावेज़ के रूप में भेजें।\n\n"
        "आप <b><u>/save_as_cookie</u></b> कमांड के साथ कुकीज़ को सादे टेक्स्ट के रूप में भी भेज सकते हैं।\n"
        "<b><b><u>/save_as_cookie</u></b> का उपयोग:</b>\n\n"
        "<pre>"
        "/save_as_cookie\n"
        "# Netscape HTTP Cookie File\n"
        "# http://curl.haxx.se/rfc/cookie_spec.html\n"
        "# This file was generated by Cookie-Editor\n"
        ".youtube.com  TRUE  /  FALSE  111  ST-xxxxx  session_logininfo=AAA\n"
        ".youtube.com  TRUE  /  FALSE  222  ST-xxxxx  session_logininfo=BBB\n"
        ".youtube.com  TRUE  /  FALSE  33333  ST-xxxxx  session_logininfo=CCC\n"
        "</pre>\n"
        "<blockquote>"
        "<b><u>निर्देश:</u></b>\n"
        "https://t.me/tg_ytdlp/203 \n"
        "https://t.me/tg_ytdlp/214 "
        "</blockquote>"
    )
    
    # Search command message (English)
    SEARCH_MSG = """
🔍 <b>वीडियो खोज</b>

@vid के माध्यम से इनलाइन खोज सक्रिय करने के लिए नीचे दिए गए बटन को दबाएं।

<blockquote>PC पर बस किसी भी चैट में <b>"@vid Your_Search_Query"</b> टाइप करें।</blockquote>
    """
    
    # Settings and Hints (English)
    
    
    IMG_HELP_MSG = (
        "<b>🖼 छवि डाउनलोड कमांड</b>\n\n"
        "उपयोग: <code>/img URL</code>\n\n"
        "<b>उदाहरण:</b>\n"
        "• <code>/img https://example.com/image.jpg</code>\n"
        "• <code>/img 11-20 https://example.com/album</code>\n"
        "• <code>/img 11- https://example.com/album</code>\n"
        "• <code>/img https://vk.com/wall-160916577_408508</code>\n"
        "• <code>/img https://2ch.hk/fd/res/1747651.html</code>\n"
        "• <code>/img https://imgur.com/abc123</code>\n\n"
        "<b>समर्थित प्लेटफॉर्म (उदाहरण):</b>\n"
        "<blockquote>vk, 2ch, 35photo, 4chan, 500px, ArtStation, Boosty, Civitai, Cyberdrop, DeviantArt, Discord, Facebook, Fansly, Instagram, Patreon, Pinterest, Reddit, TikTok, Tumblr, Twitter/X, JoyReactor, आदि — <a href=\"https://github.com/mikf/gallery-dl/blob/master/docs/supportedsites.md\">पूरी सूची</a></blockquote>"
        "यह भी देखें: "
    )
    
    LINK_HINT_MSG = (
        "गुणवत्ता चयन के साथ प्रत्यक्ष वीडियो लिंक प्राप्त करें।\n\n"
        "उपयोग: /link + URL \n\n"
        "(उदा. /link https://youtu.be/abc123)\n"
        "(उदा. /link 720 https://youtu.be/abc123)"
    )
    
    # Add bot to group command message
    ADD_BOT_TO_GROUP_MSG = """
🤖 <b>बॉट को समूह में जोड़ें</b>

उन्नत सुविधाएं और उच्च सीमाएं प्राप्त करने के लिए मेरे बॉट्स को अपने समूहों में जोड़ें!
————————————
📊 <b>वर्तमान मुफ़्त सीमाएँ (बॉट के डीएम में):</b>
<blockquote>•🗑 सभी फाइलों से अव्यवस्थित कबाड़ 👎
• अधिकतम 1 फ़ाइल आकार: <b>8 GB </b>
• अधिकतम 1 फ़ाइल गुणवत्ता: <b>UNLIM</b>
• अधिकतम 1 फ़ाइल अवधि: <b>UNLIM</b>
• अधिकतम डाउनलोड संख्या: <b>UNLIM</b>
• अधिकतम प्लेलिस्ट आइटम प्रति एक बार: <b>50</b>
• अधिकतम TikTok वीडियो प्रति एक बार: <b>500</b>
• अधिकतम छवियाँ प्रति एक बार: <b>1000</b>
• 1 डाउनलोड अधिकतम समय: <b>2 घंटे</b>
• 🔞 NSFW सामग्री का भुगतान किया जाता है! 1⭐️ = $0.02
• 🆓 सभी अन्य मीडिया पूरी तरह से मुफ़्त हैं
• 📝 सभी सामग्री लॉग और कैशिंग मेरे लॉग चैनल में तुरंत रीपोस्ट करने के लिए</blockquote>

💬<b>ये सीमाएं केवल सबस्क्रिप्ट वाले वीडियो के लिए हैं:</b>
<blockquote>• अधिकतम वीडियो+सबस्क्रिप्ट अवधि: <b>1.5 घंटे</b>
• अधिकतम वीडियो+सबस्क्रिप्ट फ़ाइल आकार: <b>500 MB</b>
• अधिकतम वीडियो+सबस्क्रिप्ट गुणवत्ता: <b>720p</b></blockquote>
————————————
🚀 <b>पेड समूह लाभ (2️⃣x सीमाएं):</b>
<blockquote>•  🗂 संरचित निष्क्रिय मीडिया वाल्ट टोपियों के अनुसार व्यवस्थित है 👍
•  📁 बॉट्स आपके बॉट्स को कॉल करने वाले टोपी में जवाब देते हैं
•  📌 डाउनलोड प्रगति के साथ स्थिति संदेश अपने लॉग चैनल में स्वचालित रूप से डाल दिया जाता है
•  🖼 /img कमांड मीडिया को 10-आइटम अल्बम के रूप में डाउनलोड करता है
• अधिकतम 1 फ़ाइल आकार: <b>16 GB</b> ⬆️
• अधिकतम प्लेलिस्ट आइटम प्रति एक बार: <b>100</b> ⬆️
• अधिकतम TikTok वीडियो प्रति एक बार: 1000 ⬆️
• अधिकतम छवियाँ प्रति एक बार: 2000 ⬆️
• 1 डाउनलोड अधिकतम समय: <b>4 घंटे</b> ⬆️
• 🔞 NSFW सामग्री: पूर्ण मेटाडेटा के साथ मुफ़्त 🆓
• 📢 समूह के लिए मेरे चैनल को सदस्यता देने की आवश्यकता नहीं है
• 👥 सभी समूह सदस्य पेड कार्यों तक पहुँच होंगे!
• 🗒 कोई लॉग / कोई कैश मेरे लॉग चैनल में नहीं है! आप समूह सेटिंग्स में कॉपी/रीपोस्ट को अस्वीकार कर सकते हैं</blockquote>

💬 <b>उपशीर्षक वाले वीडियो के लिए 2️⃣x सीमाएँ:</b>
<blockquote>• अधिकतम वीडियो+सबस्क्रिप्ट अवधि: <b>3 घंटे</b> ⬆️
• अधिकतम वीडियो+सबस्क्रिप्ट फ़ाइल आकार: <b>1000 MB</b> ⬆️
• अधिकतम वीडियो+सबस्क्रिप्ट गुणवत्ता: <b>1080p</b> ⬆️</blockquote>
————————————
💰 <b>मूल्य निर्धारण और सेटअप:</b>
<blockquote>• मूल्य: समूह में प्रति 1 बॉट <b>$5/माह</b>
• सेटअप: Contact @edite909
• भुगतान: 💎TON या अन्य तरीके💲
• समर्थन: पूर्ण तकनीकी समर्थन समाहित है</blockquote>
————————————
आप मेरे बॉट्स को अपने समूह में जोड़ सकते हैं और मुफ़्त 🔞<b>NSFW</b> को अनलॉक कर सकते हैं और सभी सीमाओं को दोगुना (x2️⃣) कर सकते हैं.
मुझे संपर्क करें अगर आप मेरे बॉट्स का उपयोग करने की अनुमति देना चाहते हैं @edite909
————————————
💡<b>TIP:</b> <blockquote>आप अपने दोस्तों के साथ किसी भी राशि के साथ पैसे चिपका सकते हैं (उदाहरण के लिए 100 लोग) और समूह के लिए 1 खरीद कर सकते हैं - सभी समूह सदस्य उस समूह में सभी बॉट्स कार्यों तक पूर्ण अनिश्चित पहुँच प्राप्त करेंगे केवल <b>0.05$</b></blockquote>
    """
    
    # NSFW Command Messages
    NSFW_ON_MSG = """
🔞 <b>NSFW मोड: चालू✅</b>

• NSFW सामग्री बिना धुंधले प्रदर्शित की जाएगी।
• स्पॉयलर NSFW मीडिया पर लागू नहीं होंगे।
• सामग्री तुरंत दिखाई देगी

<i>धुंधलापन सक्षम करने के लिए /nsfw off का उपयोग करें</i>
    """
    
    NSFW_OFF_MSG = """
🔞 <b>NSFW मोड: बंद</b>

⚠️ <b>धुंधलापन सक्षम</b>
• NSFW सामग्री स्पॉइलर के नीचे छिपा दी जाएगी
• देखने के लिए, आपको मीडिया पर क्लिक करना होगा
• स्पॉइलर NSFW मीडिया पर लागू होंगे।

<i>धुंधलापन बंद करने के लिए /nsfw on का उपयोग करें</i>
    """
    
    NSFW_INVALID_MSG = """
❌ <b>अमान्य पैरामीटर</b>

उपयोग:
• <code>/nsfw on</code> - धुंधलापन बंद करें
• <code>/nsfw off</code> - धुंधलापन सक्षम करें
    """
    
    # UI Messages - Status and Progress
    CHECKING_CACHE_MSG = "🔄 <b>कैश जांच रहा है...</b>\n\n<code>{url}</code>"
    PROCESSING_MSG = "🔄 प्रसंस्करण..."
    DOWNLOADING_MSG = "📥 <b>मीडिया डाउनलोड हो रहा है...</b>\n\n"

    DOWNLOADING_IMAGE_MSG = "📥 <b>छवि डाउनलोड हो रही है...</b>\n\n"

    DOWNLOAD_COMPLETE_MSG = "✅ <b>डाउनलोड पूरा</b>\n\n"
    
    # Download status messages
    DOWNLOADED_STATUS_MSG = "डाउनलोड किया गया:"
    SENT_STATUS_MSG = "भेजा गया:"
    PENDING_TO_SEND_STATUS_MSG = "भेजने की प्रतीक्षा में:"
    TITLE_LABEL_MSG = "शीर्षक:"
    MEDIA_COUNT_LABEL_MSG = "मीडिया की संख्या:"
    AUDIO_DOWNLOAD_FINISHED_PROCESSING_MSG = "डाउनलोड पूरा हुआ, ऑडियो प्रोसेसिंग..."
    VIDEO_PROCESSING_MSG = "📽 वीडियो प्रसंस्करण में है..."
    WAITING_HOURGLASS_MSG = "⌛️"
    
    # Cache Messages
    SENT_FROM_CACHE_MSG = "✅ <b>कैश से भेजा गया</b>\n\nभेजे गए एल्बम: <b>{count}</b>"
    VIDEO_SENT_FROM_CACHE_MSG = "✅ वीडियो कैश से सफलतापूर्वक भेजा गया।"
    PLAYLIST_SENT_FROM_CACHE_MSG = "✅ प्लेलिस्ट वीडियो कैश से भेजे गए ({cached}/{total} फाइलें)।"
    CACHE_PARTIAL_MSG = "📥 {cached}/{total} वीडियो कैश से भेजे गए, लापता वाले डाउनलोड हो रहे हैं..."
    CACHE_CONTINUING_DOWNLOAD_MSG = "✅ कैश से भेजा गया: {cached}\n🔄 डाउनलोड जारी है..."
    FALLBACK_ANALYZE_MEDIA_MSG = "🔄 मीडिया का विश्लेषण नहीं कर सका, अधिकतम अनुमतित रेंज (1-{fallback_limit}) के साथ आगे बढ़ रहे हैं..."
    FALLBACK_DETERMINE_COUNT_MSG = "🔄 मीडिया की संख्या निर्धारित नहीं कर सका, अधिकतम अनुमतित रेंज (1-{total_limit}) के साथ आगे बढ़ रहे हैं..."
    FALLBACK_SPECIFIED_RANGE_MSG = "🔄 कुल मीडिया संख्या निर्धारित नहीं कर सका, निर्दिष्ट रेंज {start}-{end} के साथ आगे बढ़ रहे हैं..."

    # Error Messages
    INVALID_URL_MSG = "❌ <b>अमान्य URL</b>\n\nकृपया http:// या https:// से शुरू होने वाला एक वैध URL प्रदान करें"

    ERROR_OCCURRED_MSG = "❌ <b>त्रुटि हुई</b>\n\n<code>{url}</code>\n\nत्रुटि: {error}"

    ERROR_SENDING_VIDEO_MSG = "❌ वीडियो भेजने में त्रुटि: {error}"
    ERROR_UNKNOWN_MSG = "❌ अज्ञात त्रुटि: {error}"
    ERROR_NO_DISK_SPACE_MSG = "❌ वीडियो डाउनलोड करने के लिए पर्याप्त डिस्क स्थान नहीं है।"
    ERROR_FILE_SIZE_LIMIT_MSG = "❌ फाइल का आकार {limit} GB सीमा से अधिक है। कृपया अनुमतित आकार के भीतर एक छोटी फाइल चुनें।"

    ERROR_GETTING_LINK_MSG = "❌ <b>लिंक प्राप्त करने में त्रुटि:</b>\n{error}"

    # Telegram Rate Limit Messages
    RATE_LIMIT_WITH_TIME_MSG = "⚠️ Telegram ने संदेश भेजने को सीमित कर दिया है।\n⏳ कृपया प्रतीक्षा करें: {time}\nटाइमर अपडेट करने के लिए URL को फिर से 2 बार भेजें।"
    RATE_LIMIT_NO_TIME_MSG = "⚠️ Telegram ने संदेश भेजने को सीमित कर दिया है।\n⏳ कृपया प्रतीक्षा करें: \nटाइमर अपडेट करने के लिए URL को फिर से 2 बार भेजें।"
    
    # Subtitles Messages
    SUBTITLES_FAILED_MSG = "⚠️ उपशीर्षक डाउनलोड करने में विफल"

    # Video Processing Messages

    # Stream/Link Messages
    STREAM_LINKS_TITLE_MSG = "🔗 <b>प्रत्यक्ष स्ट्रीम लिंक</b>\n\n"
    STREAM_TITLE_MSG = "📹 <b>शीर्षक:</b> {title}\n"
    STREAM_DURATION_MSG = "⏱ <b>अवधि:</b> {duration} सेकंड\n"

    
    # Download Progress Messages

    # Quality Selection Messages

    # NSFW Paid Content Messages

    # Callback Error Messages
    ERROR_ORIGINAL_NOT_FOUND_MSG = "❌ त्रुटि: मूल संदेश नहीं मिला।"

    # Tags Error Messages
    TAG_FORBIDDEN_CHARS_MSG = "❌ टैग #{tag} में निषिद्ध वर्ण हैं। केवल अक्षर, अंक और _ की अनुमति है।\nकृपया उपयोग करें: {example}"
    
    # Playlist Messages
    PLAYLIST_SENT_MSG = "✅ प्लेलिस्ट वीडियो भेजे गए: {sent}/{total} फाइलें।"
    PLAYLIST_CACHE_SENT_MSG = "✅ कैश से भेजा गया: {cached}/{total} फाइलें।"
    
    # Failed Stream Messages
    FAILED_STREAM_LINKS_MSG = "❌ स्ट्रीम लिंक प्राप्त करने में विफल"

    # new messages
    # Browser Cookie Messages
    SELECT_BROWSER_MSG = "कुकीज़ डाउनलोड करने के लिए एक ब्राउज़र चुनें:"
    SELECT_BROWSER_NO_BROWSERS_MSG = "इस सिस्टम पर कोई ब्राउज़र नहीं मिला। आप रिमोट URL से कुकीज़ डाउनलोड कर सकते हैं या ब्राउज़र स्थिति की निगरानी कर सकते हैं:"
    BROWSER_MONITOR_HINT_MSG = "🌐 <b>ब्राउज़र खोलें</b> - मिनी-ऐप में ब्राउज़र स्थिति की निगरानी के लिए"
    BROWSER_OPEN_BUTTON_MSG = "🌐 ब्राउज़र खोलें"
    DOWNLOAD_FROM_URL_BUTTON_MSG = "📥 रिमोट URL से डाउनलोड करें"
    COOKIE_YT_FALLBACK_SAVED_MSG = "✅ YouTube कुकी फाइल फॉलबैक के माध्यम से डाउनलोड की गई और cookie.txt के रूप में सहेजी गई"
    COOKIES_NO_BROWSERS_NO_URL_MSG = "❌ कोई समर्थित ब्राउज़र नहीं मिला और कोई COOKIE_URL कॉन्फ़िगर नहीं है। /cookie का उपयोग करें या cookie.txt अपलोड करें।"
    COOKIE_FALLBACK_URL_NOT_TXT_MSG = "❌ फॉलबैक COOKIE_URL एक .txt फाइल की ओर इंगित करना चाहिए।"
    COOKIE_FALLBACK_TOO_LARGE_MSG = "❌ फॉलबैक कुकी फाइल बहुत बड़ी है (>100KB)।"
    COOKIE_FALLBACK_UNAVAILABLE_MSG = "❌ फॉलबैक कुकी स्रोत उपलब्ध नहीं है (स्थिति {status})। /cookie का उपयोग करें या cookie.txt अपलोड करें।"
    COOKIE_FALLBACK_ERROR_MSG = "❌ फॉलबैक कुकी डाउनलोड करने में त्रुटि। /cookie का उपयोग करें या cookie.txt अपलोड करें।"
    COOKIE_FALLBACK_UNEXPECTED_MSG = "❌ फॉलबैक कुकी डाउनलोड के दौरान अप्रत्याशित त्रुटि।"
    BTN_CLOSE = "🔚बंद करें"
    
    # Args command messages
    ARGS_INVALID_BOOL_MSG = "❌ अमान्य बूलियन मान"
    ARGS_CLOSED_MSG = "बंद"
    ARGS_ALL_RESET_MSG = "✅ सभी तर्क रीसेट"
    ARGS_RESET_ERROR_MSG = "❌ तर्क रीसेट करने में त्रुटि"
    ARGS_INVALID_PARAM_MSG = "❌ अमान्य पैरामीटर"
    ARGS_BOOL_SET_MSG = "{value} पर सेट किया गया"
    ARGS_BOOL_ALREADY_SET_MSG = "पहले से {value} पर सेट है"
    ARGS_INVALID_SELECT_MSG = "❌ अमान्य चयन मान"
    ARGS_VALUE_SET_MSG = "{value} पर सेट किया गया"
    ARGS_VALUE_ALREADY_SET_MSG = "पहले से {value} पर सेट है"
    ARGS_PARAM_DESCRIPTION_MSG = "<b>📝 {description}</b>\n\n"
    ARGS_CURRENT_VALUE_MSG = "<b>वर्तमान मान:</b> <code>{current_value}</code>\n\n"
    ARGS_XFF_EXAMPLES_MSG = "<b>उदाहरण:</b>\n• <code>default</code> - डिफ़ॉल्ट XFF रणनीति का उपयोग करें\n• <code>never</code> - XFF हेडर का कभी उपयोग न करें\n• <code>US</code> - संयुक्त राज्य अमेरिका देश कोड\n• <code>GB</code> - यूनाइटेड किंगडम देश कोड\n• <code>DE</code> - जर्मनी देश कोड\n• <code>FR</code> - फ्रांस देश कोड\n• <code>JP</code> - जापान देश कोड\n• <code>192.168.1.0/24</code> - IP ब्लॉक (CIDR)\n• <code>10.0.0.0/8</code> - निजी IP रेंज\n• <code>203.0.113.0/24</code> - सार्वजनिक IP ब्लॉक\n\n"
    ARGS_XFF_NOTE_MSG = "<b>नोट:</b> यह --geo-bypass विकल्पों को प्रतिस्थापित करता है। CIDR नोटेशन में कोई भी 2-अक्षर देश कोड या IP ब्लॉक का उपयोग करें।\n\n"
    ARGS_EXAMPLE_MSG = "<b>उदाहरण:</b> <code>{placeholder}</code>\n\n"
    ARGS_SEND_VALUE_MSG = "कृपया अपना नया मान भेजें।"
    ARGS_NUMBER_PARAM_MSG = "<b>🔢 {description}</b>\n\n"
    ARGS_RANGE_MSG = "<b>रेंज:</b> {min_val} - {max_val}\n\n"
    ARGS_SEND_NUMBER_MSG = "कृपया एक संख्या भेजें।"
    ARGS_JSON_PARAM_MSG = "<b>🔧 {description}</b>\n\n"
    ARGS_HTTP_HEADERS_EXAMPLES_MSG = "<b>उदाहरण:</b>\n<code>{placeholder}</code>\n<code>{{\"X-API-Key\": \"your-key\"}}</code>\n<code>{{\"Authorization\": \"Bearer token\"}}</code>\n<code>{{\"Accept\": \"application/json\"}}</code>\n<code>{{\"X-Custom-Header\": \"value\"}}</code>\n\n"
    ARGS_HTTP_HEADERS_NOTE_MSG = "<b>नोट:</b> ये हेडर मौजूदा Referer और उपयोगकर्ता-एजेंट हेडर में जोड़े जाएंगे।\n\n"
    ARGS_CURRENT_ARGS_MSG = "<b>📋 वर्तमान yt-dlp तर्क:</b>\n\n"
    ARGS_MENU_DESCRIPTION_MSG = "• ✅/❌ <b>बूलियन</b> - सही/गलत स्विच\n• 📋 <b>चयन</b> - विकल्पों में से चुनें\n• 🔢 <b>संख्यात्मक</b> - संख्या इनपुट\n• 📝🔧 <b>पाठ</b> - पाठ/JSON इनपुट</blockquote>\n\nये सेटिंग्स आपके सभी डाउनलोड पर लागू होंगी।"
    
    # प्रदर्शन के लिए स्थानीयकृत पैरामीटर नाम
    ARGS_PARAM_NAMES = {
        "force_ipv6": "IPv6 कनेक्शन को मजबूर करें",
        "force_ipv4": "IPv4 कनेक्शन को मजबूर करें", 
        "no_live_from_start": "लाइव स्ट्रीम को शुरुआत से डाउनलोड न करें",
        "live_from_start": "लाइव स्ट्रीम को शुरुआत से डाउनलोड करें",
        "no_check_certificates": "HTTPS सर्टिफिकेट सत्यापन को दबाएं",
        "check_certificate": "SSL सर्टिफिकेट जांचें",
        "no_playlist": "केवल एक वीडियो डाउनलोड करें, प्लेलिस्ट नहीं",
        "embed_metadata": "वीडियो फाइल में मेटाडेटा एम्बेड करें",
        "embed_thumbnail": "वीडियो फाइल में थंबनेल एम्बेड करें",
        "write_thumbnail": "थंबनेल को फाइल में लिखें",
        "ignore_errors": "डाउनलोड त्रुटियों को नजरअंदाज करें और जारी रखें",
        "legacy_server_connect": "पुराने सर्वर कनेक्शन की अनुमति दें",
        "concurrent_fragments": "डाउनलोड के लिए समवर्ती फ्रैगमेंट की संख्या",
        "xff": "X-Forwarded-For हेडर रणनीति",
        "user_agent": "User-Agent हेडर",
        "impersonate": "ब्राउज़र नकली",
        "referer": "Referer हेडर",
        "geo_bypass": "भौगोलिक प्रतिबंधों को बायपास करें",
        "hls_use_mpegts": "HLS के लिए MPEG-TS का उपयोग करें",
        "no_part": ".part फाइलों का उपयोग न करें",
        "no_continue": "आंशिक डाउनलोड को फिर से शुरू न करें",
        "audio_format": "ऑडियो प्रारूप",
        "video_format": "वीडियो प्रारूप",
        "merge_output_format": "मर्ज आउटपुट प्रारूप",
        "send_as_file": "फाइल के रूप में भेजें",
        "username": "उपयोगकर्ता नाम",
        "password": "पासवर्ड",
        "twofactor": "दो-कारक प्रमाणीकरण कोड",
        "min_filesize": "न्यूनतम फाइल आकार (MB)",
        "max_filesize": "अधिकतम फाइल आकार (MB)",
        "playlist_items": "प्लेलिस्ट आइटम",
        "date": "तारीख",
        "datebefore": "तारीख से पहले",
        "dateafter": "तारीख के बाद",
        "http_headers": "HTTP हेडर",
        "sleep_interval": "स्लीप अंतराल",
        "max_sleep_interval": "अधिकतम स्लीप अंतराल",
        "retries": "पुनर्प्रयास की संख्या",
        "http_chunk_size": "HTTP चंक आकार",
        "sleep_subtitles": "सबटाइटल के लिए स्लीप"
    }
    ARGS_CONFIG_TITLE_MSG = "<b>⚙️ yt-dlp तर्क कॉन्फ़िगरेशन</b>\n\n<blockquote>📋 <b>समूह:</b>\n{groups_msg}"
    ARGS_MENU_TEXT = (
        "<b>⚙️ yt-dlp तर्क कॉन्फ़िगरेशन</b>\n\n"
        "<blockquote>📋 <b>समूह:</b>\n"
        "• ✅/❌ <b>बूलियन</b> - सही/गलत स्विच\n"
        "• 📋 <b>चयन</b> - विकल्पों में से चुनें\n"
        "• 🔢 <b>संख्यात्मक</b> - संख्या इनपुट\n"
        "• 📝🔧 <b>पाठ</b> - पाठ/JSON इनपुट</blockquote>\n\n"
        "ये सेटिंग्स आपके सभी डाउनलोड पर लागू होंगी।"
    )
    
    # Additional missing messages
    PLEASE_WAIT_MSG = "⏳ कृपया प्रतीक्षा करें..."
    ERROR_OCCURRED_SHORT_MSG = "❌ त्रुटि हुई"

    # Args command messages (continued)
    ARGS_INPUT_TIMEOUT_MSG = "⏰ निष्क्रियता के कारण इनपुट मोड स्वचालित रूप से बंद हो गया (5 मिनट)।"
    ARGS_INPUT_DANGEROUS_MSG = "❌ इनपुट में संभावित खतरनाक सामग्री है: {pattern}"
    ARGS_INPUT_TOO_LONG_MSG = "❌ इनपुट बहुत लंबा है (अधिकतम 1000 वर्ण)"
    ARGS_INVALID_URL_MSG = "❌ अमान्य URL प्रारूप। http:// या https:// से शुरू होना चाहिए"
    ARGS_INVALID_JSON_MSG = "❌ अमान्य JSON प्रारूप"
    ARGS_NUMBER_RANGE_MSG = "❌ संख्या {min_val} और {max_val} के बीच होनी चाहिए"
    ARGS_INVALID_NUMBER_MSG = "❌ अमान्य संख्या प्रारूप"
    ARGS_DATE_FORMAT_MSG = "❌ दिनांक YYYYMMDD प्रारूप में होना चाहिए (उदाहरण: 20230930)"
    ARGS_YEAR_RANGE_MSG = "❌ वर्ष 1900 और 2100 के बीच होना चाहिए"
    ARGS_MONTH_RANGE_MSG = "❌ महीना 01 और 12 के बीच होना चाहिए"
    ARGS_DAY_RANGE_MSG = "❌ दिन 01 और 31 के बीच होना चाहिए"
    ARGS_INVALID_DATE_MSG = "❌ अमान्य दिनांक प्रारूप"
    ARGS_INVALID_XFF_MSG = "❌ XFF 'default', 'never', देश कोड (उदाहरण: US), या IP ब्लॉक (उदाहरण: 192.168.1.0/24) होना चाहिए"
    ARGS_NO_CUSTOM_MSG = "कोई कस्टम तर्क सेट नहीं है। सभी पैरामीटर डिफ़ॉल्ट मानों का उपयोग करते हैं।"
    ARGS_RESET_SUCCESS_MSG = "✅ सभी तर्क डिफ़ॉल्ट पर रीसेट हो गए।"
    ARGS_TEXT_TOO_LONG_MSG = "❌ पाठ बहुत लंबा है। अधिकतम 500 वर्ण।"
    ARGS_ERROR_PROCESSING_MSG = "❌ इनपुट प्रसंस्करण में त्रुटि। कृपया फिर से कोशिश करें।"
    ARGS_BOOL_INPUT_MSG = "❌ Send As File विकल्प के लिए कृपया 'True' या 'False' दर्ज करें।"
    ARGS_INVALID_NUMBER_INPUT_MSG = "❌ कृपया एक वैध संख्या प्रदान करें।"
    ARGS_BOOL_VALUE_REQUEST_MSG = "इस विकल्प को सक्षम/अक्षम करने के लिए कृपया <code>True</code> या <code>False</code> भेजें।"
    ARGS_JSON_VALUE_REQUEST_MSG = "कृपया वैध JSON भेजें।"
    
    # Tags command messages
    TAGS_NO_TAGS_MSG = "आपके पास अभी तक कोई टैग नहीं है।"
    TAGS_MESSAGE_CLOSED_MSG = "टैग संदेश बंद।"
    
    # Subtitles command messages
    SUBS_DISABLED_MSG = "✅ उपशीर्षक अक्षम और हमेशा पूछें मोड बंद।"
    SUBS_ALWAYS_ASK_ENABLED_MSG = "✅ सब्स हमेशा पूछें सक्षम।"
    SUBS_LANGUAGE_SET_MSG = "✅ उपशीर्षक भाषा सेट की गई: {flag} {name}"
    SUBS_WARNING_MSG = (
        "<blockquote>❗️चेतावनी: उच्च CPU प्रभाव के कारण यह फ़ंक्शन बहुत धीमा है (लगभग वास्तविक समय) और सीमित है:\n"
        "- 720p अधिकतम गुणवत्ता\n"
        "- 1.5 घंटे अधिकतम अवधि\n"
        "- 500mb अधिकतम वीडियो आकार</blockquote>\n\n"
    )
    SUBS_QUICK_COMMANDS_MSG = (
        "<b>त्वरित कमांड:</b>\n"
        "• <code>/subs off</code> - उपशीर्षक अक्षम करें\n"
        "• <code>/subs on</code> - हमेशा पूछें मोड सक्षम करें\n"
        "• <code>/subs ru</code> - भाषा सेट करें\n"
        "• <code>/subs ru auto</code> - AUTO/TRANS के साथ भाषा सेट करें"
    )
    SUBS_DISABLED_STATUS_MSG = "🚫 उपशीर्षक अक्षम हैं"
    SUBS_SELECTED_LANGUAGE_MSG = "{flag} चयनित भाषा: {name}{auto_text}"
    SUBS_DOWNLOADING_MSG = "💬 उपशीर्षक डाउनलोड हो रहे हैं..."
    SUBS_DISABLED_ERROR_MSG = "❌ उपशीर्षक अक्षम हैं। कॉन्फ़िगर करने के लिए /subs का उपयोग करें।"
    SUBS_YOUTUBE_ONLY_MSG = "❌ उपशीर्षक डाउनलोड केवल YouTube के लिए समर्थित है।"
    SUBS_CAPTION_MSG = (
        "<b>💬 उपशीर्षक</b>\n\n"
        "<b>वीडियो:</b> {title}\n"
        "<b>भाषा:</b> {lang}\n"
        "<b>प्रकार:</b> {type}\n\n"
        "{tags}"
    )
    SUBS_SENT_MSG = "💬 उपशीर्षक SRT-फाइल उपयोगकर्ता को भेजी गई।"
    SUBS_ERROR_PROCESSING_MSG = "❌ उपशीर्षक फाइल प्रसंस्करण में त्रुटि।"
    SUBS_ERROR_DOWNLOAD_MSG = "❌ उपशीर्षक डाउनलोड करने में विफल।"
    SUBS_ERROR_MSG = "❌ उपशीर्षक डाउनलोड करने में त्रुटि: {error}"
    
    # Split command messages
    SPLIT_SIZE_SET_MSG = "✅ विभाजन भाग आकार सेट किया गया: {size}"
    SPLIT_INVALID_SIZE_MSG = (
        "❌ **अमान्य आकार!**\n\n"
        "**वैध रेंज:** 100MB से 2GB\n\n"
        "**वैध प्रारूप:**\n"
        "• `100mb` से `2000mb` (मेगाबाइट)\n"
        "• `0.1gb` से `2gb` (गीगाबाइट)\n\n"
        "**उदाहरण:**\n"
        "• `/split 100mb` - 100 मेगाबाइट\n"
        "• `/split 500mb` - 500 मेगाबाइट\n"
        "• `/split 1.5gb` - 1.5 गीगाबाइट\n"
        "• `/split 2gb` - 2 गीगाबाइट\n"
        "• `/split 2000mb` - 2000 मेगाबाइट (2GB)\n\n"
        "**प्रीसेट:**\n"
        "• `/split 250mb`, `/split 500mb`, `/split 1gb`, `/split 1.5gb`, `/split 2gb`"
    )
    SPLIT_MENU_TITLE_MSG = (
        "🎬 **वीडियो विभाजन के लिए अधिकतम भाग आकार चुनें:**\n\n"
        "**रेंज:** 100MB से 2GB\n\n"
        "**त्वरित कमांड:**\n"
        "• `/split 100mb` - `/split 2000mb`\n"
        "• `/split 0.1gb` - `/split 2gb`\n\n"
        "**उदाहरण:** `/split 300mb`, `/split 1.2gb`, `/split 1500mb`"
    )
    SPLIT_MENU_CLOSED_MSG = "मेनू बंद।"
    
    # Settings command messages
    SETTINGS_TITLE_MSG = "<b>बॉट सेटिंग्स</b>\n\nएक श्रेणी चुनें:"
    SETTINGS_MENU_CLOSED_MSG = "मेनू बंद।"
    SETTINGS_CLEAN_TITLE_MSG = "<b>🧹 सफाई विकल्प</b>\n\nक्या साफ करना है चुनें:"
    SETTINGS_COOKIES_TITLE_MSG = "<b>🍪 कुकीज़</b>\n\nएक क्रिया चुनें:"
    SETTINGS_MEDIA_TITLE_MSG = "<b>🎞 मीडिया</b>\n\nएक क्रिया चुनें:"
    SETTINGS_LOGS_TITLE_MSG = "<b>📖 जानकारी</b>\n\nएक क्रिया चुनें:"
    SETTINGS_MORE_TITLE_MSG = "<b>⚙️ अधिक कमांड</b>\n\nएक क्रिया चुनें:"
    SETTINGS_COMMAND_EXECUTED_MSG = "कमांड निष्पादित।"
    SETTINGS_FLOOD_LIMIT_MSG = "⏳ फ्लड सीमा। बाद में कोशिश करें।"
    SETTINGS_HINT_SENT_MSG = "संकेत भेजा गया।"
    SETTINGS_SEARCH_HELPER_OPENED_MSG = "खोज सहायक खोला गया।"
    SETTINGS_UNKNOWN_COMMAND_MSG = "अज्ञात कमांड।"
    SETTINGS_HINT_CLOSED_MSG = "संकेत बंद।"
    SETTINGS_HELP_SENT_MSG = "उपयोगकर्ता को सहायता txt भेजें"
    SETTINGS_MENU_OPENED_MSG = "/settings मेनू खोला गया"
    
    # Search command messages
    SEARCH_HELPER_CLOSED_MSG = "🔍 खोज सहायक बंद"
    SEARCH_CLOSED_MSG = "बंद"
    
    # Proxy command messages
    PROXY_ENABLED_MSG = "✅ प्रॉक्सी {status}।"
    PROXY_ERROR_SAVING_MSG = "❌ प्रॉक्सी सेटिंग्स सहेजने में त्रुटि।"
    PROXY_MENU_TEXT_MSG = "सभी yt-dlp ऑपरेशन के लिए प्रॉक्सी सर्वर का उपयोग सक्षम या अक्षम करें?"
    PROXY_MENU_TEXT_MULTIPLE_MSG = "सभी yt-dlp ऑपरेशन के लिए प्रॉक्सी सर्वर ({count} उपलब्ध) का उपयोग सक्षम या अक्षम करें?\n\nजब सक्षम हो, तो प्रॉक्सी को {method} विधि का उपयोग करके चुना जाएगा।"
    PROXY_MENU_CLOSED_MSG = "मेनू बंद।"
    PROXY_ENABLED_CONFIRM_MSG = "✅ प्रॉक्सी सक्षम। सभी yt-dlp ऑपरेशन प्रॉक्सी का उपयोग करेंगे।"
    PROXY_ENABLED_MULTIPLE_MSG = "✅ प्रॉक्सी सक्षम। सभी yt-dlp ऑपरेशन {method} चयन विधि के साथ {count} प्रॉक्सी सर्वर का उपयोग करेंगे।"
    PROXY_DISABLED_MSG = "❌ प्रॉक्सी अक्षम।"
    PROXY_ERROR_SAVING_CALLBACK_MSG = "❌ प्रॉक्सी सेटिंग्स सहेजने में त्रुटि।"
    PROXY_ENABLED_CALLBACK_MSG = "प्रॉक्सी सक्षम।"
    PROXY_DISABLED_CALLBACK_MSG = "प्रॉक्सी अक्षम।"
    
    # Other handlers messages
    AUDIO_WAIT_MSG = "⏰ अपना पिछला डाउनलोड समाप्त होने तक प्रतीक्षा करें"
    AUDIO_HELP_MSG = (
        "<b>🎧 ऑडियो डाउनलोड कमांड</b>\n\n"
        "उपयोग: <code>/audio URL</code>\n\n"
        "<b>उदाहरण:</b>\n"
        "• <code>/audio https://youtu.be/abc123</code>\n"
        "• <code>/audio https://www.youtube.com/watch?v=abc123</code>\n"
        "• <code>/audio https://www.youtube.com/playlist?list=PL123*1*10</code>\n"
        "• <code>/audio 1-10 https://www.youtube.com/playlist?list=PL123</code>\n\n"
        "यह भी देखें: /vid, /img, /help, /playlist, /settings"
    )
    AUDIO_HELP_CLOSED_MSG = "ऑडियो संकेत बंद।"
    PLAYLIST_HELP_CLOSED_MSG = "प्लेलिस्ट सहायता बंद।"
    USERLOGS_CLOSED_MSG = "लॉग संदेश बंद।"
    HELP_CLOSED_MSG = "सहायता बंद।"
    
    # NSFW command messages
    NSFW_BLUR_SETTINGS_TITLE_MSG = "🔞 <b>NSFW धुंधलापन सेटिंग्स</b>\n\nNSFW सामग्री <b>{status}</b> है।\n\nNSFW सामग्री को धुंधला करना है या नहीं चुनें:"
    NSFW_MENU_CLOSED_MSG = "मेनू बंद।"
    NSFW_BLUR_DISABLED_MSG = "NSFW धुंधलापन अक्षम।"
    NSFW_BLUR_ENABLED_MSG = "NSFW धुंधलापन सक्षम।"
    NSFW_BLUR_DISABLED_CALLBACK_MSG = "NSFW धुंधलापन अक्षम।"
    NSFW_BLUR_ENABLED_CALLBACK_MSG = "NSFW धुंधलापन सक्षम।"
    
    # MediaInfo command messages
    MEDIAINFO_ENABLED_MSG = "✅ MediaInfo {status}।"
    MEDIAINFO_MENU_TITLE_MSG = "डाउनलोड की गई फाइलों के लिए MediaInfo भेजना सक्षम या अक्षम करें?"
    MEDIAINFO_MENU_CLOSED_MSG = "मेनू बंद।"
    MEDIAINFO_ENABLED_CONFIRM_MSG = "✅ MediaInfo सक्षम। डाउनलोड के बाद, फाइल जानकारी भेजी जाएगी।"
    MEDIAINFO_DISABLED_MSG = "❌ MediaInfo अक्षम।"
    MEDIAINFO_ENABLED_CALLBACK_MSG = "MediaInfo सक्षम।"
    MEDIAINFO_DISABLED_CALLBACK_MSG = "MediaInfo अक्षम।"
    
    # List command messages
    LIST_HELP_MSG = (
        "<b>📃 उपलब्ध प्रारूप सूची</b>\n\n"
        "URL के लिए उपलब्ध वीडियो/ऑडियो प्रारूप प्राप्त करें।\n\n"
        "<b>उपयोग:</b>\n"
        "<code>/list URL</code>\n\n"
        "<b>उदाहरण:</b>\n"
        "• <code>/list https://youtube.com/watch?v=123abc</code>\n"
        "• <code>/list https://youtube.com/playlist?list=123abc</code>\n\n"
        "<b>💡 प्रारूप ID का उपयोग कैसे करें:</b>\n"
        "सूची प्राप्त करने के बाद, विशिष्ट प्रारूप ID का उपयोग करें:\n"
        "• <code>/format id 401</code> - प्रारूप 401 डाउनलोड करें\n"
        "• <code>/format id401</code> - ऊपर के समान\n"
        "• <code>/format id140 audio</code> - प्रारूप 140 को MP3 ऑडियो के रूप में डाउनलोड करें\n\n"
        "यह कमांड सभी उपलब्ध प्रारूप दिखाएगा जिन्हें डाउनलोड किया जा सकता है।"
    )
    LIST_PROCESSING_MSG = "🔄 उपलब्ध प्रारूप प्राप्त कर रहे हैं..."
    LIST_INVALID_URL_MSG = "❌ कृपया http:// या https:// से शुरू होने वाला एक वैध URL प्रदान करें"
    LIST_CAPTION_MSG = (
        "📃 के लिए उपलब्ध प्रारूप:\n<code>{url}</code>\n\n"
        "💡 <b>प्रारूप कैसे सेट करें:</b>\n"
        "• <code>/format id 134</code> - विशिष्ट प्रारूप ID डाउनलोड करें\n"
        "• <code>/format 720p</code> - गुणवत्ता के अनुसार डाउनलोड करें\n"
        "• <code>/format best</code> - सर्वोत्तम गुणवत्ता डाउनलोड करें\n"
        "• <code>/format ask</code> - हमेशा गुणवत्ता के लिए पूछें\n\n"
        "{audio_note}\n"
        "📋 ऊपर की सूची से प्रारूप ID का उपयोग करें"
    )
    LIST_AUDIO_FORMATS_MSG = (
        "🎵 <b>केवल ऑडियो प्रारूप:</b> {formats}\n"
        "• <code>/format id 140 audio</code> - प्रारूप 140 को MP3 ऑडियो के रूप में डाउनलोड करें\n"
        "• <code>/format id140 audio</code> - ऊपर के समान\n"
        "ये MP3 ऑडियो फाइलों के रूप में डाउनलोड होंगे।\n\n"
    )
    LIST_ERROR_SENDING_MSG = "❌ प्रारूप फाइल भेजने में त्रुटि: {error}"
    LIST_ERROR_GETTING_MSG = "❌ प्रारूप प्राप्त करने में विफल:\n<code>{error}</code>"
    LIST_ERROR_OCCURRED_MSG = "❌ कमांड प्रसंस्करण के दौरान त्रुटि हुई"
    LIST_ERROR_CALLBACK_MSG = "त्रुटि हुई"
    LIST_HOW_TO_USE_FORMAT_IDS_TITLE = "💡 प्रारूप ID का उपयोग कैसे करें:\n"
    LIST_FORMAT_USAGE_INSTRUCTIONS = "सूची प्राप्त करने के बाद, विशिष्ट प्रारूप ID का उपयोग करें:\n"
    LIST_FORMAT_EXAMPLE_401 = "• /format id 401 - प्रारूप 401 डाउनलोड करें\n"
    LIST_FORMAT_EXAMPLE_401_SHORT = "• /format id401 - ऊपर के समान\n"
    LIST_FORMAT_EXAMPLE_140_AUDIO = "• /format id 140 audio - प्रारूप 140 को MP3 ऑडियो के रूप में डाउनलोड करें\n"
    LIST_FORMAT_EXAMPLE_140_AUDIO_SHORT = "• /format id140 audio - ऊपर के समान\n"
    LIST_AUDIO_FORMATS_DETECTED = "🎵 केवल ऑडियो प्रारूप का पता चला: {formats}\n"
    LIST_AUDIO_FORMATS_NOTE = "ये प्रारूप MP3 ऑडियो फाइलों के रूप में डाउनलोड होंगे।\n"
    LIST_VIDEO_ONLY_FORMATS_MSG = "🎬 <b>केवल वीडियो प्रारूप:</b> {formats}\n"
    LIST_USE_FORMAT_ID_MSG = "📋 ऊपर की सूची से प्रारूप ID का उपयोग करें"
    
    # Link command messages
    LINK_USAGE_MSG = (
        "🔗 <b>उपयोग:</b>\n"
        "<code>/link [quality] URL</code>\n\n"
        "<b>उदाहरण:</b>\n"
        "<blockquote>"
        "• /link https://youtube.com/watch?v=... - सर्वोत्तम गुणवत्ता\n"
        "• /link 720 https://youtube.com/watch?v=... - 720p या नीचे\n"
        "• /link 720p https://youtube.com/watch?v=... - ऊपर के समान\n"
        "• /link 4k https://youtube.com/watch?v=... - 4K या नीचे\n"
        "• /link 8k https://youtube.com/watch?v=... - 8K या नीचे"
        "</blockquote>\n\n"
        "<b>गुणवत्ता:</b> 1 से 10000 तक (उदाहरण: 144, 240, 720, 1080)"
    )
    LINK_INVALID_URL_MSG = "❌ कृपया एक वैध URL प्रदान करें"
    LINK_PROCESSING_MSG = "🔗 प्रत्यक्ष लिंक प्राप्त कर रहे हैं..."
    LINK_DURATION_MSG = "⏱ <b>अवधि:</b> {duration} सेकंड\n"
    LINK_VIDEO_STREAM_MSG = "🎬 <b>वीडियो स्ट्रीम:</b>\n<blockquote expandable><a href=\"{url}\">{url}</a></blockquote>\n\n"
    LINK_AUDIO_STREAM_MSG = "🎵 <b>ऑडियो स्ट्रीम:</b>\n<blockquote expandable><a href=\"{url}\">{url}</a></blockquote>\n\n"
    
    # Keyboard command messages
    KEYBOARD_UPDATED_MSG = "🎹 **कीबोर्ड सेटिंग अपडेट!**\n\nनई सेटिंग: **{setting}**"
    KEYBOARD_INVALID_ARG_MSG = (
        "❌ **अमान्य तर्क!**\n\n"
        "वैध विकल्प: `off`, `1x3`, `2x3`, `full`\n\n"
        "उदाहरण: `/keyboard off`"
    )
    KEYBOARD_SETTINGS_MSG = (
        "🎹 **कीबोर्ड सेटिंग्स**\n\n"
        "वर्तमान: **{current}**\n\n"
        "एक विकल्प चुनें:\n\n"
        "या उपयोग करें: `/keyboard off`, `/keyboard 1x3`, `/keyboard 2x3`, `/keyboard full`"
    )
    KEYBOARD_ACTIVATED_MSG = "🎹 कीबोर्ड सक्रिय!"
    KEYBOARD_HIDDEN_MSG = "⌨️ कीबोर्ड छुपा"
    KEYBOARD_1X3_ACTIVATED_MSG = "📱 1x3 कीबोर्ड सक्रिय!"
    KEYBOARD_2X3_ACTIVATED_MSG = "📱 2x3 कीबोर्ड सक्रिय!"
    KEYBOARD_EMOJI_ACTIVATED_MSG = "🔣 इमोजी कीबोर्ड सक्रिय!"
    KEYBOARD_ERROR_APPLYING_MSG = "कीबोर्ड सेटिंग {setting} लागू करने में त्रुटि: {error}"
    
    # Format command messages
    FORMAT_ALWAYS_ASK_SET_MSG = "✅ प्रारूप सेट किया गया: हमेशा पूछें। आपको हर बार URL भेजने पर गुणवत्ता के लिए पूछा जाएगा।"
    FORMAT_ALWAYS_ASK_CONFIRM_MSG = "✅ प्रारूप सेट किया गया: हमेशा पूछें। अब आपको हर बार URL भेजने पर गुणवत्ता के लिए पूछा जाएगा।"
    FORMAT_BEST_UPDATED_MSG = "✅ प्रारूप सर्वोत्तम गुणवत्ता (AVC+MP4 प्राथमिकता) पर अपडेट किया गया:\n{format}"
    FORMAT_ID_UPDATED_MSG = "✅ प्रारूप ID {id} पर अपडेट किया गया:\n{format}\n\n💡 <b>नोट:</b> यदि यह केवल ऑडियो प्रारूप है, तो इसे MP3 ऑडियो फाइल के रूप में डाउनलोड किया जाएगा।"
    FORMAT_ID_AUDIO_UPDATED_MSG = "✅ प्रारूप ID {id} (केवल ऑडियो) पर अपडेट किया गया:\n{format}\n\n💡 यह MP3 ऑडियो फाइल के रूप में डाउनलोड होगा।"
    FORMAT_QUALITY_UPDATED_MSG = "✅ प्रारूप गुणवत्ता {quality} पर अपडेट किया गया:\n{format}"
    FORMAT_CUSTOM_UPDATED_MSG = "✅ प्रारूप अपडेट किया गया:\n{format}"
    FORMAT_MENU_MSG = (
        "एक प्रारूप विकल्प चुनें या कस्टम भेजें:\n"
        "• <code>/format &lt;format_string&gt;</code> - कस्टम प्रारूप\n"
        "• <code>/format 720</code> - 720p गुणवत्ता\n"
        "• <code>/format 4k</code> - 4K गुणवत्ता\n"
        "• <code>/format 8k</code> - 8K गुणवत्ता\n"
        "• <code>/format id 401</code> - विशिष्ट प्रारूप ID\n"
        "• <code>/format ask</code> - हमेशा मेनू दिखाएं\n"
        "• <code>/format best</code> - bv+ba/सर्वोत्तम गुणवत्ता"
    )
    FORMAT_CUSTOM_HINT_MSG = (
        "कस्टम प्रारूप का उपयोग करने के लिए, कमांड को निम्नलिखित रूप में भेजें:\n\n"
        "<code>/format bestvideo+bestaudio/best</code>\n\n"
        "<code>bestvideo+bestaudio/best</code> को अपनी वांछित प्रारूप स्ट्रिंग से बदलें।"
    )
    FORMAT_RESOLUTION_MENU_MSG = "अपना वांछित रिज़ॉल्यूशन और कोडेक चुनें:"
    FORMAT_ALWAYS_ASK_CONFIRM_MSG = "✅ प्रारूप सेट किया गया: हमेशा पूछें। अब आपको हर बार URL भेजने पर गुणवत्ता के लिए पूछा जाएगा।"
    FORMAT_UPDATED_MSG = "✅ प्रारूप अपडेट किया गया:\n{format}"
    FORMAT_SAVED_MSG = "✅ प्रारूप सहेजा गया।"
    FORMAT_CHOICE_UPDATED_MSG = "✅ प्रारूप विकल्प अपडेट किया गया।"
    FORMAT_CUSTOM_MENU_CLOSED_MSG = "कस्टम प्रारूप मेनू बंद"
    FORMAT_CODEC_SET_MSG = "✅ कोडेक {codec} पर सेट किया गया"
    
    # Cookies command messages
    COOKIES_BROWSER_CHOICE_UPDATED_MSG = "✅ ब्राउज़र विकल्प अपडेट किया गया।"
    
    # Clean command messages
    
    # Admin command messages
    ADMIN_ACCESS_DENIED_MSG = "❌ पहुंच अस्वीकृत। केवल व्यवस्थापक।"
    ACCESS_DENIED_ADMIN = "❌ पहुंच अस्वीकृत। केवल व्यवस्थापक।"
    WELCOME_MASTER = "स्वागत है मास्टर 🥷"
    DOWNLOAD_ERROR_GENERIC = "❌ क्षमा करें... डाउनलोड के दौरान कुछ त्रुटि हुई।"
    SIZE_LIMIT_EXCEEDED = "❌ फाइल का आकार {max_size_gb} GB सीमा से अधिक है। कृपया अनुमतित आकार के भीतर एक छोटी फाइल चुनें।"
    ADMIN_SCRIPT_NOT_FOUND_MSG = "❌ स्क्रिप्ट नहीं मिली: {script_path}"
    ADMIN_DOWNLOADING_MSG = "⏳ {script_path} का उपयोग करके ताजा Firebase डंप डाउनलोड हो रहा है..."
    ADMIN_CACHE_RELOADED_MSG = "✅ Firebase कैश सफलतापूर्वक रीलोड किया गया!"
    ADMIN_CACHE_FAILED_MSG = "❌ Firebase कैश रीलोड करने में विफल। जांचें कि {cache_file} मौजूद है या नहीं।"
    ADMIN_ERROR_RELOADING_MSG = "❌ कैश रीलोड करने में त्रुटि: {error}"
    ADMIN_ERROR_SCRIPT_MSG = "❌ {script_path} चलाने में त्रुटि:\n{stdout}\n{stderr}"
    ADMIN_PROMO_SENT_MSG = "<b>✅ प्रोमो संदेश सभी अन्य उपयोगकर्ताओं को भेजा गया</b>"
    ADMIN_CANNOT_SEND_PROMO_MSG = "<b>❌ प्रोमो संदेश नहीं भेज सकते। किसी संदेश का जवाब देने का प्रयास करें\nया कोई त्रुटि हुई</b>"
    ADMIN_USER_NO_DOWNLOADS_MSG = "<b>❌ उपयोगकर्ता ने अभी तक कोई सामग्री डाउनलोड नहीं की...</b> लॉग में मौजूद नहीं"
    ADMIN_INVALID_COMMAND_MSG = "❌ अमान्य कमांड"
    ADMIN_NO_DATA_FOUND_MSG = f"❌ कैश में <code>{{path}}</code> के लिए कोई डेटा नहीं मिला"
    ADMIN_BLOCK_USER_USAGE_MSG = "❌ उपयोग: /block_user <user_id>"
    ADMIN_CANNOT_DELETE_ADMIN_MSG = "🚫 व्यवस्थापक व्यवस्थापक को हटा नहीं सकता"
    ADMIN_USER_BLOCKED_MSG = "उपयोगकर्ता ब्लॉक 🔒❌\n \nID: <code>{user_id}</code>\nब्लॉक की तारीख: {date}"
    ADMIN_USER_ALREADY_BLOCKED_MSG = "<code>{user_id}</code> पहले से ब्लॉक है ❌😐"
    ADMIN_NOT_ADMIN_MSG = "🚫 क्षमा करें! आप व्यवस्थापक नहीं हैं"
    ADMIN_UNBLOCK_USER_USAGE_MSG = "❌ उपयोग: /unblock_user <user_id>"
    ADMIN_USER_UNBLOCKED_MSG = "उपयोगकर्ता अनब्लॉक 🔓✅\n \nID: <code>{user_id}</code>\nअनब्लॉक की तारीख: {date}"
    ADMIN_USER_ALREADY_UNBLOCKED_MSG = "<code>{user_id}</code> पहले से अनब्लॉक है ✅😐"
    ADMIN_BOT_RUNNING_TIME_MSG = "⏳ <i>बॉट चलने का समय -</i> <b>{time}</b>"
    ADMIN_UNCACHE_USAGE_MSG = "❌ कैश साफ करने के लिए कृपया एक URL प्रदान करें।\nउपयोग: <code>/uncache &lt;URL&gt;</code>"
    ADMIN_UNCACHE_INVALID_URL_MSG = "❌ कृपया एक वैध URL प्रदान करें।\nउपयोग: <code>/uncache &lt;URL&gt;</code>"
    ADMIN_CACHE_CLEARED_MSG = "✅ URL के लिए कैश सफलतापूर्वक साफ किया गया:\n<code>{url}</code>"
    ADMIN_NO_CACHE_FOUND_MSG = "ℹ️ इस लिंक के लिए कोई कैश नहीं मिला।"
    ADMIN_ERROR_CLEARING_CACHE_MSG = "❌ कैश साफ करने में त्रुटि: {error}"
    ADMIN_ACCESS_DENIED_MSG = "❌ पहुंच अस्वीकृत। केवल व्यवस्थापक।"
    ADMIN_UPDATE_PORN_RUNNING_MSG = "⏳ पोर्न सूची अपडेट स्क्रिप्ट चल रही है: {script_path}"
    ADMIN_SCRIPT_COMPLETED_MSG = "✅ स्क्रिप्ट सफलतापूर्वक पूरी हुई!"
    ADMIN_SCRIPT_COMPLETED_WITH_OUTPUT_MSG = "✅ स्क्रिप्ट सफलतापूर्वक पूरी हुई!\n\nआउटपुट:\n<code>{output}</code>"
    ADMIN_SCRIPT_FAILED_MSG = "❌ स्क्रिप्ट रिटर्न कोड {returncode} के साथ विफल:\n<code>{error}</code>"
    ADMIN_ERROR_RUNNING_SCRIPT_MSG = "❌ स्क्रिप्ट चलाने में त्रुटि: {error}"
    ADMIN_RELOADING_PORN_MSG = "⏳ पोर्न और डोमेन-संबंधित कैश रीलोड हो रहे हैं..."
    ADMIN_PORN_CACHES_RELOADED_MSG = (
        "✅ पोर्न कैश सफलतापूर्वक रीलोड किए गए!\n\n"
        "📊 वर्तमान कैश स्थिति:\n"
        "• पोर्न डोमेन: {porn_domains}\n"
        "• पोर्न कीवर्ड: {porn_keywords}\n"
        "• समर्थित साइटें: {supported_sites}\n"
        "• WHITELIST: {whitelist}\n"
        "• GREYLIST: {greylist}\n"
        "• BLACK_LIST: {black_list}\n"
        "• WHITE_KEYWORDS: {white_keywords}\n"
        "• PROXY_DOMAINS: {proxy_domains}\n"
        "• PROXY_2_DOMAINS: {proxy_2_domains}\n"
        "• CLEAN_QUERY: {clean_query}\n"
        "• NO_COOKIE_DOMAINS: {no_cookie_domains}"
    )
    ADMIN_ERROR_RELOADING_PORN_MSG = "❌ पोर्न कैश रीलोड करने में त्रुटि: {error}"
    ADMIN_CHECK_PORN_USAGE_MSG = "❌ कृपया जांच के लिए URL प्रदान करें।\nउपयोग: <code>/check_porn &lt;URL&gt;</code>"
    ADMIN_CHECK_PORN_INVALID_URL_MSG = "❌ कृपया एक वैध URL प्रदान करें।\nउपयोग: <code>/check_porn &lt;URL&gt;</code>"
    ADMIN_CHECKING_URL_MSG = "🔍 NSFW सामग्री के लिए URL जांच रहा है...\n<code>{url}</code>"
    ADMIN_PORN_CHECK_RESULT_MSG = (
        "{status_icon} <b>पोर्न जांच परिणाम</b>\n\n"
        "<b>URL:</b> <code>{url}</code>\n"
        "<b>स्थिति:</b> <b>{status_text}</b>\n\n"
        "<b>स्पष्टीकरण:</b>\n{explanation}"
    )
    ADMIN_ERROR_CHECKING_URL_MSG = "❌ URL जांचने में त्रुटि: {error}"
    
    # Clean command messages
    CLEAN_COOKIES_CLEANED_MSG = "कुकीज़ साफ की गईं।"
    CLEAN_LOGS_CLEANED_MSG = "लॉग साफ किए गए।"
    CLEAN_TAGS_CLEANED_MSG = "टैग साफ किए गए।"
    CLEAN_FORMAT_CLEANED_MSG = "प्रारूप साफ किया गया।"
    CLEAN_SPLIT_CLEANED_MSG = "स्प्लिट साफ किया गया।"
    CLEAN_MEDIAINFO_CLEANED_MSG = "मीडियाइन्फो साफ किया गया।"
    CLEAN_SUBS_CLEANED_MSG = "उपशीर्षक सेटिंग्स साफ की गईं।"
    CLEAN_KEYBOARD_CLEANED_MSG = "कीबोर्ड सेटिंग्स साफ की गईं।"
    CLEAN_ARGS_CLEANED_MSG = "तर्क सेटिंग्स साफ की गईं।"
    CLEAN_NSFW_CLEANED_MSG = "NSFW सेटिंग्स साफ की गईं।"
    CLEAN_PROXY_CLEANED_MSG = "प्रॉक्सी सेटिंग्स साफ की गईं।"
    CLEAN_FLOOD_WAIT_CLEANED_MSG = "फ्लड प्रतीक्षा सेटिंग्स साफ की गईं।"
    CLEAN_ALL_CLEANED_MSG = "सभी फाइलें साफ की गईं।"
    CLEAN_COOKIES_MENU_TITLE_MSG = "<b>🍪 कुकीज़</b>\n\nएक क्रिया चुनें:"
    
    # Cookies command messages
    COOKIES_FILE_SAVED_MSG = "✅ कुकी फाइल सहेजी गई"
    COOKIES_SKIPPED_VALIDATION_MSG = "✅ गैर-YouTube कुकीज़ के लिए सत्यापन छोड़ दिया गया"
    COOKIES_INCORRECT_FORMAT_MSG = "⚠️ कुकी फाइल मौजूद है लेकिन गलत प्रारूप है"
    COOKIES_FILE_NOT_FOUND_MSG = "❌ कुकी फाइल नहीं मिली।"
    COOKIES_YOUTUBE_TEST_START_MSG = "🔄 YouTube कुकीज़ टेस्ट शुरू हो रहा है...\n\nकृपया प्रतीक्षा करें जबकि मैं आपकी कुकीज़ की जांच और सत्यापन कर रहा हूं।"
    COOKIES_YOUTUBE_WORKING_MSG = "✅ आपकी मौजूदा YouTube कुकीज़ ठीक से काम कर रही हैं!\n\nनई डाउनलोड करने की आवश्यकता नहीं है।"
    COOKIES_YOUTUBE_EXPIRED_MSG = "❌ आपकी मौजूदा YouTube कुकीज़ समाप्त हो गई हैं या अमान्य हैं।\n\n🔄 नई कुकीज़ डाउनलोड हो रही हैं..."
    COOKIES_SOURCE_NOT_CONFIGURED_MSG = "❌ {service} कुकी स्रोत कॉन्फ़िगर नहीं है!"
    COOKIES_SOURCE_MUST_BE_TXT_MSG = "❌ {service} कुकी स्रोत .txt फाइल होनी चाहिए!"
    
    # Image command messages
    IMG_RANGE_LIMIT_EXCEEDED_MSG = "❗️ रेंज सीमा पार हो गई: {range_count} फाइलें अनुरोधित (अधिकतम {max_img_files})।\n\nअधिकतम उपलब्ध फाइलें डाउनलोड करने के लिए इनमें से एक कमांड का उपयोग करें:\n\n<code>/img {start_range}-{end_range} {url}</code>\n\n<code>/img {suggested_command_url_format}</code>"
    COMMAND_IMAGE_HELP_CLOSE_BUTTON_MSG = "🔚बंद करें"
    COMMAND_IMAGE_MEDIA_LIMIT_EXCEEDED_MSG = "❗️ मीडिया सीमा पार हो गई: {count} फाइलें अनुरोधित (अधिकतम {max_count})।\n\nअधिकतम उपलब्ध फाइलें डाउनलोड करने के लिए इनमें से एक कमांड का उपयोग करें:\n\n<code>/img {start_range}-{end_range} {url}</code>\n\n<code>/img {suggested_command_url_format}</code>"
    IMG_FOUND_MEDIA_ITEMS_MSG = "📊 लिंक से <b>{count}</b> मीडिया आइटम मिले"
    IMG_SELECT_DOWNLOAD_RANGE_MSG = "डाउनलोड रेंज चुनें:"
    
    # Args command parameter descriptions
    ARGS_IMPERSONATE_DESC_MSG = "ब्राउज़र प्रतिरूपण"
    ARGS_REFERER_DESC_MSG = "रेफरर हेडर"
    ARGS_USER_AGENT_DESC_MSG = "यूजर-एजेंट हेडर"
    ARGS_GEO_BYPASS_DESC_MSG = "भौगोलिक प्रतिबंधों को बायपास करें"
    ARGS_CHECK_CERTIFICATE_DESC_MSG = "SSL प्रमाणपत्र जांचें"
    ARGS_LIVE_FROM_START_DESC_MSG = "लाइव स्ट्रीम को शुरुआत से डाउनलोड करें"
    ARGS_NO_LIVE_FROM_START_DESC_MSG = "लाइव स्ट्रीम को शुरुआत से डाउनलोड न करें"
    ARGS_HLS_USE_MPEGTS_DESC_MSG = "HLS वीडियो के लिए MPEG-TS कंटेनर का उपयोग करें"
    ARGS_NO_PLAYLIST_DESC_MSG = "केवल एकल वीडियो डाउनलोड करें, प्लेलिस्ट नहीं"
    ARGS_NO_PART_DESC_MSG = ".part फाइलों का उपयोग न करें"
    ARGS_NO_CONTINUE_DESC_MSG = "आंशिक डाउनलोड को फिर से शुरू न करें"
    ARGS_AUDIO_FORMAT_DESC_MSG = "निष्कर्षण के लिए ऑडियो प्रारूप"
    ARGS_EMBED_METADATA_DESC_MSG = "वीडियो फाइल में मेटाडेटा एम्बेड करें"
    ARGS_EMBED_THUMBNAIL_DESC_MSG = "वीडियो फाइल में थंबनेल एम्बेड करें"
    ARGS_WRITE_THUMBNAIL_DESC_MSG = "थंबनेल को फाइल में लिखें"
    ARGS_CONCURRENT_FRAGMENTS_DESC_MSG = "डाउनलोड करने के लिए समवर्ती फ्रैगमेंट की संख्या"
    ARGS_FORCE_IPV4_DESC_MSG = "IPv4 कनेक्शन को मजबूर करें"
    ARGS_FORCE_IPV6_DESC_MSG = "IPv6 कनेक्शन को मजबूर करें"
    ARGS_XFF_DESC_MSG = "X-Forwarded-For हेडर रणनीति"
    ARGS_HTTP_CHUNK_SIZE_DESC_MSG = "HTTP चंक आकार (बाइट्स)"
    ARGS_SLEEP_SUBTITLES_DESC_MSG = "उपशीर्षक डाउनलोड से पहले स्लीप (सेकंड)"
    ARGS_LEGACY_SERVER_CONNECT_DESC_MSG = "लेगेसी सर्वर कनेक्शन की अनुमति दें"
    ARGS_NO_CHECK_CERTIFICATES_DESC_MSG = "HTTPS प्रमाणपत्र सत्यापन को दबाएं"
    ARGS_USERNAME_DESC_MSG = "खाता उपयोगकर्ता नाम"
    ARGS_PASSWORD_DESC_MSG = "खाता पासवर्ड"
    ARGS_TWOFACTOR_DESC_MSG = "दो-कारक प्रमाणीकरण कोड"
    ARGS_IGNORE_ERRORS_DESC_MSG = "डाउनलोड त्रुटियों को नजरअंदाज करें और जारी रखें"
    ARGS_MIN_FILESIZE_DESC_MSG = "न्यूनतम फाइल आकार (MB)"
    ARGS_MAX_FILESIZE_DESC_MSG = "अधिकतम फाइल आकार (MB)"
    ARGS_PLAYLIST_ITEMS_DESC_MSG = "डाउनलोड करने के लिए प्लेलिस्ट आइटम (उदा., 1,3,5 या 1-5)"
    ARGS_DATE_DESC_MSG = "इस तारीख को अपलोड किए गए वीडियो डाउनलोड करें (YYYYMMDD)"
    ARGS_DATEBEFORE_DESC_MSG = "इस तारीख से पहले अपलोड किए गए वीडियो डाउनलोड करें (YYYYMMDD)"
    ARGS_DATEAFTER_DESC_MSG = "इस तारीख के बाद अपलोड किए गए वीडियो डाउनलोड करें (YYYYMMDD)"
    ARGS_HTTP_HEADERS_DESC_MSG = "कस्टम HTTP हेडर (JSON)"
    ARGS_SLEEP_INTERVAL_DESC_MSG = "अनुरोधों के बीच स्लीप अंतराल (सेकंड)"
    ARGS_MAX_SLEEP_INTERVAL_DESC_MSG = "अधिकतम स्लीप अंतराल (सेकंड)"
    ARGS_RETRIES_DESC_MSG = "पुनः प्रयासों की संख्या"
    ARGS_VIDEO_FORMAT_DESC_MSG = "वीडियो कंटेनर प्रारूप"
    ARGS_MERGE_OUTPUT_FORMAT_DESC_MSG = "मर्जिंग के लिए आउटपुट कंटेनर प्रारूप"
    ARGS_SEND_AS_FILE_DESC_MSG = "सभी मीडिया को मीडिया के बजाय दस्तावेज़ के रूप में भेजें"
    
    # Args command short descriptions
    ARGS_IMPERSONATE_SHORT_MSG = "प्रतिरूपण"
    ARGS_REFERER_SHORT_MSG = "रेफरर"
    ARGS_GEO_BYPASS_SHORT_MSG = "जियो बायपास"
    ARGS_CHECK_CERTIFICATE_SHORT_MSG = "प्रमाणपत्र जांचें"
    ARGS_LIVE_FROM_START_SHORT_MSG = "लाइव शुरू"
    ARGS_NO_LIVE_FROM_START_SHORT_MSG = "लाइव शुरू नहीं"
    ARGS_USER_AGENT_SHORT_MSG = "यूजर एजेंट"
    ARGS_HLS_USE_MPEGTS_SHORT_MSG = "HLS MPEG-TS"
    ARGS_NO_PLAYLIST_SHORT_MSG = "प्लेलिस्ट नहीं"
    ARGS_NO_PART_SHORT_MSG = "भाग नहीं"
    ARGS_NO_CONTINUE_SHORT_MSG = "जारी नहीं"
    ARGS_AUDIO_FORMAT_SHORT_MSG = "ऑडियो प्रारूप"
    ARGS_EMBED_METADATA_SHORT_MSG = "मेटा एम्बेड करें"
    ARGS_EMBED_THUMBNAIL_SHORT_MSG = "थंबनेल एम्बेड करें"
    ARGS_WRITE_THUMBNAIL_SHORT_MSG = "थंबनेल लिखें"
    ARGS_CONCURRENT_FRAGMENTS_SHORT_MSG = "समवर्ती"
    ARGS_FORCE_IPV4_SHORT_MSG = "IPv4 फोर्स"
    ARGS_FORCE_IPV6_SHORT_MSG = "IPv6 फोर्स"
    ARGS_XFF_SHORT_MSG = "XFF हेडर"
    ARGS_HTTP_CHUNK_SIZE_SHORT_MSG = "चंक आकार"
    ARGS_SLEEP_SUBTITLES_SHORT_MSG = "सब्स स्लीप"
    ARGS_LEGACY_SERVER_CONNECT_SHORT_MSG = "लेगेसी कनेक्ट"
    ARGS_NO_CHECK_CERTIFICATES_SHORT_MSG = "प्रमाणपत्र जांच नहीं"
    ARGS_USERNAME_SHORT_MSG = "उपयोगकर्ता नाम"
    ARGS_PASSWORD_SHORT_MSG = "पासवर्ड"
    ARGS_TWOFACTOR_SHORT_MSG = "2FA"
    ARGS_IGNORE_ERRORS_SHORT_MSG = "त्रुटियां नजरअंदाज"
    ARGS_MIN_FILESIZE_SHORT_MSG = "न्यूनतम आकार"
    ARGS_MAX_FILESIZE_SHORT_MSG = "अधिकतम आकार"
    ARGS_PLAYLIST_ITEMS_SHORT_MSG = "प्लेलिस्ट आइटम"
    ARGS_DATE_SHORT_MSG = "तारीख"
    ARGS_DATEBEFORE_SHORT_MSG = "तारीख से पहले"
    ARGS_DATEAFTER_SHORT_MSG = "तारीख के बाद"
    ARGS_HTTP_HEADERS_SHORT_MSG = "HTTP हेडर"
    ARGS_SLEEP_INTERVAL_SHORT_MSG = "स्लीप अंतराल"
    ARGS_MAX_SLEEP_INTERVAL_SHORT_MSG = "अधिकतम स्लीप"
    ARGS_VIDEO_FORMAT_SHORT_MSG = "वीडियो प्रारूप"
    ARGS_MERGE_OUTPUT_FORMAT_SHORT_MSG = "मर्ज प्रारूप"
    ARGS_SEND_AS_FILE_SHORT_MSG = "फाइल के रूप में भेजें"
    
    # Additional cookies command messages
    COOKIES_FILE_TOO_LARGE_MSG = "❌ फाइल बहुत बड़ी है। अधिकतम आकार 100 KB है।"
    COOKIES_INVALID_FORMAT_MSG = "❌ केवल निम्नलिखित प्रारूप की फाइलों की अनुमति है .txt।"
    COOKIES_INVALID_COOKIE_MSG = "❌ फाइल cookie.txt जैसी नहीं दिखती ('# Netscape HTTP Cookie File' लाइन नहीं है)।"
    COOKIES_ERROR_READING_MSG = "❌ फाइल पढ़ने में त्रुटि: {error}"
    COOKIES_FILE_EXISTS_MSG = "✅ कुकी फाइल मौजूद है और सही प्रारूप है"
    COOKIES_FILE_TOO_LARGE_DOWNLOAD_MSG = "❌ {service} कुकी फाइल बहुत बड़ी है! अधिकतम 100KB, प्राप्त {size}KB।"
    COOKIES_FILE_DOWNLOADED_MSG = "<b>✅ {service} कुकी फाइल डाउनलोड की गई और आपके फोल्डर में cookie.txt के रूप में सहेजी गई।</b>"
    COOKIES_SOURCE_UNAVAILABLE_MSG = "❌ {service} कुकी स्रोत उपलब्ध नहीं है (स्थिति {status})। कृपया बाद में पुनः प्रयास करें।"
    COOKIES_ERROR_DOWNLOADING_MSG = "❌ {service} कुकी फाइल डाउनलोड करने में त्रुटि। कृपया बाद में पुनः प्रयास करें।"
    COOKIES_USER_PROVIDED_MSG = "<b>✅ उपयोगकर्ता ने एक नई कुकी फाइल प्रदान की।</b>"
    COOKIES_SUCCESSFULLY_UPDATED_MSG = "<b>✅ कुकी सफलतापूर्वक अपडेट की गई:</b>\n<code>{final_cookie}</code>"
    COOKIES_NOT_VALID_MSG = "<b>❌ मान्य कुकी नहीं है।</b>"
    COOKIES_YOUTUBE_SOURCES_NOT_CONFIGURED_MSG = "❌ YouTube कुकी स्रोत कॉन्फ़िगर नहीं हैं!"
    COOKIES_DOWNLOADING_YOUTUBE_MSG = "🔄 YouTube कुकीज़ डाउनलोड और जांच हो रही है...\n\nप्रयास {attempt} में से {total}"
    
    # Additional admin command messages
    ADMIN_ACCESS_DENIED_AUTO_DELETE_MSG = "❌ पहुंच अस्वीकृत। केवल व्यवस्थापक।"
    ADMIN_USER_LOGS_TOTAL_MSG = "कुल: <b>{total}</b>\n<b>{user_id}</b> - लॉग (अंतिम 10):\n\n{format_str}"
    
    # Additional keyboard command messages
    KEYBOARD_ACTIVATED_MSG = "🎹 कीबोर्ड सक्रिय!"
    
    # Additional subtitles command messages
    SUBS_LANGUAGE_SET_MSG = "✅ उपशीर्षक भाषा सेट की गई: {flag} {name}"
    SUBS_LANGUAGE_AUTO_SET_MSG = "✅ उपशीर्षक भाषा सेट की गई: {flag} {name} AUTO/TRANS सक्षम के साथ।"
    SUBS_LANGUAGE_MENU_CLOSED_MSG = "उपशीर्षक भाषा मेनू बंद।"
    SUBS_DOWNLOADING_MSG = "💬 उपशीर्षक डाउनलोड हो रहे हैं..."
    
    # Additional admin command messages
    ADMIN_RELOADING_CACHE_MSG = "🔄 Firebase कैश को मेमोरी में रीलोड किया जा रहा है..."
    
    # Additional cookies command messages
    COOKIES_NO_BROWSERS_NO_URL_MSG = "❌ कोई COOKIE_URL कॉन्फ़िगर नहीं है। /cookie का उपयोग करें या cookie.txt अपलोड करें।"
    COOKIES_DOWNLOADING_FROM_URL_MSG = "📥 रिमोट URL से कुकीज़ डाउनलोड हो रही है..."
    COOKIE_FALLBACK_URL_NOT_TXT_MSG = "❌ फॉलबैक COOKIE_URL .txt फाइल की ओर इंगित करना चाहिए।"
    COOKIE_FALLBACK_TOO_LARGE_MSG = "❌ फॉलबैक कुकी फाइल बहुत बड़ी है (>100KB)।"
    COOKIE_YT_FALLBACK_SAVED_MSG = "✅ YouTube कुकी फाइल फॉलबैक के माध्यम से डाउनलोड की गई और cookie.txt के रूप में सहेजी गई"
    COOKIE_FALLBACK_UNAVAILABLE_MSG = "❌ फॉलबैक कुकी स्रोत उपलब्ध नहीं है (स्थिति {status})। /cookie का प्रयास करें या cookie.txt अपलोड करें।"
    COOKIE_FALLBACK_ERROR_MSG = "❌ फॉलबैक कुकी डाउनलोड करने में त्रुटि। /cookie का प्रयास करें या cookie.txt अपलोड करें।"
    COOKIE_FALLBACK_UNEXPECTED_MSG = "❌ फॉलबैक कुकी डाउनलोड के दौरान अप्रत्याशित त्रुटि।"
    COOKIES_BROWSER_NOT_INSTALLED_MSG = "⚠️ {browser} ब्राउज़र इंस्टॉल नहीं है।"
    COOKIES_SAVED_USING_BROWSER_MSG = "✅ ब्राउज़र का उपयोग करके कुकीज़ सहेजी गईं: {browser}"
    COOKIES_FAILED_TO_SAVE_MSG = "❌ कुकीज़ सहेजने में विफल: {error}"
    COOKIES_YOUTUBE_WORKING_PROPERLY_MSG = "✅ YouTube कुकीज़ ठीक से काम कर रही हैं"
    COOKIES_YOUTUBE_EXPIRED_INVALID_MSG = "❌ YouTube कुकीज़ समाप्त हो गई हैं या अमान्य हैं\n\nनई कुकीज़ प्राप्त करने के लिए /cookie का उपयोग करें"
    
    # Additional format command messages
    FORMAT_MENU_ADDITIONAL_MSG = "• <code>/format &lt;format_string&gt;</code> - कस्टम प्रारूप\n• <code>/format 720</code> - 720p गुणवत्ता\n• <code>/format 4k</code> - 4K गुणवत्ता"
    
    # Callback answer messages
    FORMAT_HINT_SENT_MSG = "संकेत भेजा गया।"
    FORMAT_MKV_TOGGLE_MSG = "MKV अब {status} है"
    COOKIES_NO_REMOTE_URL_MSG = "❌ कोई रिमोट URL कॉन्फ़िगर नहीं है"
    COOKIES_INVALID_FILE_FORMAT_MSG = "❌ अमान्य फाइल प्रारूप"
    COOKIES_FILE_TOO_LARGE_CALLBACK_MSG = "❌ फाइल बहुत बड़ी है"
    COOKIES_DOWNLOADED_SUCCESSFULLY_MSG = "✅ कुकीज़ सफलतापूर्वक डाउनलोड की गईं"
    COOKIES_SERVER_ERROR_MSG = "❌ सर्वर त्रुटि {status}"
    COOKIES_DOWNLOAD_FAILED_MSG = "❌ डाउनलोड विफल रहा"
    COOKIES_UNEXPECTED_ERROR_MSG = "❌ अप्रत्याशित त्रुटि"
    COOKIES_BROWSER_NOT_INSTALLED_CALLBACK_MSG = "⚠️ ब्राउज़र इंस्टॉल नहीं है।"
    COOKIES_MENU_CLOSED_MSG = "मेनू बंद।"
    COOKIES_HINT_CLOSED_MSG = "कुकी संकेत बंद।"
    IMG_HELP_CLOSED_MSG = "मदद बंद।"
    SUBS_LANGUAGE_UPDATED_MSG = "उपशीर्षक भाषा सेटिंग्स अपडेट की गईं।"
    SUBS_MENU_CLOSED_MSG = "उपशीर्षक भाषा मेनू बंद।"
    KEYBOARD_SET_TO_MSG = "कीबोर्ड {setting} पर सेट किया गया"
    KEYBOARD_ERROR_PROCESSING_MSG = "सेटिंग प्रोसेस करने में त्रुटि"
    MEDIAINFO_ENABLED_CALLBACK_MSG = "MediaInfo सक्षम।"
    MEDIAINFO_DISABLED_CALLBACK_MSG = "MediaInfo अक्षम।"
    NSFW_BLUR_DISABLED_CALLBACK_MSG = "NSFW ब्लर अक्षम।"
    NSFW_BLUR_ENABLED_CALLBACK_MSG = "NSFW ब्लर सक्षम।"
    SETTINGS_MENU_CLOSED_MSG = "मेनू बंद।"
    SETTINGS_FLOOD_WAIT_ACTIVE_MSG = "फ्लड प्रतीक्षा सक्रिय। बाद में प्रयास करें।"
    OTHER_HELP_CLOSED_MSG = "मदद बंद।"
    OTHER_LOGS_MESSAGE_CLOSED_MSG = "लॉग संदेश बंद।"
    
    # Additional split command messages
    SPLIT_MENU_CLOSED_MSG = "मेनू बंद।"
    SPLIT_INVALID_SIZE_CALLBACK_MSG = "अमान्य आकार।"
    
    # Additional error messages
    MEDIAINFO_ERROR_SENDING_MSG = "❌ MediaInfo भेजने में त्रुटि: {error}"
    LINK_ERROR_OCCURRED_MSG = "❌ एक त्रुटि हुई: {error}"
    
    # Additional document caption messages
    MEDIAINFO_DOCUMENT_CAPTION_MSG = "<blockquote>📊 MediaInfo</blockquote>"
    ADMIN_USER_LOGS_CAPTION_MSG = "{user_id} - सभी लॉग"
    ADMIN_BOT_DATA_CAPTION_MSG = "{bot_name} - सभी {path}"
    
    # Additional cookies command messages (missing ones)
    DOWNLOAD_FROM_URL_BUTTON_MSG = "📥 रिमोट URL से डाउनलोड करें"
    BROWSER_OPEN_BUTTON_MSG = "🌐 ब्राउज़र खोलें"
    SELECT_BROWSER_MSG = "कुकीज़ डाउनलोड करने के लिए एक ब्राउज़र चुनें:"
    SELECT_BROWSER_NO_BROWSERS_MSG = "इस सिस्टम पर कोई ब्राउज़र नहीं मिला। आप रिमोट URL से कुकीज़ डाउनलोड कर सकते हैं या ब्राउज़र स्थिति की निगरानी कर सकते हैं:"
    BROWSER_MONITOR_HINT_MSG = "🌐 <b>ब्राउज़र खोलें</b> - मिनी-ऐप में ब्राउज़र स्थिति की निगरानी के लिए"
    COOKIES_FAILED_RUN_CHECK_MSG = "❌ /check_cookie चलाने में विफल"
    COOKIES_FLOOD_LIMIT_MSG = "⏳ फ्लड सीमा। बाद में प्रयास करें।"
    COOKIES_FAILED_OPEN_BROWSER_MSG = "❌ ब्राउज़र कुकी मेनू खोलने में विफल"
    COOKIES_SAVE_AS_HINT_CLOSED_MSG = "कुकी के रूप में सहेजें संकेत बंद।"
    
    # Link command messages
    LINK_USAGE_MSG = "🔗 <b>उपयोग:</b>\n<code>/link [quality] URL</code>\n\n<b>उदाहरण:</b>\n<blockquote>• /link https://youtube.com/watch?v=... - सर्वोत्तम गुणवत्ता\n• /link 720 https://youtube.com/watch?v=... - 720p या कम\n• /link 720p https://youtube.com/watch?v=... - ऊपर के समान\n• /link 4k https://youtube.com/watch?v=... - 4K या कम\n• /link 8k https://youtube.com/watch?v=... - 8K या कम</blockquote>\n\n<b>गुणवत्ता:</b> 1 से 10000 तक (उदा., 144, 240, 720, 1080)"
    
    # Additional format command messages
    FORMAT_8K_QUALITY_MSG = "• <code>/format 8k</code> - 8K गुणवत्ता"
    
    # Additional link command messages
    LINK_DIRECT_LINK_OBTAINED_MSG = "🔗 <b>प्रत्यक्ष लिंक प्राप्त हुआ</b>\n\n"
    LINK_FORMAT_INFO_MSG = "🎛 <b>Format:</b> <code>{format_spec}</code>\n\n"
    LINK_AUDIO_STREAM_MSG = "🎵 <b>ऑडियो स्ट्रीम:</b>\n<blockquote expandable><a href=\"{audio_url}\">{audio_url}</a></blockquote>\n\n"
    LINK_FAILED_GET_STREAMS_MSG = "❌ स्ट्रीम लिंक प्राप्त करने में विफल"
    LINK_ERROR_GETTING_MSG = "❌ <b>लिंक प्राप्त करने में त्रुटि:</b>\n{error_msg}"
    
    # Additional cookies command messages (more)
    COOKIES_INVALID_YOUTUBE_INDEX_MSG = "❌ अमान्य YouTube कुकी इंडेक्स: {selected_index}। उपलब्ध रेंज 1-{total_urls} है"
    COOKIES_DOWNLOADING_CHECKING_MSG = "🔄 YouTube कुकीज़ डाउनलोड और जांच हो रही है...\n\nप्रयास {attempt} में से {total}"
    COOKIES_DOWNLOADING_TESTING_MSG = "🔄 YouTube कुकीज़ डाउनलोड और जांच हो रही है...\n\nप्रयास {attempt} में से {total}\n🔍 कुकीज़ परीक्षण..."
    COOKIES_SUCCESS_VALIDATED_MSG = "✅ YouTube कुकीज़ सफलतापूर्वक डाउनलोड और सत्यापित की गईं!\n\nस्रोत {source} में से {total} का उपयोग किया गया"
    COOKIES_ALL_EXPIRED_MSG = "❌ सभी YouTube कुकीज़ समाप्त हो गई हैं या अनुपलब्ध हैं!\n\nउन्हें बदलने के लिए बॉट व्यवस्थापक से संपर्क करें।"
    COOKIES_YOUTUBE_RETRY_LIMIT_EXCEEDED_MSG = "⚠️ YouTube कुकी रिट्राई सीमा पार हो गई!\n\n🔢 अधिकतम: {limit} प्रति घंटे प्रयास\n⏰ कृपया बाद में पुनः प्रयास करें"
    
    # Additional other command messages
    OTHER_TAG_ERROR_MSG = "❌ टैग #{wrong} में निषिद्ध वर्ण हैं। केवल अक्षर, अंक और _ की अनुमति है।\nकृपया उपयोग करें: {example}"
    
    # Additional subtitles command messages
    SUBS_INVALID_ARGUMENT_MSG = "❌ **अमान्य तर्क!**\n\n"
    SUBS_LANGUAGE_SET_STATUS_MSG = "✅ उपशीर्षक भाषा सेट की गई: {flag} {name}"
    
    # Additional subtitles command messages (more)
    SUBS_EXAMPLE_AUTO_MSG = "उदाहरण: `/subs en auto`"
    
    # Additional subtitles command messages (more more)
    SUBS_SELECTED_LANGUAGE_MSG = "{flag} चयनित भाषा: {name}{auto_text}"
    SUBS_ALWAYS_ASK_TOGGLE_MSG = "✅ हमेशा पूछें मोड {status}"
    
    # Additional subtitles menu messages
    SUBS_DISABLED_STATUS_MSG = "🚫 उपशीर्षक अक्षम हैं"
    SUBS_SETTINGS_MENU_MSG = "<b>💬 उपशीर्षक सेटिंग्स</b>\n\n{status_text}\n\nउपशीर्षक भाषा चुनें:\n\n"
    SUBS_SETTINGS_ADDITIONAL_MSG = "• <code>/subs off</code> - उपशीर्षक अक्षम करें\n"
    SUBS_AUTO_MENU_MSG = "<b>💬 उपशीर्षक सेटिंग्स</b>\n\n{status_text}\n\nउपशीर्षक भाषा चुनें:"
    
    # Additional link command messages (more)
    LINK_TITLE_MSG = "📹 <b>शीर्षक:</b> {title}\n"
    LINK_DURATION_MSG = "⏱ <b>अवधि:</b> {duration} सेकंड\n"
    LINK_VIDEO_STREAM_MSG = "🎬 <b>वीडियो स्ट्रीम:</b>\n<blockquote expandable><a href=\"{video_url}\">{video_url}</a></blockquote>\n\n"
    
    # Additional subtitles limitation messages
    SUBS_LIMITATIONS_MSG = "- 720p अधिकतम गुणवत्ता\n- 1.5 घंटे अधिकतम अवधि\n- 500mb अधिकतम वीडियो आकार</blockquote>\n\n"
    
    # Additional subtitles warning and command messages
    SUBS_WARNING_MSG = "<blockquote>❗️चेतावनी: उच्च CPU प्रभाव के कारण यह फ़ंक्शन बहुत धीमा है (लगभग रीयल-टाइम) और सीमित है:\n"
    SUBS_QUICK_COMMANDS_MSG = "<b>त्वरित कमांड:</b>\n"
    
    # Additional subtitles command description messages
    SUBS_DISABLE_COMMAND_MSG = "• `/subs off` - उपशीर्षक अक्षम करें\n"
    SUBS_ENABLE_ASK_MODE_MSG = "• `/subs on` - हमेशा पूछें मोड सक्षम करें\n"
    SUBS_SET_LANGUAGE_MSG = "• `/subs ru` - भाषा सेट करें\n"
    SUBS_SET_LANGUAGE_AUTO_MSG = "• `/subs ru auto` - AUTO/TRANS सक्षम के साथ भाषा सेट करें\n\n"
    SUBS_SET_LANGUAGE_CODE_MSG = "• <code>/subs on</code> - हमेशा पूछें मोड सक्षम करें\n"
    SUBS_AUTO_SUBS_TEXT = " (ऑटो-सब्स)"
    SUBS_AUTO_MODE_TOGGLE_MSG = "✅ Auto-subs mode {status}"
    
    # Subtitles log messages
    SUBS_DISABLED_LOG_MSG = "कमांड के माध्यम से सब्स अक्षम: {arg}"
    SUBS_ALWAYS_ASK_ENABLED_LOG_MSG = "कमांड के माध्यम से सब्स हमेशा पूछें सक्षम: {arg}"
    SUBS_LANGUAGE_SET_LOG_MSG = "कमांड के माध्यम से सब्स भाषा सेट: {arg}"
    SUBS_LANGUAGE_AUTO_SET_LOG_MSG = "उपशीर्षक भाषा + ऑटो मोड कमांड के माध्यम से सेट: {arg} auto"
    SUBS_MENU_OPENED_LOG_MSG = "उपयोगकर्ता ने /subs मेनू खोला।"
    SUBS_LANGUAGE_SET_CALLBACK_LOG_MSG = "उपयोगकर्ता ने उपशीर्षक भाषा सेट की: {lang_code}"
    SUBS_AUTO_MODE_TOGGLED_LOG_MSG = "उपयोगकर्ता ने AUTO/TRANS मोड टॉगल किया: {new_auto}"
    SUBS_ALWAYS_ASK_TOGGLED_LOG_MSG = "उपयोगकर्ता ने हमेशा पूछें मोड टॉगल किया: {new_always_ask}"
    
    # Cookies log messages
    COOKIES_BROWSER_REQUESTED_LOG_MSG = "उपयोगकर्ता ने ब्राउज़र से कुकीज़ का अनुरोध किया।"
    COOKIES_BROWSER_SELECTION_SENT_LOG_MSG = "केवल इंस्टॉल किए गए ब्राउज़रों के साथ ब्राउज़र चयन कीबोर्ड भेजा गया।"
    COOKIES_BROWSER_SELECTION_CLOSED_LOG_MSG = "ब्राउज़र चयन बंद।"
    COOKIES_FALLBACK_SUCCESS_LOG_MSG = "फॉलबैक COOKIE_URL सफलतापूर्वक उपयोग किया गया (स्रोत छिपा हुआ)"
    COOKIES_FALLBACK_FAILED_LOG_MSG = "फॉलबैक COOKIE_URL विफल: स्थिति={status} (छिपा हुआ)"
    COOKIES_FALLBACK_UNEXPECTED_ERROR_LOG_MSG = "फॉलबैक COOKIE_URL अप्रत्याशित त्रुटि: {error_type}: {error}"
    COOKIES_BROWSER_NOT_INSTALLED_LOG_MSG = "ब्राउज़र {browser} इंस्टॉल नहीं है।"
    COOKIES_SAVED_BROWSER_LOG_MSG = "ब्राउज़र का उपयोग करके कुकीज़ सहेजी गई: {browser}"
    COOKIES_FILE_SAVED_USER_LOG_MSG = "उपयोगकर्ता {user_id} के लिए कुकी फ़ाइल सहेजी गई।"
    COOKIES_FILE_WORKING_LOG_MSG = "कुकी फ़ाइल मौजूद है, सही प्रारूप है, और YouTube कुकीज़ काम कर रही हैं।"
    COOKIES_FILE_EXPIRED_LOG_MSG = "कुकी फ़ाइल मौजूद है और सही प्रारूप है, लेकिन YouTube कुकीज़ समाप्त हो गई हैं।"
    COOKIES_FILE_CORRECT_FORMAT_LOG_MSG = "कुकी फ़ाइल मौजूद है और सही प्रारूप है।"
    COOKIES_FILE_INCORRECT_FORMAT_LOG_MSG = "कुकी फ़ाइल मौजूद है लेकिन गलत प्रारूप है।"
    COOKIES_FILE_NOT_FOUND_LOG_MSG = "कुकी फ़ाइल नहीं मिली।"
    COOKIES_SERVICE_URL_EMPTY_LOG_MSG = "उपयोगकर्ता {user_id} के लिए {service} कुकी URL खाली है।"
    COOKIES_SERVICE_URL_NOT_TXT_LOG_MSG = "{service} कुकी URL .txt नहीं है (छिपा हुआ)"
    COOKIES_SERVICE_FILE_TOO_LARGE_LOG_MSG = "{service} कुकी फ़ाइल बहुत बड़ी: {size} बाइट्स (स्रोत छिपा हुआ)"
    COOKIES_SERVICE_FILE_DOWNLOADED_LOG_MSG = "उपयोगकर्ता {user_id} के लिए {service} कुकी फ़ाइल डाउनलोड की गई (स्रोत छिपा हुआ)।"
    
    # Admin log messages
    ADMIN_SCRIPT_NOT_FOUND_LOG_MSG = "स्क्रिप्ट नहीं मिली: {script_path}"
    ADMIN_FAILED_SEND_STATUS_LOG_MSG = "प्रारंभिक स्थिति संदेश भेजने में विफल"
    ADMIN_ERROR_RUNNING_SCRIPT_LOG_MSG = "{script_path} चलाने में त्रुटि: {stdout}\n{stderr}"
    ADMIN_CACHE_RELOADED_AUTO_LOG_MSG = "ऑटो टास्क द्वारा Firebase कैश रीलोड किया गया।"
    ADMIN_CACHE_RELOADED_ADMIN_LOG_MSG = "व्यवस्थापक द्वारा Firebase कैश रीलोड किया गया।"
    ADMIN_ERROR_RELOADING_CACHE_LOG_MSG = "Firebase कैश रीलोड करने में त्रुटि: {error}"
    ADMIN_BROADCAST_INITIATED_LOG_MSG = "ब्रॉडकास्ट शुरू किया गया। टेक्स्ट:\n{broadcast_text}"
    ADMIN_BROADCAST_SENT_LOG_MSG = "सभी उपयोगकर्ताओं को ब्रॉडकास्ट संदेश भेजा गया।"
    ADMIN_BROADCAST_FAILED_LOG_MSG = "ब्रॉडकास्ट संदेश भेजने में विफल: {error}"
    ADMIN_CACHE_CLEARED_LOG_MSG = "व्यवस्थापक {user_id} ने URL के लिए कैश साफ़ किया: {url}"
    ADMIN_PORN_UPDATE_STARTED_LOG_MSG = "व्यवस्थापक {user_id} ने पोर्न सूची अपडेट स्क्रिप्ट शुरू की: {script_path}"
    ADMIN_PORN_UPDATE_COMPLETED_LOG_MSG = "व्यवस्थापक {user_id} द्वारा पोर्न सूची अपडेट स्क्रिप्ट सफलतापूर्वक पूर्ण"
    ADMIN_PORN_UPDATE_FAILED_LOG_MSG = "व्यवस्थापक {user_id} द्वारा पोर्न सूची अपडेट स्क्रिप्ट विफल: {error}"
    ADMIN_SCRIPT_NOT_FOUND_LOG_MSG = "व्यवस्थापक {user_id} ने अस्तित्वहीन स्क्रिप्ट चलाने का प्रयास किया: {script_path}"
    ADMIN_PORN_UPDATE_ERROR_LOG_MSG = "व्यवस्थापक {user_id} द्वारा पोर्न अपडेट स्क्रिप्ट चलाने में त्रुटि: {error}"
    ADMIN_PORN_CACHE_RELOAD_STARTED_LOG_MSG = "व्यवस्थापक {user_id} ने पोर्न कैश रीलोड शुरू किया"
    ADMIN_PORN_CACHE_RELOAD_ERROR_LOG_MSG = "व्यवस्थापक {user_id} द्वारा पोर्न कैश रीलोड करने में त्रुटि: {error}"
    ADMIN_PORN_CHECK_LOG_MSG = "व्यवस्थापक {user_id} ने NSFW के लिए URL जांचा: {url} - परिणाम: {status}"
    
    # Format log messages
    FORMAT_CHANGE_REQUESTED_LOG_MSG = "उपयोगकर्ता ने प्रारूप परिवर्तन का अनुरोध किया।"
    FORMAT_ALWAYS_ASK_SET_LOG_MSG = "प्रारूप ALWAYS_ASK पर सेट किया गया।"
    FORMAT_UPDATED_BEST_LOG_MSG = "प्रारूप सर्वोत्तम पर अपडेट किया गया: {format}"
    FORMAT_UPDATED_ID_LOG_MSG = "प्रारूप ID {format_id} पर अपडेट किया गया: {format}"
    FORMAT_UPDATED_ID_AUDIO_LOG_MSG = "प्रारूप ID {format_id} (केवल-ऑडियो) पर अपडेट किया गया: {format}"
    FORMAT_UPDATED_QUALITY_LOG_MSG = "प्रारूप गुणवत्ता {quality} पर अपडेट किया गया: {format}"
    FORMAT_UPDATED_CUSTOM_LOG_MSG = "प्रारूप अपडेट किया गया: {format}"
    FORMAT_MENU_SENT_LOG_MSG = "प्रारूप मेनू भेजा गया।"
    FORMAT_SELECTION_CLOSED_LOG_MSG = "प्रारूप चयन बंद।"
    FORMAT_CUSTOM_HINT_SENT_LOG_MSG = "कस्टम प्रारूप संकेत भेजा गया।"
    FORMAT_RESOLUTION_MENU_SENT_LOG_MSG = "प्रारूप रिजॉल्यूशन मेनू भेजा गया।"
    FORMAT_RETURNED_MAIN_MENU_LOG_MSG = "मुख्य प्रारूप मेनू पर वापस आए।"
    FORMAT_UPDATED_CALLBACK_LOG_MSG = "प्रारूप अपडेट किया गया: {format}"
    FORMAT_ALWAYS_ASK_SET_CALLBACK_LOG_MSG = "प्रारूप ALWAYS_ASK पर सेट किया गया।"
    FORMAT_CODEC_SET_LOG_MSG = "कोडेक प्राथमिकता {codec} पर सेट की गई"
    FORMAT_CUSTOM_MENU_CLOSED_LOG_MSG = "कस्टम प्रारूप मेनू बंद"
    
    # Link log messages
    LINK_EXTRACTED_LOG_MSG = "उपयोगकर्ता {user_id} के लिए {url} से डायरेक्ट लिंक निकाला गया"
    LINK_EXTRACTION_FAILED_LOG_MSG = "उपयोगकर्ता {user_id} के लिए {url} से डायरेक्ट लिंक निकालने में विफल: {error}"
    LINK_COMMAND_ERROR_LOG_MSG = "उपयोगकर्ता {user_id} के लिए लिंक कमांड में त्रुटि: {error}"
    
    # Keyboard log messages
    KEYBOARD_SET_LOG_MSG = "उपयोगकर्ता {user_id} ने कीबोर्ड {setting} पर सेट किया"
    KEYBOARD_SET_CALLBACK_LOG_MSG = "उपयोगकर्ता {user_id} ने कीबोर्ड {setting} पर सेट किया"
    
    # MediaInfo log messages
    MEDIAINFO_SET_COMMAND_LOG_MSG = "MediaInfo कमांड के माध्यम से सेट किया गया: {arg}"
    MEDIAINFO_MENU_OPENED_LOG_MSG = "उपयोगकर्ता ने /mediainfo मेनू खोला।"
    MEDIAINFO_MENU_CLOSED_LOG_MSG = "MediaInfo: बंद।"
    MEDIAINFO_ENABLED_LOG_MSG = "MediaInfo सक्षम।"
    MEDIAINFO_DISABLED_LOG_MSG = "MediaInfo अक्षम।"
    
    # Split log messages
    SPLIT_SIZE_SET_ARGUMENT_LOG_MSG = "तर्क के माध्यम से विभाजन आकार {size} बाइट्स पर सेट किया गया।"
    SPLIT_MENU_OPENED_LOG_MSG = "उपयोगकर्ता ने /split मेनू खोला।"
    SPLIT_SELECTION_CLOSED_LOG_MSG = "विभाजन चयन बंद।"
    SPLIT_SIZE_SET_CALLBACK_LOG_MSG = "विभाजन आकार {size} बाइट्स पर सेट किया गया।"
    
    # Proxy log messages
    PROXY_SET_COMMAND_LOG_MSG = "प्रॉक्सी कमांड के माध्यम से सेट की गई: {arg}"
    PROXY_MENU_OPENED_LOG_MSG = "उपयोगकर्ता ने /proxy मेनू खोला।"
    PROXY_MENU_CLOSED_LOG_MSG = "प्रॉक्सी: बंद।"
    PROXY_ENABLED_LOG_MSG = "प्रॉक्सी सक्षम।"
    PROXY_DISABLED_LOG_MSG = "प्रॉक्सी अक्षम।"
    
    # Other handlers log messages
    HELP_MESSAGE_CLOSED_LOG_MSG = "सहायता संदेश बंद।"
    AUDIO_HELP_SHOWN_LOG_MSG = "/audio मदद दिखाई गई"
    PLAYLIST_HELP_REQUESTED_LOG_MSG = "उपयोगकर्ता ने प्लेलिस्ट सहायता का अनुरोध किया।"
    PLAYLIST_HELP_CLOSED_LOG_MSG = "प्लेलिस्ट सहायता बंद।"
    AUDIO_HINT_CLOSED_LOG_MSG = "ऑडियो संकेत बंद।"
    
    # Down and Up log messages
    DIRECT_LINK_MENU_CREATED_LOG_MSG = "उपयोगकर्ता {user_id} के लिए LINK बटन के माध्यम से {url} से डायरेक्ट लिंक मेनू बनाया गया"
    DIRECT_LINK_EXTRACTION_FAILED_LOG_MSG = "उपयोगकर्ता {user_id} के लिए LINK बटन के माध्यम से {url} से डायरेक्ट लिंक निकालने में विफल: {error}"
    LIST_COMMAND_EXECUTED_LOG_MSG = "उपयोगकर्ता {user_id} के लिए LIST कमांड निष्पादित, url: {url}"
    QUICK_EMBED_LOG_MSG = "त्वरित एम्बेड: {embed_url}"
    ALWAYS_ASK_MENU_SENT_LOG_MSG = "{url} के लिए हमेशा पूछें मेनू भेजा गया"
    CACHED_QUALITIES_MENU_CREATED_LOG_MSG = "त्रुटि के बाद उपयोगकर्ता {user_id} के लिए कैश किए गए गुणवत्ता मेनू बनाया गया: {error}"
    ALWAYS_ASK_MENU_ERROR_LOG_MSG = "{url} के लिए हमेशा पूछें मेनू त्रुटि: {error}"
    ALWAYS_ASK_FORMAT_FIXED_VIA_ARGS_MSG = "प्रारूप /args सेटिंग्स के माध्यम से निश्चित है"
    ALWAYS_ASK_AUDIO_TYPE_MSG = "ऑडियो"
    ALWAYS_ASK_VIDEO_TYPE_MSG = "वीडियो"
    ALWAYS_ASK_VIDEO_TITLE_MSG = "वीडियो"
    ALWAYS_ASK_NEXT_BUTTON_MSG = "अगला ▶️"
    ALWAYS_ASK_PREV_BUTTON_MSG = "◀️ पिछला"
    SUBTITLES_NEXT_BUTTON_MSG = "अगला ➡️"
    PORN_ALL_TEXT_FIELDS_EMPTY_MSG = "ℹ️ सभी टेक्स्ट फील्ड खाली हैं"
    SENDER_VIDEO_DURATION_MSG = "वीडियो अवधि:"
    SENDER_UPLOADING_FILE_MSG = "📤 फाइल अपलोड हो रही है..."
    SENDER_UPLOADING_VIDEO_MSG = "📤 वीडियो अपलोड हो रहा है..."
    DOWN_UP_VIDEO_DURATION_MSG = "🎞 वीडियो अवधि:"
    DOWN_UP_ONE_FILE_UPLOADED_MSG = "1 फाइल अपलोड की गई।"
    DOWN_UP_VIDEO_INFO_MSG = "📋 वीडियो जानकारी"
    DOWN_UP_NUMBER_MSG = "संख्या"
    DOWN_UP_TITLE_MSG = "शीर्षक"
    DOWN_UP_ID_MSG = "आईडी"
    DOWN_UP_DOWNLOADED_VIDEO_MSG = "☑️ वीडियो डाउनलोड किया गया।"
    DOWN_UP_PROCESSING_UPLOAD_MSG = "📤 अपलोड के लिए प्रसंस्करण..."
    DOWN_UP_SPLITTED_PART_UPLOADED_MSG = "📤 विभाजित भाग {part} फाइल अपलोड की गई"
    DOWN_UP_UPLOAD_COMPLETE_MSG = "✅ अपलोड पूर्ण"
    DOWN_UP_FILES_UPLOADED_MSG = "फाइलें अपलोड की गईं"
    
    # Always Ask Menu Button Messages
    ALWAYS_ASK_VLC_ANDROID_BUTTON_MSG = "🎬 VLC (Android)"
    ALWAYS_ASK_CLOSE_BUTTON_MSG = "🔚 बंद करें"
    ALWAYS_ASK_CODEC_BUTTON_MSG = "📼कोडेक"
    ALWAYS_ASK_DUBS_BUTTON_MSG = "🗣 डब्स"
    ALWAYS_ASK_SUBS_BUTTON_MSG = "💬 सब्स"
    ALWAYS_ASK_BROWSER_BUTTON_MSG = "🌐 ब्राउज़र"
    ALWAYS_ASK_VLC_IOS_BUTTON_MSG = "🎬 VLC (iOS)"
    
    # Always Ask Menu Callback Messages
    ALWAYS_ASK_GETTING_DIRECT_LINK_MSG = "🔗 डायरेक्ट लिंक प्राप्त कर रहे हैं..."
    ALWAYS_ASK_GETTING_FORMATS_MSG = "📃 उपलब्ध प्रारूप प्राप्त कर रहे हैं..."
    ALWAYS_ASK_STARTING_GALLERY_DL_MSG = "🖼 गैलरी-डीएल शुरू कर रहे हैं…"
    
    # Always Ask Menu F-String Messages
    ALWAYS_ASK_DURATION_MSG = "⏱ <b>अवधि:</b>"
    ALWAYS_ASK_FORMAT_MSG = "🎛 <b>प्रारूप:</b>"
    ALWAYS_ASK_BROWSER_MSG = "🌐 <b>ब्राउज़र:</b> वेब ब्राउज़र में खोलें"
    ALWAYS_ASK_AVAILABLE_FORMATS_FOR_MSG = "के लिए उपलब्ध प्रारूप"
    ALWAYS_ASK_HOW_TO_USE_FORMAT_IDS_MSG = "💡 प्रारूप ID का उपयोग कैसे करें:"
    ALWAYS_ASK_AFTER_GETTING_LIST_MSG = "सूची प्राप्त करने के बाद, विशिष्ट प्रारूप ID का उपयोग करें:"
    ALWAYS_ASK_FORMAT_ID_401_MSG = "• /format id 401 - प्रारूप 401 डाउनलोड करें"
    ALWAYS_ASK_FORMAT_ID401_MSG = "• /format id401 - ऊपर के समान"
    ALWAYS_ASK_FORMAT_ID_140_AUDIO_MSG = "• /format id 140 audio - प्रारूप 140 को MP3 ऑडियो के रूप में डाउनलोड करें"
    ALWAYS_ASK_AUDIO_ONLY_FORMATS_DETECTED_MSG = "🎵 केवल-ऑडियो प्रारूप मिला"
    ALWAYS_ASK_THESE_FORMATS_MP3_MSG = "ये प्रारूप MP3 ऑडियो फ़ाइलों के रूप में डाउनलोड होंगे।"
    ALWAYS_ASK_HOW_TO_SET_FORMAT_MSG = "💡 <b>प्रारूप कैसे सेट करें:</b>"
    ALWAYS_ASK_FORMAT_ID_134_MSG = "• <code>/format id 134</code> - विशिष्ट प्रारूप ID डाउनलोड करें"
    ALWAYS_ASK_FORMAT_720P_MSG = "• <code>/format 720p</code> - गुणवत्ता के अनुसार डाउनलोड करें"
    ALWAYS_ASK_FORMAT_BEST_MSG = "• <code>/format best</code> - सर्वोत्तम गुणवत्ता डाउनलोड करें"
    ALWAYS_ASK_FORMAT_ASK_MSG = "• <code>/format ask</code> - हमेशा गुणवत्ता के लिए पूछें"
    ALWAYS_ASK_AUDIO_ONLY_FORMATS_MSG = "🎵 <b>केवल-ऑडियो प्रारूप:</b>"
    ALWAYS_ASK_FORMAT_ID_140_AUDIO_CAPTION_MSG = "• <code>/format id 140 audio</code> - प्रारूप 140 को MP3 ऑडियो के रूप में डाउनलोड करें"
    ALWAYS_ASK_THESE_WILL_BE_MP3_MSG = "ये MP3 ऑडियो फ़ाइलों के रूप में डाउनलोड होंगे।"
    ALWAYS_ASK_USE_FORMAT_ID_MSG = "📋 ऊपर की सूची से प्रारूप ID का उपयोग करें"
    ALWAYS_ASK_ERROR_ORIGINAL_MESSAGE_NOT_FOUND_MSG = "❌ त्रुटि: मूल संदेश नहीं मिला।"
    ALWAYS_ASK_FORMATS_PAGE_MSG = "प्रारूप पृष्ठ"
    ALWAYS_ASK_ERROR_SHOWING_FORMATS_MENU_MSG = "❌ प्रारूप मेनू दिखाने में त्रुटि"
    ALWAYS_ASK_ERROR_GETTING_FORMATS_MSG = "❌ प्रारूप प्राप्त करने में त्रुटि"
    ALWAYS_ASK_ERROR_GETTING_AVAILABLE_FORMATS_MSG = "❌ उपलब्ध प्रारूप प्राप्त करने में त्रुटि।"
    ALWAYS_ASK_PLEASE_TRY_AGAIN_LATER_MSG = "कृपया बाद में पुनः प्रयास करें।"
    ALWAYS_ASK_YTDLP_CANNOT_PROCESS_MSG = "🔄 <b>yt-dlp इस सामग्री को प्रोसेस नहीं कर सकता"
    ALWAYS_ASK_SYSTEM_RECOMMENDS_GALLERY_DL_MSG = "सिस्टम इसके बजाय gallery-dl का उपयोग करने की सिफारिश करता है।"
    ALWAYS_ASK_OPTIONS_MSG = "**विकल्प:**"
    ALWAYS_ASK_FOR_IMAGE_GALLERIES_MSG = "• छवि गैलरी के लिए: <code>/img 1-10</code>"
    ALWAYS_ASK_FOR_SINGLE_IMAGES_MSG = "• एकल छवियों के लिए: <code>/img</code>"
    ALWAYS_ASK_GALLERY_DL_WORKS_BETTER_MSG = "Gallery-dl अक्सर Instagram, Twitter और अन्य सोशल मीडिया सामग्री के लिए बेहतर काम करता है।"
    ALWAYS_ASK_TRY_GALLERY_DL_BUTTON_MSG = "🖼 Gallery-dl कोशिश करें"
    ALWAYS_ASK_FORMAT_FIXED_VIA_ARGS_MSG = "🔒 /args के माध्यम से प्रारूप निश्चित"
    ALWAYS_ASK_SUBTITLES_MSG = "🔤 उपशीर्षक"
    ALWAYS_ASK_DUBBED_AUDIO_MSG = "🎧 डब किया गया ऑडियो"
    ALWAYS_ASK_SUBTITLES_ARE_AVAILABLE_MSG = "💬 — उपशीर्षक उपलब्ध हैं"
    ALWAYS_ASK_CHOOSE_SUBTITLE_LANGUAGE_MSG = "💬 — उपशीर्षक भाषा चुनें"
    ALWAYS_ASK_SUBS_NOT_FOUND_MSG = "⚠️ उपशीर्षक नहीं मिला और एम्बेड नहीं होगा"
    ALWAYS_ASK_INSTANT_REPOST_MSG = "🚀 — कैश से तुरंत रीपोस्ट"
    ALWAYS_ASK_CHOOSE_AUDIO_LANGUAGE_MSG = "🗣 — ऑडियो भाषा चुनें"
    ALWAYS_ASK_NSFW_IS_PAID_MSG = "⭐️ — 🔞NSFW पेड है (⭐️$0.02)"
    ALWAYS_ASK_CHOOSE_DOWNLOAD_QUALITY_MSG = "📹 — डाउनलोड गुणवत्ता चुनें"
    ALWAYS_ASK_DOWNLOAD_IMAGE_MSG = "🖼 — छवि डाउनलोड करें (gallery-dl)"
    ALWAYS_ASK_WATCH_VIDEO_MSG = "👁 — poketube में वीडियो देखें"
    ALWAYS_ASK_GET_DIRECT_LINK_MSG = "🔗 — वीडियो के लिए प्रत्यक्ष लिंक प्राप्त करें"
    ALWAYS_ASK_SHOW_AVAILABLE_FORMATS_MSG = "📃 — उपलब्ध प्रारूप सूची दिखाएं"
    ALWAYS_ASK_CHANGE_VIDEO_EXT_MSG = "📼 — वीडियो एक्सटेंशन/कोडेक बदलें"
    ALWAYS_ASK_EMBED_BUTTON_MSG = "🚀एम्बेड"
    ALWAYS_ASK_EXTRACT_AUDIO_MSG = "🎧 — केवल ऑडियो निकालें"
    ALWAYS_ASK_NSFW_PAID_MSG = "⭐️ — 🔞NSFW भुगतान योग्य है (⭐️$0.02)"
    ALWAYS_ASK_INSTANT_REPOST_MSG = "🚀 — कैश से तत्काल रिपोस्ट"
    ALWAYS_ASK_WATCH_VIDEO_MSG = "👁 — poketube में वीडियो देखें"
    ALWAYS_ASK_CHOOSE_AUDIO_LANGUAGE_MSG = "🗣 — ऑडियो भाषा चुनें"
    ALWAYS_ASK_BEST_BUTTON_MSG = "सर्वोत्तम"
    ALWAYS_ASK_OTHER_LABEL_MSG = "🎛अन्य"
    ALWAYS_ASK_SUB_ONLY_BUTTON_MSG = "📝केवल उपशीर्षक"
    ALWAYS_ASK_SMART_GROUPING_MSG = "स्मार्ट ग्रुपिंग"
    ALWAYS_ASK_ADDED_ACTION_BUTTON_ROW_3_MSG = "एक्शन बटन पंक्ति जोड़ी गई (3)"
    ALWAYS_ASK_ADDED_ACTION_BUTTON_ROWS_2_2_MSG = "एक्शन बटन पंक्तियां जोड़ी गईं (2+2)"
    ALWAYS_ASK_ADDED_BOTTOM_BUTTONS_TO_EXISTING_ROW_MSG = "मौजूदा पंक्ति में निचले बटन जोड़े गए"
    ALWAYS_ASK_CREATED_NEW_BOTTOM_ROW_MSG = "नई निचली पंक्ति बनाई गई"
    ALWAYS_ASK_NO_VIDEOS_FOUND_IN_PLAYLIST_MSG = "प्लेलिस्ट में कोई वीडियो नहीं मिला"
    ALWAYS_ASK_UNSUPPORTED_URL_MSG = "असमर्थित URL"
    ALWAYS_ASK_NO_VIDEO_COULD_BE_FOUND_MSG = "कोई वीडियो नहीं मिल सका"
    ALWAYS_ASK_NO_VIDEO_FOUND_MSG = "कोई वीडियो नहीं मिला"
    ALWAYS_ASK_NO_MEDIA_FOUND_MSG = "कोई मीडिया नहीं मिली"
    ALWAYS_ASK_THIS_TWEET_DOES_NOT_CONTAIN_MSG = "यह ट्वीट शामिल नहीं है"
    ALWAYS_ASK_ERROR_RETRIEVING_VIDEO_INFO_MSG = "❌ <b>वीडियो जानकारी प्राप्त करने में त्रुटि:</b>"
    ALWAYS_ASK_ERROR_RETRIEVING_VIDEO_INFO_SHORT_MSG = "वीडियो जानकारी प्राप्त करने में त्रुटि"
    ALWAYS_ASK_TRY_CLEAN_COMMAND_MSG = "<code>/clean</code> कमांड आज़माएं और फिर से कोशिश करें। यदि त्रुटि बनी रहती है, तो YouTube को प्राधिकरण की आवश्यकता है। <code>/cookie</code> या <code>/cookies_from_browser</code> के माध्यम से cookies.txt को अपडेट करें और फिर से कोशिश करें।"
    ALWAYS_ASK_MENU_CLOSED_MSG = "मेनू बंद।"
    ALWAYS_ASK_MANUAL_QUALITY_SELECTION_MSG = "🎛 मैनुअल गुणवत्ता चयन"
    ALWAYS_ASK_CHOOSE_QUALITY_MANUALLY_MSG = "स्वचालित पहचान विफल होने के कारण मैनुअल रूप से गुणवत्ता चुनें:"
    ALWAYS_ASK_ALL_AVAILABLE_FORMATS_MSG = "🎛 सभी उपलब्ध प्रारूप"
    ALWAYS_ASK_AVAILABLE_QUALITIES_FROM_CACHE_MSG = "📹 उपलब्ध गुणवत्ताएं (कैश से)"
    ALWAYS_ASK_USING_CACHED_QUALITIES_MSG = "⚠️ कैश की गई गुणवत्ताओं का उपयोग - नए प्रारूप उपलब्ध नहीं हो सकते"
    ALWAYS_ASK_DOWNLOADING_FORMAT_MSG = "📥 प्रारूप डाउनलोड हो रहा है"
    ALWAYS_ASK_DOWNLOADING_QUALITY_MSG = "📥 डाउनलोड हो रहा है"
    ALWAYS_ASK_DOWNLOADING_HLS_MSG = "📥 प्रगति ट्रैकिंग के साथ डाउनलोड हो रहा है..."
    ALWAYS_ASK_DOWNLOADING_FORMAT_USING_MSG = "📥 प्रारूप का उपयोग करके डाउनलोड �