from flask import Flask, jsonify, request

from SentenceTransformers import SentenceTransformers

app = Flask(__name__)


@app.route('/doc/embedding/<transformer>', methods=['POST'])
def get_doc_embedding(transformer):
    return jsonify(SentenceTransformers.get_transformer(transformer).encode(request.json).tolist())


if __name__ == '__main__':
    app.run()
