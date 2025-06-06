from flask import Flask, request, jsonify
import paramiko
import os

app = Flask(__name__)

IPAD_HOST = os.environ.get("IPAD_HOST")
IPAD_USER = os.environ.get("IPAD_USER")
SSH_KEY = os.environ.get("SSH_KEY")
SHORTCUT_NAME = "CreateThingsTask"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'invalid payload'}), 400

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(IPAD_HOST, username=IPAD_USER, key_filename=SSH_KEY)
    payload = json.dumps(data)
    cmd = f"shortcuts://run-shortcut?name={SHORTCUT_NAME}&input=text&text={payload}"
    ssh.exec_command(f"open '{cmd}'")
    ssh.close()
    return jsonify({'status': 'triggered'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
