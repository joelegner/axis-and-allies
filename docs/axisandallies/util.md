Module axisandallies.util
=========================

Functions
---------

    
`battle(attackers: axisandallies.forces.Forces, defenders: axisandallies.forces.Forces, is_sea_battle=False, runs: int = 1000, results=None)`
:   

    
`battle_from_yaml(filename: str) ‑> List[str]`
:   

    
`roll_dice(num, hit_score=1)`
:   

    
`wprint(txt: str, file: <class 'TextIO'> = None) ‑> NoneType`
:   Print a string wrapped to a file

Classes
-------

`BattleResults(attackers: axisandallies.forces.Forces, defenders: axisandallies.forces.Forces)`
:   

    ### Methods

    `attack_prob(self)`
    :

    `len_ratio(self)`
    :

    `set_wins_losses(self, attacker_wins: int, defender_wins: int) ‑> NoneType`
    :

    `strength_per_unit(self)`
    :   Return tuple of strength per unit (attacker, defender)

    `strength_ratio(self)`
    :