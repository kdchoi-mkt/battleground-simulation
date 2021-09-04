from ..Card import Card

class RazorgoreTheUntamed(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = '내 턴이 끝날 때, 아군 용족 하나당 +1/+1을 얻습니다.'
        self.type = 'Dragon'
        self.name = '폭군 서슬송곳니'
        self.name_eng = 'Razorgore, the Untamed'
        self.attack = 4
        self.health = 6
        self.tier = 5
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
        