import json

def generate_toffee_files():
    # আপনার ওয়ার্কার লিঙ্ক
    WORKER_URL = "https://toffee.rayhankabirrana1.workers.dev"
    PASS = "Rayhan52247S"

    channels = [
        {"title": "Sony Sports 1 HD", "id": "sony_sports_1_hd"},
        {"title": "Sony Sports 2 HD", "id": "sony_sports_2_hd"},
        {"title": "T-Sports HD", "id": "tsports_hd"},
    ]

    m3u_content = "#EXTM3U\n"
    for ch in channels:
        # লিঙ্কটি এখন ওয়ার্কারের মাধ্যমে যাবে
        proxy_url = f"{WORKER_URL}/?id={ch['id']}&pass={PASS}"
        m3u_content += f'#EXTINF:-1, {ch["title"]}\n{proxy_url}\n'

    with open("Toffee.m3u", "w", encoding="utf-8") as f:
        f.write(m3u_content)

if __name__ == "__main__":
    generate_toffee_files()
