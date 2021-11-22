
import pygame

# lớp các nút phím chứa chữ cái


class Button:
    def __init__(self):
        self.buttons = []

    def setButton(self, width):  # cài đặt cái thông tin về ô chữ
        increase = round(width / 13)
        for i in range(26):
            if i < 13:
                x = 25 + (increase * i)
                y = 120
            else:
                x = 25 + (increase * (i - 13))
                y = 165
            self.buttons.append([(224, 255, 255), x, y, 20, True, 65 + i])
            # buttons.append([color, x_pos, y_pos, radius, visible, char])

    def draw_button(self, ai_game, setting):  # vẽ các nút chữ cái
        for i in range(len(self.buttons)):
            if self.buttons[i][4]:
                pygame.draw.circle(
                    ai_game.win, setting.BLACK, (self.buttons[i][1], self.buttons[i][2]), self.buttons[i][3])
                pygame.draw.circle(ai_game.win, self.buttons[i][0], (
                    self.buttons[i][1], self.buttons[i][2]), self.buttons[i][3] - 2)
                # pygame.draw.circle(surface, color, center, radius, width)
                label = setting.btn_font.render(
                    chr(self.buttons[i][5]), 1, setting.BLACK)
                ai_game.win.blit(label, (self.buttons[i][1] - (
                    label.get_width() / 2), self.buttons[i][2] - (label.get_height() / 2)))

    def update_button(self):  # cập nhật lại nút
        for i in range(len(self.buttons)):
            self.buttons[i][4] = True

    def draw_Play(self, setting, ai_game):  # vẽ mà hình play
        ai_game.win.fill((255, 255, 255))
        pic = pygame.image.load("pic/hehe.png")

        ai_game.win.blit(pic, (200, 50))
        pic = pygame.image.load("pic/may.png")

        ai_game.win.blit(pic, (200, 50))

        pygame.draw.rect(ai_game.win, (0, 0, 0), (300, 330, 100, 50), 2, 5)
        pygame.draw.rect(ai_game.win, (224, 255, 255),
                         (302, 332, 96, 46), 0, 4)

        play = setting.chude.render("PLAY", 1, (0, 0, 0))
        ai_game.win.blit(
            play, (350-play.get_width()/2, 355-play.get_height()/2))
        chao = setting.chude.render("Welcome to Hangman game!!!", 1, (0, 0, 0))
        ai_game.win.blit(chao, (350-chao.get_width()/2, 325-chao.get_height()))
        pygame.draw.rect(ai_game.win, (0, 0, 0), (8, 20, 70, 45), 2, 5)
        pic = pygame.image.load("pic/dots.png")  # chèn dấu 3 chấm
        ai_game.win.blit(pic, (10, 10))

    def draw_GoiY(self, setting, ai_game):  # vẽ ô gợi ý
        pygame.draw.rect(ai_game.win, setting.BLACK,
                         (600, 230, 50, 50), 2, 5)  # vẽ ô gọi ý
        pic = pygame.image.load("pic/idea.png")  # chèn ảnh cái bóng đèn
        ai_game.win.blit(pic, (609, 237))

        if ai_game.mark_hint == True:  # nếu có ấn vào ô gợi ý thì hiện hình ảnh
            pic = pygame.image.load(
                str(setting.Word.word1)+"/"+str(setting.Word.word)+".png")
            ai_game.win.blit(pic, (440, 310))

    def draw_LuatChoi(self, setting, ai_game):  # vẽ luật chơi
        win = ai_game.win
        win.fill((248, 248, 255))  # vẽ màn hình luật chơi
        # điền luật chơi
        hehe = pygame.font.SysFont("MTO Astro City", 25)
        file = "chude/ruleHangman.txt"
        f = open(file, 'r')  # mở file và in từng dòng
        i = 0
        while True:
            r = f.readline()
            if r == '':
                break
            # strip dùng để xóa nội dung xuống dòng
            luatchoi1 = hehe.render(r.strip(), 1, (0, 0, 0))
            win.blit(luatchoi1, (50, 100+i*30))
            i += 1
        f.close()

        pygame.draw.rect(win, (0, 0, 0), (638, 18, 35, 35))
        pic = pygame.image.load("pic/daux.png")  # chèn dấu X thoát game
        win.blit(pic, (640, 20))
