# CS_Fundamentals: Understanding Bubble Sort

Welcome to the CS_Fundamentals project! This repository serves as a resource for learning about the **Bubble Sort** algorithm. It includes its implementation in Python, C, and Java, a comparative analysis, and an interactive visualization.

The `src` directory contains more complete, or "end," versions of the Bubble Sort algorithm for each language. During live coding sessions or as exercises, we might start with simpler "begin" versions (e.g., `bubble_sort_begin.py`, `bubble_sort_begin.c`, `BubbleSort_begin.java`). You can use the "end" versions provided here to check your work or see a more fleshed-out example.

## Interactive Learning Experience

A key part of this project is the interactive web page where you can:

* Learn the core concepts of Bubble Sort.
* See a side-by-side comparison of its implementation in Python, C, and Java.
* **Visualize the Bubble Sort algorithm in action** with an interactive simulation!

**Explore the Bubble Sort SPA (Single Page Application) here:**
[https://berkunis.github.io/CS_Fundamentals/](https://berkunis.github.io/CS_Fundamentals/)

## What You Can Learn

* **The Bubble Sort Algorithm:** Understand its mechanics, step-by-step logic, and efficiency (O(n<sup>2</sup>)).
* **Multi-Language Implementation:** Observe how the same algorithm is expressed in Python, C, and Java.
* **Language Syntax & Features:** Gain insights into the differences in syntax, data types, and program structure across these languages.
* **Compilation vs. Interpretation:** See firsthand that Python scripts are typically interpreted, while C and Java code require a compilation step.
* **Basic Code Compilation & Execution:** Learn fundamental command-line operations for running programs in these languages.

## Repository Structure

* `index.html`: The main file for the interactive Single Page Application (SPA) linked above. It uses HTML, Tailwind CSS, and JavaScript.
* `src/`: This directory contains example implementations. We encourage you to try coding your own "begin" versions and then compare them with these "end" versions:
    * `bubble_sort_end.py`: A Python version. (You might work on a `bubble_sort_begin.py` in class/exercises).
    * `bubble_sort_end.c`: A C version. (You might work on a `bubble_sort_begin.c` in class/exercises).
    * `BubbleSort_end.java`: A Java version. (You might work on a `BubbleSort_begin.java` in class/exercises).

## Pre-Work & Setup Tutorial

To run the standalone code examples from the `src` directory locally, and to follow along with potential live coding, you'll want to set up your development environment.

### 1. Recommended Code Editor: Cursor

* **Cursor** ([https://cursor.sh/](https://cursor.sh/)) is a highly recommended code editor (a fork of VS Code with integrated AI features).
* Alternatively, **Visual Studio Code (VS Code)** ([https://code.visualstudio.com/](https://code.visualstudio.com/)) is an excellent choice.
* Ensure you install relevant extensions for Python, C/C++, and Java in your chosen editor for the best experience (e.g., extensions provided by Microsoft).

### 2. Git Installation & GitHub Setup

* **Install Git:** Download and install Git from [https://git-scm.com/](https://git-scm.com/). This is essential for version control and interacting with GitHub repositories.
* **Configure Git User:** After installing Git, configure your name and email globally (this information is embedded in your commits):
    ```bash
    git config --global user.name "Your Name or GitHub Username"
    git config --global user.email "your.email@example.com"
    ```
    To set it for a specific project (repository), navigate into the project folder in your terminal and run the commands without `--global`.
* **Connecting to GitHub from Cursor/VS Code:**
    * When you clone a repository or try to push/pull changes for the first time, Cursor/VS Code will typically prompt you to authenticate with GitHub, usually by opening a browser window for you to sign in. Follow the prompts.
    * You can check your GitHub account status in Cursor/VS Code via the "Accounts" icon (often a person silhouette in the bottom-left).

### 3. Language-Specific Setup

* **Python:**
    1.  Download and install Python 3 from [https://www.python.org/downloads/](https://www.python.org/downloads/).
    2.  **Important:** During installation, make sure to check the box that says "Add Python to PATH" or "Add python.exe to Path".
    3.  Verify installation by opening a new terminal/command prompt and typing: `python --version` (or `python3 --version`).

* **C (using GCC on Windows via MSYS2):**
    1.  **Install MSYS2:** Go to [https://www.msys2.org/](https://www.msys2.org/) and download/run the installer.
    2.  **Update MSYS2 packages:** Open the MSYS2 terminal and run:
        ```bash
        pacman -Syu
        ```
        (You might need to close and reopen the terminal and run it again if prompted).
    3.  **Install MinGW-w64 GCC toolchain:** In the MSYS2 terminal, run:
        ```bash
        pacman -S mingw-w64-x86_64-gcc
        ```
    4.  **Add MinGW-w64 to Windows PATH:**
        * Find the `bin` directory of your MinGW-w64 installation (commonly `C:\msys64\mingw64\bin`).
        * Add this directory to your System `Path` environment variable (Search for "environment variables" in Windows search -> "Edit the system environment variables" -> "Environment Variables..." -> Select "Path" under "System variables" -> "Edit..." -> "New" -> Paste the path).
    5.  Verify: Open a *new* PowerShell or Command Prompt and type `gcc --version`.

* **Java (using OpenJDK 8 or later):**
    1.  **Download OpenJDK:** You can get builds from various sources (e.g., Adoptium Temurin, Red Hat, Oracle OpenJDK). An LTS (Long-Term Support) version like 8, 11, 17, or 21 is recommended.
    2.  **Extract:** Extract the downloaded ZIP/TAR.GZ file to a permanent location (e.g., `C:\Program Files\Java\your-openjdk-folder`).
    3.  **Set `JAVA_HOME` Environment Variable:**
        * Search "environment variables" -> "Edit the system environment variables" -> "Environment Variables..."
        * Under "System variables", click "New...".
        * Variable name: `JAVA_HOME`
        * Variable value: Path to your extracted OpenJDK folder (e.g., `C:\Program Files\Java\jdk-17.0.2`)
    4.  **Add JDK's `bin` to `Path`:**
        * Edit the System `Path` variable.
        * Add a new entry: `%JAVA_HOME%\bin`
    5.  Verify: Open a *new* PowerShell or Command Prompt and type `java -version` and `javac -version`.

### 4. Verification Summary

After setup, open a **new terminal** and check:
* `python --version` (or `python3 --version`)
* `gcc --version`
* `java -version`
* `javac -version`

## Running the Standalone Programs (from `src` directory)

Once your environment is set up:

1.  **Clone or Download this Repository:**
    * Using Git: `git clone https://github.com/berkunis/CS_Fundamentals.git`
    * Or download the ZIP from GitHub and extract it.
2.  **Navigate to the `src` Directory:**
    Open your terminal or command prompt and change your current directory to the `src` folder. For example:
    ```bash
    cd path/to/CS_Fundamentals/src
    ```
    If you have created language-specific subfolders within `src` (e.g., `src/Python`, `src/C`, `src/Java`), navigate into those before running the respective commands.

3.  **Run the Python version (`bubble_sort_end.py`):**
    (Assuming `bubble_sort_end.py` is in `src` or its subfolder)
    ```bash
    python bubble_sort_end.py
    ```

4.  **Compile and Run the C version (`bubble_sort_end.c`):**
    (Assuming `bubble_sort_end.c` is in `src` or its subfolder)
    * Compile:
        ```bash
        gcc bubble_sort_end.c -o bubble_sort_c_executable
        ```
    * Run:
        * Windows: `.\bubble_sort_c_executable.exe`
        * macOS/Linux: `./bubble_sort_c_executable`

5.  **Compile and Run the Java version (`BubbleSort_end.java`):**
    (Assuming `BubbleSort_end.java` is in `src` or its subfolder and the class inside is `public class BubbleSort_end`)
    * Compile:
        ```bash
        javac BubbleSort_end.java
        ```
    * Run:
        ```bash
        java BubbleSort_end
        ```

---

We hope this project and setup guide enhance your learning experience. Start with the "begin" versions of the code in class or on your own, and use these "end" versions as a reference. Happy coding!