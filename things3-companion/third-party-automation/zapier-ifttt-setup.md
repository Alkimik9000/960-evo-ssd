# Zapier/IFTTT Setup

1. Create an account on [Zapier](https://zapier.com) or [IFTTT](https://ifttt.com).
2. Create a new Zap/Applet with a **Webhooks** trigger. Choose the option to receive a JSON payload via POST.
3. Copy the generated webhook URL and configure the Android app to send POST requests to it.
4. Add an action to forward this JSON payload to your EC2 webhook handler endpoint (e.g., `http://YOUR_EC2_IP:5000/webhook`).
