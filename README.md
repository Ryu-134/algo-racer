# ⚡ AlgoRacer: Advanced Sorting Visualizer

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Pygame](https://img.shields.io/badge/Pygame-2.5-green)
![NumPy](https://img.shields.io/badge/NumPy-Sound_Engine-orange)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

**AlgoRacer** is an interactive, multi-sensory educational tool designed to demystify sorting algorithms. Unlike standard visualizers, this project focuses on **comparative benchmarking**, **auditory feedback**, and **software architecture**, bridging the gap between theoretical CS concepts and real-time visualization.

> **[PLACEHOLDER: Insert GIF of "Race Mode" here]**
> *Recommendation: Record a 10s clip of the 4x4 grid running all algorithms at once.*
> `![Race Mode Demo](assets/demo_race.gif)`

---

## 🚀 Key Features

* **16+ Algorithms Implemented:** From standard sorts (Quick, Merge) to hybrids (Tim Sort) and educational examples (Stooge, Gnome).
* **Auditory Feedback Engine:** Uses `NumPy` to generate procedural sine waves. The pitch corresponds to the element's value—sorted arrays "sing," while random arrays sound like static.
* **Dual View Modes:**
    * **Single Mode:** Focus on one algorithm to understand its behavior in detail.
    * **Race Mode:** Run up to 16 algorithms concurrently on a 4x4 grid to compare efficiency visually.
* **Interactive Controls:** Real-time speed adjustment (exponential scaling), pause/resume, and reverse-step capabilities.
* **Educational Overlay:** Built-in "Cheat Sheet" pop-up detailing Time/Space Complexity, Stability, and Use Cases for every algorithm.
* **Themes:** Toggle between **Dark Mode** (High Contrast) and **Light Mode** (Classroom/Paper style).

---

## 🛠️ Installation & Usage

### Option A: 🚀 Quick Start (No Install Required)
The easiest way to try AlgoRacer is to download the standalone executable. You do **not** need Python installed.

1.  Navigate to the **[Releases](../../releases)** section on the right sidebar of this repository.
2.  Download the latest `AlgoRacer.exe` (Windows) or `AlgoRacer.app` (Mac).
3.  Double-click the file to launch the visualizer immediately.

---

### Option B: 🐍 Run from Source (For Developers)
If you want to modify the code or run it raw:

1.  **Clone the Repository**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/AlgoRacer.git](https://github.com/YOUR_USERNAME/AlgoRacer.git)
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

## 🎮 Controls

> **[PLACEHOLDER: Insert GIF of "Interactive Controls" here]**
> *Recommendation: Show yourself changing speed, pausing, and opening the Info Sheet.*
> `![Interactive Demo](assets/demo_interactive.gif)`

| Key | Action |
| :--- | :--- |
| **SPACE** | Start / Pause Sorting |
| **R** | Reset Array (New Random Seed) |
| **M** | Toggle Mode (Single vs. Grid Race) |
| **T** | Toggle Theme (Dark / Light) |
| **S** | Toggle Sound (Mute/Unmute) |
| **I** | Toggle Info Sheet (Complexities & Notes) |
| **+/-** | Increase / Decrease Speed (Exponential) |
| **Arrows** | Adjust Array Size (Fine tuning) |
| **Shift/Ctrl** | Hold with Arrows for larger increments (±100, ±1000) |

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

> **[PLACEHOLDER: Insert GIF of "Themes & Green Sweep" here]**
> *Recommendation: Show toggling 'T' for Light Mode and the green finish animation.*
> `![Theme Demo](assets/demo_theme.gif)`

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

📂 Project Structure
Plaintext

AlgoRacer/
├── assets/              # GIFs and Images for documentation
├── main.py              # Entry point and Event Loop
├── algorithms.py        # Logic for all 16 sorting algorithms
├── visualizer.py        # UI rendering and State management
├── sound_manager.py     # NumPy audio generation engine
├── settings.py          # Configuration constants and Themes
└── requirements.txt     # Project dependencies

---

*Created by Casey Dane - 2025*
