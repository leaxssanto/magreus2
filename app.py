from flask import Flask

app = Flask(__name__)

html_content = """
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MagreusElleticisi</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #111;
            color: #eee;
            margin: 0;
            padding: 0;
        }
        header, section, footer {
            padding: 40px;
            text-align: center;
        }
        header {
            background-color: #222;
            font-size: 2em;
        }
        section {
            margin: 20px 0;
        }
        a {
            color: #1DA1F2;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>

    <header>
       BEN MAGREUS BEN GAYİM
    </header>

    <section id="about">
        <h2>Hakkında</h2>
        <p>BEN MAGREUS ELLETİYORUM </p>
    </section>

    <section id="contact">
        <h2>İletişim</h2>
        <p>Instagram: <a href="https://instagram.com/747magreus" target="_blank">@747magreus</a></p>
    </section>

    <footer>
        &copy; 2025 Magreus
    </footer>

</body>
</html>
"""

@app.route('/')
def index():
    return html_content