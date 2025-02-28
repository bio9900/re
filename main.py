import aiohttp
from flask import Flask, jsonify, request


app = Flask(__name__)


@app.route("/<path:path>", methods=["GET", "POST", "PUT",
"DELETE"])
async def main(path):
    if request.get_data():
        payload = request.get_json()
    else:
        payload = None

    headers = dict(request.headers)
    headers.pop("Host", None)
    headers.pop("Content-Length", None)

    async with aiohttp.request(
        request.method,
        f"https://gw.sandboxol.com/{path}",
        headers=headers,
        json=payload,
        ssl=False
    ) as response:
        return jsonify(await response.json())


app.run()
