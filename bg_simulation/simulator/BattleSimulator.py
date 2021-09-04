import random
import math


class BattleSimulator(object):
    def __init__(
        self,
        mine,
        opponent,
    ):
        self.players = [mine, opponent]
        self.turn = 0
        self.battle_log = str()
        self.simulation_json = dict()

    def derive_player_role(self):
        if self.players[0].get_live_card_num() > self.players[1].get_live_card_num():
            return 0, 1
        elif self.players[1].get_live_card_num() > self.players[0].get_live_card_num():
            return 1, 0
        else:
            rand_index = random.randint(0, 1)
            return rand_index, 1 - rand_index

    def simulation(self):
        attacker_index, shielder_index = self.derive_player_role()
        first_player = "User" if attacker_index == 0 else "Opponent"
        previous_attacked = [-1, -1]
        battle_log = str()

        self.players[attacker_index].trigger_start_of_combat(
            self.players[shielder_index]
        )
        self.players[shielder_index].trigger_start_of_combat(
            self.players[attacker_index]
        )

        while math.prod([player.get_live_card_num() for player in self.players]) > 0:
            attack_player, shield_player = (
                self.players[attacker_index],
                self.players[shielder_index],
            )
            (
                attack_card,
                previous_attacked[attacker_index],
            ) = self.select_attackable_minion(
                attack_player,
                previous_attacked[attacker_index],
            )
            target_card = self.possible_target_to_attack(shield_player)
            attack_card.battle(target_card, attack_player, shield_player)

            battle_log += self.write_battle_log(
                attack_player, shield_player, attack_card, target_card
            )

            attacker_index, shielder_index = shielder_index, attacker_index
            self.turn += 1

        result, damage = self.judge_who_win(self.players)

        self.simulation_json = self.construct_json(
            FirstPlayer=first_player,
            Result=result,
            Damage=damage,
            BattleLog=battle_log,
            UserCard=self.players[0].get_card_list(),
            OpponentCard=self.players[1].get_card_list(),
            Turn=self.turn,
        )
        return self.get_result()

    def possible_target_to_attack(
        self,
        shield_player,
    ):
        """도발 하수인이 있다면 도발 하수인을 우선적으로 공격함"""
        if shield_player.get_taunt_live_card_num() > 0:
            shield_minion = shield_player.get_live_taunt_card_list()
        else:
            shield_minion = shield_player.get_live_card_list()
        return random.choice(shield_minion)

    def select_attackable_minion(
        self,
        attack_player,
        previous_index: int,
    ):
        """공격권을 가지는 하수인 선택하기
        Attack[attack_person]은 공격을 할 수 있는 하수인을 의미
        이전에 공격한 하수인은 다시 공격할 수 없으며
        이번턴 공격 이후 새로 오른쪽에 생긴 하수인은 바로 공격권을 가짐"""
        attackable_index = self._update_minion_index(attack_player, previous_index)
        attacker_card_list = attack_player.get_card_list()

        while attacker_card_list[attackable_index].is_live() == False:
            attackable_index = self._update_minion_index(
                attack_player, attackable_index
            )

        return attacker_card_list[attackable_index], attackable_index

    def judge_who_win(
        self,
        players,
    ):
        if players[0].get_live_card_num() > 0:
            return "Win", players[0].attack()
        elif players[1].get_live_card_num() > 0:
            return "Lose", players[1].attack()
        else:
            return "Tie", 0

    def write_battle_log(
        self,
        attack_player,
        shield_player,
        attack_card,
        target_card,
    ):
        battle_log = str()
        battle_log += f"Attacking Card: {attack_card.get_name()}\n"
        battle_log += f"Targeted Card: {target_card.get_name()}\n"
        battle_log += f"After Attacked (Attack): {attack_player.show_live_cards()}\n"
        battle_log += f"After Attacked (Targeted): {shield_player.show_live_cards()}\n"
        return battle_log

    def _update_minion_index(
        self,
        player,
        index: int,
    ):
        index += 1
        card_num = player.get_card_num()

        if index >= card_num:
            index %= card_num
        return index

    def construct_json(self, **kwarg):
        return kwarg

    def get_result(self):
        return self.simulation_json
