from flask import Flask, render_template, request
import telebot
from config import TOKEN

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/message', methods=['POST','GET'])
def message():
    status = None
    
    if request.method == 'POST':
        message = request.form.get('message')
        bot = telebot.TeleBot(TOKEN)
        try:
            bot.send_message(6673359808, message)
            status = 'Sent.'
        except:
            status = 'Error.'
        
        
        
    
    return render_template('message.html', status=status)


if __name__ == '__main__':
    app.run(debug=True)