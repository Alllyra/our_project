from nltk.stem import WordNetLemmatizer
import json
from nltk.stem import SnowballStemmer
import pymorphy2
from sklearn.feature_extraction.text import CountVectorizer

morph = pymorphy2.MorphAnalyzer()
snowball = SnowballStemmer(language="russian")
lemmatizer = WordNetLemmatizer()
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
                        'особенно','её','самому','наше','кроме','вообще','вон','мною','никто','это']




def del_punc(text):
    punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for ele in text:
        if ele in punc:
            text = text.replace(ele, "")
    return text


#with open('clean_responsibilities.json', 'r', encoding='utf-8') as f:
#    json_data = json.load(f)
with open('responsibilities.json',encoding="utf8") as f:
    d = json.load(f)


def del_stopwords(json_data,stop_words):
    for i in json_data:
        i["name"] = del_punc(i["name"])
        for i1 in stop_words:
            i["name"]= i["name"].replace(i1,'')
    return json_data

def stemming(json_data):
    for i in json_data:
        for i1 in i["name"].split():
            i["name"]=i["name"].replace(i1,snowball.stem(i1))
    return json_data

def lemming(json_data):
    for i in json_data:
        for i1 in i["name"].split():
            #print(i1)
            i["name"]=i["name"].replace(i1,morph.parse(i1)[0].normal_form)
    return json_data


b=lemming(d)
f=open('responsibilities_lemming.json',"w",encoding="utf8")
json.dump(b, f, ensure_ascii=False)
a=del_stopwords(b,additional_stopwords)
f=open('responsibilities_stop_words.json',"w",encoding="utf8")
json.dump(a, f, ensure_ascii=False)
c=stemming(b)
f=open('responsibilities_stemming.json',"w",encoding="utf8")
json.dump(c, f, ensure_ascii=False)


#count = CountVectorizer(stop_words="english")
#matrix = count.fit_transform(new_text).toarray()