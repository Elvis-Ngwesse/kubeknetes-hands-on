from flask import Flask, request, jsonify
import json
import base64

app = Flask(__name__)

# Admission Webhook: Mutate incoming Kubernetes objects
@app.route('/mutate', methods=['POST'])
def mutate():
    admission_review = request.get_json()

    # Create a JSON patch to modify the object (e.g., add a label)
    patch = [
        {
            "op": "add",
            "path": "/metadata/labels/example-mutating-webhook",
            "value": "mutated"
        }
    ]

    # Base64 encode the patch (required by Kubernetes)
    patch_b64 = base64.b64encode(json.dumps(patch).encode()).decode()

    admission_response = {
        "uid": admission_review['request']['uid'],
        "allowed": True,
        "patchType": "JSONPatch",
        "patch": patch_b64
    }

    return jsonify({"response": admission_response})


# Event Webhook: Handle external events
@app.route('/event', methods=['POST'])
def event():
    event_data = request.get_json()
    
    # Log the event (or process it as needed)
    print("Received Event:", json.dumps(event_data, indent=2))

    return jsonify({"status": "success", "message": "Event received"}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, ssl_context=('cert.pem', 'key.pem'))
