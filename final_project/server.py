from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    results=translator.englishToFrench(textToTranslate)
    return results

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    results=translator.frenchToEnglish(textToTranslate)
    return results

@app.route("/")
def renderIndexPage():
    return render_template("index.html")
    # Write the code to render template

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
