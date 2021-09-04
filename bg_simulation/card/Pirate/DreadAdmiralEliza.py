from ..Card import Card

class DreadAdmiralEliza(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = '아군 해적이 공격할 때마다 모든 아군 하수인에게 +2/+1을 부여합니다.'
        self.type = 'Pirate'
        self.name = '공포의 제독 엘리자'
        self.name_eng = 'Dread Admiral Eliza'
        self.attack = 6
        self.health = 7
        self.tier = 6
        self.live = True
        self.taunt = False
        self.divine_shield = False
        self.windfury = False
        self.reborn = False
        self.frenzy = False
        self.poison = False
        self.avenge = False
        self.avenge_count = 0
        self.death_rattle = False
        self.battle_cry = False
        self.available_in_shop = True
        self.death_rattle_list = self.set_death_rattle_list()
        