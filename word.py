import pygame
import random
# chọn chủ đề


class Word:
    def __init__(self):
        self.word1 = ""  # chu de
        self.word = ""  # tu
        self.guessed = []  # chứa các chữ cái mà người chơi đã chọn

    def randomWord(self):  # chon ngau nhien chu de
        with open('words.txt') as file:
            f = file.readlines()
        i = random.randrange(0, len(f) - 1)
        return f[i][:-1]# trả về chuỗi từ không chứa kí tự xuống dòng

    def randomWord1(self):  # chon ngau nhien tu khoa
        with  open("chude"+"/"+self.word1+".txt") as file2:
            f2 = file2.readlines()
        j = random.randrange(0, len(f2)-1)
        return f2[j][:-1] #trả về chuỗi từ không chứa kí tự xuống dòng

    def spacedOut(self):  # trả về chuỗi _ _ _ _ và các chữ cái đc điền
        spacedWord = ''
        guessedLetters = self.guessed
        for x in range(len(self.word)):
            if self.word[x] != ' ':
                spacedWord += '_ '
                # kiểm tra xem có chữ nào đc ấn chưa nếu có rồi thì in ra chữ đó
                for i in range(len(guessedLetters)):
                    if self.word[x].upper() == guessedLetters[i]:
                        spacedWord = spacedWord[:-2]
                        spacedWord += self.word[x].upper() + ' '
            elif self.word[x] == ' ':
                spacedWord += ' '
        return spacedWord  # trả về chuỗi đến hiện tại mà người chơi tìm đc

    # hiện thị các dấu _ _ .. và các chữ cái người chơi điền đc
    def draw_answer(self, setting, ai_game):
        spaced = self.spacedOut()  # tao cac dau gach _ _ _
        label1 = setting.guess_font.render(spaced, 1, setting.BLACK)
        rect = label1.get_rect()  # get the rectangular area of the Surface
        length = rect[2]
        ai_game.win.blit(label1, (setting.winWidth/2 - length/2, 480))

    def draw_chude(self, setting, ai_game):  # hiển thị chủ đề lên màn hình trò chơi
        pygame.draw.rect(ai_game.win, setting.BLACK,
                         (400, 230, 150, 50), 2, 5)  # ve hinh chu nhat
        # ve hinh chu nhat ben trong
        pygame.draw.rect(ai_game.win, (224, 255, 255),
                         (402, 232, 146, 46), 0, 4)

        tmp = setting.chude.render(
            self.word1, 1, setting.BLACK)  # viet ten chu de
        ai_game.win.blit(tmp, (475-tmp.get_width()/2, 255-tmp.get_height()/2))

    def update_word(self):  # cập nhật lại các biến
        self.guessed = []
        self.word1 = self.randomWord()
        self.word = self.randomWord1()
