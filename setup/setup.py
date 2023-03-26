import logging
import openai

from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackContext, Filters
from telegram import Update, ForceReply

openai.api_key = "my key"

TELEGRAM_API_KEY = "my key"
