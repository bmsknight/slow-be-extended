import math,time

from flask import Flask, request, jsonify

app = Flask(__name__)


def compute_prime(num):
    prime_list = []
    for count in range(num + 1):
        isprime = True

        for x in range(2, int(math.sqrt(count) + 1)):
            if count % x == 0:
                isprime = False
                break

        if isprime:
            prime_list.append(count)

    return prime_list


@app.route('/')
def info():
    return "Sample app to imitate latency..."


@app.route('/echo', methods=['POST'])
def normal_echo():
    content = request.get_json()
    print(content)
    return jsonify(content)


@app.route('/echo-with-process', methods=['POST'])
def echo_with_process():
    content = request.get_json()
    n = content["number"]
    v = compute_prime(n)
    return jsonify(content)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9090, threaded=True)
