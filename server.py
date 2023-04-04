import os

from flask import Flask, render_template, request, redirect, url_for, session

import openai

# for dev
from pprint import pprint

import dotenv
dotenv.load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
openai.api_key = OPENAI_API_KEY

app = Flask(__name__)

# NOTE：View以外の関数が一つだけだったので、分けずにここに配置している。
# 　　　もし増えてきたら、別ファイルに分けてね🙇
def fetch_gpt(sentence):
    
    req_message = f"下記の文はGPTによって生成されたものですか？\n\n{sentence}"
    
    # HACK: しっかりログに
    print('========================')
    print(req_message)
    print('========================')
    
    res = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {'role': 'user', 'content': sentence},
        ]
    )
    
    return res['choices'][0]['message']['content']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/background')
def background():
    return render_template('background.html')

@app.route('/gpt')
def gpt():
    return render_template('gpt.html')

@app.route('/not-gpt')
def not_gpt():
    return render_template('not-gpt.html')

@app.route('/judge/')
def judge():
    req_msg = request.args.get('req_msg')
    # TODO: get gpt res
    res = fetch_gpt(req_msg)
    
    # HACK：しっかりログに
    print('========================')
    pprint(res)
    print('========================')
    
    # TODO: check if the sentence is gpt or not
    if 'はい' in res or 'Yes' in res:
        return render_template('gpt.html')
    else:
        return render_template('not-gpt.html')

if __name__ == '__main__':
    app.run(debug=True)