from pyrogram import Client
from pyrogram.raw.functions.contacts import ResolveUsername
from secret_keys import TELEGRAM_BOT_TOKEN, BOT_API_ID, BOT_API_HASH

BOT_TOKEN = TELEGRAM_BOT_TOKEN


pyrogram_client = Client(
    "bot",
    api_id=BOT_API_ID,
    api_hash=BOT_API_HASH,
    bot_token=BOT_TOKEN
)


def resolve_username_to_user_id(username: str) -> int | None:
    with pyrogram_client:
        r = pyrogram_client.invoke(ResolveUsername(username=username))
        if r.users:
            return r.users[0].id
        return None

