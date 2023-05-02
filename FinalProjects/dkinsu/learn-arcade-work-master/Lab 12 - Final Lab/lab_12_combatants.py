
class PlayerClass:
    def __init__(self, player_description, class_name, class_hp, class_max_hp,
                 class_attack, mana, max_mana, p_skill1, p_skill2, p_range,
                 p_skill1_desc, p_skill2_desc, passive):
        self.player_description = player_description
        self.class_name = class_name
        self.class_hp = class_hp
        self.class_max_hp = class_max_hp
        self.class_attack = class_attack
        self.mana = mana
        self.max_mana = max_mana
        self.p_skill1 = p_skill1
        self.p_skill2 = p_skill2
        self.p_range = p_range
        self.p_skill1desc = p_skill1_desc
        self.p_skill2desc = p_skill2_desc
        self.passive = passive


class Enemy:
    def __init__(self, monster_description, monster_name, monster_hp,
                 m_skill1, m_skill1_dmg, m_skill2, m_skill2_dmg, m_taunt):
        self.monster_description = monster_description
        self.monster_name = monster_name
        self.monster_hp = monster_hp
        self.m_skill1 = m_skill1
        self.m_skill1_dmg = m_skill1_dmg
        self.m_skill2 = m_skill2
        self.m_skill2_dmg = m_skill2_dmg
        self.m_taunt = m_taunt
