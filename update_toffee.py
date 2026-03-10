import requests
import json

def get_toffee_cookie():
    # এই ফাংশনটি অটোমেটিক নতুন কুকি জেনারেট করার চেষ্টা করবে
    try:
        url = "https://toffeelive.com/en/watch/sony-sports-ten-1-hd/py5j-JQBv9knK3AHxDTY"
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
        response = requests.get(url, headers=headers, timeout=10)
        cookie = response.headers.get('Set-Cookie', '')
        return cookie
    except:
        return ""

def generate_playlist():
    # আপনার অ্যাপের জন্য সঠিক ইউজার এজেন্ট
    USER_AGENT = "Mozilla/5.0 (Linux; Android 10; SM-G981B) AppleWebKit/537.36"
    COOKIE = get_toffee_cookie() # অথবা আপনার লেটেস্ট কাজ করা কুকিটি ম্যানুয়ালি দিন

    channels = [
        {"name": "Sony Sports 1 HD", "id": "sony_sports_1_hd"},
        {"name": "Sony Sports 2 HD", "id": "sony_sports_2_hd"},
        {"name": "T-Sports HD", "id": "tsports_hd"}
    ]

    m3u_content = "#EXTM3U\n"
    for ch in channels:
        url = f"https://bldcmprod-cdn.toffeelive.com/cdn/live/{ch['id']}/playlist.m3u8"
        # libvlc এবং VLC-র জন্য নিচের এই বিশেষ ফরম্যাটটি ব্যবহার করুন
        m3u_content += f'#EXTINF:-1, {ch["name"]}\n'
        m3u_content += f'#EXTVLCOPT:http-user-agent={USER_AGENT}\n'
        m3u_content += f'#EXTVLCOPT:http-cookie={COOKIE}\n'
        m3u_content += f'#EXTHTTP:{{"cookie":"{COOKIE}", "user-agent":"{USER_AGENT}"}}\n'
        m3u_content += f'{url}\n'

    with open("Toffee.m3u", "w", encoding="utf-8") as f:
        f.write(m3u_content)

if __name__ == "__main__":
    generate_playlist()
