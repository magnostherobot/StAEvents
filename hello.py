import os
from flask import Flask, render_template, send_from_directory

app=Flask("MyApp", static_url_path="")

@app.route("/")
def serve_index():
    return render_template("index.html")

@app.route("/assets/<path:filename>")
def serve_assets(filename):
    return send_from_directory("assets", filename)

@app.route("/scripts/<path:filename>")
def serve_scripts(filename):
    return send_from_directory("scripts", filename)

port = int(os.environ.get("PORT", 5000))
app.run(debug=True, host="0.0.0.0", port=port)
