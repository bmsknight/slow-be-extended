import math

from flask import Flask, request, jsonify

app = Flask(__name__)

global_n = 100


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
    n = max(n, global_n)
    v = compute_prime(n)
    return jsonify(content)


@app.route('/set-global-n', methods=['POST'])
def set_global_n():
    global global_n
    content = request.get_json()
    n = content["number"]
    global_n = n
    return jsonify({"success": True})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9090, threaded=True)
