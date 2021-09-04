from ..Card import Card

class ChampionofYShaarj(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = '아군 도발 하수인이 공격당할 때마다 영구히 +1/+1을 얻습니다.'
        self.type = 'Neutral'
        self.name = '이샤라즈의 용사'
        self.name_eng = 'Champion of Y’Shaarj'
        self.attack = 4
        self.health = 4
        self.tier = 4
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
        