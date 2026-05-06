#!/usr/bin/env python3
import sys
sys.path.insert(0, '/Users/admin/Developer/1-Agentes-Inteligentes-master')

from agent_core import ActionSpace, State
from environments import DosCuartosStochastic

print("Creating DosCuartosStochastic...")
state = State(
    robot_position="A",
    room_states=("sucio", "sucio")
)
print(f"Before creating env: state.robot_position = {state.robot_position}")
print(f"Before creating env: state.room_states = {state.room_states}")

env = DosCuartosStochastic()
print(f"\nAfter creating env:")
print(f"env.state = {env.state}")
print(f"type(env.state) = {type(env.state)}")
print(f"env.state.robot_position = {env.state.robot_position}")
print(f"type(env.state.robot_position) = {type(env.state.robot_position)}")
print(f"env._state = {env._state}")
print(f"env._state.robot_position = {env._state.robot_position}")

print(f"\n_position_map = {env._position_map}")

# Try to access
try:
    idx = env._position_map[env._state.robot_position]
    print(f"Index: {idx}")
except Exception as e:
    print(f"Error accessing _position_map: {e}")
