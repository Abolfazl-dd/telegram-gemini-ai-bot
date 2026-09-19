# 🤖 Telegram Gemini AI Bot

A Telegram AI assistant built with **Python**, **python-telegram-bot**, and the **Google Gemini API**.

The bot can chat with users, remember conversations separately for each user, store personal notes, summarize notes with AI, and reset chat memory when needed.

## ✨ Features

* 💬 AI conversations with Google Gemini
* 🧠 Per-user conversation memory
* 🔐 Separate chat history for each Telegram user
* 📝 Personal note management
* 📋 Show saved notes
* 🗑️ Delete notes
* 🧾 AI-powered note summarization
* 🔄 Reset AI conversation memory
* 🔑 Environment variables for API keys
* ⚡ Asynchronous Telegram bot handlers

## 🛠️ Tech Stack

* Python
* python-telegram-bot
* Google Gemini API
* `google-genai`
* JSON
* python-dotenv

## 📌 Bot Commands

| Command                 | Description                       |
| ----------------------- | --------------------------------- |
| `/start`                | Start the bot                     |
| `/help`                 | Show available commands           |
| `/chat <text>`          | Send a message to the AI          |
| `/reset`                | Reset your AI conversation memory |
| `/add_note <text>`      | Save a personal note              |
| `/show_notes`           | Show your saved notes             |
| `/delete_note <number>` | Delete a note                     |
| `/summarize <number>`   | Summarize a note with AI          |

## 🧠 How Memory Works

The bot creates a separate Gemini chat session for each Telegram user.

For example:

```text
User A → Chat Session A
User B → Chat Session B
User C → Chat Session C
```

This prevents one user's conversation history from being mixed with another user's data.

The bot keeps these sessions in a Python dictionary:

```python
user_chat_sessions = {}
```

When a user sends a message, the bot checks whether that user already has a chat session. If not, it creates one.

```python
def get_or_create_chat(user_id):
    if user_id not in user_chat_sessions:
        user_chat_sessions[user_id] = client.chats.create(
            model="gemini-3.7-flash"
        )

    return user_chat_sessions[user_id]
```

## 📂 Project Structure

```text
telegram-gemini-ai-bot/
│
├── Python.py
├── note.json
├── README.md
├── .gitignore
└── .env
```

### Important

The `.env` file contains your private API keys and should **never be uploaded to GitHub**.

Example:

```env
BOT_TOKEN=your_telegram_bot_token
GEMINI_API_KEY=your_gemini_api_key
```

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/Abolfazl-dd/telegram-gemini-ai-bot.git
```

Move into the project directory:

```bash
cd telegram-gemini-ai-bot
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

Install the required packages:

```bash
pip install python-telegram-bot google-genai python-dotenv
```

Create a `.env` file:

```env
BOT_TOKEN=your_telegram_bot_token
GEMINI_API_KEY=your_gemini_api_key
```

Then run:

```bash
python Python.py
```

## 💡 Example

A user can send:

```text
/chat Explain what an API is
```

The bot sends the message to Gemini and returns the AI response.

The same user can continue the conversation:

```text
/chat Give me a Python example
```

Because the conversation uses the same user-specific chat session, the AI can use the previous context.

## 📝 Notes System

Users can save personal notes directly in Telegram.

Example:

```text
/add_note Learn how Python decorators work
```

Then:

```text
/show_notes
```

The bot displays the saved notes.

A specific note can be summarized with:

```text
/summarize 1
```

And notes can be removed with:

```text
/delete_note 1
```

## 🔄 Reset Memory

Users can reset their AI conversation with:

```text
/reset
```

This removes their current Gemini chat session and allows them to start a new conversation.

## 🎯 What I Learned From This Project

This project helped me practice:

* Telegram bot development
* Asynchronous Python
* API integration
* Working with environment variables
* JSON data storage
* User-specific application state
* AI chatbot development
* Conversation memory
* Error handling
* Git and GitHub
* Writing project documentation

## 🔮 Future Improvements

Possible future improvements include:

* Database instead of JSON storage
* Inline keyboards and buttons
* Better error handling
* Conversation history stored permanently
* Admin commands
* User authentication
* More AI-powered features
* Improved deployment and monitoring

## 👨‍💻 Author

**Abolfazl-dd**

GitHub:
https://github.com/Abolfazl-dd

---

⭐ This project is part of my journey toward becoming an **AI / Machine Learning Engineer**.
