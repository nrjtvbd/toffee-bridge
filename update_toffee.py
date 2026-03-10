import requests
import re

def get_toffee_cookie():
    # আপনার দেওয়া নির্দিষ্ট ইউজার এজেন্ট
    ua = "Mozilla/5.0 (Linux; Android 9; Redmi S2 Build/PKQ1.181203.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.7049.79 Mobile Safari/537.36"
    url = "https://toffeelive.com/en/watch/sony-sports-ten-1-hd/py5j-JQBv9knK3AHxDTY"
    
    headers = {
        "User-Agent": ua,
        "Referer": "https://toffeelive.com/",
        "Origin": "https://toffeelive.com"
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=15)
        cookie_header = response.headers.get('Set-Cookie', '')
        # সঠিক কুকিটি খুঁজে বের করা
        match = re.search(r'(Edge-Cache-Cookie=[^;]+)', cookie_header)
        if match:
            return match.group(1)
    except:
        return None
    return None

def update_playlist():
    fresh_cookie = get_toffee_cookie()
    
    # যদি কুকি না পাওয়া যায়, তবে স্ক্রিপ্ট এখানে থেমে যাবে যাতে ভুল ডাটা আপডেট না হয়
    if not fresh_cookie:
        print("Error: Could not fetch fresh cookie from Toffee!")
        return

    ua = "Mozilla/5.0 (Linux; Android 9; Redmi S2 Build/PKQ1.181203.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.7049.79 Mobile Safari/537.36"
    
    channels = [
        {"name": "Sony Sports 1 HD", "id": "sony_sports_1_hd"},
        {"name": "Sony Sports 2 HD", "id": "sony_sports_2_hd"},
        {"name": "T-Sports HD", "id": "tsports_hd"}
    ]

    m3u_content = "#EXTM3U\n"
    for ch in channels:
        stream_url = f"https://bldcmprod-cdn.toffeelive.com/cdn/live/{ch['id']}/playlist.m3u8"
        
        m3u_content += f'#EXTINF:-1, {ch["name"]}\n'
        m3u_content += f'#EXTVLCOPT:http-user-agent={ua}\n'
        m3u_content += f'#EXTVLCOPT:http-cookie={fresh_cookie}\n'
        m3u_content += f'#EXTHTTP:{{"cookie":"{fresh_cookie}", "user-agent":"{ua}"}}\n'
        m3u_content += f'{stream_url}\n'

    with open("Toffee.m3u", "w", encoding="utf-8") as f:
        f.write(m3u_content)
    print("Playlist successfully updated with fresh cookie!")

if __name__ == "__main__":
    update_playlist()
