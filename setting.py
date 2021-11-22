import pygame
from hangmanPics import HangManPics
from button import Button
from word import Word
from score import Score
import sys


class Setting:
    def __init__(self):
        # thiết lập cửa sổ game
        self.winHeight = 550
        self.winWidth = 700
        # thiet lap màu
        self.BLACK = (0, 0, 0)
        self.LIGHT_BLUE = (176, 224, 230)
        self.GREEN = (248, 248, 255)
        self.WHITE = (255, 255, 255)
        # thiet lap am thanh
        self.sound1 = pygame.mixer.Sound("amthanh/but0.wav")
        self.sound2 = pygame.mixer.Sound("amthanh/but.wav")
        self.sound3 = pygame.mixer.Sound("amthanh/win.wav")
        self.sound4 = pygame.mixer.Sound("amthanh/fail.wav")
        # thiet lap font chu
        self.btn_font = pygame.font.SysFont("MTO Astro City", 30)
        self.guess_font = pygame.font.SysFont("MTO Astro City", 34)
        self.chude = pygame.font.SysFont("MTO Astro City", 35)
        self.lost_font = pygame.font.SysFont("MTO Astro City", 40)
        # thêm lớp ảnh Hangman
        self.HangmanPics = HangManPics()
        # thêm lớp Button
        self.Buttons = Button()
        # thêm lớp Word(lớp từ)
        self.Word = Word()
        self.Word.word1 = self.Word.randomWord()  # chọn chủ đề ngẫu nhiên
        self.Word.word = self.Word.randomWord1()  # chọn từ ngẫu nhiên trong chủ đề đó

        # thêm lớp Score(điểm)
        self.Score = Score()

    def hang(self, guess, word):  # kiểm tra xem chữ cái được ấn có thuộc từ được điền không
        if guess.lower() not in word.lower():
            return True  # nếu không thì về true --> hiện sang một hình người khác
        else:
            return False

    def buttonHit(self, x, y, buttons):  # kiểm tra xem người chơi có ấn vào chữ cái nào không
        for i in range(len(buttons)):
            if x < buttons[i][1] + 20 and x > buttons[i][1] - 20:
                if y < buttons[i][2] + 20 and y > buttons[i][2] - 20:
                    # sửa : nếu ấn vào vị trí nút cũ thì không nhận nữa
                    if buttons[i][4] == True:
                        return buttons[i][5]
                    else:
                        return None
        return None

    def ktraAnNutPlay(self, x, y):  # kiem tra xem co an nut play khong
        if x > 300 and x < 400:
            if y > 330 and y < 380:
                return True
        return False

    def ktraAnNutLuatChoi(self, x, y):  # kiem tra xem co an nut luat choi khong
        if x > 8 and x < 78:
            if y > 20 and y < 65:
                return True
        return False

    def ktra(self, x, y, word):  # kiem tra xem có ấn vào ô gợi ý không
        if x > 600 and x < 650:
            if y > 230 and y < 280:
                return word
        return None

    def redraw_game_window(self, ai_game):
        if ai_game.mark_play == False:
            if ai_game.mark_rule == False:
                # vẽ màn hình có chữ play
                self.Buttons.draw_Play(self, ai_game)
            else:
                # vẽ màn hình chứa luật chơi
                self.Buttons.draw_LuatChoi(self, ai_game)
        else:
            # vẽ các hình hiện lên màn hình chính để chơi
            ai_game.win.fill((self.GREEN))
            # Buttons
            # Buttons là lớp, buttons là list các nút (thuộc tính của lớp Buttons)
            if len(self.Buttons.buttons) == 0:
                self.Buttons.setButton(self.winWidth)
            # HangMan
            # HangmanPics là lớp, hangmanPics là list các ảnh hangman(thuộc tính của lớp HangmanPics)
            if len(self.HangmanPics.hangmanPics) == 0:
                self.HangmanPics.setHangManPic()
            # vẽ các nút
            self.Buttons.draw_button(ai_game, self)
            # vẽ _ _ _ và các chữ người chơi tìm được
            self.Word.draw_answer(self, ai_game)
            # vẽ chủ đề
            self.Word.draw_chude(self, ai_game)
            # vẽ hình hangman
            self.HangmanPics.draw_hangman(ai_game.limbs, ai_game)
            # vẽ ô gợi ý
            self.Buttons.draw_GoiY(self, ai_game)
            # vẽ ô điểm
            self.Score.draw_score(self, ai_game)
        pygame.display.update()

    def end(self, ai_game, winner=False):
        lostTxt = 'You Lost, press any key to play again...'
        winTxt = 'WINNER! Press any key to play next...'
        print(self.Score.score)
        ai_game.win.fill(self.GREEN)

        if winner == True:
            self.Score.update_score(ai_game.mark_hint)
            label = self.lost_font.render(winTxt, 1, self.BLACK)
        else:
            label = self.lost_font.render(lostTxt, 1, self.BLACK)

        self.Score.check_highScore()

        wordTxt = self.lost_font.render(self.Word.word.upper(), 1, self.BLACK)
        wordWas = self.lost_font.render('The phrase was: ', 1, self.BLACK)
        if winner == False:
            scoreOfYou = self.lost_font.render(
                'Your score: '+str(self.Score.score), 1, self.BLACK)
            ai_game.win.blit(scoreOfYou, (self.winWidth / 2 -
                             scoreOfYou.get_width() / 2, 130))
            HighScore = self.lost_font.render(
                'High Score: '+str(self.Score.HighScore), 1, self.BLACK)
            ai_game.win.blit(HighScore, (20, 20))

            pic = pygame.image.load(
                str(self.Word.word1)+"/"+str(self.Word.word)+".png")
            ai_game.win.blit(pic, (350 - pic.get_width()/2,320))            

        ai_game.win.blit(wordTxt, (self.winWidth/2 -
                         wordTxt.get_width()/2, 280))
        ai_game.win.blit(wordWas, (self.winWidth/2 -
                         wordWas.get_width()/2, 230))
        ai_game.win.blit(label, (self.winWidth / 2 -
                         label.get_width() / 2, 180))
        pygame.display.update()

        again = True
        while again:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()  # thoát trò chơi
                if event.type == pygame.KEYDOWN:
                    again = False
        if(winner == False):
            self.Score.reset_score()
        self.reset(ai_game)

    def reset(self, ai_game):
        self.Buttons.update_button()
        self.Word.update_word()
        ai_game.update_screen()
