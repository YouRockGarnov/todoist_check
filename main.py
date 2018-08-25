from flask import Flask, json, request

app = Flask(__name__)



@app.route('/')
def receive():
    print(request.args)

    import json

    r = (requests.post('https://todoist.com/oauth/access_token', {"client_id": "fb26051eb06649bb968791f3d7c2f185",
                                                             "client_secret": "f912232a8fe14128a74bb36577aa6a6f",
                                                             "code": request.args["code"]}))

    obj = json.loads(r.content)
    # print(requests.get("https://beta.todoist.com/API/v8/projects",
    #                    headers={"Authorization": "Bearer %s" % obj['access_token']}).json())

    print(todoist.login_with_api_token(obj['access_token']))
    
    return 200
