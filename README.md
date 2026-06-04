

# Getting Started

Setup Python development environment.


## Install Python
This is the most important part - pay close attention to step 2!

1.) Find and run the downloaded installer
    Important: Check ✓ “Add python.exe to PATH” at the bottom

2.) If you miss the “Add to PATH” checkbox, Python won’t work from Terminal. This is the #1 installation mistake.

3.) Click “Install Now” (not “Customize installation” unless you know what you’re doing)

4.) If Windows asks “Do you want to allow this app to make changes?”, click “Yes”

5.) Wait for installation (usually takes 1-2 minutes)

6.) Click “Close” when you see “Setup was successful”
​
### Verify installation
Let’s make sure Python installed correctly:

1.) Open Terminal:

    - Press Windows + R
    - Type wt and press Enter
    - Or search “Terminal” in Start menu

2.) Type this command:
   
    - python --version

3.) You should see the Python version you just installed

## Code Editor
Download VS Code

1.) Go to code.visualstudio.com

2.) Click the big download button (it detects Windows automatically)

3.) Run the downloaded installer

4.) Important: Check these options during installation:

    ✓ Add “Open with Code” action to Windows Explorer file context menu
    ✓ Add “Open with Code” action to Windows Explorer directory context menu
    ✓ Register Code as an editor for supported file types
    ✓ Add to PATH

5.) Click “Next” and “Install”

6.) Click “Finish” when done

## Install Pyhon Extension

VS Code needs the Python extension to work properly with Python files:

1.) Click the Extensions icon in the left sidebar (it looks like 4 squares)

2.) Search for “Python”

3.) Find the one by Microsoft (it has millions of downloads)

4.) Click “Install”

5.) Wait for installation to complete

## Configure Python Execution
After installing the Python extension, enable this important setting:

1.) Open Settings (Ctrl/Cmd + ,)

2.) Search for “Python Terminal Execute In File Dir”

3.) Check the box to enable it

What this does: When you run a Python file, VS Code will execute it from the file’s directory instead of your workspace root.

**Recommend** : This prevents common path-related errors. For example, if your script reads a file with open('data.csv'), it will look for the file in the same folder as your script, which is usually what you want. Without this setting, it would look in your project root instead, causing “file not found” errors.

### Additional recommended extensions
While VS Code works great with just the Python extension, here are a few more I recommend:
​
#### Pylance
    - Search for “Pylance” by Microsoft
    - Provides even better code completion and error detection
    - Works alongside the Python extension
​
#### Jupyter
    - Search for “Jupyter” by Microsoft
    - Enables interactive Python mode (we’ll use this later)
    - Essential for data science and AI work

#### Black Formatter

Integrated formatting: Once this extension is installed in VS Code, Black will be automatically available as a formatter for Python. This is because the extension ships with a Black binary. You can ensure VS Code uses Black by default for all your Python files by setting the following in your User settings (View > Command Palette... and run Preferences: Open User Settings (JSON)):

  "[python]": {
    "editor.defaultFormatter": "ms-python.black-formatter"
  }
Format on save: Automatically format your Python files on save by setting the editor.formatOnSave setting to true and the editor.defaultFormatter setting to ms-python.black-formatter. You can also enable format on save for Python files only by adding the following to your settings:

  "[python]": {
    "editor.defaultFormatter": "ms-python.black-formatter",
    "editor.formatOnSave": true
  }
Customize Black: You can customize the behavior of Black by setting the black-formatter.args setting.

Keyboard Shortcuts: The code formatting is available in Visual Studio Code through the following keyboard shortcuts:

On Windows: Shift + Alt + F
On Mac: Shift + Option + F
On Linux: Ctrl + Shift + I

    pip install --user black

## Setting Virual Environments
Keep your Python pojects organized

What are virtual environments?
A virtual environment is like a private copy of Python for each project. Think of it as:

- A separate folder for each project
- Its own Python installation
- Its own place to install packages
- Complete isolation from other projects

### Create your first virtual environment
Let’s create one for our python-for-ai project. You have two methods:
​
#### Method 1: VS Code Command Palette (easier)

1.) Open your project in VS Code

2.) Press Ctrl/Cmd + Shift + P

3.) Type “Python: Create Environment”

4.) Select “Venv”

5.) Select your Python installation

6.) VS Code creates and activates everything for you!
​
#### Method 2: Terminal command
1.) Open the terminal in VS Code (View > Terminal)

2.) Make sure you’re in your project folder

3.) Run this command:

    python -m venv .venv

##### What this does:
- python -m venv - Run Python’s virtual environment module
- .venv - The name of the folder to create (convention is to use “.venv” with a dot)

#### Activate your virtual environment

1.)VS Code makes activation super easy:
Press Ctrl/Cmd + Shift + P to open Command Palette

2.)Type “Python: Select Interpreter”

3.)Choose the one that says .venv (it will show the full path like ./.venv/bin/python)

4.)That’s it! VS Code automatically activates it for you

You’ll know it’s working when you see (.venv) in your terminal:

    .venv\Scripts\activate


#### DEactivate your virtual environment
        deactivate


#### Installing Packages
Packages are collections of Python code that solve specific problems:
- requests - Download web pages and data
- pandas - Work with spreadsheets and data
- numpy - Fast mathematical operations
- openai - Connect to AI models
- beautifulsoup4 - Extract data from websites

#### Meet pip
pip (Pip Installs Packages) is Python’s package manager. It:
- Downloads packages from the internet
- Installs them in your environment
- Manages versions and dependencies


Command for Installing and Uninstalling:

        pip install requests

        pip uninstall requests

## Interactive Python
Interactive Python mode is the favorite way to write Python code. It combines the organization of Python files with the interactivity of Jupyter notebooks.

### Perfect for AI development
When working with AI and data:
- You’re constantly inspecting data
- Testing transformations
- Checking outputs
- Experimenting with different approaches

Running an entire file every time (like we did with hello.py) would be slow and frustrating. Interactive mode lets you work iteratively.

### What is Interactive Python?
Imagine you’re cooking and tasting as you go, rather than waiting until the entire meal is done. That’s Interactive Python:
- Write code in a .py file (organized and clean)
- Run pieces of it instantly with Shift + Enter
- See results immediately in a side panel
- Keep all your variables in memory

### Prerequisites
1.) Make sure your virtual environment is activated:
- You should see (.venv) in your terminal

2.) Install the required package:

        pip install ipykernel

This package allows Jupyter to run Python code interactively.


### Set up Interactive Python
Now let’s enable the interactive feature:

1.) Open VS Code settings:

        Press Ctrl/Cmd + , (comma)
        Or File > Preferences > Settings

2.) Search for “execute selection”

3.) Find this setting: 

        Jupyter > Interactive Window >  Text Editor: Execute Selection

4.) Check the box to enable it

How it works? : When you press **Shift + Enter**, your selected code will run in the Jupyter interactive window instead of the Python terminal. This gives you a much richer, more visual experience.
That’s it! You’re ready to use interactive mode.

Run selected code
Highlight any code
        
        Press Shift + Enter
        
Only that selection runs