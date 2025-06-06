# Webhook Handler

A minimal Flask server that receives POST requests from Zapier or IFTTT and triggers an Apple Shortcut on a dedicated iPad via SSH.

Set the following environment variables before running:

- `IPAD_HOST` – iPad hostname or IP address
- `IPAD_USER` – SSH username
- `SSH_KEY` – path to the private key for authentication

Run the server:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python server.py
```
