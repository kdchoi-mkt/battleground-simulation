from ..Card import Card

class GoldrinnTheGreatWolf(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = '죽음의 메아리: 내 야수들에게 +5/+5를 부여합니다.'
        self.type = 'Beast'
        self.name = '위대한 늑대 골드린'
        self.name_eng = 'Goldrinn, the Great Wolf'
        self.attack = 4
        self.health = 4
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
        self.death_rattle = True
        self.battle_cry = False
        self.available_in_shop = True
        self.death_rattle_list = self.set_death_rattle_list()
        