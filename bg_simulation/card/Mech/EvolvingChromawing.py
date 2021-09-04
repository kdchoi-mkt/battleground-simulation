from ..Card import Card

class EvolvingChromawing(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = '내가 선술집을 강화한 후에, 이 하수인은 공격력이 2배가 됩니다.'
        self.type = 'Mech'
        self.name = '진화하는 오색날개 '
        self.name_eng = 'Evolving Chromawing '
        self.attack = 1
        self.health = 3
        self.tier = 1
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
        