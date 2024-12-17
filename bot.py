from telegram.ext import Updater, CommandHandler
from damage_calculator import calculate_damage

def calc_damage(update, context):
    try:
        # Example input: /calc charizard flamethrower adamant 100 1.5
        args = context.args
        if len(args) != 5:
            raise ValueError("Invalid input format.")

        pokemon_name = args[0]
        move_name = args[1]
        nature_name = args[2]
        opponent_stat = int(args[3])
        effectiveness = float(args[4])

        # Call the calculate_damage function
        damage = calculate_damage(pokemon_name, move_name, nature_name, opponent_stat, effectiveness)
        update.message.reply_text(damage)
    except Exception as e:
        update.message.reply_text(f"Error: {e}")

def main():
    TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("calc", calc_damage))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
