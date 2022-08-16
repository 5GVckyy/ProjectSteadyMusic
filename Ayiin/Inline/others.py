from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, InputMediaPhoto, Message)

from Ayiin import db_mem


def others_markup(videoid, user_id):
    if videoid not in db_mem:
        db_mem[videoid] = {}
    db_mem[videoid]["check"] = 1
    buttons = [
        [
            InlineKeyboardButton(
                text="🔎 Search Lyrics",
                callback_data=f"lyrics {videoid}|{user_id}",
            )
        ],
        [
            InlineKeyboardButton(
                text="✚ Your Playlist",
                callback_data=f"your_playlist {videoid}|{user_id}",
            ),
            InlineKeyboardButton(
                text="✚ Group Playlist",
                callback_data=f"group_playlist {videoid}|{user_id}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="☟︎︎︎ Download Video/Audio",
                callback_data=f"audio_video_download {videoid}|{user_id}",
            )
        ],
        [
            InlineKeyboardButton(
                text="❮ Go back",
                callback_data=f"pr_go_back_timer {videoid}|{user_id}",
            ),
            InlineKeyboardButton(
                text="Close",
                callback_data=f"close",
            ),
        ],
    ]
    return buttons


def download_markup(videoid, user_id):
    buttons = [
        [
            InlineKeyboardButton(
                text="☟︎︎︎ Get Audio",
                callback_data=f"gets audio|{videoid}|{user_id}",
            ),
            InlineKeyboardButton(
                text="☟︎︎︎ Get Video",
                callback_data=f"gets video|{videoid}|{user_id}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="❮ Go Back", callback_data=f"goback {videoid}|{user_id}"
            ),
            InlineKeyboardButton(text="Close​", callback_data=f"close"),
        ],
    ]
    return buttons
