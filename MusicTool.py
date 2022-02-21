import pygame
import os

class MusicTool:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.volume = 0.5
        self.Mulen = 0

    def playMusic(self, path: str):
        pygame.mixer.music.load(path)
        pygame.mixer.music.set_volume(float(self.volume))
        self.Mulen = pygame.mixer.Sound(path).get_length()
        self.just_play(0)

    def just_play(self, start):
        pygame.mixer.music.play(loops=0, start=start)

    def pauseMusic(self):
        pygame.mixer.music.pause()

    def continueMusic(self):
        pygame.mixer.music.unpause()

    def getMusicLen(self):
        return self.Mulen

    def getMusicPos(self):
        return pygame.mixer.music.get_pos()

    def setMusicPos(self, var):
        pygame.mixer.music.set_pos(var)

    def rewind(self):
        pygame.mixer.music.rewind()

    def changeVolume(self, value):
        try:
            self.volume = value
            pygame.mixer.music.set_volume(float(self.volume))
        except Exception as e:
            print(e)



