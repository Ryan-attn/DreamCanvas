#!/usr/bin/env python3
from environments import NueveCuartosCiego, RoomLocation
from agents import BlindNineRoomAgent
from agent_core import ActionSpace, State

env = NueveCuartosCiego()
agent = BlindNineRoomAgent(ActionSpace.ALL_ACTIONS)

print(f'Agent name: {agent.name}')
print(f'Initial position: {env.robot_position}')
print(f'Room states: {env.room_states}')

for i in range(100):
    perception = env.perceive()
    print(f'\nStep {i}:')
    print(f'  Actual: {env.robot_position}, State robot: {env._state.robot_position}')
    print(f'  Model: {agent._model[0]}')
    print(f'  _just_cleaned: {agent._just_cleaned}')

    action = agent.select_action(perception)
    print(f'  Action: {action}')

    result = env.execute_action(action)
    print(f'  Success: {result.success}, New pos: {result.new_state.robot_position}')

    if result.new_state.robot_position not in [
        "F1C0", "F1C1", "F1C2",
        "F2C0", "F2C1", "F2C2",
        "F3C0", "F3C1", "F3C2"
    ]:
        print(f'  *** ERROR: Invalid position {result.new_state.robot_position}')
        break
