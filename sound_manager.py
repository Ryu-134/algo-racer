import pygame
import numpy as np

class SoundManager:
    def __init__(self):
        mixer_settings = pygame.mixer.get_init()
        
        if not mixer_settings:
            pygame.mixer.init(frequency=44100, size=-16, channels=1, buffer=512)
            mixer_settings = pygame.mixer.get_init()
            
        frequency, size, channels = mixer_settings
        self.enabled = True
        self.muted = False 
        self.sounds = {}
        self.num_tones = 100  
        
        for i in range(self.num_tones):
            freq = 200 + (i / self.num_tones) * 1000 
            duration = 0.05  
            n_samples = int(frequency * duration)
            t = np.linspace(0, duration, n_samples, False)
            
            wave = (4096 * np.sin(2 * np.pi * freq * t)).astype(np.int16)
            
            if channels == 2:
                wave = np.column_stack((wave, wave))
            
            self.sounds[i] = pygame.sndarray.make_sound(wave)
            self.sounds[i].set_volume(0.1)

    def toggle(self):
        self.muted = not self.muted

    def play(self, val, max_val):
        if not self.enabled or self.muted or max_val == 0: return
        idx = int((val / max_val) * (self.num_tones - 1))
        idx = max(0, min(idx, self.num_tones - 1))
        self.sounds[idx].play()