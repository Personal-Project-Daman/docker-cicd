from flask import Flask

app = Flask(__name__)

def page(message):
    html = """
        <html>
        <head lang> 
            <meta charset="utf-8">
            <title>Index</title>
        </head>
        <body>
            <div style='font-size:60px;'>
            <center>
                {0}<br>
            </center>
            </div>
        </body>
        </html>""".format(message)
    return html

@app.route('/')
def get_page():
    message = "Hello!!! Welcome to the world of NordCloud ;)"
    return page(message)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
