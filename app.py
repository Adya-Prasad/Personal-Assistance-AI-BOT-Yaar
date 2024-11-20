from flask import Flask, render_template, request, jsonify
from modules.joke_module import get_random_joke
from modules.mood_module import get_mood_response

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/docs')
def docs():
    return render_template('docs.html')

@app.route('/chat')
def chat():
    return render_template('index2.html')

@app.route('/get-response', methods=['POST'])
def get_response():
    user_message = request.form['message']
    mood = request.form.get('mood', 'neutral')  # Default to 'neutral' if no mood is selected

    print(f"User Message: {user_message}, Mood: {mood}")

    # Check specific phrases to adjust the response based on user message content
    if "not feeling well" in user_message.lower() or "stomach pain" in user_message.lower():
        return jsonify({"response": "I'm really sorry to hear that. It’s important to take care of yourself. Is there anything I can help with?"})

    # Get mood-based response
    response = get_mood_response(mood)
    if mood == 'sad' and "sorry" in response:
        # If mood is sad and response indicates empathy, consider adding a joke
        joke = get_random_joke()
        response += f" Would you like to hear a joke? Here's one: {joke}"

    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
