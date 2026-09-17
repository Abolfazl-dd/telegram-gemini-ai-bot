from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from google import genai
from dotenv import load_dotenv
import os
import json

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=GEMINI_API_KEY)
user_chat_sessions = {}




def load_notes():
    try:
        with open("note.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def save_note(note):
    with open("note.json", "w") as file:
        json.dump(note,file)



async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I am your AI bot. Use /chat <message> to talk to me.")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Commands:\n/start - greet\n/help - this message\n/chat <text> - ask the AI something"
    )


def get_or_create_chat(user_id):
    if user_id not in user_chat_sessions:
        user_chat_sessions[user_id] = client.chats.create(
            model="gemini-3.8-flash"
        )

    return user_chat_sessions[user_id]


async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = str(update.effective_user.id)

    user_message = " ".join(context.args)

    if not user_message:
        await update.message.reply_text(
            "Please type something after /chat, like: /chat what is Python?"
        )
        return

    chat_session = get_or_create_chat(user_id)

    response = chat_session.send_message(user_message)

    await update.message.reply_text(response.text)

async def summarize(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if not context.args:
        await update.message.reply_text(
            "Please type a note number, like: /summarize 2"
        )
        return

    try:
        note_number = int(context.args[0])
    except ValueError:
        await update.message.reply_text(
            "Please enter a valid note number."
        )
        return

    notes = load_notes()
    user_id = str(update.effective_user.id)

    if user_id not in notes:
        await update.message.reply_text(
            "You don't have any notes."
        )
        return

    if note_number < 1 or note_number > len(notes[user_id]):
        await update.message.reply_text(
            "That note number doesn't exist."
        )
        return

    note = notes[user_id][note_number - 1]

    response = client.models.generate_content(
        model="gemini-3.7-flash",
        contents=f"Summarize this note:\n\n{note}"
    )

    await update.message.reply_text(
        f"{note}\n\nSummary:\n{response.text}"
    )



async def reset(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = str(update.effective_user.id)
    if user_id not in user_chat_sessions:
        await update.message.reply_text("sorry you didn't chat with AI there is nothing to reset")
    else:
        user_chat_sessions.pop(user_id)
        await update.message.reply_text("AI history deleted")


async def addnote(update, context):
    if not context.args:
        await update.message.reply_text(
            "Please write a note after /add_note."
        )
        return
    user_id = str(update.effective_user.id)
    note_text = " ".join(context.args)
    notes = load_notes()
    if user_id not in notes:
        notes[user_id] = []

    notes[user_id].append(note_text)

    save_note(notes)
    await update.message.reply_text("note added")


async def show_notes(update, context):
    user_id = str(update.effective_user.id)
    notes = load_notes()

    if user_id not in notes:
        await update.message.reply_text("You don't have any note")
        return

    note_list = notes.get(user_id)

    for i, note in enumerate(note_list, start=1):
        await update.message.reply_text(f"{i}_ {note}")



async def delete_note(update, context):
    user_id = str(update.effective_user.id)
    notes = load_notes()

    if user_id not in notes:
        await update.message.reply_text("You don't have any note")
        return

    try:
        selected_note = int(context.args[0])
    except (ValueError, IndexError):
        await update.message.reply_text("Please enter a valid note number")
        return

    if selected_note < 1 or selected_note > len(notes[user_id]):
        await update.message.reply_text("Please enter a valid note number")
        return

    notes[user_id].pop(selected_note - 1)
    save_note(notes)

    await update.message.reply_text("Note deleted")



app = Application.builder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("add_note", addnote))
app.add_handler(CommandHandler("show_notes", show_notes))
app.add_handler(CommandHandler("delete_note", delete_note))
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("chat", chat))
app.add_handler(CommandHandler("summarize", summarize))
app.add_handler(CommandHandler("reset", reset))

app.run_polling()