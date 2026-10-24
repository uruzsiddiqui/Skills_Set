import os
import datetime
import requests

# GitHub Secrets se values automatically uthayega
BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

POSTS = [
    """🔥 Day Update: OpenAI Agent Loops & Tool Traces
Aaj maine Agent loop me structured fallbacks aur break conditions implement kiye taaki recursive tool calling infinite cycle me na fase.

💡 Key takeaway: Janky JSON parsing se bachne ke liye strict schemas use karo!
🔗 GitHub: https://github.com/uruzsiddiqui
#BuildInPublic #AgenticAI""",

    """🚀 Day Update: System Design & Rate Limiting
Redis sliding window rate-limiter ko Lua script ke sath test kiya to avoid race conditions. 

Latency drastically drop hui aur server traffic safe hai!
🔗 GitHub: https://github.com/uruzsiddiqui
#SystemDesign #DevJourney""",

    """⚡ Day Update: Deep Research Agent Architecture
Scrape -> Filter -> Synthesize loop ko optimize kiya. Meilisearch + LLM subgraphs se hallucinations 40% reduce ho gayi.

🔗 GitHub: https://github.com/uruzsiddiqui
#AI #LangGraph #OpenSource"""
]

def send_telegram_reminder():
    if not BOT_TOKEN or not CHAT_ID:
        print("Error: BOT_TOKEN ya CHAT_ID missing hai!")
        return

    day_of_year = datetime.datetime.now().timetuple().tm_yday
    today_post = POSTS[day_of_year % len(POSTS)]

    message = f"🚨 *DEV REMINDER: Raat ke 9:30 PM ho gaye!*\n\nAaj ka post ready hai, ishe review/share karo:\n\n---\n{today_post}\n---\n\n👉 [Open GitHub Repo](https://github.com/uruzsiddiqui)"

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        print("Notification Telegram par successfully bhej diya gaya!")
    else:
        print("Error:", response.text)

if __name__ == "__main__":
    send_telegram_reminder()