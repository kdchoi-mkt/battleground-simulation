from ..Card import Card


class DeflectoBot(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = '천상의 보호막, 전투 중에 내가 기계를 소환할 때마다 공격력 +2와 천상의 보호막을 얻습니다.'
        self.type = 'Mech'
        self.name = '반사로봇'
        self.name_eng = 'Deflect-o-Bot'
        self.attack = 3
        self.health = 2
        self.tier = 3
        self.live = True
        self.taunt = False
        self.divine_shield = True
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

    def when_summon(self, mine, targeted):
        if targeted.get_type() == 'Mech' or targeted.get_type() == 'All':
            self.divine_shield = True
            self.gain_attack(2)
