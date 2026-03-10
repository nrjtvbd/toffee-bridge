import requests
import re

def get_real_cookie():
    # Toffee-r live page theke cookie collect korar chesta
    url = "https://toffeelive.com/en/watch/sony-sports-ten-1-hd/py5j-JQBv9knK3AHxDTY"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
    }
    try:
        session = requests.Session()
        response = session.get(url, headers=headers, timeout=15)
        cookies = session.cookies.get_dict()
        if 'Edge-Cache-Cookie' in cookies:
            return f"Edge-Cache-Cookie={cookies['Edge-Cache-Cookie']}"
    except Exception as e:
        print(f"Error fetching cookie: {e}")
    
    # Backup/Hardcoded Cookie (Jodi scraper fail kore)
    return "Edge-Cache-Cookie=URLPrefix=aHR0cHM6Ly9ibGRjbXByb2QtY2RuLnRvZmZlZWxpdmUuY29t:Expires=1773331373:KeyName=prod_linear:Signature=LLPpsVfQH_UcxfJ53MAWunVnd1yGEYjKYNc3d20EQJfvIzCesL8EFeyPVWQjMGs9aJA9KdIFdAL8WCOcacB6Dg"

def generate_vlc_m3u():
    cookie = get_real_cookie()
    ua = "Mozilla/5.0 (Linux; Android 10; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36"
    
    channels = [
        {"name": "Sony Sports 1 HD", "id": "sony_sports_1_hd"},
        {"name": "Sony Sports 2 HD", "id": "sony_sports_2_hd"},
        {"name": "T-Sports HD", "id": "tsports_hd"}
    ]

    m3u_content = "#EXTM3U\n"
    for ch in channels:
        url = f"https://bldcmprod-cdn.toffeelive.com/cdn/live/{ch['id']}/playlist.m3u8"
        # VLC ebong libvlc-te chalanor jonno niche deya tag-gulo guruttopurno
        m3u_content += f'#EXTINF:-1, {ch["name"]}\n'
        m3u_content += f'#EXTVLCOPT:http-user-agent={ua}\n'
        m3u_content += f'#EXTVLCOPT:http-referrer=https://toffeelive.com/\n'
        m3u_content += f'#EXTVLCOPT:http-cookie={cookie}\n'
        m3u_content += f'{url}\n'

    with open("Toffee.m3u", "w", encoding="utf-8") as f:
        f.write(m3u_content)
    print("VLC Playlist Updated Successfully!")

if __name__ == "__main__":
    generate_vlc_m3u()
