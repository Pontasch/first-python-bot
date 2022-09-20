from flask import Flask
from threading import Thread

templ = '''<!DOCTYPE html>
<html>
<title> My Discord Server </title>
<head>
<body>
<a href="%(href)s">%(size)s</a><br>
</body>
</html>'''
context = {}
context['href'] = 'https://discord.gg/qzC424gG2k'
context['size'] = "Join the Republic of Pekea"
html = templ % context

app = Flask("")

@app.route('/')
def home():
    return html
    

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()