import asyncio

from flask import Flask, request, abort
from waitress import serve
from .freezone import webhook_handlers

app = Flask(__name__)




class Webhooks:
    def run_webhook(self, url=None, loop=None, port=3000, route="/webhook", host="0.0.0.0", monobank_ip=None):
        if url:
            if loop:
                loop.create_task(self.activate_webhook(url))

            else:
                loop = asyncio.get_event_loop()
                loop.create_task(self.activate_webhook(url))
        self.__webhook_route(port, route, host, monobank_ip)

    async def activate_webhook(self, url):
        await asyncio.sleep(1)
        self.create_webhook(url)

    def create_webhook(self, url):
        raise NotImplementedError("Please implement create_webhook")

    def __webhook_route(self, port, route, host, monobank_ip):
        print(request.remote_addr)
        @app.route(f"{route}", methods=["POST"])
        def webhook_page():
            if monobank_ip:
                if request.remote_addr != monobank_ip:
                    abort(305)
                    return "Use Proxy", 305

            if request.method == "POST":
                req = request.json
                try:
                    if req["type"] != "StatementItem":

                        return "OK", 200

                    data = req["data"]["statementItem"]
                except KeyError:
                    return 200
                for handler in webhook_handlers:
                    func, amount, comment, may_be_bigger, account = handler
                    if amount == abs(data["amount"]) or (amount <= abs(data["amount"]) and may_be_bigger):
                        if comment:
                            try:

                                if comment != data["comment"]:

                                    continue
                            except KeyError:
                                continue
                        if account:
                            if req["data"]["account"] != account:
                                continue

                        if asyncio.iscoroutinefunction(func):
                            loop = asyncio.get_event_loop()
                            loop.create_task(func(data))
                        else:
                            func(data)
                return "OK", 200
            else:
                abort(400)

        serve(app, host=host, port=port)
if __name__ == '__main__':
    serve(app, host="0.0.0.0", port=3000)
