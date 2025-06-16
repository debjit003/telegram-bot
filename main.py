# from telegram import Update
# from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text("Hello, Welcome to the Bot.Please write\
#     /help to see the commands available.")

# app = ApplicationBuilder().token("7923917813:AAH_Lop-J2h75JGlAEVqEOUnL1-lsHaaqfI").build()



# # updater = Updater("8157609017:AAFlsA6PMypd8apFfu1IpnNcYGzrBWMaHr4", 
#                 #   use_context=True)

# # def start(update: Update, context: CallbackContext):
# #     update.message.reply_text("Hello, Welcome to the Bot.Please write\
# #         /help to see the commands available.")
    
# async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
#      await update.message.reply_text("""The commands available are:\n\
#         /youtube - To get the youtube URL
#         /linkedin - To get the LinkedIn profile URL
#         /gmail - To get gmail URL
#         /geeks - To get the GeeksforGeeks URL
#         /github - To get the GitHub URL
#         /instagram - To get the Instagram URL""")
    
# async def gmail_url(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text("https://mail.google.com/mail/u/0/#inbox")

# async def youtube_url(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text("Youtube Link =>\
#     https://www.youtube.com/")


# async def linkedIn_url(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text(
#         "LinkedIn URL => \
#         https://www.linkedin.com/in/debjit-roy-07353021b/")


# async def geeks_url(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text(
#         "GeeksforGeeks URL => https://www.geeksforgeeks.org/")
    
# async def github_url(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text(
#         "GitHub URL => https://github.com/debjit003/")

# async def insta_url(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text(
#         "Instagram URL => https://www.instagram.com/")


# async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text(
#         "Sorry '%s' is not a valid command" % update.message.text)


# async def unknown_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text(
#         "Sorry I can't recognize you , you said '%s'" % update.message.text)


# app.add_handler(CommandHandler("start", start))
# app.add_handler(CommandHandler('youtube', youtube_url))
# app.add_handler(CommandHandler('help', help))
# app.add_handler(CommandHandler('linkedin', linkedIn_url))
# app.add_handler(CommandHandler('gmail', gmail_url))
# app.add_handler(CommandHandler('geeks', geeks_url))
# app.add_handler(CommandHandler('github', github_url))
# app.add_handler(CommandHandler('instagram', insta_url))
# app.add_handler(CommandHandler('unknown', unknown))
# app.add_handler(CommandHandler('unknown_text', unknown_text))
# #app.add_handler(MessageHandler(Filters.text, unknown))
# #app.add_handler(MessageHandler(
#     #Filters.command, unknown))  # Filters out unknown commands

# # Filters out unknown messages.
# #app.add_handler(MessageHandler(Filters.text, unknown_text))

# #updater.start_polling()
# print("Bot is now running...")
# app.run_polling()


from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)
import logging

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

# Command Handlers
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hello, Welcome to the Bot.\nPlease write /help to see the commands available."
    )

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        """The commands available are:
/youtube - To get the YouTube URL
/linkedin - To get the LinkedIn profile URL
/gmail - To get Gmail URL
/geeks - To get the GeeksforGeeks URL
/github - To get the GitHub URL
/instagram - To get the Instagram URL"""
    )

async def gmail_url(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("https://mail.google.com/mail/u/0/#inbox")

async def youtube_url(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("https://www.youtube.com/")

async def linkedIn_url(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "https://www.linkedin.com/in/debjit-roy-07353021b/"
    )

async def geeks_url(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("https://www.geeksforgeeks.org/")

async def github_url(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("https://github.com/debjit003/")

async def insta_url(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("https://www.instagram.com/")

# Unknown command/message handlers
async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"Sorry, '{update.message.text}' is not a valid command."
    )

async def unknown_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"Sorry, I can't recognize what you said: '{update.message.text}'"
    )

# Main application
app = ApplicationBuilder().token("7923917813:AAH_Lop-J2h75JGlAEVqEOUnL1-lsHaaqfI").build()

# Command Handlers
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help))
app.add_handler(CommandHandler("youtube", youtube_url))
app.add_handler(CommandHandler("linkedin", linkedIn_url))
app.add_handler(CommandHandler("gmail", gmail_url))
app.add_handler(CommandHandler("geeks", geeks_url))
app.add_handler(CommandHandler("github", github_url))
app.add_handler(CommandHandler("instagram", insta_url))

# Message Handlers
app.add_handler(MessageHandler(filters.COMMAND, unknown))  # unknown commands
app.add_handler(MessageHandler(filters.TEXT, unknown_text))  # all other messages

print("Bot is now running...")
app.run_polling()
