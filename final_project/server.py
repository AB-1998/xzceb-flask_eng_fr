from machinetranslation import translator
from flask import Flask, render_template, request
import json
import machinetranslation
app = Flask("Web Translator")

@app.route("/englishToFrench/<text>")
def englishToFrench(text):
    textToTranslate = request.args.get('text')


    # Write your code here
    return "Translated text to French :"+translator.english_to_french(textToTranslate)

@app.route("/frenchToEnglish/<text>")
def frenchToEnglish(text):
    textToTranslate = request.args.get('text')
    
    # Write your code here
    return "Translated text to English :"+translator.french_to_english(textToTranslate)

@app.route("/")
def renderIndexPage():
    # Write the code to render template
    render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
