import requests
import re

def get_toffee_cookie():
    ua = "Mozilla/5.0 (Linux; Android 9; Redmi S2 Build/PKQ1.181203.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.7049.79 Mobile Safari/537.36"
    url = "https://toffeelive.com/en/watch/sony-sports-ten-1-hd/py5j-JQBv9knK3AHxDTY"
    try:
        r = requests.get(url, headers={"User-Agent": ua}, timeout=10)
        match = re.search(r'(Edge-Cache-Cookie=[^;]+)', r.headers.get('Set-Cookie', ''))
        return match.group(1) if match else None
    except: return None

def update():
    cookie = get_toffee_cookie()
    
    # কুকি না পেলেও যেন ফাইল আপডেট হয়, তাই নিচে আপনার সচল কুকিটি ব্যাকআপ হিসেবে থাকবে
    if not cookie:
        print("Auto-scraping failed, using manual backup...")
        cookie = "Edge-Cache-Cookie=URLPrefix=aHR0cHM6Ly9ibGRjbXByb2QtY2RuLnRvZmZlZWxpdmUuY29t:Expires=1773337747:KeyName=prod_linear:Signature=MhJ3pv26Yjf2jrmWtCQt1rvo-3MmYPgtFotZQFEc_IUKBbDdjDlKVXL9UDEuy-DOaPm4HH_MkKC6OqA1UYX0Aw"

    ua = "Mozilla/5.0 (Linux; Android 9; Redmi S2 Build/PKQ1.181203.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.7049.79 Mobile Safari/537.36"
    channels = [{"n": "Sony Sports 1 HD", "id": "sony_sports_1_hd"}, {"n": "Sony Sports 2 HD", "id": "sony_sports_2_hd"}]

    m3u = "#EXTM3U\n"
    for ch in channels:
        m3u += f'#EXTINF:-1, {ch["n"]}\n#EXTVLCOPT:http-user-agent={ua}\n#EXTVLCOPT:http-cookie={cookie}\nhttps://bldcmprod-cdn.toffeelive.com/cdn/live/{ch["id"]}/playlist.m3u8\n'

    with open("Toffee.m3u", "w", encoding="utf-8") as f:
        f.write(m3u)
    print("Toffee.m3u updated successfully!")

update()
