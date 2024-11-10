import pandas as pd
from flask import Flask, request, jsonify, render_template
import pickle
import torch
from sentence_transformers import util, SentenceTransformer

# Create a Flask app
app = Flask(__name__)

# Load models and embeddings once at the beginning
embeddings = pickle.load(open('embeddings.pkl', 'rb'))
sentences = pickle.load(open('sentences.pkl', 'rb'))
rec_model = pickle.load(open('rec_model.pkl','rb'))

# Function to recommend similar papers based on input paper
def recommendation(input_paper):
    # Calculate cosine similarity scores between the embeddings of input_paper and all papers in the dataset.
    cosine_scores = util.cos_sim(embeddings, rec_model.encode(input_paper))

    # Get the indices of the top-k most similar papers based on cosine similarity.
    top_similar_papers = torch.topk(cosine_scores, dim=0, k=5, sorted=True)

    # Retrieve the titles of the top similar papers.
    papers_list = []
    for i in top_similar_papers.indices:
        papers_list.append(sentences[i.item()])

    return papers_list

@app.route('/')
def transaction_form():
    return render_template('main.html')

@app.route('/check_fraud', methods=['POST'])
def check_fraud():
    # Get the user input from the POST request
    data = request.get_json(force=True)
    input_paper = data.get('input_paper')  # The paper title should come from the POST request

    if not input_paper:
        return jsonify({'error': 'No input paper title provided'}), 400

    # Call the recommendation function
    recommend_papers = recommendation(input_paper)

    # Return the recommendations
    response = {
        'recommended_papers': recommend_papers
    }

    return jsonify(response)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
