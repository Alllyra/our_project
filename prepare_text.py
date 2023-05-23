import json
import re
from nltk.corpus import stopwords
from nltk import word_tokenize


additional_stopwords = ['которых','которые','твой','которой','которого',
                        'сих','ком','свой','твоя','этими','слишком','нами',
                        'всему', 'будь','саму','чаще','ваше','сами','наш','затем', 'самих','наши',
                        'ту','каждое','мочь','весь','этим', 'наша','своих','оба',
                        'который','зато','те','этих','вся', 'ваш','такая','теми','ею',
                        'которая','нередко','каждая', 'также','чему','собой','самими',
                        'нем','вами','ими', 'откуда','такие','тому','та','очень','сама','нему',
                        'алло','оно','этому','кому','тобой','таки','твоё', 'каждые','твои','нею','самим','ваши',
                        'ваша','кем','мои','однако','сразу','свое','ними','всё','неё','тех',
                        'хотя','всем','тобою','тебе','одной','другие','само','эта', 'самой',
                        'моё','своей','такое','всею','будут','своего', 'кого','свои','мог','нам',
                        'особенно','её','самому',
'                       наше','кроме','вообще','вон','мною','никто','это']

stop_words = stopwords.words('russian') + additional_stopwords


# Define regular expressions for cleaning
del_n = re.compile('\n')
del_tags = re.compile('<[^>]*>')
del_brackets = re.compile('\([^)]*\)')
clean_text = re.compile('[^а-яa-z\s]')
del_spaces = re.compile('\s{2,}')

def prepare_text(text):
    text = del_n.sub(' ', str(text).lower())
    text = del_tags.sub('', text)
    text = del_brackets.sub('', text)
    res_text = clean_text.sub('', text)
    return del_spaces.sub(' ', res_text)

# Read the JSON file into a Python object
with open('responsibilities.json', 'r', encoding='utf-8') as f:
    json_data = json.load(f)

# Extract the text you want to clean from the object
text_to_clean = []
clean_texts = []

for i in json_data:
    text_to_clean.append(i.get('name'))

for i in text_to_clean:
    if len(prepare_text(i)) > 4:
        clean_texts.append(prepare_text(i))


# Tokenize the cleaned text and remove stop words (optional)



with open('clean_responsibilities.json', 'w', encoding='utf-8') as f:
    json.dump(clean_texts, f, ensure_ascii=False, indent=4)
