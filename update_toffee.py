import json
import os

# --- CONFIGURATION (Test korar jonno apatoto placeholders) ---
# Ekhon amra direct link use korbo na, just check korbo file toiri hoy kina
BASE_URL = "https://bldcmprod-cdn.toffeelive.com/cdn/live" 

def generate_toffee_playlist():
    # Toffee-r kichu real ID (apnar deya Sony Sports 1 soho)
    channels = [
        {"title": "Sony Sports 1 HD", "id": "sony_sports_1_hd"},
        {"title": "Sony Sports 2 HD", "id": "sony_sports_2_hd"},
        {"title": "Sony Ten 1 HD", "id": "sony_ten_1_hd"},
        {"title": "T-Sports HD", "id": "tsports_hd"},
        {"title": "GTV HD", "id": "gtv_hd"},
    ]

    m3u_content = "#EXTM3U\n"
    json_data = {
        "status": "success",
        "provider": "Toffee",
        "total_channels": len(channels),
        "response": []
    }

    for ch in channels:
        # Apatoto amra direct m3u8 link tai rakhchi check korar jonno
        stream_url = f"{BASE_URL}/{ch['id']}/playlist.m3u8"
        
        # M3U Format
        m3u_content += f"#EXTINF:-1, {ch['title']}\n{stream_url}\n"
        
        # JSON Format
        json_data["response"].append({
            "id": ch['id'],
            "title": ch['title'],
            "url": stream_url
        })

    # File save kora (PC-te script thaka folder-e create hobe)
    try:
        with open("Toffee.m3u", "w", encoding="utf-8") as f:
            f.write(m3u_content)
        
        with open("Toffee_data.json", "w", encoding="utf-8") as f:
            json.dump(json_data, f, indent=2)
            
        print("✅ Success! 'Toffee.m3u' ebong 'Toffee_data.json' toiri hoyeche.")
        print(f"📂 Apnar folder-e check korun, mot {len(channels)} ti channel add hoyeche.")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    generate_toffee_playlist()
