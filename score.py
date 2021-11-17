import pygame


class Score:
    def __init__(self):
        self.score = 0

    def draw_score(self, setting, ai_game):  # hiện thị điểm
        # vẽ ô điểm
        pygame.draw.rect(ai_game.win, setting.BLACK,
                         (20, 23, 150, 50), 2, 5)  # ve hinh chu nhat
        pygame.draw.rect(ai_game.win, (224, 255, 255),
                         (22, 25, 146, 46), 0, 5)  # ve hinh chu nhat
        # vẽ chữ score
        score1 = setting.chude.render(
            "SCORE: "+str(self.score), 1, setting.BLACK)
        ai_game.win.blit(score1, (27, 48-score1.get_height()/2))

    def update_score(self, mark):  # cập nhật điểm
        if(mark == True):
            self.score = self.score+5
        else:
            self.score = self.score+10
            
    def check_highScore(self):
        with open("score.txt",'r') as f:
            r=f.read()
        self.HighScore=int(r)
        if self.HighScore<self.score:
            self.HighScore=self.score
            with open("score.txt",'w') as f:
                f.write(str(self.HighScore))
                
    def reset_score(self):  # cho điểm về 0
        self.score = 0
