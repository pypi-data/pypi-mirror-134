import os
import json
from sys import exec_prefix
import numpy as np

class dynamicWorld():
    """
        Represents all dynamic objects in a dataset

        :param path2JSON: Path to automatum data json file


        :var UUID:  Unique UUID of the dataset 
        :var frame_count:  Number of images/frames 
        :var fps:  Frame Rate 
        :var delta_t:  Time between two frames (1/fps) \[s\]
        :var environmental:  Additional environmental info, see dataset documentation for further information.
        :var utm_referene_point: Reference point in the world coordinate system in UTM-Format. This reference point is the center of the coordinate system for the given position. The points is given as a tuple of (x \[m\], y \[m\], letter, number)-
        :var dynamicObjects: List of dynamic object. Its recommended to use the included functions to access the dynamic objects. 
        :var maxTime:  Maximum time of the dataset \[s\]

    """
    def __init__(self, path2JSON):
        """
            Loads the dataset

            :param dataSetFolderPath: Path to a folder containing a valid automatum.data dataset.
        """        
        if(not os.path.isfile(path2JSON)):
            raise FileNotFoundError("The dynamic world json couldn't be found - Path: %s"%path2JSON)

        with open(path2JSON) as f:
            dynamicWorldData = json.load(f) 

        self.UUID = dynamicWorldData["UUID"]

        self.frame_count = dynamicWorldData["videoInfo"]["frame_count"]
        self.fps = dynamicWorldData["videoInfo"]["fps"]
        self.delta_t = 1/self.fps
        self.environmental = dynamicWorldData["EnvironmentInfo"]
        self.utm_referene_point = dynamicWorldData["UTM-ReferencePoint"]
        self.dynamicObjects =  dict()
        self.maxTime  = 0
        for dynObjData in dynamicWorldData["objects"]:
            dynObj = dynamicObject.dynamic_object_factory(dynObjData, self.delta_t)
            self.dynamicObjects[dynObjData["UUID"]] = dynObj
            self.maxTime = max(self.maxTime, dynObj.get_last_time())


    def get_length_of_dataset_in_seconds(self):
        """Returns the complete length of the dataset in seconds. 

        """
        return self.maxTime 

    def __len__(self):
        """
            Overwrite the length operator 
        """
        return len(self.dynamicObjects)

    def __str__(self):
        """
            Overwrite the string Method
        """
        dataSetString = "Dataset %s consits of the %d objects:\n"%(self.UUID, len(self))
        for dynObj in self.dynamicObjects.values():
            dataSetString += "'--> %s [%s] with %d entries from %0.2f s to %0.2f s\n"%(str(type(dynObj)), dynObj.UUID, len(dynObj), dynObj.get_first_time(), dynObj.get_last_time())

        return dataSetString

    def get_dynObj_by_UUID(self, UUID):
        """
            Returns the dynamic object with the given UUID string. 
            If no object is found, None is returned. 
        """
        if(UUID in self.dynamicObjects):
            return self.dynamicObjects[UUID]
        else:
            return None

    def get_list_of_dynamic_objects(self):
        """
            Returns the list of dynamic objects.
        """
        return list(self.dynamicObjects.values())

    def get_list_of_dynamic_objects_for_specific_time(self, time):
        """
            Returns the list of dynamic objects that are visitable at the given time.
        """
        objList = list()
        for obj in self.dynamicObjects.values():
            if(obj.is_visible_at(time)):
                objList.append(obj)
        return objList
               

