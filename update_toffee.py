import requests
import re

def get_toffee_cookie():
    url = "https://toffeelive.com/en/watch/sony-sports-ten-1-hd/py5j-JQBv9knK3AHxDTY"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    try:
        response = requests.get(url, headers=headers, timeout=15)
        # সেট-কুকি হেডার থেকে কুকি খুঁজে বের করা
        cookie = response.headers.get('Set-Cookie', '')
        match = re.search(r'(Edge-Cache-Cookie=[^;]+)', cookie)
        return match.group(1) if match else None
    except:
        return None

def update_playlist():
    cookie = get_toffee_cookie()
    if not cookie:
        print("Failed to get fresh cookie.")
        return

    ua = "Mozilla/5.0 (Linux; Android 10; SM-G981B) AppleWebKit/537.36"
    channels = [
        {"name": "Sony Sports 1 HD", "id": "sony_sports_1_hd"},
        {"name": "Sony Sports 2 HD", "id": "sony_sports_2_hd"},
        {"name": "T-Sports HD", "id": "tsports_hd"}
    ]

    m3u_content = "#EXTM3U\n"
    for ch in channels:
        url = f"https://bldcmprod-cdn.toffeelive.com/cdn/live/{ch['id']}/playlist.m3u8"
        # VLC এবং libvlc এর জন্য সরাসরি হেডার ইনজেকশন
        m3u_content += f'#EXTINF:-1, {ch["name"]}\n'
        m3u_content += f'#EXTVLCOPT:http-user-agent={ua}\n'
        m3u_content += f'#EXTVLCOPT:http-cookie={cookie}\n'
        m3u_content += f'{url}\n'

    with open("Toffee.m3u", "w", encoding="utf-8") as f:
        f.write(m3u_content)
    print("Playlist Updated with fresh cookie!")

if __name__ == "__main__":
    update_playlist()
