import numpy as np
from homework1 import Hw1Env
import matplotlib.pyplot as plt

env = Hw1Env(render_mode="gui")
positions = []
for _ in range(5):
    env.reset()
    action_id = np.random.randint(4)
    # inputs
    _, img_before = env.state()
    env.step(action_id)
    #print(action_id)
    # output
    pos_after, img_after = env.state()

    # control
    """   print(pos_after)
        plt.imshow(img_before.reshape(128, 128, 3))
        plt.show()
        plt.imshow(img_after.reshape(128, 128, 3))
        plt.show()"""
    
    positions.append(pos_after)
    env.reset()

print(positions)
