from ..Card import Card

class Bigfernal(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = '내가 악마를 소환한 후에, 영구히 +1/+1을 얻습니다.'
        self.type = 'Demon'
        self.name = '거대불악마'
        self.name_eng = 'Bigfernal'
        self.attack = 6
        self.health = 6
        self.tier = 4
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
        