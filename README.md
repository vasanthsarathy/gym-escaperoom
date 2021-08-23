# Escape Room Puzzles Environment (EscapeRoom)

This is a gridworld environment that extends [MiniGrid](https://github.com/maximecb/gym-minigrid) for escape-room type puzzles. Will integrate VGDL to allow users to specify levels and use it to procedurally generate levels. 


## Installation

You can clone this repo and install the dependencies with `pip`

```
conda create -n escaperoomenv python=3.8
conda activate escaperoomenv

git clone https://github.com/vasanthsarathy/gym-escaperoom.git
cd gym-escaperoom
pip install -e .
```

## Basic Usage

Can quickly check if things work by trying to render the environment inside of
a python shell

```
conda activate escaperoomenv
python
>>> import gym
>>> env = gym.make('gym_escaperoom:MiniGrid-SpotterLevel2-v0')
>>> env.render()
```

UI package from `gym-minigrid`

`./manual_control.py`

You can also choose the spotter environments with the `--env` option:

`./manual_control.py --env gym_escaperoom:MiniGrid-SpotterLevel2-v0`



