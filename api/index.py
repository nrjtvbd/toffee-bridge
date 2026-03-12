from http.server import BaseHTTPRequestHandler
import requests
import re
import random

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # ১. বাংলাদেশের কিছু র‍্যান্ডম আইপি জেনারেট করা (টুফিকে বোকা বানাতে)
        bd_ips = ["103.147.111.", "119.30.32.", "203.76.96.", "43.231.20."]
        fake_ip = random.choice(bd_ips) + str(random.randint(1, 254))
        
        ua = "Mozilla/5.0 (Linux; Android 9; Redmi S2 Build/PKQ1.181203.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.7049.79 Mobile Safari/537.36"
        toffee_url = "https://toffeelive.com/en/watch/py5j-JQBv9knK3AHxDTY"
        
        # ২. স্পেশাল হেডার ট্রিক
        headers = {
            "User-Agent": ua,
            "Referer": "https://toffeelive.com/",
            "X-Forwarded-For": fake_ip,
            "X-Real-IP": fake_ip,
            "Client-IP": fake_ip,
            "X-Requested-With": "com.bti.toffee"
        }
        
        fresh_cookie = ""
        try:
            # টুফিতে রিকোয়েস্ট পাঠানো
            session = requests.Session()
            r = session.get(toffee_url, headers=headers, timeout=12)
            cookie_header = r.headers.get('Set-Cookie', '')
            
            # সিগনেচার বা কুকি খুঁজে বের করা
            match = re.search(r'(Edge-Cache-Cookie=[^;]+)', cookie_header)
            if match:
                fresh_cookie = match.group(1)
            else:
                # যদি না পায়, তবে সেশন থেকে খোঁজা
                for c in session.cookies:
                    if c.name == 'Edge-Cache-Cookie':
                        fresh_cookie = f"Edge-Cache-Cookie={c.value}"
        except:
            pass

        # ব্যাকআপ কুকি (যদি উপরের পদ্ধতি কাজ না করে)
        if not fresh_cookie:
            fresh_cookie = "Edge-Cache-Cookie=URLPrefix=aHR0cHM6Ly9ibGRjbXByb2QtY2RuLnRvZmZlZWxpdmUuY29t:Expires=1773337747:KeyName=prod_linear:Signature=MhJ3pv26Yjf2jrmWtCQt1rvo-3MmYPgtFotZQFEc_IUKBbDdjDlKVXL9UDEuy-DOaPm4HH_MkKC6OqA1UYX0Aw"

        # ৩. চ্যানেল লিস্ট
        channels = [
            {"name": "Sony Sports 1 HD", "id": "sony_sports_1_hd"},
            {"name": "Sony Sports 2 HD", "id": "sony_sports_2_hd"},
            {"name": "T-Sports HD", "id": "tsports_hd"},
            {"name": "Sony Sports Ten 5", "id": "sony_sports_ten_5"}
        ]

        m3u = "#EXTM3U\n"
        for ch in channels:
            m3u += f'#EXTINF:-1, {ch["name"]}\n'
            m3u += f'#EXTVLCOPT:http-user-agent={ua}\n'
            m3u += f'#EXTVLCOPT:http-cookie={fresh_cookie}\n'
            m3u += f'https://bldcmprod-cdn.toffeelive.com/cdn/live/{ch["id"]}/playlist.m3u8\n'

        self.send_response(200)
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(m3u.encode('utf-8'))
