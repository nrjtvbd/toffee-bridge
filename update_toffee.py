import requests
import re

def get_toffee_cookie():
    url = "https://toffeelive.com/en/watch/sony-sports-ten-1-hd/py5j-JQBv9knK3AHxDTY"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
    try:
        r = requests.get(url, headers=headers, timeout=15)
        cookie = r.headers.get('Set-Cookie', '')
        match = re.search(r'(Edge-Cache-Cookie=[^;]+)', cookie)
        return match.group(1) if match else None
    except:
        return None

def generate():
    cookie = get_toffee_cookie()
    # Scraper fail korle apnar deya shesh kaj kora cookie-ti ekhane backup thakbe
    if not cookie:
        cookie = "Edge-Cache-Cookie=URLPrefix=aHR0cHM6Ly9ibGRjbXByb2QtY2RuLnRvZmZlZWxpdmUuY29t:Expires=1773337747:KeyName=prod_linear:Signature=MhJ3pv26Yjf2jrmWtCQt1rvo-3MmYPgtFotZQFEc_IUKBbDdjDlKVXL9UDEuy-DOaPm4HH_MkKC6OqA1UYX0Aw"

    ua = "Mozilla/5.0 (Linux; Android 10; SM-G981B) AppleWebKit/537.36"
    channels = [
        {"name": "Sony Sports 1 HD", "id": "sony_sports_1_hd"},
        {"name": "Sony Sports 2 HD", "id": "sony_sports_2_hd"},
        {"name": "T-Sports HD", "id": "tsports_hd"}
    ]

    m3u = "#EXTM3U\n"
    for ch in channels:
        stream = f"https://bldcmprod-cdn.toffeelive.com/cdn/live/{ch['id']}/playlist.m3u8"
        m3u += f'#EXTINF:-1, {ch["name"]}\n'
        m3u += f'#EXTVLCOPT:http-user-agent={ua}\n'
        m3u += f'#EXTVLCOPT:http-cookie={cookie}\n'
        m3u += f'{stream}\n'

    with open("Toffee.m3u", "w", encoding="utf-8") as f:
        f.write(m3u)

if __name__ == "__main__":
    generate()
