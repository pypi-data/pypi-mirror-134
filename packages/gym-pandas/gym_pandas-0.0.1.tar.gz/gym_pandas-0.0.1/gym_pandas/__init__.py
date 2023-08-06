from gym.envs.registration import register

register(
    id='pandas-v0',
    entry_point='gym_pandas.envs:PandasEnv'
)