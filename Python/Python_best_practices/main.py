from collections import Counter
from http import HTTPStatus

from flask import Flask, Response, request

app = Flask(__name__)
storage = Counter()

PIXEL = (
    b'GIF89a\x01\x00\x01\x00\x80\x00\x00\x00'
    b'\x00\x00\xff\xff\xffl\xf9\x04\x01\x00'
    b'\x00\x00\x00,\x00\x00\x00\x00\x01\x00'
    b'\x01\x00\x00\x02\x01D\x00;'
)


@app.route("/track")
def track():
    try:
        referer = request.headers["Referer"]
    except KeyError:
        return Response(status=HTTPStatus.BAD_REQUEST)

    storage[referer] += 1
    return Response(
        PIXEL, headers={
            "Content-Type": "image/gif",
            "Cache-Control": "no-cache, no-store, must-revalidate",
            "Pragma": "no-cache",
        }
    )


@app.route("/stats")
def get_stats():
    return dict(storage.most_common(10))


@app.route('/test')
def test():
    return """<html><head></head><body><img src="/track"></body></html>"""


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
