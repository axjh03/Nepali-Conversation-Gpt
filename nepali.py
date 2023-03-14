import speech_recognition as sr
import openai
from gtts import gTTS
import os

# set up OpenAI API key
openai.api_key = "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"

# create a recognizer object
r = sr.Recognizer()

# function to generate response from OpenAI GPT-3 language model
def generate_response(text):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=text,
        temperature=0.5,
        max_tokens=100,
        n=1,
        stop=None,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.choices[0].text.strip()

# use the microphone as the audio source
with sr.Microphone() as source:
    print("अहिले बोल्नुहोस्...")
    audio = r.listen(source)

# recognize speech using Google Speech Recognition
try:
    text = r.recognize_google(audio, language="ne-NP")
    print("तपाईंले भने: {}".format(text))

    # generate response from OpenAI GPT-3 language model
    response_text = generate_response(text)

    # print response text
    print("उत्तर: " + response_text)

    # convert response text to Nepali speech
    speech = gTTS(text=response_text, lang='ne')
    speech.save('output.mp3')

    # play the speech
    os.system('mpg321 output.mp3')

    while True:
        # use the microphone as the audio source
        with sr.Microphone() as source:
            print("अहिले बोल्नुहोस्...")
            audio = r.listen(source)

        # recognize speech using Google Speech Recognition
        try:
            text = r.recognize_google(audio, language="ne-NP")
            print("तपाईंले भने: {}".format(text))

            # generate response from OpenAI GPT-3 language model
            response_text = generate_response(text)

            # print response text
            print("उत्तर: " + response_text)

            # convert response text to Nepali speech
            speech = gTTS(text=response_text, lang='ne')
            speech.save('output.mp3')

            # play the speech
            os.system('mpg321 output.mp3')

        except sr.UnknownValueError:
            print("क्षमा गर्नुहोस्, म भनेको कुनै पनि बुझिनसकेको छैन।")
        except sr.RequestError as e:
            print("क्षमा गर्नुहोस्, Google API संग कनेक्ट गर्दा त्रुटि देखियो। त्रुटि: {}".format(e))

except sr.UnknownValueError:
    print("क्षमा गर्नुहोस्, म भनेको कुनै पनि बुझिनसकेको छैन।")
except sr.RequestError as e:
    print("क्षमा गर्नुहोस्, Google API संग कनेक्ट गर डेटा इन्टरनेट कनेक्सनसँग सम्बन्धित हुन सक्दैन अथवा Google API कुनै समस्या अनुभव गर्दै छ, कृपया नेटवर्क समस्याहरू रेखानुहोस् र फेरि प्रयास गर्नुहोस्। त्रुटि: {}".format(e))
