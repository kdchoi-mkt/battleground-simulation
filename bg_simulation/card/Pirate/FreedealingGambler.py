from ..Card import Card

class FreedealingGambler(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = '이 하수인은 판매할 때의 가격이 3골드입니다.'
        self.type = 'Pirate'
        self.name = '선상 도박꾼'
        self.name_eng = 'Freedealing Gambler'
        self.attack = 3
        self.health = 3
        self.tier = 2
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
        