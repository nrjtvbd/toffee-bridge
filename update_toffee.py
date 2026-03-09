import json

def generate_toffee_files():
    # Toffee-r channel list (Apnar deya ID gulo)
    channels = [
        {"title": "Sony Sports 1 HD", "id": "sony_sports_1_hd"},
        {"title": "Sony Sports 2 HD", "id": "sony_sports_2_hd"},
        {"title": "T-Sports HD", "id": "tsports_hd"},
        {"title": "Sony Ten 1 HD", "id": "sony_ten_1_hd"},
    ]

    # M3U content toiri
    m3u_content = "#EXTM3U\n"
    json_response = {"response": []}

    for ch in channels:
        # Apatoto direct link (pore amra Worker URL diye update korbo)
        url = f"https://bldcmprod-cdn.toffeelive.com/cdn/live/{ch['id']}/playlist.m3u8"
        m3u_content += f"#EXTINF:-1, {ch['title']}\n{url}\n"
        json_response["response"].append({"id": ch['id'], "title": ch['title'], "url": url})

    # File likha
    with open("Toffee.m3u", "w", encoding="utf-8") as f:
        f.write(m3u_content)
    
    with open("Toffee_data.json", "w", encoding="utf-8") as f:
        json.dump(json_response, f, indent=2)

    print("Toffee files generated successfully!")

if __name__ == "__main__":
    generate_toffee_files()
