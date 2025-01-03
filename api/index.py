from flask import Flask, request, jsonify
import firebase_admin
from firebase_admin import credentials, messaging

app = Flask(__name__)
firebase_apps = {}

def get_firebase_app(service_account_json, project_id):
    global firebase_apps
    if project_id in firebase_apps:
        return firebase_apps[project_id]

    cred = credentials.Certificate(service_account_json)
    app_instance = firebase_admin.initialize_app(cred, name=project_id)
    firebase_apps[project_id] = app_instance
    return app_instance

@app.route('/api/send-notification', methods=['POST'])
def send_notification():
    try:
        data = request.get_json()

        service_account_json = {
            "type": data.get("type"),
            "project_id": data.get("project_id"),
            "private_key_id": data.get("private_key_id"),
            "private_key": data.get("private_key"),
            "client_email": data.get("client_email"),
            "client_id": data.get("client_id"),
            "auth_uri": data.get("auth_uri"),
            "token_uri": data.get("token_uri"),
            "auth_provider_x509_cert_url": data.get("auth_provider_x509_cert_url"),
            "client_x509_cert_url": data.get("client_x509_cert_url"),
        }
        project_id = data.get("project_id")

        if not service_account_json or not project_id:
            return jsonify({'success': False, 'error': 'Missing service_account or project_id'}), 400

        firebase_app = get_firebase_app(service_account_json, project_id)

        topic = data.get('topic')
        token = data.get('token')

        img_url = data.get('img_url', '')

        notification = messaging.Notification(
            title=data.get('title', 'Default Title'),
            body=data.get('body', 'Default Body'),
            image=img_url if img_url.strip() else None  # Include image if not empty
        )

        additional_data = data.get('data', {})

        if topic:
            message = messaging.Message(
                notification=notification,
                data=additional_data,
                topic=topic,
            )
        elif token:
            message = messaging.Message(
                notification=notification,
                data=additional_data,
                token=token,
            )
        else:
            return jsonify({'success': False, 'error': 'Missing topic or token'}), 400

        response = messaging.send(message, app=firebase_app)
        return jsonify({'success': True, 'response': response}), 200

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
    
