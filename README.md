# Game Review Sentiment Analyzer

## Collaborators
- **Lucas Sanchez**
  - GitHub: [`LUCASSANCHEZ12`](https://github.com/LUCASSANCHEZ12)
- **Gabriel Villarreal**
  - GitHub: [`GabrielVillarrealPonce`](https://github.com/GabrielVillarrealPonce)
- **Nicolas Vargas**
  - GitHub: [`kI0r203`](https://github.com/kI0r203)

## Objective
This project was created as a task for the *"Inteligencia Artificial"* course at *Universidad Privada Boliviana* (UPB).

## Project Description
The Game Review Sentiment Analyzer is designed to analyze sentiments of a provided text, trainend with Steam reviews. It focuses on determining whether reviews are positive or negative, providing insights into user feedback on various games.

## Framework and Technologies
- Website Framework: `Angular`
- AI Model Language: `Python`

## Model Training and Selection
We used Logistic Regression for binary sentiment analysis (positive or negative reviews). The model was implemented using the `sklearn` library and trained on datasets sourced from Kaggle.com. The dataset name is [Steam Game Reviews](https://www.kaggle.com/datasets/smeeeow/steam-game-reviews/data).

## Website Functionality
The website features five example games, each with its own set of reviews. Users can submit new reviews through a prompt. Upon submission, the sentiment analyzer evaluates the review and categorizes it as either positive or negative.

## How to Use
1. Explore the example games and their reviews.
2. Submit your own review using the provided prompt.
3. View the sentiment analysis result (Positive or Negative) for your review.

## Installation
To run the project locally, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/LUCASSANCHEZ12/Sentiment_Analyzer.git
    ```

2. Install all Python dependencies
    ```bash
    pip install uvicorn sklearn nltk fastapi dill pandas pydantic 
    ```

3. Install Angular dependencies:
    * For Windows download node js installer (follow this [tutorial](https://kinsta.com/blog/how-to-install-node-js/))
        ```bash
        npm install -g @angular/cli
        ng --version
        ```
    * For Linux
        ```bash
        sudo apt install nodejs
        sudo apt install npm
        sudo npm install npm@latest -g
        sudo npm install -g @angular/cli
        ```
    * Install tailwind inside the project at `frontend/` (only if the file `tailwind.config.js` doesn't exist already)
        ```bash
        npm install -D tailwindcss postcss autoprefixer
        npx tailwindcss init 
        ```
## Lauch the project

1. Start the python API:
    Inside of `backend/`
    * For Linux
    ```bash
    uvicorn api:app --reload
    ```
    * For Windows
    ```bash
    python.exe -m uvicorn api:app --reload
    ```
2. Start the Angular development server:
    Inside of `frontend/`
    ```bash
    ng serve
    ```

3. Navigate to `http://localhost:4200/` in your browser.

## Contributing
If you wish to contribute to the project, please fork the repository and submit a pull request.

## Acknowledgements
We would like to thank the Universidad Privada Boliviana (UPB) and our course instructor for the guidance and support throughout this project.

Feel free to contact us for any queries or feedback.

*Cochabamba, Bolivia*
*June, 2024*