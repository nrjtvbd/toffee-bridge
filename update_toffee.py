import okhttp3.OkHttpClient
import okhttp3.Request

fun getToffeeCookie(): String? {
    val client = OkHttpClient()
    val ua = "Mozilla/5.0 (Linux; Android 9; Redmi S2 Build/PKQ1.181203.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.7049.79 Mobile Safari/537.36"
    
    // আপনার দেওয়া সেই ক্লিন URL
    val url = "https://toffeelive.com/en/watch/py5j-JQBv9knK3AHxDTY"
    
    val request = Request.Builder()
        .url(url)
        .header("User-Agent", ua)
        .build()

    return try {
        val response = client.newCall(request).execute()
        val cookies = response.headers("Set-Cookie")
        // Edge-Cache-Cookie খুঁজে বের করা
        cookies.find { it.contains("Edge-Cache-Cookie") }?.split(";")?.get(0)
    } catch (e: Exception) {
        null
    }
}
