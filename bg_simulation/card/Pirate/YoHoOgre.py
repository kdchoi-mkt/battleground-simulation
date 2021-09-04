from ..Card import Card

class YoHoOgre(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = '도발, 이 하수인은 공격을 받고 생존한 후에, 즉시 공격합니다.'
        self.type = 'Pirate'
        self.name = '요호우거'
        self.name_eng = 'Yo-Ho-Ogre'
        self.attack = 2
        self.health = 6
        self.tier = 2
        self.live = True
        self.taunt = True
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
        