class dynamicObject():
    """
        Base Class for all dynamic objects


        Per Object the following information are available as scalar:

        :var length:  Length of the object \[m\]
        :var width:  Width of the object \[m\]
        :var UUID:  Unique UUID of the object 
        :var delta_t:  Time difference between two data points (equal at all objects and with the ```dynamicObject```)

        Per object the following information are available as vector over time: 

        :var x_vec:  X-Position of the assumed center of gravity of the object in the local coordinate system
        :var y_vec:  Y-Position of the assumed center of gravity of the object in the local coordinate system
        :var vx_vec:  Velocity in X-direction of the local coordinate system 
        :var vy_vec:  Velocity in Y-direction of the local coordinate system 
        :var ax_vec:  Acceleration of the object in X-direction **in the vehicle coordinate system**
        :var ay_vec:  Acceleration of the object in Y-direction **in the vehicle coordinate system**
        :var time:  Vector of the timestamp in the dataset recording for the mention values. 

    """
    def __init__(self, movement_dynamic, delta_t):
        self.x_vec = movement_dynamic["x_vec"]
        self.y_vec = movement_dynamic["y_vec"]
        self.vx_vec = movement_dynamic["vx_vec"]
        self.vy_vec = movement_dynamic["vy_vec"]
        self.psi_vec = movement_dynamic["psi_vec"]
        self.ax_vec = movement_dynamic["ax_vec"]
        self.ay_vec = movement_dynamic["ay_vec"]
        self.length = movement_dynamic["length"]
        self.width = movement_dynamic["width"]
        self.time = movement_dynamic["time"]
        self.UUID = movement_dynamic["UUID"]
        self.delta_t = delta_t

        # On demand values_
        self.lane_id = None 
        self.object_relation_dict_list = None

    def __eq__(self, other):
        """Overwrite compare operator

        :param other: Other dynamic world object
        """
        self.UUID == other.UUID
        
    def __len__(self):
        """
            Overwrite the length operator 
        """
        return len(self.x_vec)

    def get_first_time(self):
        """
            Returns the time the object occurs the first time
        """
        return self.time[0]

    def get_last_time(self):
        """
            Returns the time the object occurs the last time
        """
        return self.time[-1]

    def is_visible_at(self, time):
        """
            Checks if the object is visible at the given time
        """
        return (time > self.get_first_time() - self.delta_t/2 and time < self.get_last_time() + self.delta_t/2)

    def next_index_of_specific_time(self, time):
        """
            Returns the index that is next to the given time. 
            If the object is not visible in that time step. 
            The function returns None.
        """
        if(not self.is_visible_at(time)):
            return None
        return max(0,min(len(self),round((time - self.get_first_time())/self.delta_t)))

    def get_object_relation_for_defined_time(self, time):
        """Returns object relation for a given time stamp. 
        Returns None if object relation are not calculated or object not in that time

        :param time: Evaluted Time

        """
        if(self.object_relation_dict_list is not None):
            idx = self.next_index_of_specific_time(time)
            if(idx is not None):
                return self.object_relation_dict_list[idx]
        return None


    def get_object_position_for_defined_time(self, time):
        """Returns object position for a given time stamp. 
        Returns None if object relation are not calculated or object not in that time

        :param time: Evaluted Time

        """
        if(self.object_relation_dict_list is not None):
            idx = self.next_index_of_specific_time(time)
            if(idx is not None):
                return self.x_vec[idx], self.y_vec[idx]
        return None


    def calculate_object_relations(self, surrounding_object_list, time):
        """Calculations the relations between objects

        :param surrounding_object_list: List of surrounding objects. (included the called one)
        :param time: Time
        :raises Exception: If the object releations are not calculated step by step
        """

        uuid_obj_in_front_ego = None
        uuid_obj_in_behind_ego = None
        uuid_obj_in_front_left = None
        uuid_obj_in_behind_left = None
        uuid_obj_in_front_right = None
        uuid_obj_in_behind_right = None
        ego_idx = self.next_index_of_specific_time(time)
        ego_lane_id = self.lane_id[ego_idx]
        obj_on_ego_lane = filter(lambda obj: obj.lane_id[obj.next_index_of_specific_time(time)] == ego_lane_id and obj.UUID != self.UUID, surrounding_object_list)
        obj_on_right_lane = filter(lambda obj: obj.lane_id[obj.next_index_of_specific_time(time)] == ego_lane_id + (1 * np.sign(ego_lane_id)), surrounding_object_list)
        obj_on_left_lane = filter(lambda obj: obj.lane_id[obj.next_index_of_specific_time(time)] == ego_lane_id + (-1 * np.sign(ego_lane_id)), surrounding_object_list)

        x_vec_ego = dict()
        for obj in obj_on_ego_lane:
            x, y = obj.rotate_and_translate_position(-self.x_vec[ego_idx], -self.y_vec[ego_idx], -self.psi_vec[ego_idx], time)
            x_vec_ego[obj.UUID] = x
        x_vec_ego_pos = {k:v for k,v in x_vec_ego.items() if v > 0}
        x_vec_ego_neg = {k:v for k,v in x_vec_ego.items() if v < 0}


        if(len(x_vec_ego_pos) > 0):
            uuid_obj_in_front_ego = min(x_vec_ego_pos, key=x_vec_ego_pos.get)
        if(len(x_vec_ego_neg) > 0):
            uuid_obj_in_behind_ego = max(x_vec_ego_neg, key=x_vec_ego_neg.get)


        x_vec_right = dict()
        for obj in obj_on_right_lane:
            x, y = obj.rotate_and_translate_position(-self.x_vec[ego_idx], -self.y_vec[ego_idx], -self.psi_vec[ego_idx], time)
            x_vec_right[obj.UUID] = x
        x_vec_right_pos = {k:v for k,v in x_vec_right.items() if v > 0}
        x_vec_right_neg = {k:v for k,v in x_vec_right.items() if v < 0}

        if(len(x_vec_right_pos) > 0):
            uuid_obj_in_front_right = min(x_vec_right_pos, key=x_vec_right_pos.get)
        if(len(x_vec_right_neg) > 0):
            uuid_obj_in_behind_right = max(x_vec_right_neg, key=x_vec_right_neg.get)


        x_vec_left = dict()
        for obj in obj_on_left_lane:
            x, y = obj.rotate_and_translate_position(-self.x_vec[ego_idx], -self.y_vec[ego_idx], -self.psi_vec[ego_idx], time)
            x_vec_left[obj.UUID] = x
        x_vec_left_pos = {k:v for k,v in x_vec_left.items() if v > 0}
        x_vec_left_neg = {k:v for k,v in x_vec_left.items() if v < 0}

        if(len(x_vec_left_pos) > 0):
            uuid_obj_in_front_left = min(x_vec_left_pos, key=x_vec_left_pos.get)
        if(len(x_vec_left_neg) > 0):
            uuid_obj_in_behind_left = max(x_vec_left_neg, key=x_vec_left_neg.get)

        if(self.object_relation_dict_list is None):
            self.object_relation_dict_list = list()

        if(ego_idx == len(self.object_relation_dict_list)):
            self.object_relation_dict_list.append({
                "front_ego":uuid_obj_in_front_ego,
                "behind_ego":uuid_obj_in_behind_ego,
                "front_left":uuid_obj_in_front_left,
                "behind_left":uuid_obj_in_behind_left,
                "front_right":uuid_obj_in_front_right,
                "behind_right":uuid_obj_in_behind_right
            })

        else:
            raise Exception("calculate_object_relations have to be called timestep after timestep")
        
    @staticmethod
    def dynamic_object_factory(obj_data_dict, delta_t):
        """
            Object factory to decode the objects that are 
            specified in the json right into the corresponding objects.
        """
        obj_factory_dict = {
            "car":carObject,
            "van":carObject,
            "truck":truckObject,
            "carWithTrailer":carWithTrailerObject,
            "motorcycle":motorcycleObject
        }
        return obj_factory_dict[obj_data_dict["objType"]](obj_data_dict, delta_t)


    def rotate_and_translate_position(self, dx, dy, dps, time):
        """Returns the position after rotation with dpsi and translation with dx and dy.
        """
        idx = self.next_index_of_specific_time(time)
        c, s = np.cos(dps), np.sin(dps)
        R = np.array(((c, -s), (s, c)))

        pos = np.matmul(R, np.array([self.x_vec[idx] + dx, self.y_vec[idx] + dy]))
        return pos[0], pos[1]


    def get_lat_and_long(self, time, other):
        """Returns the lateral and longitudinal distance from the current object to the given object.

        :param time: Time of evaluation
        :param other: Other dynamic object.

        :return: Longitudinal Distance 
        :return: Lateral Distance 

        """
        if(not self.is_visible_at(time)):
            raise Exception("The object %s is not visible at time %f. Therefore, the lateral and longitudinal distance to %s, can not be calculated." % (self.UUID, time, other.UUID))
        if(not other.is_visible_at(time)):
            raise Exception("The object %s is not visible at time %f. Therefore, the lateral and longitudinal distance to %s, can not be calculated." % (other.UUID, time, self.UUID))
            
        idx = self.next_index_of_specific_time(time)

        return other.rotate_and_translate_position(-self.x_vec[idx], -self.y_vec[idx],
                                                   -self.psi_vec[idx], time)

class carObject(dynamicObject):
    """
        Class for representing a car object. 
        Inheritances from dynamicObject which currently provides the main functionality. 
    """
    
    def __init__(self, movement_dynamic, delta_t):
        dynamicObject.__init__(self, movement_dynamic, delta_t)
        

class truckObject(dynamicObject):
    """
        Class for representing a track object. 
        Inheritances from dynamicObject which currently provides the main functionality. 
    """
    def __init__(self, movement_dynamic, delta_t):
        dynamicObject.__init__(self, movement_dynamic, delta_t)
        

class carWithTrailerObject(dynamicObject):
    """
        Class for representing a trailer object. 
        Inheritances from dynamicObject which currently provides the main functionality. 
    """
    def __init__(self, movement_dynamic, delta_t):
        dynamicObject.__init__(self, movement_dynamic, delta_t)
        

class motorcycleObject(dynamicObject):
    """
        Class for representing a trailer object. 
        Inheritances from dynamicObject which currently provides the main functionality. 
    """
    def __init__(self, movement_dynamic, delta_t):
        dynamicObject.__init__(self, movement_dynamic, delta_t)



            