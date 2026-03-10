import json

def generate_toffee_files():
    # লেটেস্ট কুকি এবং ইউজার এজেন্ট (এটি অটোমেটিক করার জন্য স্ক্র্যাপার প্রয়োজন, আপাতত ম্যানুয়াল)
    COOKIE = "Edge-Cache-Cookie=URLPrefix=aHR0cHM6Ly9ibGRjbXByb2QtY2RuLnRvZmZlZWxpdmUuY29t:Expires=1773331373:KeyName=prod_linear:Signature=LLPpsVfQH_UcxfJ53MAWunVnd1yGEYjKYNc3d20EQJfvIzCesL8EFeyPVWQjMGs9aJA9KdIFdAL8WCOcacB6Dg"
    USER_AGENT = "Mozilla/5.0 (Linux; Android 9; Redmi S2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36"

    channels = [
        {"title": "Sony Sports 1 HD", "id": "sony_sports_1_hd"},
        {"title": "Sony Sports 2 HD", "id": "sony_sports_2_hd"},
        {"title": "T-Sports HD", "id": "tsports_hd"},
    ]

    m3u_content = "#EXTM3U\n"
    for ch in channels:
        url = f"https://bldcmprod-cdn.toffeelive.com/cdn/live/{ch['id']}/playlist.m3u8"
        # বিভিন্ন প্লেয়ারের জন্য হেডার ইনজেকশন
        m3u_content += f'#EXTINF:-1, {ch["title"]}\n'
        m3u_content += f'#EXTVLCOPT:http-user-agent={USER_AGENT}\n'
        m3u_content += f'#EXTHTTP:{{"cookie":"{COOKIE}", "user-agent":"{USER_AGENT}"}}\n'
        m3u_content += f'{url}\n'

    with open("Toffee.m3u", "w", encoding="utf-8") as f:
        f.write(m3u_content)
    print("Playlist Updated!")

if __name__ == "__main__":
    generate_toffee_files()
