from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Hey {}

Welcome to ImageToTextMJBot {}

I can extract text from images using OCR technology.

By @mazi_efx
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("Joim channel 💓", url="https://t.me/mazi_efx")],
        [InlineKeyboardButton("Bot Owner 😁", url="https://t.me/azeezmazin")],
        [InlineKeyboardButton("✨ Bot Status and More Bots ✨", url="https://t.me/mazi_efx")],
        [InlineKeyboardButton(text="🏠 Return Home 🏠", callback_data="home")],
    ]
    # Rest Buttons
    buttons = [
        [
            InlineKeyboardButton("✨ Bot Status and More Bots ✨", url="https://t.me/mazi_efx")
        ],
        [
            InlineKeyboardButton("How to Use ❔", callback_data="help"),
            InlineKeyboardButton("🎪 About 🎪", callback_data="about")
        ],
        [InlineKeyboardButton("BOT github repo", bot repo paid dm for owner)],
        [InlineKeyboardButton("♥ More Amazing bots ♥", url="https://t.me/mazi_efx")],
        [InlineKeyboardButton("🎨 Support Group 🎨", url="https://t.me/mazi_efx")],
    ]
   

    # Help Message
    HELP = """
You Really Need Help ?!?!?!?!

Just send an image. Rest is on me.

Note : You can send any amount of images at once and it will work with same speed and accuracy.

More features in development. Keep track by joining @mazi_efx.
    """

    # About Message
    ABOUT = """
**About This Bot** 

Bot created by @azeezmazin @mazi_efx

Source Code : [Click Here](bot source has paid dm for owner @azeezmazin )

Framework : [Pyrogram](docs.pyrogram.org)

Language : [Python](www.python.org)

Develma, : @mazi_efx
    """
