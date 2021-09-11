import pyttsx3
import webbrowser
import datetime
import pywhatkit
import yfinance as yf
import pyjokes
import speech_recognition as sr
import pyaudio
import wikipedia

#listen our microphone and return to text using google

def transform():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.8
        said =  r.listen(source)
        try:
            print("iam all ears")
            q = r.recognize_google(said, language="en")
            return q
        except sr.UnknownValueError:
       
            print("Sorry i did not understand")
            return "iam waiting"
        except sr.RequestError:
            print("Sorry the service is down ")
            
            return "iam waiting"
       
        except :
            return "iam waiting"

#speaking test

def speaking(message):
    engine = pyttsx3.init()
    engine.say(message)
    engine.runAndWait()

def query_day():
    day = datetime.date.today()
    weekday = day.weekday()
    mapping = { 0:'Monday', 1:'tuesday', 2: 'Wednesday', 3:'Thursday', 4:'Friday', 5:'Saturday', 6:'Sunday'}
    try:
        speaking(f'Today is {mapping[weekday]}')
    except:
        pass


##returns the time
def query_time():
    time = datetime.date.now().strftime('%I:%M:%S')
    speaking(f"{time[1]} o'clock and {time[3:5]}minutes")

##greetings from our bot
def whatsapp():
    speaking('''HI, my name is bot. I am your personal assistent. How may i help you''')


###main body
def main():
    whatsapp()
    start = True
    while (start):
        q = transform().lower() 
        if 'start youtube' in q:
            speaking('starting youtube. just a second')
            webbrowser.open('https://www.youtube.com')
            continue
        elif 'start web browser' in q:
            speaking('Starting web browser. hold on')
            webbrowser.open('https://www.google.com')
            continue
        elif 'what is the day' in q:
            query_day()
            continue
        elif 'what is the time' in q:
            query_time()
            continue
        elif 'shutdown' in q:
            speaking('ok shutting down')
            break
        elif 'from wikipedia' in q:
            speaking("checking wikipedia")
            q = q.replace("wikipedia","")
            result = wikipedia.summary(q, sentences=2)
            speaking('found on wikipedia')
            speaking(result)
            continue
        elif 'your name' in q:
            speaking('iam bot ,your VA')
            continue
        elif 'play' in q:
            speaking(f'playing {q}')
            pywhatkit.playonyt(q)
            continue
        elif 'search web' in q:
            pywhatkit.search(q)
            speaking('that is what i found')
            continue
        elif 'joke' in q:
            speaking(pyjokes.get_jokes())
            continue
        elif 'stock price' in q:
            search = q.split('of')[-1].strip()
            lookup = {'apple':'AAPL',
                      'Amazon':'AMZN',
                      'google' :'GOOGL',}
            try:
                stock = lookup[search]
                stock = yf.Ticker(stock)
                counterprice = stock.info["regularMarketPrice"]
                speaking(f'found it, the price for {search} is {counterprice}')
                continue
            except:
                speaking(f'sorry i have no data for {search}')
                continue 
main()