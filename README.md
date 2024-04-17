# Fake-News-Classifier Class Project CS-4371

## Prerequisites

- [Visual Studio Code](https://code.visualstudio.com/download) installed.
- [Python](https://www.python.org/downloads/) installed (latest version recommended).

## Setup Instructions

### Install Extensions
- Open Visual Studio Code.
- Go to the Extensions view by clicking on the Extensions icon in the Activity Bar on the side of VS Code or by pressing `Ctrl+Shift+X` (or `Cmd+Shift+X` on macOS).
- Search for and install the following extensions:
- - Python (by Microsoft)
- - Jupyter (by Microsoft)

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
### Run Jupyter Notebook

- Open `fake_news_model.ipynb` from the Explorer sidebar.
- Run notebook cells by clicking the play button (`▶`) in each cell.
  
### Research
-Prior research: THE CURIOUS CASE OF NEURAL TEXT DeGENERATION https://arxiv.org/pdf/1904.09751v2.pdf
-Contemporary: RoFT: A Tool for Evaluating Human Detection of Machine-Generated Text https://arxiv.org/pdf/2010.03070.pdf

