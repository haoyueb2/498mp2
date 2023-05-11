from flask import Flask, request
import subprocess
import socket

app = Flask(__name__)

@app.route('/', methods=['POST'])
def start_cpu_stress():
    # Start a separate process for running stress_cpu.py
    subprocess.Popen(['python3', 'stress_cpu.py'])
    return 'CPU stress started'

@app.route('/', methods=['GET'])
def get_private_ip():
    # Get the private IP address of the EC2 instance
    private_ip = socket.gethostbyname(socket.gethostname())
    return f'Private IP: {private_ip}'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
