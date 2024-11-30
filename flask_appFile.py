from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Lambda Function URL
LAMBDA_FUNCTION_URL = 'https://ld6xbpwhq6kwmrkroovdd4j5aq0euyjy.lambda-url.us-east-1.on.aws/'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    user_message = request.json.get('message', '')

    # Send user message to Lambda function
    lambda_response = call_lambda_function(user_message)

    return jsonify(lambda_response)

def call_lambda_function(user_message):
    # Payload for Lambda function
    payload = {"message": user_message}

    try:
        # Call the Lambda function via HTTP POST request
        response = requests.post(LAMBDA_FUNCTION_URL, json=payload)

        if response.status_code == 200:
            # Parse the response from Lambda
            return response.json()
        else:
            return {"response_text": "Sorry, there was an issue with the server. Please try again later."}
    except Exception as e:
        # Handle errors in calling the Lambda function
        return {"response_text": f"Error occurred: {str(e)}"}

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)