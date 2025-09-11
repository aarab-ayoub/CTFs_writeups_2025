import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, ConversationHandler

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

# Define conversation states
AUTHENTICATE, LEVEL1, LEVEL2, LEVEL3, LEVEL4, LEVEL5 = range(6)

# Challenge data
AUTH_PASSPHRASE = "calma calma!"  # Participants need to find this elsewhere in your CTF
LEVEL1_ANSWER = "steganography"
LEVEL2_ANSWER = "18395721"  # Answer to a math or crypto puzzle
LEVEL3_ANSWER = "bluewhaleswim"  # Answer to a riddle
LEVEL4_ANSWER = "xor1337"  # Answer to a programming challenge
FLAG = "MED{R0n4ld0_C4lm4_0r4cl3_m4st3r}"

# Initial welcome handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text(
        "Welcome to the Obfuscated Oracle.\n\n"
        "You've found the hidden path, but your journey has just begun.\n"
        "To proceed, authenticate with the passphrase."
    )
    return AUTHENTICATE

# Authentication handler
async def authenticate(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    if update.message.text == AUTH_PASSPHRASE:
        await update.message.reply_text(
            "Authentication successful.\n\n"
            "LEVEL 1: Decrypt this message to proceed:\n"
            "01001001 00100000 01100001 01101101 00100000 01110100 01101000 01100101 00100000 "
            "01110100 01100101 01100011 01101000 01101110 01101001 01110001 01110101 01100101 "
            "00100000 01101111 01100110 00100000 01101000 01101001 01100100 01101001 01101110 "
            "01100111 00100000 01100100 01100001 01110100 01100001 00100000 01101001 01101110 "
            "00100000 01110000 01101100 01100001 01101001 01101110 00100000 01110011 01101001 "
            "01100111 01101000 01110100"
        )
        return LEVEL1
    else:
        await update.message.reply_text("Incorrect passphrase. Try again.")
        return AUTHENTICATE

# Level 1 handler
async def level1(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    if update.message.text.lower() == LEVEL1_ANSWER:
        await update.message.reply_text(
            "Correct! You've completed Level 1.\n\n"
            "LEVEL 2: Solve this cryptographic sequence:\n"
            "Calculate: (17^23) % 31337 + 1337"
        )
        return LEVEL2
    else:
        await update.message.reply_text("Incorrect. Try again.")
        return LEVEL1

# Level 2 handler
async def level2(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    if update.message.text == LEVEL2_ANSWER:
        await update.message.reply_text(
            "Impressive! You've completed Level 2.\n\n"
            "LEVEL 3: Solve this riddle:\n"
            "I'm the largest mammal on Earth,\n"
            "In oceans deep I roam.\n"
            "My heart beats just ten times per minute,\n"
            "As through dark waters I swim alone.\n"
            "What am I and what do I do? (one word for each, no spaces)"
        )
        return LEVEL3
    else:
        await update.message.reply_text("Incorrect. Try again.")
        return LEVEL2

# Level 3 handler
async def level3(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    if update.message.text.lower() == LEVEL3_ANSWER:
        await update.message.reply_text(
            "Brilliant! You've completed Level 3.\n\n"
            "LEVEL 4: Complete this programming challenge:\n"
            "Write a function that XORs each byte of 'ronaldo' with the hex value 0x13.\n"
            "What operation and value did you use? (format: operation+value)"
        )
        return LEVEL4
    else:
        await update.message.reply_text("Incorrect. Try again.")
        return LEVEL3

# Level 4 handler
async def level4(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    if update.message.text.lower() == LEVEL4_ANSWER:
        await update.message.reply_text(
            "Outstanding! You've reached the final challenge.\n\n"
            "LEVEL 5 - FINAL CHALLENGE:\n"
            "Combine the following clues to find the hidden message:\n"
            "1. The first letters of each correct answer you've provided\n"
            "2. Ronaldo's jersey number at Real Madrid\n"
            "3. The name of his celebration\n\n"
            "Format your answer as: answer1+number+passfrase[0]"
        )
        return LEVEL5
    else:
        await update.message.reply_text("Incorrect. Try again.")
        return LEVEL4

# Final level handler
async def level5(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    expected_answer = "sbx+7+calma"  # First letters of previous answers + Ronaldo's number + celebration name
    
    if update.message.text.lower() == expected_answer:
        await update.message.reply_text(
            f"CONGRATULATIONS! You've mastered the Obfuscated Oracle!\n\n"
            f"Here's your flag: {FLAG}"
        )
        return ConversationHandler.END
    else:
        await update.message.reply_text("Incorrect. Try again.")
        return LEVEL5

# Cancel conversation handler
async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text("Challenge aborted. Use /start to begin again.")
    return ConversationHandler.END

def main() -> None:
    # Create application
    application = Application.builder().token("8118975932:AAEx5L5lnJTxncPKmlqud4j08qv0Y4m7fIQ").build()

    # Add conversation handler
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            AUTHENTICATE: [MessageHandler(filters.TEXT & ~filters.COMMAND, authenticate)],
            LEVEL1: [MessageHandler(filters.TEXT & ~filters.COMMAND, level1)],
            LEVEL2: [MessageHandler(filters.TEXT & ~filters.COMMAND, level2)],
            LEVEL3: [MessageHandler(filters.TEXT & ~filters.COMMAND, level3)],
            LEVEL4: [MessageHandler(filters.TEXT & ~filters.COMMAND, level4)],
            LEVEL5: [MessageHandler(filters.TEXT & ~filters.COMMAND, level5)],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )

    application.add_handler(conv_handler)

    # Run the bot
    application.run_polling()

if __name__ == "__main__":
    main()
