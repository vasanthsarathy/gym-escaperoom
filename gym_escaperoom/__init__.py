
from gym_minigrid.register import register

register(
    id='MiniGrid-UnblockedGoal-v0',
    entry_point='gym_escaperoom.envs:UnblockedGoal'
)

register(
    id='MiniGrid-SpotterLevel1-v0',
    entry_point='gym_escaperoom.envs:SpotterLevel1'
)

register(
    id='MiniGrid-SpotterLevel2-v0',
    entry_point='gym_escaperoom.envs:SpotterLevel2'
)

register(
    id='MiniGrid-SpotterLevel3-v0',
    entry_point='gym_escaperoom.envs:SpotterLevel3'
)
