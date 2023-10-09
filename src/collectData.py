import numpy as np
from homework1 import Hw1Env

# change to gui for visualization, offscreen for fast training
env = Hw1Env(render_mode="offscreen")

before = np.zeros((1000,3,128,128))
after = np.zeros((1000,3,128,128))
loc = np.zeros((1000,2))
actions = np.zeros((1000,1))


for i in range(1000):
    env.reset()
    action_id = np.random.randint(4)
    _, img_before = env.state()
    env.step(action_id)
    pos_after, img_after = env.state()
    before[i,:,:,:] = img_before
    after[i,:,:,:] = img_after
    loc[i,:] = pos_after
    actions[i,:] = action_id
    env.reset()
    print('step = ',i)

print('done')

np.save("data/before-image-1000.npy",before)
np.save("data/after-image-1000.npy",after)
np.save("data/after-object-location-1000.npy",loc)
np.save("data/actions-1000.npy",actions)
