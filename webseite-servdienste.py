from flask import Flask, render_template_string

app = Flask(__name__)

# Dein HTML-Code als Template
html_code = """
<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Serverdienste Dashboard</title>
    <style>
        /* --- Dein CSS von der HTML-Datei --- */
        @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600&family=Inter:wght@400;500;600&display=swap');
        body { font-family: 'Inter', sans-serif; background: #1a1a1a; color: #e0e0e0; min-height: 100vh; }
        .container { max-width: 1400px; margin: 0 auto; padding: 20px; }
        /* ... (den kompletten CSS-Teil hier einfügen) ... */
    </style>
</head>
<body>
    <!-- Dein kompletter HTML-Body -->
    <div class="container">
        <div class="header">
            <button class="back-button" id="backButton" onclick="goBack()">← Zurück</button>
            <h1>💻 Serverdienste</h1>
            <p>Übersicht und Analyse der verfügbaren Server-Services</p>
        </div>
        <div class="services-grid" id="servicesGrid">
            <!-- ... alle Service-Cards usw. hier einfügen ... -->
        </div>
        <div class="service-details" id="serviceDetails"></div>
        <div class="author-tab" id="authorTab" onclick="toggleAuthorDetails()">Autoren</div>
        <div class="author-details" id="authorDetails">
            <h5>Entwickelt von:</h5>
            <ul>
                <li>Lukas Langlets</li>
                <li>Jonas Kern</li>
                <li>Fabian Funke</li>
                <li>Hauke Götz</li>
            </ul>
        </div>
    </div>

    <script>
        // Dein kompletter JavaScript-Teil aus der HTML-Datei hier einfügen
    </script>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(html_code)

if __name__ == "__main__":
    app.run(debug=True)
