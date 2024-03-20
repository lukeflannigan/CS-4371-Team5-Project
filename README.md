# Fake-News-Classifier Class Project CS-4371

## Prerequisites

- [Visual Studio Code](https://code.visualstudio.com/download) installed.
- [Python](https://www.python.org/downloads/) installed (latest version recommended).

## Setup Instructions

### Clone the Repository

- Open Visual Studio Code.
- To clone the repository into a specific folder, you can drag and drop the folder into VS Code or use the Terminal to navigate:
  - Press `Ctrl+` (or `Cmd+` on macOS) to open the Terminal in VS Code.
  - Navigate to your desired directory with `cd <directory-path>`.
- Run the command in the terminal to clone the repository: 
  ```
  git clone https://github.com/lukeflannigan/CS-4371-Team5-Project.git
  ```
- - If you cloned the repository using VS Code's integrated terminal and are already in the project directory, your project should be accessible in the current VS Code window. If not, use `File > Open Folder...` from the VS Code menu bar to navigate to and open the cloned project directory.

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

### Run Jupyter Notebook

- Open `fake_news_model.ipynb` from the Explorer sidebar.
- Run notebook cells by clicking the play button (`▶`) in each cell.