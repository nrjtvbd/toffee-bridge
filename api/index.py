import requests
from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # আপনার গিটহাবের Raw লিঙ্ক (আমি আপনার ইউজারনাম ও রিপো সেট করে দিয়েছি)
        github_raw_url = "https://raw.githubusercontent.com/nrjtvbd/toffee-bridge/main/cookie.txt"
        
        ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        
        try:
            # গিটহাব থেকে অটো-আপডেটেড কুকিটা নিয়ে আসা
            r = requests.get(github_raw_url, timeout=10)
            fresh_cookie = r.text.strip() if r.status_code == 200 else ""
        except:
            fresh_cookie = ""

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
