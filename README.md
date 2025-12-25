# ⚡ AlgoRacer: Advanced Sorting Visualizer

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Pygame](https://img.shields.io/badge/Pygame-2.5-green)
![NumPy](https://img.shields.io/badge/NumPy-Sound_Engine-orange)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

**AlgoRacer** is an interactive, multi-sensory educational tool designed to demystify sorting algorithms. Unlike standard visualizers, this project focuses on **comparative benchmarking**, **auditory feedback**, and **software architecture**, bridging the gap between theoretical CS concepts and real-time visualization.

![Intro Demo](assets/demo_intro.gif)

---

## 🚀 Key Features

### 🏁 Race Mode (Grid View)
Run up to 16 algorithms concurrently on a 4x4 grid to compare efficiency visually. This highlights the massive performance difference between $O(n^2)$ and $O(n \log n)$ algorithms in real-time.

![Race Mode Demo](assets/demo_all.gif)

### 🔊 Auditory Feedback Engine
Uses `NumPy` to generate procedural sine waves. The pitch corresponds to the element's value—sorted arrays "sing," while random arrays sound like static.

### 📚 Educational Overlay
Built-in "Cheat Sheet" pop-up detailing Time/Space Complexity, Stability, and Use Cases for every algorithm.

---

## 🎮 Interactive Controls

AlgoRacer offers granular control over the visualization environment.

### 1. Dynamic Speed Control
Adjust execution speed in real-time using exponential scaling. This allows you to slow down for critical swaps or speed up to finish long runs.
* **Keys:** `+` (Increase) / `-` (Decrease)

![Speed Control Demo](assets/demo_speed.gif)

### 2. Array Size Manipulation
Dynamically resize the dataset. Use modifiers to jump between fine-tuning and massive stress testing.
* **Fine Tune:** `Arrow Keys` (±10)
* **Fast Tune:** `Shift + Arrows` (±100)
* **Turbo Tune:** `Ctrl + Arrows` (±1000)

![Size Control Demo](assets/demo_size.gif)

### 3. General Management
Full control over the simulation state including themes, audio, and resetting.
* **Space:** Start/Pause
* **R:** Reset
* **T:** Toggle Theme
* **S:** Mute/Unmute
* **I:** Info Sheet

![General Controls Demo](assets/demo_controls.gif)

---

## 🛠️ Installation & Usage

### Option A: 🚀 Quick Start (No Install Required)
The easiest way to try AlgoRacer is to download the standalone executable. You do **not** need Python installed.

1.  Navigate to the **[Releases](../../releases)** section on the right sidebar of this repository.
2.  Download the latest `AlgoRacer.exe` (Windows) or `AlgoRacer.app` (Mac).
3.  Double-click the file to launch the visualizer immediately.

### Option B: 🐍 Run from Source (For Developers)
If you want to modify the code or run it raw:

1.  **Clone the Repository**
    ```bash
    git clone [https://github.com/Ryu-134/AlgoRacer.git](https://github.com/Ryu-134/AlgoRacer.git)
    cd AlgoRacer
    ```

2.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```
    *(Requires `pygame` and `numpy`)*

3.  **Run the Application**
    ```bash
    python main.py
    ```

---

## ⌨️ Master Keybindings Reference

| Key | Action |
| :--- | :--- |
| **SPACE** | Start / Pause Sorting |
| **R** | Reset Array (New Random Seed) |
| **M** | Toggle Mode (Single vs. Grid Race) |
| **T** | Toggle Theme (Dark / Light) |
| **S** | Toggle Sound (Mute/Unmute) |
| **I** | Toggle Info Sheet (Complexities & Notes) |
| **+/-** | Increase / Decrease Speed (Exponential) |
| **Arrows** | Adjust Array Size (±10) |
| **Shift + Arrows** | Adjust Array Size (±100) |
| **Ctrl + Arrows** | Adjust Array Size (±1000) |
| **Left / Right** | Cycle Algorithm (Single Mode) |

---

## 🧠 Engineering Highlights

### 1. Coroutine-Based State Management
Instead of blocking the main thread, all sorting algorithms are implemented as Python **Generators** (`yield`).
* **Why?** This allows the `Pygame` event loop to remain responsive (60 FPS) while the algorithm "pauses" execution to let the screen draw.
* **Result:** Smooth, interruptible animations without multithreading complexity.

```python
# Example of Generator Pattern
def bubble_sort(arr):
    for i in range(len(arr)):
        if arr[i] > arr[i+1]:
            swap(arr, i, i+1)
            yield True # Return control to Main Loop to render frame

```

### 2. Procedural Sound Generation

We avoid loading hundreds of `.wav` files by synthesizing audio on the fly using `NumPy`. This ensures low memory usage and infinite pitch granularity.

---

## 📚 Algorithms Included

This project includes a comprehensive suite of algorithms to demonstrate various complexity classes:

| Algorithm | Best | Average | Worst | Stable? |
| --- | --- | --- | --- | --- |
| **Tim Sort** | O(n) | O(n log n) | O(n log n) | ✅ |
| **Quick Sort** | O(n log n) | O(n log n) | O(n²) | ❌ |
| **Merge Sort** | O(n log n) | O(n log n) | O(n log n) | ✅ |
| **Heap Sort** | O(n log n) | O(n log n) | O(n log n) | ❌ |
| **Bubble Sort** | O(n) | O(n²) | O(n²) | ✅ |
| **Insertion Sort** | O(n) | O(n²) | O(n²) | ✅ |
| **Selection Sort** | O(n²) | O(n²) | O(n²) | ❌ |
| **Cocktail Shaker** | O(n) | O(n²) | O(n²) | ✅ |
| **Comb Sort** | O(n log n) | O(n²) | O(n²) | ❌ |
| **Shell Sort** | O(n log n) | O(n⁴/³) | O(n²) | ❌ |
| **Gnome Sort** | O(n) | O(n²) | O(n²) | ✅ |
| **Odd-Even Sort** | O(n) | O(n²) | O(n²) | ✅ |
| **Stooge Sort** | O(n^2.7) | O(n^2.7) | O(n^2.7) | ❌ |
| **Counting Sort** | O(n+k) | O(n+k) | O(n+k) | ✅ |
| **Bucket Sort** | O(n+k) | O(n+k) | O(n²) | ✅ |
| **Radix Sort** | O(nk) | O(nk) | O(nk) | ✅ |

---

## 📂 Project Structure

```text
AlgoRacer/
├── assets/              # GIFs and Images for documentation
├── main.py              # Entry point and Event Loop
├── algorithms.py        # Logic for all 16 sorting algorithms
├── visualizer.py        # UI rendering and State management
├── sound_manager.py     # NumPy audio generation engine
├── settings.py          # Configuration constants and Themes
└── requirements.txt     # Project dependencies

```

---

*Created by Casey Dane - 2025*

