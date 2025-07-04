#main.py
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
    CallbackQueryHandler
)
import logging
import re

def escape_markdown(text: str) -> str:
    """
    Escapes text for Telegram MarkdownV2 formatting.
    """
    escape_chars = r"\_*[]()~`>#+-=|{}.!<>"
    return re.sub(rf"([{re.escape(escape_chars)}])", r"\\\1", text)


# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

# Command Handlers
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hello, Welcome to Assistant Bot.\nPlease write /help to see the commands available."
    )

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        """The commands available are:
/youtube - To get the YouTube URL
/linkedin - To get the LinkedIn profile URL
/gmail - To get Gmail URL
/geeks - To get the GeeksforGeeks URL
/github - To get the GitHub URL
/instagram - To get the Instagram URL

To create a to-do list, use:
/add <task> - To add a task to your to-do list
/list - To list all your tasks
/remove <task number> - To remove a specific task by its number
/remove_all - To remove all tasks from your to-do list"""
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

async def add_task(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = str(update.effective_user.id)
    task = ' '.join(context.args)
    if not task:
        await update.message.reply_text("Usage: /add <task>")
        return

    user_tasks.setdefault(user_id, []).append({"text": task, "done": False})
    await update.message.reply_text(f"Task added: {task}")
    print("Current tasks dict:", user_tasks)
# Dictionary to store user tasks
user_tasks = {}



async def list_tasks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = str(update.effective_user.id)
    tasks = user_tasks.get(user_id, [])

    if not tasks:
        await update.message.reply_text("Your to-do list is empty.")
        return

    message = "📝 *Your tasks:*\n"
    keyboard = []

    for i, task in enumerate(tasks):
        checkbox = "[x]" if task["done"] else "[ ]"
        message += f"{i+1}. {checkbox} {task['text']}\n"

        button_text = "🔁 Mark as undone" if task["done"] else "✅ Mark as done"
        callback_data = f"toggle:{i}"
        keyboard.append([InlineKeyboardButton(button_text, callback_data=callback_data)])

    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(message, reply_markup=reply_markup, parse_mode="Markdown")


async def toggle_task(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    user_id = str(query.from_user.id)
    await query.answer()

    data = query.data
    if not data.startswith("toggle:"):
        return

    index = int(data.split(":")[1])
    tasks = user_tasks.get(user_id, [])

    if 0 <= index < len(tasks):
        tasks[index]["done"] = not tasks[index]["done"]

    # Edit the message to reflect changes
    message = "📝 *Your tasks:*\n"
    keyboard = []
    for i, task in enumerate(tasks):
        checkbox = "[x]" if task["done"] else "[ ]"
        message += f"{i+1}. {checkbox} {task['text']}\n"

        button_text = "🔁 Mark as undone" if task["done"] else "✅ Mark as done"
        callback_data = f"toggle:{i}"
        keyboard.append([InlineKeyboardButton(button_text, callback_data=callback_data)])

    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(message, reply_markup=reply_markup, parse_mode="Markdown")


# Remove a specific task by its index
async def remove_task(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = str(update.effective_user.id)
    tasks = user_tasks.get(user_id, [])

    if not context.args or not context.args[0].isdigit():
        await update.message.reply_text("Usage: /remove <task number>")
        return

    index = int(context.args[0]) - 1
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        await update.message.reply_text(f"Removed task: {removed}")
    else:
        await update.message.reply_text("Invalid task number.")


# Remove all tasks for the user
async def remove_all(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = str(update.effective_user.id)
    user_tasks[user_id] = []
    await update.message.reply_text("All tasks have been removed.")


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
app.add_handler(CommandHandler("add", add_task))
app.add_handler(CommandHandler("list", list_tasks))
app.add_handler(CommandHandler("remove", remove_task))
app.add_handler(CommandHandler("remove_all", remove_all))

# Callback handler for buttons
app.add_handler(CallbackQueryHandler(toggle_task))

# Message Handlers
app.add_handler(MessageHandler(filters.COMMAND, unknown))  # unknown commands
app.add_handler(MessageHandler(filters.TEXT, unknown_text))  # all other messages

print("Bot is now running...")
app.run_polling()
