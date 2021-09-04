from ..Card import Card

class SoulJuggler(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = '아군 악마가 죽은 후에, 무작위 적 하수인에게 피해를 3 줍니다.'
        self.type = 'Neutral'
        self.name = '영혼 곡예사'
        self.name_eng = 'Soul Juggler'
        self.attack = 3
        self.health = 5
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
        