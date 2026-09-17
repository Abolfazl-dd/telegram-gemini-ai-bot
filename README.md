# Telegram Gemini AI Assistant

A Python Telegram bot that integrates the Google GenAI SDK to provide conversational memory, note management, and AI text summarization.

## Features

- **Context-Aware Chat:** Uses Gemini chat sessions to retain conversation history.
- **Isolated User Sessions:** Stores separate chat threads for each Telegram user ID.
- **Session Reset:** Deletes current conversation history on demand with `/reset`.
- **Note Management:** Saves, displays, and deletes personal notes with JSON persistence.
- **AI Note Summarization:** Generates summaries of saved notes directly with Gemini.
- **Secure Configuration:** Protects API keys and bot tokens through `.env` variables.

## Tech Stack

- **Language:** Python 3.10+
- **Telegram Library:** `python-telegram-bot`
- **AI SDK:** `google-genai`
- **Configuration:** `python-dotenv`
- **Storage:** JSON file storage

## Installation

1. Clone the repository:
   ```bash
   git clone [https://github.com/Abolfazl-dd/telegram-gemini-ai-bot.git](https://github.com/Abolfazl-dd/telegram-gemini-ai-bot.git)
   cd telegram-gemini-ai-bot
