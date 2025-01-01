from flask import Flask, request, jsonify
import firebase_admin
from firebase_admin import credentials, messaging

app = Flask(__name__)
firebase_apps = {}

def get_firebase_app(service_account_json, project_id):
    """
    Initialize and retrieve Firebase app for a given service account JSON.
    """
    global firebase_apps
    if project_id in firebase_apps:
        return firebase_apps[project_id]

    cred = credentials.Certificate(service_account_json)
    app_instance = firebase_admin.initialize_app(cred, name=project_id)
    firebase_apps[project_id] = app_instance
    return app_instance

@app.route('/send-notification', methods=['POST'])
def send_notification():
    try:
        data = request.get_json()
        
        service_account_json = data.get('service_account')
        project_id = data.get('project_id')
        
        if not service_account_json or not project_id:
            return jsonify({'success': False, 'error': 'Missing service_account or project_id'}), 400
        
        firebase_app = get_firebase_app(service_account_json, project_id)
        
        topic = data.get('topic')
        token = data.get('token')
        
        notification = messaging.Notification(
            title=data.get('title', 'Default Title'),
            body=data.get('body', 'Default Body')
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
