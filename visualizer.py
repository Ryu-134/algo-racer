import pygame
import random
import math
import sys
from settings import *
from algorithms import SortingAlgorithms
from sound_manager import SoundManager

class SortState:
    def __init__(self, name, func, array_size, min_val, max_val):
        self.name = name
        self.func = func
        self.array = [random.randint(max(1, min_val), max_val) for _ in range(array_size)]
        self.generator = None
        self.finished = False
        self.highlighted = []
        self.pivot_index = -1
        self.comparisons = 0
        self.accesses = 0
        self.animating_finish = False
        self.finish_index = 0

    def start(self):
        self.generator = self.func(self.array, self)
        self.finished = False
        self.animating_finish = False
        self.finish_index = 0
        self.comparisons = 0
        self.accesses = 0

class SorterVisualizer:
    def __init__(self):
        pygame.init()
        self.sound = SoundManager()
        
        info = pygame.display.Info()
        screen_w = info.current_w
        screen_h = info.current_h
        
        self.width = int(screen_w * 0.9)
        self.height = int(screen_h * 0.9)
        self.screen = pygame.display.set_mode((self.width, self.height), pygame.RESIZABLE)
        
        pygame.display.set_caption("AlgoRacer: Advanced Sorting Visualizer")
        self.clock = pygame.time.Clock()
        self.running = True
        self.frame_count = 0 
        
        self.array_size = 100
        self.speed_value = 1 
        self.show_info = False 
        self.close_btn_rect = None 
        self.info_btn_rect = None
        self.mute_btn_rect = None 
        
        self.theme_name = "dark"
        self.colors = THEMES[self.theme_name]
        
        self.algo_map = {
            "Bubble Sort": SortingAlgorithms.bubble_sort,       
            "Insertion Sort": SortingAlgorithms.insertion_sort, 
            "Selection Sort": SortingAlgorithms.selection_sort, 
            "Merge Sort": SortingAlgorithms.merge_sort,         

            "Quick Sort": SortingAlgorithms.quick_sort,         
            "Heap Sort": SortingAlgorithms.heap_sort,           
            "Tim Sort": SortingAlgorithms.tim_sort,              
            "Shell Sort": SortingAlgorithms.shell_sort,         

            "Counting Sort": SortingAlgorithms.counting_sort,   
            "Radix Sort": SortingAlgorithms.radix_sort,         
            "Bucket Sort": SortingAlgorithms.bucket_sort,       
            "Cocktail Shaker": SortingAlgorithms.cocktail_shaker_sort, 

            "Comb Sort": SortingAlgorithms.comb_sort,           
            "Gnome Sort": SortingAlgorithms.gnome_sort,         
            "Odd-Even Sort": SortingAlgorithms.odd_even_sort,   
            "Stooge Sort": SortingAlgorithms.stooge_sort,       
        }
        self.algo_names = list(self.algo_map.keys())
        self.current_algo_idx = 0
        
        self.view_mode = "single" 
        self.active_states = [] 
        self.is_sorting = False
        self.paused = False

        self.font_large = pygame.font.SysFont('Arial', 32, bold=True)
        self.font_medium = pygame.font.SysFont('Arial', 22) 
        self.font_small = pygame.font.SysFont('Arial', 20)
        self.font_title = pygame.font.SysFont('Arial', 22, bold=True)
        self.font_mono = pygame.font.SysFont('Consolas', 18) 
        
        self.rebuild_states()

    def toggle_theme(self):
        self.theme_name = "light" if self.theme_name == "dark" else "dark"
        self.colors = THEMES[self.theme_name]

    def rebuild_states(self):
        self.active_states = []
        self.width = self.screen.get_width()
        self.height = self.screen.get_height()
        
        if self.view_mode == "single":
            name = self.algo_names[self.current_algo_idx]
            self.active_states.append(
                SortState(name, self.algo_map[name], self.array_size, 5, self.height - 200)
            )
        else:
            rows = 4
            cols = 4
            grid_h = (self.height - 120) // rows
            for i, name in enumerate(self.algo_names):
                if i >= rows * cols: break
                self.active_states.append(
                    SortState(name, self.algo_map[name], self.array_size // 2, 2, grid_h - HEADER_ZONE - 10)
                )

        self.is_sorting = False
        self.paused = False

    def handle_events(self):
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                self.running = False
            
            if event.type == pygame.VIDEORESIZE:
                self.width = event.w
                self.height = event.h
                self.screen = pygame.display.set_mode((self.width, self.height), pygame.RESIZABLE)
                self.rebuild_states()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.show_info:
                    if self.close_btn_rect and self.close_btn_rect.collidepoint(mouse_pos):
                        self.show_info = False
                else:
                    if self.info_btn_rect and self.info_btn_rect.collidepoint(mouse_pos):
                        self.show_info = not self.show_info
                    elif self.mute_btn_rect and self.mute_btn_rect.collidepoint(mouse_pos):
                        self.sound.toggle()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_i: self.show_info = not self.show_info
                if event.key == pygame.K_t: self.toggle_theme()
                if event.key == pygame.K_s: self.sound.toggle()
                
                if not self.show_info: 
                    if event.key == pygame.K_r: self.rebuild_states()
                    elif event.key == pygame.K_SPACE:
                        if not self.is_sorting: self.start_sorting()
                        else: self.paused = not self.paused
                    elif event.key == pygame.K_m:
                        self.view_mode = "all" if self.view_mode == "single" else "single"
                        self.rebuild_states()

                    if not self.is_sorting:
                        step = 10
                        keys = pygame.key.get_pressed()
                        if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]: step = 100
                        elif keys[pygame.K_LCTRL] or keys[pygame.K_RCTRL]: step = 1000

                        if event.key == pygame.K_UP:
                            self.array_size = min(10000, self.array_size + step)
                            self.rebuild_states()
                        elif event.key == pygame.K_DOWN:
                            self.array_size = max(10, self.array_size - step)
                            self.rebuild_states()

                    if self.view_mode == "single" and not self.is_sorting:
                        if event.key == pygame.K_RIGHT:
                            self.current_algo_idx = (self.current_algo_idx + 1) % len(self.algo_names)
                            self.rebuild_states()
                        elif event.key == pygame.K_LEFT:
                            self.current_algo_idx = (self.current_algo_idx - 1) % len(self.algo_names)
                            self.rebuild_states()
                    
                    if event.key == pygame.K_EQUALS: 
                        if self.speed_value < 1:
                            self.speed_value += 1
                            if self.speed_value == 0: self.speed_value = 1
                        else:
                            self.speed_value = min(5000, int(self.speed_value * 1.5) + 1)
                    elif event.key == pygame.K_MINUS: 
                        if self.speed_value > 1:
                            self.speed_value = int(self.speed_value / 1.5)
                        else:
                            self.speed_value -= 5
                            self.speed_value = max(-60, self.speed_value)

    def start_sorting(self):
        for state in self.active_states:
            state.start()
        self.is_sorting = True
        self.paused = False

    def update(self):
        if self.is_sorting and not self.paused and not self.show_info:
            self.frame_count += 1
            all_finished = True
            
            should_update = True
            ops_to_run = 1
            
            if self.speed_value < 0:
                delay = abs(self.speed_value)
                if self.frame_count % delay != 0: should_update = False
                else: ops_to_run = 1
            else:
                ops_to_run = self.speed_value
                
            if should_update:
                for state in self.active_states:
                    if state.generator:
                        if self.view_mode != "single" and ops_to_run > 1:
                            ops_to_run = max(1, ops_to_run // 2)
                        
                        for _ in range(ops_to_run):
                            try:
                                next(state.generator)
                                all_finished = False 
                                if state.highlighted and ops_to_run < 500:
                                    idx = state.highlighted[0]
                                    val = state.array[idx]
                                    self.sound.play(val, max(state.array))
                            except StopIteration:
                                state.generator = None
                                state.finished = True
                                state.highlighted = []
                                state.animating_finish = True
                                all_finished = False 
                                break
                    else:
                        if state.animating_finish:
                            all_finished = False
                            state.finish_index += max(1, len(state.array) // 20)
                            if state.finish_index >= len(state.array):
                                state.animating_finish = False
                        elif not state.finished: 
                            all_finished = False
            else:
                for state in self.active_states:
                     if not state.finished: all_finished = False
            
            if all_finished:
                self.is_sorting = False

    def draw_state(self, state, x_offset, y_offset, width, height):
        border_col = self.colors["bar_border"] if self.colors["bar_border"] else (60, 60, 60)
        pygame.draw.rect(self.screen, border_col, (x_offset, y_offset, width, height), 1)
        
        title_surf = self.font_title.render(f"{state.name}", True, self.colors["text"])
        self.screen.blit(title_surf, (x_offset + 5, y_offset + 5))

        stats_color = self.colors["text"]
        if state.finished and not state.animating_finish: stats_color = FINISH_COLOR
        
        cmp_text = f"Comparisons: {state.comparisons}"
        acc_text = f"Array Accesses: {state.accesses}"
        
        cmp_surf = self.font_small.render(cmp_text, True, stats_color)
        acc_surf = self.font_small.render(acc_text, True, stats_color)
        
        self.screen.blit(cmp_surf, (x_offset + 5, y_offset + 40)) 
        self.screen.blit(acc_surf, (x_offset + 5, y_offset + 65)) 

        bar_area_y = y_offset + HEADER_ZONE 
        bar_area_h = height - HEADER_ZONE
        
        if not state.array: return
        bar_width = width / len(state.array)
        
        for i, val in enumerate(state.array):
            bx = x_offset + (i * bar_width)
            draw_val = min(val, bar_area_h)
            by = (y_offset + height) - draw_val
            
            color = pygame.Color(0,0,0)
            hue = (val / (bar_area_h + 10)) * 280 
            hue = min(280, max(0, hue))
            
            if self.theme_name == "light":
                color.hsva = (hue, 80, 80, 100)
            else:
                color.hsva = (hue, 100, 100, 100)
            
            if state.animating_finish:
                if i <= state.finish_index: color = FINISH_COLOR
            elif state.finished: color = FINISH_COLOR
            elif i in state.highlighted: color = WHITE if self.theme_name == "dark" else (50, 50, 50)
            elif i == state.pivot_index: color = (255, 0, 0)
            
            pygame.draw.rect(self.screen, color, (int(bx), int(by), math.ceil(bar_width), draw_val))

    def draw_info_overlay(self):
        overlay = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        overlay.fill(self.colors["overlay"])
        self.screen.blit(overlay, (0,0))

        panel_w = int(self.width * 0.95)
        panel_h = int(self.height * 0.85)
        panel_x = (self.width - panel_w) // 2
        panel_y = (self.height - panel_h) // 2
        
        pygame.draw.rect(self.screen, self.colors["info_bg"], (panel_x, panel_y, panel_w, panel_h))
        pygame.draw.rect(self.screen, self.colors["text"], (panel_x, panel_y, panel_w, panel_h), 2)

        title_surf = self.font_large.render("Algorithm Reference Sheet", True, self.colors["text"])
        self.screen.blit(title_surf, (panel_x + 20, panel_y + 20))

        col_headers = ["Algorithm", "Best", "Avg", "Worst", "Space", "Stable", "Use Case / Notes"]
        col_x_offsets = [10, 280, 440, 600, 760, 880, 1000]
        
        header_y = panel_y + 70
        pygame.draw.rect(self.screen, self.colors["info_header"], (panel_x + 10, header_y, panel_w - 20, 35))
        
        for i, header in enumerate(col_headers):
            txt_col = YELLOW_TEXT if self.theme_name == "dark" else (50, 50, 150)
            txt = self.font_title.render(header, True, txt_col)
            self.screen.blit(txt, (panel_x + 10 + col_x_offsets[i], header_y + 5))

        row_y = header_y + 40
        for i, (name, info) in enumerate(ALGO_INFO.items()):
            bg_color = self.colors["info_row_even"] if i % 2 == 0 else self.colors["info_row_odd"]
            pygame.draw.rect(self.screen, bg_color, (panel_x + 10, row_y, panel_w - 20, 30))
            
            name_surf = self.font_mono.render(name, True, self.colors["text"])
            self.screen.blit(name_surf, (panel_x + 15, row_y + 5))
            
            for j, text in enumerate(info):
                color = self.colors["text"]
                if "n^2" in text or "n!" in text: color = RED_TEXT
                elif "log" in text or "O(n)" == text or "O(1)" == text: color = GREEN_TEXT
                if self.theme_name == "light" and color == GREEN_TEXT: color = (0, 150, 0)
                
                txt_surf = self.font_mono.render(text, True, color)
                self.screen.blit(txt_surf, (panel_x + 10 + col_x_offsets[j+1], row_y + 5))
            row_y += 32

        close_txt_str = "Press 'I' or Click Here to Close"
        mouse_pos = pygame.mouse.get_pos()
        text_w, text_h = self.font_medium.size(close_txt_str)
        text_x = panel_x + 20
        text_y = panel_y + panel_h - 40
        self.close_btn_rect = pygame.Rect(text_x, text_y, text_w, text_h)
        
        color = self.colors["text"]
        if self.close_btn_rect.collidepoint(mouse_pos):
            color = HOVER_COLOR
        close_txt = self.font_medium.render(close_txt_str, True, color)
        self.screen.blit(close_txt, (text_x, text_y))

    def draw(self):
        self.screen.fill(self.colors["bg"])
        pygame.draw.rect(self.screen, self.colors["ui_bg"], (0, 0, self.width, 120))
        
        header_text = f"Mode: {self.view_mode.upper()} (Press 'M')"
        self.screen.blit(self.font_large.render(header_text, True, self.colors["text"]), (20, 15))
        
        mouse_pos = pygame.mouse.get_pos()
        
        btn_w = 140
        btn_h = 40
        btn_x = self.width - 160 
        btn_y = 15
        self.info_btn_rect = pygame.Rect(btn_x, btn_y, btn_w, btn_h)
        
        col = BTN_HOVER_COLOR if self.info_btn_rect.collidepoint(mouse_pos) else BTN_COLOR
        pygame.draw.rect(self.screen, col, self.info_btn_rect, border_radius=5)
        btn_txt = self.font_title.render("INFO (I)", True, WHITE)
        btn_rect = btn_txt.get_rect(center=self.info_btn_rect.center)
        self.screen.blit(btn_txt, btn_rect)

        mute_x = self.width - 310
        self.mute_btn_rect = pygame.Rect(mute_x, btn_y, btn_w, btn_h)
        
        if self.sound.muted:
            base_col = MUTE_COLOR
            hover_col = MUTE_HOVER_COLOR
        else:
            base_col = BTN_COLOR
            hover_col = BTN_HOVER_COLOR
            
        m_col = hover_col if self.mute_btn_rect.collidepoint(mouse_pos) else base_col
        pygame.draw.rect(self.screen, m_col, self.mute_btn_rect, border_radius=5)
        mute_label = "UNMUTE" if self.sound.muted else "SOUND"
        mute_txt = self.font_title.render(f"{mute_label} (S)", True, WHITE)
        mute_rect = mute_txt.get_rect(center=self.mute_btn_rect.center)
        self.screen.blit(mute_txt, mute_rect)

        if self.speed_value > 0:
            speed_str = f"{self.speed_value} Ops/Frame"
        else:
            speed_str = f"Delay {abs(self.speed_value)} Frames"
            
        paused_text = " | PAUSED" if self.paused and self.is_sorting else ""
        sep = "   |   "
        ctrl_text_1 = f"Speed (+/-): {speed_str}{sep}SPACE: Start/Pause{paused_text}{sep}R: Reset{sep}T: Theme{sep}ESC: Quit"
        ctrl_text_2 = f"Size: {self.array_size}{sep}Adjust: Arrow (10),  + Shift (100),  + Ctrl (1000)"
        
        self.screen.blit(self.font_medium.render(ctrl_text_1, True, self.colors["text"]), (20, 55))
        self.screen.blit(self.font_medium.render(ctrl_text_2, True, self.colors["text"]), (20, 85))

        if self.view_mode == "single":
            self.draw_state(self.active_states[0], 20, 120, self.width - 40, self.height - 140)
        else:
            cols = 4
            rows = 4
            cell_w = self.width // cols
            cell_h = (self.height - 120) // rows
            for idx, state in enumerate(self.active_states):
                row = idx // cols
                col = idx % cols
                x = col * cell_w
                y = 120 + (row * cell_h)
                pad = 5
                self.draw_state(state, x + pad, y + pad, cell_w - (pad*2), cell_h - (pad*2))

        if self.show_info:
            self.draw_info_overlay()

        pygame.display.flip()

    def run(self):
        while self.running:
            self.clock.tick(FPS)
            self.handle_events()
            self.update()
            self.draw()
    
    def quit(self):
        pygame.quit()
        sys.exit()