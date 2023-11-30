import traceback

from flask import Flask, request, jsonify
from driver import Driver
from loguru import logger


BASE_URL = "/api/"


app = Flask(__name__)
driver = Driver()


@app.route(f"{BASE_URL}summary/", methods=['POST'])
def get_summary_of_url():
    url = request.get_json().get('url')
    if not url:
        return jsonify({"message": "Please specify a url"}), 400
    try:
        summary = driver.get_summary(url)
    except Exception:
        exception_traceback = traceback.format_exc()
        logger.error(f"Error processing: {exception_traceback}")
        return jsonify({"message": "Error processing the request"}), 500
    if summary is None:
        return jsonify({"message": "Please specify a valid url"}), 400
    return jsonify({'summary': summary}), 200


if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=5000)
