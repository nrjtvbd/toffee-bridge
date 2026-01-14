import requests
from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        query = parse_qs(urlparse(self.path).query)
        id = query.get('id', [None])[0]
        proxy_url = query.get('proxyUrl', [None])[0]

        # Toffee Channels
        channels = {
            "ten-cricket": "https://bldcmprod-cdn.toffeelive.com/cdn/live/ten_cricket_576/ten_cricket_576.m3u8",
            "sony-ten-1": "https://bldcmprod-cdn.toffeelive.com/cdn/live/sony_ten_1/playlist.m3u8"
        }

        target_url = channels.get(id) if id else proxy_url

        if not target_url:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b"Please use ?id=ten-cricket")
            return

        # আপনার দেওয়া ফাইল থেকে সংগৃহীত ডাটা
        headers = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 9; Redmi S2 Build/PKQ1.181203.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.7049.79 Mobile Safari/537.36",
            "Cookie": "Edge-Cache-Cookie=URLPrefix=aHR0cHM6Ly9ibGRjbXByb2QtY2RuLnRvZmZlZWxpdmUuY29t:Expires=1768591340:KeyName=prod_linear:Signature=N2pe6EUZ4gRrLQtQXKmDfuLaRcDMcOlciOD5QV7v8iDQJPQHzOieViNZDUNjKca4hmOyxa3M5dEOyW6_9OeRDA",
            "X-Requested-With": "com.toffee.live"
        }

        try:
            res = requests.get(target_url, headers=headers, stream=True, timeout=10)
            self.send_response(200)
            
            # M3U8 প্লেলিস্ট মডিফাই করা (VLC-র জন্য)
            if ".m3u8" in target_url:
                self.send_header('Content-type', 'application/vnd.apple.mpegurl')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                
                content = res.text
                base_url = target_url.rsplit('/', 1)[0] + '/'
                host = self.headers.get('Host')
                
                new_content = ""
                for line in content.splitlines():
                    if line.startswith('#') or not line.strip():
                        new_content += line + "\n"
                    else:
                        segment_url = line if line.startswith('http') else base_url + line
                        new_content += f"https://{host}/api/index?proxyUrl={segment_url}\n"
                
                self.wfile.write(new_content.encode())
            
            # ভিডিও সেগমেন্ট (.ts) সরাসরি পাঠানো
            else:
                self.send_header('Content-type', 'video/mp2t')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                for chunk in res.iter_content(chunk_size=8192):
                    self.wfile.write(chunk)

        except Exception as e:
            self.send_response(500)
            self.end_headers()
            self.wfile.write(str(e).encode())
