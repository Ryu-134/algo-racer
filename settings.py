# settings.py

# --- Configuration ---
FPS = 60
HEADER_ZONE = 115 

# --- Global Colors ---
BACKGROUND_COLOR = (24, 29, 39)
WHITE = (255, 255, 255)
UI_BACKGROUND_COLOR = (44, 51, 64)
TEXT_COLOR = (200, 200, 200)

# Colors for UI Elements
OVERLAY_COLOR = (0, 0, 0, 200) 
INFO_BG_COLOR = (30, 35, 45)
INFO_HEADER_COLOR = (60, 70, 90)
INFO_ROW_EVEN = (35, 40, 50)
INFO_ROW_ODD = (30, 35, 45)
GREEN_TEXT = (100, 255, 100)
RED_TEXT = (255, 100, 100)
YELLOW_TEXT = (255, 255, 100)
HOVER_COLOR = (50, 205, 50)
BTN_COLOR = (0, 120, 215)
BTN_HOVER_COLOR = (60, 160, 240)
MUTE_COLOR = (200, 60, 60)
MUTE_HOVER_COLOR = (240, 100, 100)
FINISH_COLOR = (0, 200, 80)

# --- Color Themes ---
THEMES = {
    "dark": {
        "bg": (24, 29, 39),
        "ui_bg": (44, 51, 64),
        "text": (200, 200, 200),
        "bar_border": None,
        "info_bg": (30, 35, 45),
        "info_header": (60, 70, 90),
        "info_row_even": (35, 40, 50),
        "info_row_odd": (30, 35, 45),
        "overlay": (0, 0, 0, 200)
    },
    "light": {
        "bg": (245, 245, 250),
        "ui_bg": (220, 220, 225),
        "text": (40, 40, 50),
        "bar_border": (100, 100, 100),
        "info_bg": (255, 255, 255),
        "info_header": (200, 200, 220),
        "info_row_even": (240, 240, 245),
        "info_row_odd": (255, 255, 255),
        "overlay": (255, 255, 255, 150)
    }
}

# --- Algorithm Educational Data ---
ALGO_INFO = {
    "Bubble Sort":      ["O(n)", "O(n^2)", "O(n^2)", "O(1)", "Yes", "Teaching & small datasets"],
    "Cocktail Shaker":  ["O(n)", "O(n^2)", "O(n^2)", "O(1)", "Yes", "Slightly faster Bubble Sort"],
    "Comb Sort":        ["O(n log n)", "O(n^2)", "O(n^2)", "O(1)", "No", "Improved Bubble Sort (Gaps)"],
    "Odd-Even Sort":    ["O(n)", "O(n^2)", "O(n^2)", "O(1)", "Yes", "Parallel processing variant"],
    "Insertion Sort":   ["O(n)", "O(n^2)", "O(n^2)", "O(1)", "Yes", "Small or nearly sorted data"],
    "Gnome Sort":       ["O(n)", "O(n^2)", "O(n^2)", "O(1)", "Yes", "Teaching; Conceptually simple"],
    "Shell Sort":       ["O(n log n)", "O(n^4/3)", "O(n^2)", "O(1)", "No", "Medium arrays; Gap sequence"],
    "Selection Sort":   ["O(n^2)", "O(n^2)", "O(n^2)", "O(1)", "No", "Minimizes memory writes"],
    "Merge Sort":       ["O(n log n)", "O(n log n)", "O(n log n)", "O(n)", "Yes", "Linked Lists; Stable sorting"],
    "Quick Sort":       ["O(n log n)", "O(n log n)", "O(n^2)", "O(log n)", "No", "Fastest general purpose (avg)"],
    "Heap Sort":        ["O(n log n)", "O(n log n)", "O(n log n)", "O(1)", "No", "Systems with low memory"],
    "Tim Sort":          ["O(n)", "O(n log n)", "O(n log n)", "O(n)", "Yes", "Python/Java standard; Real-world"],
    "Stooge Sort":      ["O(n^2.7)", "O(n^2.7)", "O(n^2.7)", "O(n)", "No", "Teaching only; Very slow!"],
    "Counting Sort":    ["O(n+k)", "O(n+k)", "O(n+k)", "O(k)", "Yes", "Integers with small range"],
    "Bucket Sort":      ["O(n+k)", "O(n+k)", "O(n^2)", "O(n)", "Yes", "Uniformly distributed data"],
    "Radix Sort":       ["O(nk)", "O(nk)", "O(nk)", "O(n+k)", "Yes", "Integers/Strings; Fixed length"],
}