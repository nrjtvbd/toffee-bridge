import requests
import re
import os

def get_toffee_cookie():
    # আপনার নির্দিষ্ট Redmi S2 ইউজার এজেন্ট
    ua = "Mozilla/5.0 (Linux; Android 9; Redmi S2 Build/PKQ1.181203.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.7049.79 Mobile Safari/537.36"
    url = "https://toffeelive.com/en/watch/sony-sports-ten-1-hd/py5j-JQBv9knK3AHxDTY"
    
    try:
        response = requests.get(url, headers={"User-Agent": ua}, timeout=10)
        cookie_header = response.headers.get('Set-Cookie', '')
        match = re.search(r'(Edge-Cache-Cookie=[^;]+)', cookie_header)
        if match:
            return match.group(1)
    except:
        return None
    return None

def update_playlist():
    # ১. প্রথমে অটোমেটিক চেষ্টা করবে
    cookie = get_toffee_cookie()
    
    # ২. অটোমেটিক না পারলে নিচে আপনার কাছে থাকা সচল কুকিটি বসান (Signature সহ অংশটি)
    if not cookie:
        print("Automatic scraping failed, using manual backup cookie.")
        cookie = "Edge-Cache-Cookie=URLPrefix=aHR0cHM6Ly9ibGRjbXByb2QtY2RuLnRvZmZlZWxpdmUuY29t:Expires=1773337747:KeyName=prod_linear:Signature=MhJ3pv26Yjf2jrmWtCQt1rvo-3MmYPgtFotZQFEc_IUKBbDdjDlKVXL9UDEuy-DOaPm4HH_MkKC6OqA1UYX0Aw"

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
        m3u_content += f'#EXTVLCOPT:http-cookie={cookie}\n'
        m3u_content += f'#EXTHTTP:{{"cookie":"{cookie}", "user-agent":"{ua}"}}\n'
        m3u_content += f'{stream_url}\n'

    with open("Toffee.m3u", "w", encoding="utf-8") as f:
        f.write(m3u_content)
    print("Toffee.m3u file has been updated!")

if __name__ == "__main__":
    update_playlist()
