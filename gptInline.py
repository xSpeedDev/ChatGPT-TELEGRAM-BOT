import openai
import telebot
import re

# Configurações do bot e do OpenAI GPT :)
TELEGRAM_TOKEN = 'TELEGRAM_TOKEN'
OPENAI_API_KEY = 'OPENAI_API_KEY'
openai.api_key = OPENAI_API_KEY
bot = telebot.TeleBot(TELEGRAM_TOKEN)

# Função que converte o texto em código usando o OpenAI GPT
def generate_code_from_text(text):
    # Define o prompt e a temperatura para a geração de texto do GPT
    prompt = f'{text}'
    temperature = 1

    # Gera o código usando o OpenAI GPT
    response = openai.Completion.create(
        engine='text-davinci-002',
        prompt=prompt,
        temperature=temperature,
        max_tokens=2048,
        n=1,
        stop=None,
        timeout=0,
    )

    # Extrai e retorna o código gerado pelo GPT
    code = response.choices[0].text.strip()
    return code

# Função que processa as queries inline enviadas pelos usuários
@bot.inline_handler(lambda query: True)
def process_inline_query(query):
    try:
        # Obtém o texto da query
        text = query.query.strip()

        # Gera o código usando o OpenAI GPT
        code = generate_code_from_text(text)

        # Cria a resposta inline com o código gerado
        r = telebot.types.InlineQueryResultArticle(
            id='0',
            title='Código Gerado by @xSpeed#5812:',
            description=code,
            input_message_content=telebot.types.InputTextMessageContent(
                message_text=code
            )
        )
        bot.answer_inline_query(query.id, [r])

    except Exception as e:
        print(e)
print('Bot online! by xSpeed')
# Inicia o bot
bot.polling()
