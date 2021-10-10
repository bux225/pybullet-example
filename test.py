# import pybullet as p
# import time
# import pybullet_data
# physicsClient = p.connect(p.GUI)#or p.DIRECT for non-graphical version
# p.setAdditionalSearchPath(pybullet_data.getDataPath()) #optionally
# p.setGravity(0,0,-10)
# planeId = p.loadURDF("plane.urdf")
# startPos = [0,0,1]
# startOrientation = p.getQuaternionFromEuler([0,0,0])
# boxId = p.loadURDF("r2d2.urdf",startPos, startOrientation)
# #set the center of mass frame (loadURDF sets base link frame) startPos/Ornp.resetBasePositionAndOrientation(boxId, startPos, startOrientation)
# for i in range (10000):
#     p.stepSimulation()
#     time.sleep(1./240.)
# cubePos, cubeOrn = p.getBasePositionAndOrientation(boxId)
# print(cubePos,cubeOrn)
# p.disconnect()

import gym
import pybullet_envs
import pybullet as p

import time

# p.GUI for graphical version similar to the MuJoCo one
# it will shut down on my pc though
p.connect(p.DIRECT)

# check the link below for some common environments
# https://github.com/bulletphysics/bullet3/releases
env = gym.make('AntBulletEnv-v0')

# it is different from how MuJoCo renders environments
# it doesn't differ too much to me w/ and w/o mode='human'
env.render()

# you should call render() before reset()
env.reset()

for _ in range(10000):
	# call sleep() so that it can render at a normal speed
	time.sleep(1./60.)
	action = env.action_space.sample()
	obs, reward, done, _ = env.step(action)
	if done:
		break