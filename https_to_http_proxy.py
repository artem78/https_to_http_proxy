from flask import Flask, request, url_for, Response
import requests

app = Flask(__name__)

@app.route("/proxy")
def proxy():
    url = request.args.get('url')
    if not url:
        return 'Argument "url" is missed, usage: ' + url_for('proxy', _external=True, url="https://example.com/"), 400
    else:
        #return "url:" + url
        try:
            headers = {}
            user_agent = request.headers.get('User-Agent')
            if user_agent:
                headers['User-Agent'] = user_agent
            # todo:what about pass other headers?
            r = requests.get(url, headers=headers)
        except Exception as e:
            return str(e), 500
        
        return Response(
            response=r.content,
            status=r.status_code,
            headers=dict(r.headers)
        )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8088)