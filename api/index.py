from http.server import BaseHTTPRequestHandler
import requests
import re

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # 1. Toffee theke fresh cookie/signature newar logic
        ua = "Mozilla/5.0 (Linux; Android 9; Redmi S2 Build/PKQ1.181203.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.7049.79 Mobile Safari/537.36"
        target_url = "https://toffeelive.com/en/watch/py5j-JQBv9knK3AHxDTY"
        
        headers = {"User-Agent": ua, "Referer": "https://toffeelive.com/"}
        
        try:
            response = requests.get(target_url, headers=headers, timeout=10)
            cookie_header = response.headers.get('Set-Cookie', '')
            match = re.search(r'(Edge-Cache-Cookie=[^;]+)', cookie_header)
            cookie = match.group(1) if match else ""
        except:
            cookie = ""

        # 2. M3U Playlist jenerate kora
        # Ekhane apni apnar channel gulo add korun
        channels = [
            {"name": "Sony Sports 1 HD", "id": "sony_sports_1_hd"},
            {"name": "T-Sports HD", "id": "tsports_hd"}
        ]

        playlist = "#EXTM3U\n"
        for ch in channels:
            stream_url = f"https://bldcmprod-cdn.toffeelive.com/cdn/live/{ch['id']}/playlist.m3u8"
            playlist += f'#EXTINF:-1, {ch["name"]}\n'
            playlist += f'#EXTVLCOPT:http-user-agent={ua}\n'
            playlist += f'#EXTVLCOPT:http-cookie={cookie}\n'
            playlist += f'{stream_url}\n'

        # 3. Response pathano
        self.send_response(200)
        self.send_header('Content-type', 'application/vnd.apple.mpegurl')
        self.end_headers()
        self.wfile.write(playlist.encode('utf-8'))
