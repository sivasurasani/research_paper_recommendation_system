# Research Paper Recommendation System

This project is a Flask-based web application that provides research paper recommendations based on an input paper title. Users can enter a research paper title, and the app will suggest similar papers using a pre-trained recommendation model.

## Features

- **User Input**: Enter the title of a research paper.
- **Paper Recommendations**: Based on the input title, the system suggests related research papers.
- **Interactive Interface**: User-friendly HTML form for input and easy-to-read display of recommended papers.

## Requirements

- **Python**: 3.7+
- **Flask**: To set up the web server.
- **Torch**: For loading and running the recommendation model.
- **Additional Libraries**: `pandas`, `json`, `pickle`

### Detailed Libraries:
- `Flask`: To create the web server and handle requests.
- `pandas`: For data handling and preprocessing, if required.
- `torch`: For using the recommendation model (PyTorch).
- `sentence-transformers`: If using Sentence Transformers in PyTorch for encoding.
- `pickle`: To load and save model files and embeddings (included in Python's standard library).
- `json`: For handling JSON requests and responses (also part of Python's standard library).

## Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/research-paper-recommendation-system.git
cd research-paper-recommendation-system
```

### 2. Install Dependencies
It's recommended to use a virtual environment to manage dependencies.

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Set Up Model Files

Ensure that your model files are placed in the same directory:
- `embeddings.pkl`: Precomputed embeddings for research papers.
- `sentences.pkl`: List of titles of the research papers.
- `rec_model.pkl`: Trained recommendation model.

> **Note**: If you don't have these files, you will need to train or obtain a suitable recommendation model.

### 4. Run the Application

To start the Flask app, use:
```bash
python main.py
```

The app will run at `http://127.0.0.1:5000`.

### 5. Access the Web Interface

- Open a web browser and navigate to `http://127.0.0.1:5000`.
- You’ll see a form where you can enter a research paper title.
- Click the **"Get Recommendations"** button to receive a list of similar papers.

## How It Works

1. The Flask app receives the paper title as input.
2. The API endpoint loads the pre-trained embeddings and recommendation model.
3. The model calculates cosine similarity scores between the input and existing paper embeddings.
4. The top 5 most similar papers are returned and displayed on the web page.



## Troubleshooting

- **Error: No model files found**: Ensure the `Models` directory contains the `embeddings.pkl`, `sentences.pkl`, and `rec_model.pkl` files.
- **Error: Flask not installed**: Run `pip install Flask` to install Flask manually if required.

## Contributing

Feel free to submit issues or pull requests if you’d like to contribute to the project.

## License

This project is open-source and available under the MIT License.
```
