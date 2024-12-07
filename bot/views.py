from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from telebot import TeleBot, types
from telebot.types import Message

bot = TeleBot('7617005963:AAEMA5DGh7gP-Rydou4FVtq-Ut9P9_Q2Jx4')


@bot.message_handler(commands=['start'])
def start(message: Message):
    user_id = message.from_user.id
    bot.send_message(user_id, 'Salom')


@csrf_exempt
def webhook(request):
    if request.method == 'POST':
        json_str = request.body.decode('utf-8')
        update = types.Update.de_json(json_str)
        bot.process_new_updates([update])
        return JsonResponse({"status": "success"})
    return JsonResponse({"error": "Invalid request"})
