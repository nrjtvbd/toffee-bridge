import re
from playwright.sync_api import sync_playwright

def get_fresh_data():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36")
        page = context.new_page()
        
        # Sony Sports page-e jawa
        page.goto("https://toffeelive.com/en/watch/sony-sports-ten-1-hd/py5j-JQBv9knK3AHxDTY", wait_until="networkidle")
        
        # Cookie collect kora
        cookies = context.cookies()
        edge_cookie = next((c['value'] for c in cookies if c['name'] == 'Edge-Cache-Cookie'), None)
        
        browser.close()
        return f"Edge-Cache-Cookie={edge_cookie}" if edge_cookie else None

def update_m3u():
    fresh_cookie = get_fresh_data()
    if not fresh_cookie:
        print("Fresh cookie pawa jayni!")
        return

    # Ekhon fresh_cookie-te notun Expires code ebong Signature thakbe
    ua = "Mozilla/5.0 (Linux; Android 9; Redmi S2 Build/PKQ1.181203.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.7049.79 Mobile Safari/537.36"
    
    # Playlist lekha
    m3u_content = f"#EXTM3U\n#EXTINF:-1, Sony Sports 1 HD\n#EXTVLCOPT:http-user-agent={ua}\n#EXTVLCOPT:http-cookie={fresh_cookie}\nhttps://bldcmprod-cdn.toffeelive.com/cdn/live/sony_sports_1_hd/playlist.m3u8"
    
    with open("Toffee.m3u", "w") as f:
        f.write(m3u_content)
    print("Playlist refresh holo notun Expires code shoho!")

update_m3u()
