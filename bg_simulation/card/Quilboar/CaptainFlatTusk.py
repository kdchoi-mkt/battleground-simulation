from ..Card import Card


class CaptainFlatTusk(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = "내가 4골드를 소모한 후에, 혈석을 얻습니다."
        self.type = "Quilboar"
        self.name = "호위대장 납작엄니"
        self.name_eng = "Captain Flat Tusk"
        self.attack = 9
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
