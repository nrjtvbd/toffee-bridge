import requests
import re

def get_automatic_cookie():
    # Amra ekta specific API endpoint ba mobile web view use korbo jeta block kora kothin
    url = "https://toffeelive.com/en/watch/sony-sports-ten-1-hd/py5j-JQBv9knK3AHxDTY"
    headers = {
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=20)
        cookie_header = response.headers.get('Set-Cookie', '')
        match = re.search(r'(Edge-Cache-Cookie=[^;]+)', cookie_header)
        if match:
            print("Successfully found new cookie!")
            return match.group(1)
    except Exception as e:
        print(f"Scraping failed: {e}")
    
    return None

def update_playlist():
    cookie = get_automatic_cookie()
    if not cookie:
        return

    ua = "Mozilla/5.0 (Linux; Android 10; SM-G981B) AppleWebKit/537.36"
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
        m3u_content += f'#EXTHTTP:{{"cookie":"{cookie}"}}\n'
        m3u_content += f'{stream_url}\n'

    with open("Toffee.m3u", "w", encoding="utf-8") as f:
        f.write(m3u_content)

if __name__ == "__main__":
    update_playlist()
