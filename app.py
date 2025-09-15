from flask import Flask, render_template, send_from_directory
from datetime import timedelta

app = Flask(__name__, static_folder="static", template_folder="templates")

# Optional: disable aggressive caching during dev so CSV updates reflect immediately
@app.after_request
def add_no_cache_headers(resp):
    resp.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
    resp.headers["Pragma"] = "no-cache"
    resp.headers["Expires"] = "0"
    return resp

@app.route("/")
def index():
    return render_template("index.html")

# Optional: explicit CSV route (static already serves it, but this guarantees path)
@app.route("/static/<path:filename>")
def static_files(filename):
    return send_from_directory(app.static_folder, filename, cache_timeout=0)

if __name__ == "__main__":
    # Run: python app.py
    app.run(host="0.0.0.0", port=5000, debug=True)
