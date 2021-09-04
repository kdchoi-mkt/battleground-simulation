from ..Card import Card

class BristlebackBrute(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = '내 턴마다 이 하수인에게 처음 내는 혈석은 추가로 +2/+2을 부여합니다.'
        self.type = 'Quilboar'
        self.name = '뾰족털 투사'
        self.name_eng = ' Bristleback Brute'
        self.attack = 3
        self.health = 3
        self.tier = 3
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
        