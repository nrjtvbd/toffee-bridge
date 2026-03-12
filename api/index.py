from http.server import BaseHTTPRequestHandler
import requests
import re

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        ua = "Mozilla/5.0 (Linux; Android 9; Redmi S2 Build/PKQ1.181203.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.7049.79 Mobile Safari/537.36"
        # আমরা সরাসরি এই লিঙ্কে হিট করে কুকি নেব
        toffee_url = "https://toffeelive.com/en/watch/py5j-JQBv9knK3AHxDTY"
        
        headers = {
            "User-Agent": ua,
            "Referer": "https://toffeelive.com/",
            "X-Forwarded-For": "103.147.111.1" # বাংলাদেশের একটি আইপি নকল করা
        }
        
        fresh_cookie = ""
        try:
            # বাংলাদেশের আইপি ব্যবহার করে কুকি সংগ্রহের চেষ্টা
            r = requests.get(toffee_url, headers=headers, timeout=10)
            cookie_header = r.headers.get('Set-Cookie', '')
            match = re.search(r'(Edge-Cache-Cookie=[^;]+)', cookie_header)
            if match:
                fresh_cookie = match.group(1)
        except:
            pass

        # যদি অটোমেটিক কুকি না পায়, তবে এখানে আপনার হাতে থাকা সচল কুকিটি ব্যাকআপ হিসেবে থাকবে
        if not fresh_cookie:
            fresh_cookie = "Edge-Cache-Cookie=URLPrefix=aHR0cHM6Ly9ibGRjbXByb2QtY2RuLnRvZmZlZWxpdmUuY29t:Expires=1773337747:KeyName=prod_linear:Signature=MhJ3pv26Yjf2jrmWtCQt1rvo-3MmYPgtFotZQFEc_IUKBbDdjDlKVXL9UDEuy-DOaPm4HH_MkKC6OqA1UYX0Aw"

        channels = [
            {"name": "Sony Sports 1 HD", "id": "sony_sports_1_hd"},
            {"name": "Sony Sports 2 HD", "id": "sony_sports_2_hd"},
            {"name": "T-Sports HD", "id": "tsports_hd"}
        ]

        m3u = "#EXTM3U\n"
        for ch in channels:
            m3u += f'#EXTINF:-1, {ch["name"]}\n'
            m3u += f'#EXTVLCOPT:http-user-agent={ua}\n'
            m3u += f'#EXTVLCOPT:http-cookie={fresh_cookie}\n'
            m3u += f'https://bldcmprod-cdn.toffeelive.com/cdn/live/{ch["id"]}/playlist.m3u8\n'

        self.send_response(200)
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()
        self.wfile.write(m3u.encode('utf-8'))
