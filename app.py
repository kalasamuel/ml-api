from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

# load your trained model
with open('association_rules.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return 'ML API is running! 🎉'

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        stock = data['stock']
        sales_velocity = data['salesVelocity']
        days_to_expiry = data['daysToExpiry']
        category = data['category']
        # adjust to your model input
        X = [[stock, sales_velocity, days_to_expiry]]  # example
        prediction = model.predict(X)[0]
        return jsonify({'prediction': prediction})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
