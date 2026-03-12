from http.server import BaseHTTPRequestHandler
import requests
import re

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # ১. হেডারের জন্য সেটিংস
        ua = "Mozilla/5.0 (Linux; Android 9; Redmi S2 Build/PKQ1.181203.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.7049.79 Mobile Safari/537.36"
        toffee_url = "https://toffeelive.com/en/watch/py5j-JQBv9knK3AHxDTY"
        
        headers = {
            "User-Agent": ua,
            "Referer": "https://toffeelive.com/"
        }
        
        # ২. কুকি সংগ্রহের চেষ্টা
        fresh_cookie = ""
        try:
            r = requests.get(toffee_url, headers=headers, timeout=10)
            cookie_header = r.headers.get('Set-Cookie', '')
            match = re.search(r'(Edge-Cache-Cookie=[^;]+)', cookie_header)
            if match:
                fresh_cookie = match.group(1)
        except Exception as e:
            print(f"Error fetching cookie: {e}")

        # ৩. চ্যানেল লিস্ট
        channels = [
            {"name": "Sony Sports 1 HD", "id": "sony_sports_1_hd"},
            {"name": "Sony Sports 2 HD", "id": "sony_sports_2_hd"},
            {"name": "T-Sports HD", "id": "tsports_hd"}
        ]

        # ৪. M3U কনটেন্ট তৈরি
        m3u = "#EXTM3U\n"
        for ch in channels:
            m3u += f'#EXTINF:-1, {ch["name"]}\n'
            m3u += f'#EXTVLCOPT:http-user-agent={ua}\n'
            m3u += f'#EXTVLCOPT:http-cookie={fresh_cookie}\n'
            m3u += f'https://bldcmprod-cdn.toffeelive.com/cdn/live/{ch["id"]}/playlist.m3u8\n'

        # ৫. রেসপন্স পাঠানো (Vercel ফ্রেন্ডলি ফরম্যাট)
        self.send_response(200)
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(m3u.encode('utf-8'))
        return
