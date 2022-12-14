from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, InputMediaPhoto, Message)


def check_markup(user_name, user_id, videoid):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"Playlist",
                callback_data=f"playlist_check {user_id}|Group|{videoid}",
            ),
            InlineKeyboardButton(
                text=f"{user_name[:8]}'s Playlist",
                callback_data=f"playlist_check {user_id}|Personal|{videoid}",
            ),
        ],
        [InlineKeyboardButton(text="Close", callback_data="close")],
    ]
    return buttons


def playlist_markup(user_name, user_id, videoid):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"Playlistβ",
                callback_data=f"show_genre {user_id}|Group|{videoid}",
            ),
            InlineKeyboardButton(
                text=f"{user_name[:8]}'s Playlist",
                callback_data=f"show_genre {user_id}|Personal|{videoid}",
            ),
        ],
        [InlineKeyboardButton(text="Closeβ", callback_data="close")],
    ]
    return buttons


def play_genre_playlist(user_id, type, videoid):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"π³πΉ",
                callback_data=f"play_playlist {user_id}|{type}|π±πΎπ»π»πππΎπΎπ³",
            ),
            InlineKeyboardButton(
                text=f"ππ»π΄π΄πΏ",
                callback_data=f"play_playlist {user_id}|{type}|π·πΎπ»π»πππΎπΎπ³",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"ππ°π³",
                callback_data=f"play_playlist {user_id}|{type}|πΏπ°πππ",
            ),
            InlineKeyboardButton(
                text=f"πΏπ°πππ",
                callback_data=f"play_playlist {user_id}|{type}|π»πΎπ΅πΈ",
            ),
        ],
        [
            InlineKeyboardButton(
                text="Back",
                callback_data=f"main_playlist {videoid}|{type}|{user_id}",
            ),
            InlineKeyboardButton(text="Close", callback_data="close"),
        ],
    ]
    return buttons


def add_genre_markup(user_id, type, videoid):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"β π³πΉ",
                callback_data=f"add_playlist {videoid}|{type}|ππ΄π΄π±",
            ),
            InlineKeyboardButton(
                text=f"β πΏπ°πππ",
                callback_data=f"add_playlist {videoid}|{type}|ππ°π³",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"β ππ°π³",
                callback_data=f"add_playlist {videoid}|{type}|πΏπ°πππ",
            ),
            InlineKeyboardButton(
                text=f"β ππ»π΄π΄πΏ",
                callback_data=f"add_playlist {videoid}|{type}|π»πΎπ΅πΈ",
            ),
        ],
        [
            InlineKeyboardButton(
                text="Back", callback_data=f"goback {videoid}|{user_id}"
            ),
            InlineKeyboardButton(text="Close", callback_data="close"),
        ],
    ]
    return buttons


def check_genre_markup(type, videoid, user_id):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"π³πΉ", callback_data=f"check_playlist {type}|ππ΄π΄π±"
            ),
            InlineKeyboardButton(
                text=f"πΏπ°πππ", callback_data=f"check_playlist {type}|ππ°π³"
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"ππ°π³", callback_data=f"check_playlist {type}|πΏπ°πππ"
            ),
            InlineKeyboardButton(
                text=f"ππ»π΄π΄πΏ", callback_data=f"check_playlist {type}|π»πΎπ΅πΈ"
            ),
        ],
        [InlineKeyboardButton(text="Closeβ", callback_data="close")],
    ]
    return buttons


def third_playlist_markup(user_name, user_id, third_name, userid, videoid):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"Playlistβ",
                callback_data=f"show_genre {user_id}|Group|{videoid}",
            ),
            InlineKeyboardButton(
                text=f"{user_name[:8]}'s Playlist",
                callback_data=f"show_genre {user_id}|Personal|{videoid}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"{third_name[:16]}'s Playlist",
                callback_data=f"show_genre {userid}|third|{videoid}",
            ),
        ],
        [InlineKeyboardButton(text="Closeβ", callback_data="close")],
    ]
    return buttons


def paste_queue_markup(url):
    buttons = [
        [
            InlineKeyboardButton(text="βΆοΈ", callback_data=f"resumecb"),
            InlineKeyboardButton(text="βΈοΈ", callback_data=f"pausecb"),
            InlineKeyboardButton(text="β­οΈ", callback_data=f"skipcb"),
            InlineKeyboardButton(text="βΉοΈ", callback_data=f"stopcb"),
        ],
        [InlineKeyboardButton(text="Checkout Queued Playlist", url=f"{url}")],
        [InlineKeyboardButton(text="Closeβ", callback_data=f"close")],
    ]
    return buttons


def fetch_playlist(user_name, type, genre, user_id, url):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"πΏπ»π°π {user_name[:10]}'s {genre} Playlist",
                callback_data=f"play_playlist {user_id}|{type}|{genre}",
            ),
        ],
        [InlineKeyboardButton(text="Checkout Playlist", url=f"{url}")],
        [InlineKeyboardButton(text="Close", callback_data=f"close")],
    ]
    return buttons


def delete_playlist_markuup(type, genre):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"Yes Delete!",
                callback_data=f"delete_playlist {type}|{genre}",
            ),
            InlineKeyboardButton(text="Noβ", callback_data=f"close"),
        ],
    ]
    return buttons
