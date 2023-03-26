def start(update: Update, _: CallbackContext) -> None:
    user = update.effective_user
    update.message.reply_markdown_v2(fr'Hi {user.mention_markdown_v2()}\! Please describe the incident you would like to report:')
    

def incident_report(update: Update, context: CallbackContext) -> None:
    incident_description = update.message.text
    manager_response, resident_response = analyze_incident(incident_description)
    
    chat_id = update.message.chat_id
    
    
    
    
    user = update.message.from_user
    nickname = user.username  # This is the sender's nickname (username)
    first_name = user.first_name  # This is the sender's first name
    logging.info(f"{nickname} named {first_name} response: {update.message.text}")


    update.message.reply_text(f"Thank you for reporting the incident. We've notified the manager.\n")
    update.message.reply_text(f"For the manager: {manager_response}\n\nFor the resident: {resident_response} ")
    update.message.reply_text(f"Is there anything I can help you with?")
    
  
    
 
    context.bot.send_message(
        chat_id= <manager's Id>,
        text=f"{nickname} named {first_name} reported an incident: {manager_response}"
    )
    
    
    
    
def unknown(update: Update, _: CallbackContext) -> None:
    update.message.reply_text("Sorry, I didn't understand that command.")

def main() -> None:
    updater = Updater(TELEGRAM_API_KEY)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, incident_report))
    dispatcher.add_handler(MessageHandler(Filters.command, unknown))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
    
