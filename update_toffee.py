import requests
import re
import os

def get_toffee_cookie():
    url = "https://toffeelive.com/en/watch/sony-sports-ten-1-hd/py5j-JQBv9knK3AHxDTY"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    try:
        response = requests.get(url, headers=headers, timeout=10)
        cookie_header = response.headers.get('Set-Cookie', '')
        # Edge-Cache-Cookie extract kora
        match = re.search(r'(Edge-Cache-Cookie=[^;]+)', cookie_header)
        if match:
            return match.group(1)
    except:
        pass
    # Jodi scrape fail kore, tobe default/manual cookie (backup)
    return "Edge-Cache-Cookie=URLPrefix=aHR0cHM6Ly9ibGRjbXByb2QtY2RuLnRvZmZlZWxpdmUuY29t:Expires=1773331373:KeyName=prod_linear:Signature=LLPpsVfQH_UcxfJ53MAWunVnd1yGEYjKYNc3d20EQJfvIzCesL8EFeyPVWQjMGs9aJA9KdIFdAL8WCOcacB6Dg"

def generate_playlist():
    cookie = get_toffee_cookie()
    user_agent = "Mozilla/5.0 (Linux; Android 10; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36"
    
    channels = [
        {"name": "Sony Sports 1 HD", "id": "sony_sports_1_hd"},
        {"name": "Sony Sports 2 HD", "id": "sony_sports_2_hd"},
        {"name": "T-Sports HD", "id": "tsports_hd"}
    ]

    m3u_content = "#EXTM3U\n"
    for ch in channels:
        stream_url = f"https://bldcmprod-cdn.toffeelive.com/cdn/live/{ch['id']}/playlist.m3u8"
        # VLC ebong libvlc-te cookie pass korar standard format
        m3u_content += f'#EXTINF:-1, {ch["name"]}\n'
        m3u_content += f'#EXTVLCOPT:http-user-agent={user_agent}\n'
        m3u_content += f'#EXTVLCOPT:http-referrer=https://toffeelive.com/\n'
        # VLC-te cookie pathanor jonno niche deya format-ti guruttopurno
        m3u_content += f'#EXTVLCOPT:http-cookie={cookie}\n'
        m3u_content += f'{stream_url}\n'

    with open("Toffee.m3u", "w") as f:
        f.write(m3u_content)

if __name__ == "__main__":
    generate_playlist()
