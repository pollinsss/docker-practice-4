import os
from flask import Flask
from datetime import datetime

app = Flask(__name__)

DATA_DIR = '/data'
COUNTER_FILE = os.path.join(DATA_DIR, 'counter.txt')


@app.route('/')
def hello():
    os.makedirs(DATA_DIR, exist_ok=True)

    count = 0
    if os.path.exists(COUNTER_FILE):
        with open(COUNTER_FILE, 'r') as f:
            count = int(f.read().strip())

    count += 1

    with open(COUNTER_FILE, 'w') as f:
        f.write(str(count))

    return (
        f"Hello from Docker!<br>"
        f"Время: {datetime.now().strftime('%H:%M:%S')}<br>"
        f"Количество посещений: {count}"
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
