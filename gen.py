import asyncio
from pyrogram import Client

async def generate_session():
    print("--- Pyrogram V2 Session String Generator ---")
    api_id = int(input("Enter your Telegram API_ID: ").strip())
    api_hash = input("Enter your Telegram API_HASH: ").strip()
    
    # Using ':memory:' keeps it light without clogging local files
    async with Client(":memory:", api_id=api_id, api_hash=api_hash) as app:
        session_string = await app.export_session_string()
        print("\n" + "="*50)
        print("YOUR STENZLE_SESSION STRING (COPY EVERYTHING BELOW):")
        print("="*50 + "\n")
        print(session_string)
        print("\n" + "="*50)

if __name__ == "__main__":
    asyncio.run(generate_session())
