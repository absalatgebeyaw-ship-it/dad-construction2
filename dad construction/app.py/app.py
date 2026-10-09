from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit-contact', methods=['POST'])
def submit_contact():
    try:
        data = request.get_json()
        name = data.get('name', 'N/A')
        phone = data.get('phone', 'N/A')
        service_type = data.get('type', 'N/A')
        message = data.get('message', 'N/A')

        print("\n==========================================")
        print("   NEW CLIENT LEAD RECEIVED!")
        print("==========================================")
        print(f" Name:    {name}")
        print(f" Phone:   {phone}")
        print(f" Service: {service_type}")
        print(f" Details: {message}")
        print("==========================================\n")

        return jsonify({
            "status": "success",
            "message": f"Thank you, {name}! We have received your request and will call you at {phone} shortly."
        }), 200
    except Exception as e:
        print(f"Error handling form submission: {e}")
        return jsonify({"status": "error", "message": "Something went wrong!"}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)