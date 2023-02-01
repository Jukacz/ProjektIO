from flask import Flask, Response, request, jsonify
app = Flask(__name__)


@app.get("/ping")
def ping():
    return Response(status=501)


@app.get("/users_get")
def users_get():
    return Response(status=501)


@app.post("/users_post")
def users_post() -> Response:
    user = request.json
    return jsonify(user), 201


@app.put("/users_put/<id>")
def users_put(id):
    idFromPost = request.json
    return jsonify(idFromPost), 200


@app.patch("/users_patch/<id>")
def users_patch(id):
    user = request.json
    return jsonify(user), 200


@app.delete("/users_delete/<id>")
def users_delete(id):
    return Response(status=204)
