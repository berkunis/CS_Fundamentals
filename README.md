# CS_Fundamentals: Understanding Bubble Sort

Welcome to the CS_Fundamentals project! This repository serves as a resource for learning about the **Bubble Sort** algorithm. It includes its implementation in Python, C, and Java, a comparative analysis, and an interactive visualization.

The `src` directory and its subfolders contain two versions of the Bubble Sort algorithm for each language:
* A `_begin` version (e.g., `bubble_sort_begin.py`): This version has the core sorting logic (comparison and swap) partially removed. I will use these "begin" files during live coding sessions or for exercises, where you will fill in the missing parts.
* An `_end` version (e.g., `bubble_sort_end.py`): This is the complete, working example. You can use these to check your work or see a fully fleshed-out implementation.

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
* `src/`: This directory contains language-specific subfolders (e.g., `src/Python/`, `src/C/`, `src/Java/`). Each subfolder contains:
    * A `_begin` version of the Bubble Sort program (e.g., `bubble_sort_begin.py`). This is for you to complete.
    * An `_end` version of the Bubble Sort program (e.g., `bubble_sort_end.py`). This is the completed reference.

    **Example File Names (assuming you place them in these subfolders):**
    * `src/Python/bubble_sort_begin.py` and `src/Python/bubble_sort_end.py`
    * `src/C/bubble_sort_begin.c` and `src/C/bubble_sort_end.c`
    * `src/Java/BubbleSort_begin.java` and `src/Java/BubbleSort_end.java`

## Pre-Work & Setup Tutorial

To run the standalone code examples from the `src` directory locally, and to follow along with live coding, I recommend setting up your development environment.

### 1. Recommended Code Editor: Cursor

* **Cursor** ([https://cursor.sh/](https://cursor.sh/)) is a code editor I find very useful (a fork of VS Code with integrated AI features).
* Alternatively, **Visual Studio Code (VS Code)** ([https://code.visualstudio.com/](https://code.visualstudio.com/)) is an excellent choice.
* Ensure you install relevant extensions for Python, C/C++, and Java in your chosen editor for the best experience (e.g., extensions provided by Microsoft).

### 2. Git Installation & GitHub Setup

* **Install Git:** Download and install Git from [https://git-scm.com/](https://git-scm.com/).
* **Configure Git User:** After installing Git, configure your name and email:
    ```bash
    git config --global user.name "Your Name or GitHub Username"
    git config --global user.email "your.email@example.com"
    ```
* **Connecting to GitHub from Cursor/VS Code:** Usually prompts for authentication on first push/pull.

### 3. Language-Specific Setup

* **Python:**
    1.  Install Python 3 from [python.org](https://www.python.org/downloads/).
    2.  Ensure "Add Python to PATH" is checked during installation.
    3.  Verify: `python --version` (or `python3 --version`).

* **C (using GCC on Windows via MSYS2):**
    1.  Install MSYS2 from [msys2.org](https://www.msys2.org/).
    2.  In MSYS2 terminal, update: `pacman -Syu` (may need to repeat).
    3.  Install GCC: `pacman -S mingw-w64-x86_64-gcc`.
    4.  Add MinGW `bin` (e.g., `C:\msys64\mingw64\bin`) to Windows System `Path`.
    5.  Verify (in a new terminal): `gcc --version`.

* **Java (using OpenJDK 8 or later):**
    1.  Download OpenJDK (e.g., Adoptium Temurin, Red Hat). An LTS (Long-Term Support) version like 8, 11, 17, or 21 is recommended.
    2.  Extract to a permanent location (e.g., `C:\Program Files\Java\your-openjdk-folder`).
    3.  Set `JAVA_HOME` System Environment Variable to this path.
    4.  Add `%JAVA_HOME%\bin` to System `Path`.
    5.  Verify (in a new terminal): `java -version` and `javac -version`.

### 4. Verification Summary

After setup, open a **new terminal** and check:
* `python --version` (or `python3 --version`)
* `gcc --version`
* `java -version`
* `javac --version`

## Running the Standalone Programs

Once your environment is set up and you have organized your files into subfolders within `src` (e.g., `src/Python`, `src/C`, `src/Java`):

1.  **Clone or Download this Repository.**
2.  **Navigate to the Specific Language Directory within `src`:**
    Open your terminal. For example, to work with the Python files:
    ```bash
    cd path/to/CS_Fundamentals/src/Python 
    ```
    (Replace `Python` with `C` or `Java` as needed.)

3.  **Python (e.g., `bubble_sort_begin.py` or `bubble_sort_end.py`):**
    ```bash
    python your_python_file_name.py 
    ```

4.  **C (e.g., `bubble_sort_begin.c` or `bubble_sort_end.c`):**
    * Compile: `gcc your_c_file_name.c -o executable_name`
    * Run (Windows): `.\executable_name.exe`
    * Run (macOS/Linux): `./executable_name`

5.  **Java (e.g., `BubbleSort_begin.java` or `BubbleSort_end.java`):**
    (Ensure class name inside the file matches the filename, e.g., `public class BubbleSort_begin` for `BubbleSort_begin.java`)
    * Compile: `javac YourJavaFileName.java`
    * Run: `java YourJavaClassName` (e.g., `java BubbleSort_begin`)

---

I hope this project and setup guide enhance your learning experience. I encourage you to start with the "begin" versions of the code in your exercises or during our sessions, and use these "end" versions as a reference. Happy coding!