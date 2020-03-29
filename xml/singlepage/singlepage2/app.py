from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

texts = ['I heard the echo, from the valleys and the heart. Open to the lonely soul of sickle harvesting. Repeat outrightly, but also repeat the well-being of. Eventually swaying in the desert oasis. I believe I am. Born as the bright summer flowers. Do not withered undefeated fiery demon rule. Heart rate and breathing to bear the load of the cumbersome. Bored',
        'I heard the music, from the moon and carcass. Auxiliary extreme aestheticism bait to capture misty. Filling the intense life, but also filling the pure. There are always memories throughout the earth. I believe I am. Died as the quiet beauty of autumn leaves. Sheng is not chaos, smoke gesture. Even wilt also retained bone proudly Qing Feng muscle. Occult',
        'I hear love, I believe in love. Love is a pool of struggling blue-green algae. As desolate micro-burst of wind. Bleeding through my veins. Years stationed in the belief', 
        'I believe that all can hear. Even anticipate discrete, I met the other their own. Some can not grasp the moment. Left to the East to go West, the dead must not return to nowhere. See, I wear Zan Flowers on my head, in full bloom along the way all the way. Frequently missed some, but also deeply moved by wind, frost, snow or rain',
        'Prajna Paramita, soon as soon as life be beautiful like summer flowers and death like autumn leaves. Also care about what has']

@app.route('/first')
def first():
    return texts[0]

@app.route('/second')
def second():
    return texts[1]

@app.route('/third')
def third():
    return texts[2]

@app.route('/fourth')
def fourth():
    return texts[3]

@app.route('/fifth')
def fifth():
    return texts[4]