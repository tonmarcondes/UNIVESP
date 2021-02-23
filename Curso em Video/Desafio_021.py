# MP3
import selenium
import pygame

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('c:/Users/wmarc/OneDrive/Documentos/UNIVESP/Curso em Video/Desafio_021.mp3')
pygame.mixer.music.play()
pygame.event.wait()