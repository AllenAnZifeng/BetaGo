import gym

go_env = gym.make('gym_go:go-v0', size=7, komi=0, reward_method='real')

go_env.reset()

first_action = (2,5)
second_action = (5,2)
state, reward, done, info = go_env.step(first_action)
go_env.render('terminal')

state, reward, done, info = go_env.step(second_action)
go_env.render('terminal')
