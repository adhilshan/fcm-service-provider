# FCM Service Provider API

This project provides an API for sending Firebase Cloud Messaging (FCM) notifications dynamically by allowing you to configure the Firebase service account JSON and target multiple Firebase projects. The service is hosted on Vercel, making it accessible at [https://fcm-service-provider.vercel.app/](https://fcm-service-provider.vercel.app/).

## Features
- Dynamically configure Firebase service accounts per request.
- Support for sending notifications to individual device tokens or to topics for broadcasting.
- Hosted on Vercel with request logs available for monitoring.

---

## API Endpoints

### **POST** `/send-notification`

#### **Request Body**
- **`service_account`** (required): The Firebase service account JSON object for the project you wish to use.
- **`project_id`** (required): The Firebase project ID.
- **`token`** (optional): The device token to send a notification to.
- **`topic`** (optional): The topic name to send a notification to (for broadcasting).
- **`title`** (optional): Title of the notification. Default: "Default Title".
- **`body`** (optional): Body of the notification. Default: "Default Body".
- **`data`** (optional): Key-value pair object for custom data to include with the notification.

#### **Example Request**
1. **Send to a Topic (Broadcast Notification)**:
```json
{
   "type": "service_account",
   "project_id": "your-project-id",
   "private_key_id": "your-private-key-id",
   "private_key": "-----BEGIN PRIVATE KEY-----\n...\n-----END PRIVATE KEY-----\n",
   "client_email": "firebase-adminsdk@your-project-id.iam.gserviceaccount.com",
   "client_id": "your-client-id",
   "auth_uri": "https://accounts.google.com/o/oauth2/auth",
   "token_uri": "https://oauth2.googleapis.com/token",
   "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
   "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk%40your-project-id.iam.gserviceaccount.com"
  "topic": "all-users",
  "title": "Broadcast Title",
  "body": "This is a broadcast notification.",
  "data": {
    "key1": "value1",
    "key2": "value2"
  }
}
```

2. **Send to an Individual Token**:
```json
{
   "type": "service_account",
   "project_id": "your-project-id",
   "private_key_id": "your-private-key-id",
   "private_key": "-----BEGIN PRIVATE KEY-----\n...\n-----END PRIVATE KEY-----\n",
   "client_email": "firebase-adminsdk@your-project-id.iam.gserviceaccount.com",
   "client_id": "your-client-id",
   "auth_uri": "https://accounts.google.com/o/oauth2/auth",
   "token_uri": "https://oauth2.googleapis.com/token",
   "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
   "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk%40your-project-id.iam.gserviceaccount.com"
  "project_id": "your-project-id",
  "token": "device_token_here",
  "title": "Direct Title",
  "body": "This is a direct notification.",
  "data": {
    "key1": "value1",
    "key2": "value2"
  }
}
```

#### **Response**
- **`200 OK`**: Notification was sent successfully.
- **`400 Bad Request`**: Missing required fields.
- **`500 Internal Server Error`**: Error occurred during processing.

---

## Logs and Data Collection
- **Request Logs**: Vercel automatically logs all incoming requests and payloads. Logs include sensitive information such as the service account JSON, project ID, tokens, and notification data.
  - Ensure that sensitive data is managed responsibly to avoid unintentional exposure.
  - Use environment-specific restrictions on your Firebase service accounts.

---

## Setup and Usage

### **1. Host on Vercel**
1. Clone this repository to your local machine.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Deploy to Vercel:
   - Use the Vercel CLI to deploy:
     ```bash
     vercel deploy
     ```

### **2. Local Development**
Run the Flask app locally:
```bash
python app.py
```

### **3. Test the API**
Use tools like Postman or `curl` to send requests to the hosted endpoint or local server.

---

## Security Recommendations
1. **Service Account Security**:
   - Avoid sharing your service account JSON publicly.
   - Rotate keys periodically.
2. **API Access**:
   - Implement authentication or IP whitelisting to restrict access to the API.
3. **Log Management**:
   - Monitor Vercel logs regularly for unauthorized access attempts or anomalies.
   - Configure log retention policies in Vercel if sensitive information is present.

---

## Contributing
Feel free to contribute to this project by submitting issues or pull requests. Please ensure your changes are well-documented and tested.

---

## License
This project is licensed under the MIT License. See the LICENSE file for more details.


<hr>


[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fvercel%2Fexamples%2Ftree%2Fmain%2Fpython%2Fflask3&demo-title=Flask%203%20%2B%20Vercel&demo-description=Use%20Flask%203%20on%20Vercel%20with%20Serverless%20Functions%20using%20the%20Python%20Runtime.&demo-url=https%3A%2F%2Fflask3-python-template.vercel.app%2F&demo-image=https://assets.vercel.com/image/upload/v1669994156/random/flask.png)

# Flask + Vercel

This example shows how to use Flask 3 on Vercel with Serverless Functions using the [Python Runtime](https://vercel.com/docs/concepts/functions/serverless-functions/runtimes/python).

## Demo

https://flask-python-template.vercel.app/

## How it Works

This example uses the Web Server Gateway Interface (WSGI) with Flask to enable handling requests on Vercel with Serverless Functions.

## Running Locally

```bash
npm i -g vercel
vercel dev
```

Your Flask application is now available at `http://localhost:3000`.

## One-Click Deploy

Deploy the example using [Vercel](https://vercel.com?utm_source=github&utm_medium=readme&utm_campaign=vercel-examples):

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fvercel%2Fexamples%2Ftree%2Fmain%2Fpython%2Fflask3&demo-title=Flask%203%20%2B%20Vercel&demo-description=Use%20Flask%203%20on%20Vercel%20with%20Serverless%20Functions%20using%20the%20Python%20Runtime.&demo-url=https%3A%2F%2Fflask3-python-template.vercel.app%2F&demo-image=https://assets.vercel.com/image/upload/v1669994156/random/flask.png)
