

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