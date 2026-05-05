
import pygame
import sys
import random
import obstacle
import time
import sounddevice as sd
import numpy as np
import bar
import Runner

#Initialize pygame
pygame.init()

current_volume = 0.0

def audio_callback(indata, frames, time, status):
    global current_volume
    volume_norm = np.linalg.norm(indata) * 10
    current_volume = volume_norm

# Start microphone stream
stream = sd.InputStream(callback=audio_callback)
stream.start()

# ── Config ─────────────────────────────────────────────────────────────────
BASE_THRESHOLDS = [0.01, 0.02, 0.04, 0.07, 0.11, 0.16, 0.22, 0.29, 0.37, 0.46]
SENSITIVITY     = 200  # lower = more sensitive, higher = need to shout more
THRESHOLDS      = [t * SENSITIVITY for t in BASE_THRESHOLDS]

barGraphicSet = [
    pygame.image.load('graphics/bar0.png'),
    pygame.image.load('graphics/bar1.png'),
    pygame.image.load('graphics/bar2.png'),
    pygame.image.load('graphics/bar3.png'),
    pygame.image.load('graphics/bar4.png'),
    pygame.image.load('graphics/bar5.png'),
    pygame.image.load('graphics/bar6.png'),
    pygame.image.load('graphics/bar7.png'),
    pygame.image.load('graphics/bar8.png'),
    pygame.image.load('graphics/bar9.png'),
    pygame.image.load('graphics/bar10.png')
]

def get_bar_level():
    """Returns 0–10 based on current mic volume."""
    level = 0
    for threshold in THRESHOLDS:
        if current_volume >= threshold:
            level += 1
        else:
            break
    return level