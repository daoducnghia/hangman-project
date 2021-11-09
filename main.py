import pygame
from setting import Setting
import pygame.locals


class HangMan:
    def __init__(self):
        """Khởi tạo game và tạo nguồn game"""
        pygame.init()
        # thiết lập của sổ game
        self.setting = Setting()
        self.win = pygame.display.set_mode(
            (self.setting.winWidth, self.setting.winHeight))
        # tạo tiêu đề tên cửa sổ game
        pygame.display.set_caption("Hangman game!!!")
        # tạo icon của cửa sổ
        icon_img = pygame.image.load('pic/icon.png')
        pygame.display.set_icon(icon_img)

        self.inplay = True  # để đánh dấu xem đã kết thúc trò chơi hay chưa
        self.mark_hint = False  # để kiểm tra xem người chơi có ấn vào nút gợi ý không
        self.mark_play = False  # kiểm tra xem có ấn nút play hay không
        self.mark_rule = False  # kiểm tra xem có ấn vào nút luật chơi không
        self.again = True
        # biến đánh dấu xem in hình hangman nào
        self.limbs = 0

    def update_screen(self):
        '''Đi đến màn hình bắt đầu khi bất đầu chơi'''
        self.limbs = 0
        self.mark_hint = False

    def run_game(self):
        '''Chạy game'''
        while self.inplay:
            self.setting.redraw_game_window(self)
            self._check_events()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.inplay = False
            elif event.type == pygame.KEYDOWN:
                self._check_keydown(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self._check_mousebuttondown()

    def _check_keydown(self, event):
        '''Nhấn q để thoát game'''
        if event.key == pygame.K_q:
            self.inplay = False

    def _check_mousebuttondown(self):
        clickPos = pygame.mouse.get_pos()
        if self.mark_play == False:  # màn hình chứa chữ play
            pygame.mixer.Sound.play(self.setting.sound1)
            self.mark_rule = self.setting.ktraAnNutLuatChoi(
                clickPos[0], clickPos[1])
            self.mark_play = self.setting.ktraAnNutPlay(
                clickPos[0], clickPos[1])
        else:  # Bắt đầu vào màn hình chơi mark_play = true
            pygame.mixer.Sound.play(self.setting.sound2)
            letter = self.setting.buttonHit(
                clickPos[0], clickPos[1], self.setting.Buttons.buttons)  # chữ đc ấn
            if letter != None:
                # guessed[] chứa các chữ đc ấn
                self.setting.Word.guessed.append(chr(letter))
                self.setting.Buttons.buttons[letter - 65][4] = False
                # kiểm tra xem chữ ấy có thuộc từ cần điền không
                if self.setting.hang(chr(letter), self.setting.Word.word):
                    if self.limbs != 5:
                        self.limbs += 1  # nếu sai thi sẽ hiện thêm một thêm một phần
                    else:
                        pygame.mixer.Sound.play(
                            self.setting.sound4)  # chèn âm thanh
                        self.setting.end(self)  # ra màn hình kết thúc game
                else:
                    # hien day chu tren man hinh terminal
                    print(self.setting.Word.spacedOut())
                    if self.setting.Word.spacedOut().count('_') == 0:  # nếu số gạch bằng 0 --> thắng
                        pygame.mixer.Sound.play(
                            self.setting.sound3)  # chèn âm thanh
                        self.setting.end(self, True)  # thắng
            # kiem tra xem có ấn vào nút gợi ý không
            letter1 = self.setting.ktra(
                clickPos[0], clickPos[1], self.setting.Word.word)
            if letter1 != None:  # nếu có ấn thì mark bằng True
                self.mark_hint = True


if __name__ == '__main__':
    ai = HangMan()
    ai.run_game()
