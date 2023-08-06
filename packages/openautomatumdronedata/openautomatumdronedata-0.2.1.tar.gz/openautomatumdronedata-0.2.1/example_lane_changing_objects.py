from openautomatumdronedata.dataset import * 

dataset = droneDataset(os.path.abspath("datasets/hw-a9-stammhamm-015-39f0066a-28f0-4a68-b4e8-5d5024720c4e"))

dataset.calculate_on_demand_values_for_all_objects() # Calculates the values which are not included in the dataset

list_of_objects_which_performs_a_lane_change = list()
for dynObj in dataset.dynWorld.get_list_of_dynamic_objects():
    if(min(dynObj.lane_id) != max(dynObj.lane_id)):
        print("Object found with UUID %s to type %s"%(dynObj.UUID, str(type(dynObj))))
        list_of_objects_which_performs_a_lane_change.append(dynObj)


time_vec = np.arange(0, dataset.dynWorld.maxTime, dataset.dynWorld.delta_t)
distance_vec = []
for time in time_vec:
    print("Analyzing lane change object for time %f" % time)
    obj_in_timestamp = dataset.dynWorld.get_list_of_dynamic_objects_for_specific_time(time)
    for dyn_obj in obj_in_timestamp:
        if(dyn_obj in list_of_objects_which_performs_a_lane_change):
            object_relation = dyn_obj.get_object_relation_for_defined_time(time)
            obj_uuid_front_ego_line = object_relation["front_ego"]
            if(obj_uuid_front_ego_line is not None):
                obj_front_ego_line = dataset.dynWorld.get_dynObj_by_UUID(obj_uuid_front_ego_line)
                x_front, y_front = obj_front_ego_line.get_object_position_for_defined_time(time)
                x_ego, y_ego = dyn_obj.get_object_position_for_defined_time(time)
                dx = x_ego - x_front
                dy = y_ego - y_front
                distance = math.sqrt(dx*dx + dy*dy)
                distance_vec.append(distance)


print("Min distance to front object of all object performing a lane change is %f" % min(distance_vec))