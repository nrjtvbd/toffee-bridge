import requests
import re

def get_toffee_cookie():
    # আপনার দেওয়া রেডমি এস২ ইউজার এজেন্ট
    ua = "Mozilla/5.0 (Linux; Android 9; Redmi S2 Build/PKQ1.181203.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.7049.79 Mobile Safari/537.36"
    
    url = "https://toffeelive.com/en/watch/sony-sports-ten-1-hd/py5j-JQBv9knK3AHxDTY"
    headers = {"User-Agent": ua}
    
    try:
        response = requests.get(url, headers=headers, timeout=15)
        cookie = response.headers.get('Set-Cookie', '')
        match = re.search(r'(Edge-Cache-Cookie=[^;]+)', cookie)
        return match.group(1) if match else None
    except:
        return None

def update_playlist():
    cookie = get_toffee_cookie()
    # যদি স্ক্র্যাপার কাজ না করে তবে ব্যাকআপ কুকি (এখানে আপনার নতুন কুকিটি বসিয়ে দিবেন)
    if not cookie:
        cookie = "Edge-Cache-Cookie=... (আপনার ম্যানুয়াল কুকি)"

    ua = "Mozilla/5.0 (Linux; Android 9; Redmi S2 Build/PKQ1.181203.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.7049.79 Mobile Safari/537.36"
    
    channels = [
        {"name": "Sony Sports 1 HD", "id": "sony_sports_1_hd"},
        {"name": "Sony Sports 2 HD", "id": "sony_sports_2_hd"},
        {"name": "T-Sports HD", "id": "tsports_hd"}
    ]

    m3u_content = "#EXTM3U\n"
    for ch in channels:
        url = f"https://bldcmprod-cdn.toffeelive.com/cdn/live/{ch['id']}/playlist.m3u8"
        m3u_content += f'#EXTINF:-1, {ch["name"]}\n'
        m3u_content += f'#EXTVLCOPT:http-user-agent={ua}\n' # VLC-র জন্য ফিক্সড UA
        m3u_content += f'#EXTVLCOPT:http-cookie={cookie}\n'
        m3u_content += f'#EXTHTTP:{{"cookie":"{cookie}", "user-agent":"{ua}"}}\n'
        m3u_content += f'{url}\n'

    with open("Toffee.m3u", "w", encoding="utf-8") as f:
        f.write(m3u_content)

if __name__ == "__main__":
    update_playlist()
