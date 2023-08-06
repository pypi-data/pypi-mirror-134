from openautomatumdronedata.dataset import droneDataset
import os
import numpy as np

dataset = droneDataset(os.path.abspath("datasets/hw-a9-stammhamm-015-39f0066a-28f0-4a68-b4e8-5d5024720c4e"))

for dynObj in dataset.dynWorld.get_list_of_dynamic_objects():
    vx_vec = np.asarray(dynObj.vx_vec)
    vy_vec = np.asarray(dynObj.vy_vec)
    mean_v = 3.6*np.mean(np.sqrt(vx_vec*vx_vec + vy_vec*vy_vec)) # Calculate the velocity in km/h
    print("%s %s drives with %.2f km/h"%(dynObj.__class__.__name__, dynObj.UUID, mean_v))
