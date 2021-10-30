import pygame


class HangManPics:
    def __init__(self):
        self.hangmanPics = []

    def setHangManPic(self):
        for i in range(7):
            self.hangmanPics.append(pygame.image.load(
                "hangManPic"+"/"+"hangman"+str(i)+".png"))

    def draw_hangman(self, limbs, ai_game):
        pic = self.hangmanPics[limbs]
        ai_game.win.blit(pic, (100, 230))
