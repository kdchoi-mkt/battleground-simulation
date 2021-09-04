from ..Card import Card

class NosyLooter(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = '두 턴마다 무작위 황금 하수인을 내 손으로 가져옵니다.'
        self.type = 'Pirate'
        self.name = '참견쟁이 노략꾼'
        self.name_eng = 'Nosy Looter'
        self.attack = 7
        self.health = 6
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
        