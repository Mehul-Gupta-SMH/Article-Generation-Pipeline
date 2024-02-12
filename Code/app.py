from flask import Flask, render_template, request, jsonify
from Summary import generate_article

app = Flask(__name__)

# Sample function to generate article content (replace this with your actual implementation)
# def generate_article(api_key, topic):
#     # Perform some actions to generate article content
#     content = f"Article on {topic} generated using API key: {api_key}"
#     return content

@app.route('/')
def index():
    return render_template('app_template.html')

@app.route('/generate-article', methods=['GET'])
def generate_article_route():
    api_key = request.args.get('api_key')
    topic = request.args.get('topic')

    # Call function to generate article content
    article_content = generate_article(api_key, topic)

    # Return article content as JSON response
    return jsonify({'content': article_content})

if __name__ == '__main__':
    app.run(debug=True)
