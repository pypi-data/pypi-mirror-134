from openautomatumdronedata.dataset import * 

dataset = droneDataset(os.path.abspath("datasets/hw-a9-stammhamm-015-39f0066a-28f0-4a68-b4e8-5d5024720c4e"))

time_vec = np.arange(0, dataset.dynWorld.maxTime, dataset.dynWorld.delta_t)
distance_vec = []
for time in time_vec:
    print("Analyzing objects for time %f" % time)
    obj_in_timestamp = dataset.dynWorld.get_list_of_dynamic_objects_for_specific_time(time)
    for dyn_obj in obj_in_timestamp:
        for other_dyn_obj in obj_in_timestamp:
            if(dyn_obj.UUID != other_dyn_obj.UUID):
                long, lat = dyn_obj.get_lat_and_long(time, other_dyn_obj)
                if(abs(long) < dyn_obj.length/2):
                    
                    passing_distance = lat - np.sign(lat) * dyn_obj.width/2 - np.sign(lat) * other_dyn_obj.width/2
                    distance_vec.append(abs(passing_distance))

print("Min lateral passing distance between two objects is  %f" % min(distance_vec))