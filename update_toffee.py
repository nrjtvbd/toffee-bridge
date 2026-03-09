import json

def generate_toffee_files():
    # --- CONFIGURATION ---
    # Apnar Worker URL (Sheshe "/" thakbe na)
    WORKER_URL = "https://toffee.rayhankabirrana1.workers.dev" 
    PASS = "Rayhan52247S"

    # Channel list
    channels = [
        {"title": "Sony Sports 1 HD", "id": "sony_sports_1_hd"},
        {"title": "Sony Sports 2 HD", "id": "sony_sports_2_hd"},
        {"title": "T-Sports HD", "id": "tsports_hd"},
        {"title": "Sony Ten 1 HD", "id": "sony_ten_1_hd"},
    ]

    m3u_content = "#EXTM3U\n"
    json_response = {"response": []}

    for ch in channels:
        # Worker proxy link toiri
        proxy_url = f"{WORKER_URL}/?id={ch['id']}&pass={PASS}"
        
        m3u_content += f"#EXTINF:-1, {ch['title']}\n{proxy_url}\n"
        json_response["response"].append({"id": ch['id'], "title": ch['title'], "url": proxy_url})

    # File save kora
    with open("Toffee.m3u", "w", encoding="utf-8") as f:
        f.write(m3u_content)
    
    with open("Toffee_data.json", "w", encoding="utf-8") as f:
        json.dump(json_response, f, indent=2)

    print("✅ GitHub files updated with worker links!")

if __name__ == "__main__":
    generate_toffee_files()
