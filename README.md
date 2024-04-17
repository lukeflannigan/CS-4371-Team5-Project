# Fake-News-Classifier Class Project CS-4371

## Overview
In this project, we developed several machine learning models to classify real and fake news articles.
Our project uses Python for data processing and model building on the backend as well as a Flask web interface for users. The application employs various machine learning models to predict and display the legitimacy of news articles based on their text.

### Datasets and Models
The project makes use of multiple datasets sourced from Kaggle, featuring labeled real and fake news articles. These datasets were concatonated, cleaned, and preprocessed to train three main models: Logistic Regression, Random Forest, and XGBoost. The models evaluate text data transformed via TF-IDF vectorization to predict a given news article's legitimacy.

#### Datasets:

- [Kaggle True News Dataset](https://www.kaggle.com/datasets/emineyetm/fake-news-detection-datasets)
- [Kaggle Fake News Dataset](https://www.kaggle.com/datasets/emineyetm/fake-news-detection-datasets)
- [Kaggle News Dataset 2](https://www.kaggle.com/c/fake-news/data?select=test.csv)
- [Kaggle News Dataset 3](https://www.kaggle.com/datasets/nopdev/real-and-fake-news-dataset)

### User Interface
The user interface, accessible via a web browser, allows users to test a news article's authenticity. The classification findings, along with a comparison graph of the probability scores from each model, are displayed on the results page.


## Setup Instructions

### Prerequisites

- [Visual Studio Code](https://code.visualstudio.com/download) installed.
- [Python](https://www.python.org/downloads/) installed (latest version recommended).
- 
### Install Extensions
- Open Visual Studio Code.
- Go to the Extensions view by clicking on the Extensions icon in the Activity Bar on the side of VS Code or by pressing `Ctrl+Shift+X` (or `Cmd+Shift+X` on macOS).
- Search for and install the following extensions:
- - Python (by Microsoft)
- - Jupyter (by Microsoft)


### Git LFS
Before you can use this repository, you'll need to have Git and Git LFS installed:

1. **Install Git** (if not already installed): [https://git-scm.com/downloads](https://git-scm.com/downloads)
2. **Install Git LFS**:

#### For macOS Users
- **Install Using Homebrew**:
  - If you do not have Homebrew installed, open Terminal and install Homebrew by running:
    ```
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    ```
  - Install Git LFS with Homebrew by executing:
    ```
    brew install git-lfs
    ```

#### For Windows Users
- **Download the Installer**:
  - Visit the [Git LFS Releases Page](https://github.com/git-lfs/git-lfs/releases) and download the `git-lfs-windows-vX.X.X.exe` file (where `X.X.X` is the latest version).
  - Run the installer and follow the prompts to install Git LFS.

### 3. Initialize Git LFS

After installing Git LFS, you must run the following command in your terminal to set it up for use:
```
git lfs install
```

### Clone the Repository

- Open Visual Studio Code.
- To clone the repository into a specific folder, you can drag and drop the folder into VS Code or use the Terminal to navigate:
  - Press `Ctrl+` (or `Cmd+` on macOS) to open the Terminal in VS Code.
  - Navigate to your desired directory with `cd <directory-path>`.
- Run the command in the VS Code terminal `View > Terminal` to clone the repository:
  ```
  git clone https://github.com/lukeflannigan/CS-4371-Team5-Project.git
  ```

- After cloning, you need to change the directory to the project folder. Run:
    ```
    cd CS-4371-Team5-Project
    ```
   
### Create and Activate a Virtual Environment

Within the project directory in VS Code Terminal:
- Run the command to create a virtual environment:
  - Windows: `python -m venv venv`
  - macOS/Linux: `python3 -m venv venv`
- Then, run the command to activate the virtual environment:
  - Windows: `.\venv\Scripts\activate`
  - macOS/Linux: `source venv/bin/activate`

### Install Dependencies

With the virtual environment activated, install the dependencies by running:
```
pip install -r requirements.txt
```

### Configure Python Interpreter

- Ensure the Python interpreter is set to the virtual environment you created. This interpreter will typically have `venv` in its path, indicating it's the virtual environment for this project.
- If not set automatically, open Command Palette with `Ctrl+Shift+P` (or `Cmd+Shift+P` on macOS), type `Python: Select Interpreter`, and select the interpreter that includes `venv` and is located within your project directory.
- If necessary:
  - Install the `ipykernel` package using pip: `pip install ipykernel`.
  - Run the command `python -m ipykernel install --user --name=myenv` to create a new kernel named `myenv` associated with your virtual environment (`venv`).
  - In VS Code, open a Jupyter Notebook and select the newly created kernel (`myenv`) from the kernel dropdown menu in the top-right corner of the notebook interface.

### Running the Flask Application

1. With the virtual environment activated and dependencies installed, start the Flask server by running the following command in the VS Code Terminal:
 ```
python app.py
 ```
 
This command will start running the Flask server.

2. Once running, open a web browser and navigate to `http://127.0.0.1:5000/`. This will take you to the homepage of the user interface.

3. To use the application, paste the plaintext of a news article in the input box and submit it for analysis. The application will display the results, showing whether the article is likely real or fake along with the probability scores from the three models.


### Jupyter Notebook Configuration

- If you need to use a Jupyter Notebook:
- Ensure `ipykernel` is installed:
 ```
 pip install ipykernel
 ```
- Register a new kernel associated with the virtual environment:
 ```
 python -m ipykernel install --user --name=myenv
 ```
- Open a Jupyter Notebook in VS Code and select `myenv` from the kernel dropdown menu in the notebook interface.
-

## Research

### Prior Research
Our project builds on findings from the paper "The Curious Case of Neural Text Degeneration" by Holtzman et al. (https://arxiv.org/pdf/1904.09751v2.pdf). This study looks at the challenges associated with text generation by neural networks, which helped us understand the context and difficulties surrounding machine learning based fake news detection.

### Original Research
The initial inspiration for our project comes from the paper "Defending Against Neural Fake News" (https://arxiv.org/abs/1905.12616). This study provides valuable context for considering the impact of AI-generated content in news media, which informed our exploration into effective fake news detection strategies.

### Contemporary Research
We also examined ideas from "RoFT: A Tool for Evaluating Human Detection of Machine-Generated Text" by Dugan et al. (https://arxiv.org/pdf/2010.03070.pdf). This paper introduces new techniques used for detecting machine-generated texts, updating our understanding surrounding fake news detection and furthering this topic of ongoing reasearch.