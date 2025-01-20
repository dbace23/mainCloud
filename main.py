import logging
from flask import Flask, request
from scraper import scraping_tennis

app = Flask(__name__)

@app.route("/", methods=["POST"])
def run_scraper():
    try:
        response = scraping_tennis()
        return {"status": "success", "message": response}, 200
    except Exception as exc:
        logging.error(exc)
        return {"status": "error", "message": str(exc)}, 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
