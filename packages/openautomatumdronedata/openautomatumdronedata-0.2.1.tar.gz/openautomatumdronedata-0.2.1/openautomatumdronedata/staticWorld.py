import xml.etree.ElementTree as ET
import numpy as np
import copy
import math
import os



class xodrStaticWorld():
    """
        Representing the static world of dataset

        

        Notice: This implementation is only a very basic xodr-reader. 
        Its just handling the basic functionality needed for the current state of 
        automatum-data datasets.

        :param path2XODR: Path to a xodr file. 

        :var roads: A List of roads contained in the xodr. Roads are represtend by ``xodrRoad``.

    """

    def __init__(self, path2XODR):
        """
            Init function. 
        """
        self.roads = list()

        if(not os.path.isfile(path2XODR)):
            raise FileNotFoundError("The xodr-file could not be found under: %s"%path2XODR)
        tree = ET.parse(path2XODR)
        root = tree.getroot()
        for child in root:
            if "road" in child.tag:
                self.roads.append(xodrRoad(child))

    def calculate_point_to_lane_assignment(self, x, y):
        """Calculates the lane assignment of a given point.

        Therefore all roads are evaluated. 

        :param x: Position X of Point
        :param y: Position y of point
        :return: Lane ID of the Lane, in which the point is. (Notice: 0 means no lane could be assigned, e.g. if the point is outside of the road.)
        :return: Road ID in which the lane assignment is valid. (Notice: 0 means no assignment)
        """
        for road in self.roads:
            lane_id = road.calculate_point_to_lane_assignment(x, y)
            if(lane_id != 0):
                return lane_id, road.id
        return 0, 0

    def get_lane_marking_dicts(self, with_centerline = 0):
        """
        This functions returns all lane markings of the static world. 

        Therefore, a list of line samplings, e.g. for plotting is created.

        The format of the return type is:
        [{x_vec: [...], y_vec: [...], type: "borken", color: "white", width: 0.12}, 
        {x_vec: [...], y_vec: [...], type: "solid",  color: "white", width: 0.12},
        .
        .
        .
        {x_vec: [...], y_vec: [...], type: "solid",  color: "white", width: 0.12},
        ]
        
        Types:
        
        * solid: Solid lane marking
        * dashed: Dashed lane marking
        * center_line: Center line fo the corresponding road element

        with_centerline: controles if the center line is included in the list of lines, or if only real road markings are returned

        """
        allLineList = list()
        for road in self.roads:
            allLineList = allLineList + road.get_lane_marking_dicts()
        
        return allLineList

class xodrRoad():
    """
        This class represents a road.

        :param roadXML: XML-Tree of a road element
        :param sampleWidth: Sample width that is used to calculate a plotable representation of the xodr.

        :var name: Name of th road 
        :var length: Length of the road
        :var id: ID of Road (Currently unused, since automatum-data currently constit of one road)
        :var junction: Information about Junctions (Currently unused, since automatum-data currently constit of one road)
        :var geometry: Representation of reference line 
        :var lanesections: Object that represents all lanes 

    """

    def __init__(self, roadXML, sampleWidth = 1.0):
        """
            Inits a Road element and decodes the given roadxml tree. 
            Aditionally the sampling is triggered. 
        """


        self.name = roadXML.attrib['name']
        self.length = float(roadXML.attrib['length'])
        self.id = int(roadXML.attrib['id'])
        self.junction = int(roadXML.attrib['junction'])

        self.geometry = list()
        self.lanesections = list()
        

        for child in roadXML:
            if "planView" in child.tag:
                for geoChild in child:
                    if "geometry" in geoChild.tag:
                        self.geometry.append(xodrGeometry.create_geo_obj(geoChild))
                    else:
                        raise Exception("Unexpected XODR Format: Expected geometry, however given is %s"%geoChild.tag)

            if "lanes" in child.tag:
                for laneChild in child:
                    if "laneSection" in laneChild.tag:
                        self.lanesections.append(xodrLaneSection(laneChild))
                    elif "laneOffset" in laneChild.tag:
                        print("Not implemented yet.")
                    else:
                        raise Exception("Unexpected XODR Format: Expected geometry, however given is %s"%laneChild.tag)
        self.sample_me(sampleWidth)



    def get_lane_marking_dicts(self):
        """
        This functions returns all lane markings corresponding to this static world object.

        Therefore, a list of line samplings, e.g. for plotting is created.

        The format of the return type is:
        [{x_vec: [...], y_vec: [...], type: "borken", color: "white", width: 0.12}, 
        {x_vec: [...], y_vec: [...], type: "solid",  color: "white", width: 0.12},
        .
        .
        .
        {x_vec: [...], y_vec: [...], type: "solid",  color: "white", width: 0.12},
        ]

        Types:

        * solid: Solid lane marking
        * dashed: Dashed lane marking
        * center_line: Center line fo the corresponding road element
            
        """

        lineList = list()

        for geo in self.geometry:
            lineList += geo.get_lane_marking_dicts()
        for laneSec in self.lanesections:
            lineList += laneSec.get_lane_marking_dicts()

        return lineList

    def sample_me(self, sampleWidth):
        """ Calculates the sampled value (point vector) of this static world element. """

        for geo in self.geometry:
            geo.sample_me(sampleWidth)
            for laneSec in self.lanesections:
                laneSec.sample_me(geo)            

    def __str__(self):
        """ Overwrite to string method"""
        return "Road %s length %.2f, ID: %d, Junction: %d"%(self.name, self.length, self.id, self.junction)

    def calculate_point_to_lane_assignment(self, x, y):
        """Calculates the lane assignment of a given point.

        Therefore all roads are evaluated. 

        :param x: Position X of Point
        :param y: Position y of point
        :return: Lane ID of the Lane, in which the point is. (Notice: 0 means no lane could be assigned, e.g. if the point is outside of the road.)
        """
        d, l, idx = self.get_track_and_orthogonal_distance(x, y)
        if(idx is not None):
            lane_section = self.lanesections[idx]
            lane_id = lane_section.get_lane_id(d, l)
            if(lane_id != 0):
                return lane_id
        return 0



    def get_track_and_orthogonal_distance(self, x, y):
        """Calculates for a given point the orthogonal distance from the road center line and the distance along the road:


        :param x: Position X of Point
        :param y: Position y of point
        :return: Orthogonal distane to center line
        :return: Distance along the road
        :return: Idx of the geometry object where the point is assigned to
        """
        self.geometry.sort()
        for seg_idx, geo in enumerate(self.geometry):
            d, l = geo.get_track_and_orthogonal_distance(x, y)
            if(l < geo.length):
                return (d,l + geo.s, seg_idx)
        return 0,0,None


        

class xodrGeometry():
    """
        Main class for all further geometry objects. 

        Based on xodr specification the following forms are supported by the corresponding child classes: 

        * Straight Line by ``xodrGeometryLine``
        * Arc by ``xodrGeometryCurvature``
        * Spiral (not implemented)
        * Cubic polynom (not implemented)
        * Parametric cubic curve (not implemented)

        :param xmlGeometry: xmlTree of a geometry object

        :var s: Start distance of the Geometry 
        :var x: Coordinate system x-position
        :var y:  Coordinate system y-position
        :var hdg:  Coordinate system heading
        :var length: Relevant length of the geometry object
    """
    def __init__(self, xmlGeometry):
        """
            Init function that decodes the given xmlTree
            
            
        """
        self.s = float(xmlGeometry.attrib['s'])
        self.x = float(xmlGeometry.attrib['x'])
        self.y = float(xmlGeometry.attrib['y'])
        self.hdg = float(xmlGeometry.attrib['hdg'])
        self.length = float(xmlGeometry.attrib['length'])

        self.s_vec = None
        self.x_vec = None
        self.y_vec = None

    @staticmethod
    def create_geo_obj(xmlGeometry):
        """
            Object factory thats create the correct child class
        """
        if("line" in xmlGeometry[0].tag):
            return xodrGeometryLine(xmlGeometry)
        if("arc" in xmlGeometry[0].tag):
            return xodrGeometryCurvature(xmlGeometry)


    def sample_me(self, sampleWidth):
        """ Sample of geometry object have to be overwritten by the child class"""
        raise NotImplementedError("Have to be overwritten by child class")

    def get_track_and_orthogonal_distance(self, x, y):
        """Calculates the distance between Reference Line alias Geometry and a given point"""
        raise NotImplementedError("Have to be overwritten by child")
    def __lt__(self, other):
        """Overwrite left operator to enable a sorting based on start distance s
        """
        return self.s < other.s

class xodrGeometryCurvature(xodrGeometry):
    """ Geometry Class for a XODR Curvature

    Overwrites the base class ``xodrGeometry``

    :param xmlGeometry: xmlTree of a geometry object

    :var curvature: Curvature of the reference line
    """
    def __init__(self, xmlGeometry):
        """ Reads the Curvature relevant parameter and call the main class"""


        xodrGeometry.__init__(self, xmlGeometry) 
        self.curvature = float(xmlGeometry[0].attrib['curvature'])


    def get_track_and_orthogonal_distance(self, x, y):
        """Calculates the distance between Reference Line alias Geometry and a given point
        

        :param x: Position x of given Point
        :param y: Position y of given point
        
        """
        c, s = np.cos(-self.hdg), np.sin(-self.hdg)

        R = np.array(((c, -s), (s, c)))         
       
        p = np.array([x - self.x,y - self.y])
        sign_curvature = np.sign(self.curvature)
        p_normed = np.matmul(R, p)
        p_normed[1] = sign_curvature * p_normed[1]

        r = 1/abs(self.curvature)

        alpha = math.atan2(p_normed[0], r -p_normed[1])

        if(alpha < 0 or alpha > math.pi/2):
            return 0,0

        l = r * alpha

        c, s = np.cos(alpha), np.sin(alpha)


        p_a = np.matmul(np.array(((c, -s), (s, c))), np.array((0, -r))) + np.array((0, r))
        dx = p_a[0] - p_normed[0]
        dy = p_a[1] - p_normed[1]
        d = math.sqrt(dx**2 + dy**2)

        dx = 0 - p_normed[0]
        dy = r - p_normed[1]
        d_middle_point = math.sqrt(dx**2 + dy**2)
        if(d_middle_point < r):
            d = -1 * d

        return d, l

    def __str__(self):
        return "Curvature: curvature: %.2f, s: %.2f, x: %.2f, y: %.2f, hgd: %.2f, length %.2f"%(self.curvature, self.s, self.x, self.y, self.hdg, self.length)

    def sample_me(self, sampleWidth):  
        """ Samples this geometry object """
        self.s_vec = np.arange(self.s, self.s + self.length + sampleWidth, sampleWidth)
        d_psi = 0
        x_vec_local = [0]
        y_vec_local = [0]        
        for index, s_sample in enumerate(self.s_vec):
            d_psi += sampleWidth * self.curvature
        
            theta = (d_psi)
            c, s = np.cos(theta), np.sin(theta)
            R = np.array(((c, -s), (s, c)))

            lineVec = np.matmul(R, np.array([1,0]))
            lineVec = sampleWidth*lineVec/math.sqrt(lineVec[0]*lineVec[0] + lineVec[1] * lineVec[1])
            if(index > 0):
                x_vec_local.append(x_vec_local[-1] + lineVec[0])
                y_vec_local.append(y_vec_local[-1] + lineVec[1])


        theta = (self.hdg)
        c, s = np.cos(theta), np.sin(theta)
        R = np.array(((c, -s), (s, c)))

        self.x_vec = list()
        self.y_vec = list()

        for x_value, y_value in zip(x_vec_local, y_vec_local):
            global_point = np.matmul(R, np.array([x_value,y_value])) + np.array([self.x,self.y])

            self.x_vec.append(global_point[0])
            self.y_vec.append(global_point[1])

    def get_lane_marking_dicts(self):
        """ Returns the lane marking plotting vector for the center line"""
        if(self.s_vec is None):
            raise Exception("Please call sample_me before activating the plotting")

        return [{"x_vec": list(self.x_vec), "y_vec": list(self.y_vec), "type": "centerline",  "color": "white", "width": 0.12}]



class xodrGeometryLine(xodrGeometry):
    """ Geometry Class for a XODR Line
    
    Notice: No further variables than xodrGeometry
    """
    def __init__(self, xmlGeometry):
        """ Reads no additional and call the main class"""
        xodrGeometry.__init__(self, xmlGeometry) 

    def __str__(self):
        """ Overwrite str()"""
        return "Line: s: %.2f, x: %.2f, y: %.2f, hgd: %.2f, length %.2f"%(self.s, self.x, self.y, self.hdg, self.length)

    def sample_me(self, sampleWidth):
        """ Samples this geometry object """
        self.s_vec = np.arange(self.s, self.s + self.length + sampleWidth, sampleWidth)
        #self.s_vec = np.arange(0, self.length, sampleWidth)
        theta = (self.hdg)
        c, s = np.cos(theta), np.sin(theta)
        R = np.array(((c, -s), (s, c)))

        lineVec = np.matmul(R, np.array([1,0]))
        lineVec = lineVec/math.sqrt(lineVec[0]*lineVec[0] + lineVec[1] * lineVec[1])

        self.x_vec = list()
        self.y_vec = list()
        for s_sample in self.s_vec:
            scaledLineVec = lineVec * (s_sample - self.s)
            self.x_vec.append(self.x + scaledLineVec[0])
            self.y_vec.append(self.y + scaledLineVec[1])
        self.x_vec = np.asarray(self.x_vec)
        self.y_vec = np.asarray(self.y_vec)

        
    def get_lane_marking_dicts(self):
        """
        This functions returns all lane markings corresponding to this static world object.

        Therefore, a list of line samplings, e.g. for plotting is created.

        The format of the return type is:
        [{x_vec: [...], y_vec: [...], type: "borken", color: "white", width: 0.12}, 
        {x_vec: [...], y_vec: [...], type: "solid",  color: "white", width: 0.12},
        .
        .
        .
        {x_vec: [...], y_vec: [...], type: "solid",  color: "white", width: 0.12},
        ]

        Types:
        
        * solid: Solid lane marking
        * dashed: Dashed lane marking
        * center_line: Center line fo the corresponding road element
            
        """
        if(self.s_vec is None):
            raise Exception("Please call sample_me before activating the plotting")

        return [{"x_vec": list(self.x_vec), "y_vec": list(self.y_vec), "type": "centerline",  "color": "white", "width": 0.12}]

    def get_track_and_orthogonal_distance(self, x, y):
        """Calculates the distance between Reference Line alias Geometry and a given point
        

        :param x: Position x of given Point
        :param y: Position y of given point
        
        """
        c, s = np.cos(self.hdg), np.sin(self.hdg)

        R = np.array(((c, -s), (s, c)))         
        dir_vec = np.matmul(R, np.array([1,0]))
       
        p1=np.array([0,0])
        p2=np.array([0,0]) + dir_vec
        p3=np.array([x - self.x,y - self.y])
        d=np.cross(p2-p1,p3-p1)/np.linalg.norm(p2-p1)


        n = p2 - p1
        v = p3 - p1

        z = p1 + n*(np.dot(v, n)/np.dot(n, n))
        l = math.sqrt(z[0] * z[0] + z[1] * z[1])


        return d, l

 
class xodrLaneSection():
    """
        Defines a XODR laneSection thats holds a number of lanes. 

        :param xmlLaneSection: xmlTree of a lane section

        :var s: Length of this lane section element along the reference line
        :var lane: List of lane elements which belong to this lane section
    """
    def __init__(self, xmlLaneSection):
        """ Decodes the xmlTree of a LaneSection"""
        self.s = float(xmlLaneSection.attrib['s'])
        self.lanes = list()

        for child in xmlLaneSection:
            if("right" in child.tag or "left" in child.tag):
                for leftrightLanes in child:
                    if "lane" in leftrightLanes.tag:
                        self.lanes.append(xodrLane(leftrightLanes))
                    else:
                        raise Exception("Unexpected XODR Format: Expectation lane, given %s"%child.tag)

    def get_lane_id(self, d, l):
        """Returns the lane_id for a given point, defined by the distance l along the reference line 
        and the orthogonal distance from the reference line. 

        :param d: Orthogonal distance from reference line (signed according definition in xodr)
        :param l: Distance along the reference line

        :return: Id of the lane (0 if out of range)
        """

        posLines = list()
        negLines = list()

        for lane in self.lanes:
            if(lane.id < 0):
                negLines.append(lane)
            else:
                posLines.append(lane)

        negLines.sort()
        negLines.reverse()

        posLines.sort()
        
        if(d > 0):
            last_offset = 0
            for lane in posLines:
                lat_offset = lane.get_lateral_offset(l, offset_inner_lane=last_offset)
                last_offset = lat_offset
                if(lat_offset > d):
                    return lane.id

        if(d < 0):
            last_offset = 0
            for lane in negLines:
                lat_offset = lane.get_lateral_offset(l, offset_inner_lane=last_offset)
                last_offset = lat_offset
                if(lat_offset < d):
                    return lane.id
        return 0


    def __str__(self):
        """
            Overwrites str()
        """
        return "LaneSection: s: %.2f, x: %.2f, y: %.2f, hgd: %.2f, length %.2f"%(self.s, self.x, self.y, self.hdg, self.length)


    def get_lane_marking_dicts(self):
        """
        This functions returns all lane markings corresponding to this static world object.

        Therefore, a list of line samplings, e.g. for plotting is created.

        The format of the return type is:
        [{x_vec: [...], y_vec: [...], type: "borken", color: "white", width: 0.12}, 
        {x_vec: [...], y_vec: [...], type: "solid",  color: "white", width: 0.12},
        .
        .
        .
        {x_vec: [...], y_vec: [...], type: "solid",  color: "white", width: 0.12},
        ]

        Types:
        
        * solid: Solid lane marking
        * dashed: Dashed lane marking
        * center_line: Center line fo the corresponding road element
            
        """        
        lineList = list()
        for lane in self.lanes:   
            lineList += lane.get_lane_marking_dicts()
        return lineList

    def sample_me(self, geo):
        """ Samples this geometry object """        
        posLines = list()
        negLines = list()

        for lane in self.lanes:
            if(lane.id < 0):
                negLines.append(lane)
            else:
                posLines.append(lane)

        negLines.sort()
        negLines.reverse()

        posLines.sort()
        
        lastLane = None
        for lane in posLines:
            lane.sample_me(geo, innerLane = lastLane)
            lastLane = lane


        lastLane = None
        for lane in negLines:
            lane.sample_me(geo, innerLane = lastLane)
            lastLane = lane


class xodrLane():
    """
        Represents a XODR lane


        :param xmlLane: xmlTree of a lane

        :var id: ID of the Lane
        :var type: Type of the lane, e.g. drivable or shoulder
        :var width: Dict with all primate's of a third order polynom to define the width of the lane
        :var roadmark: Dict of further information of road marks (Not completely set in automatum data)
        :var material: Dict of further information of road material (Not set in automatum data)
        :var speed: Dict of further information of speed limits (Not set in automatum data)

    """
    def __init__(self, xmlLane):
        """Init function 

        :param xmlLane: xmlTree of a lane
        """
        self.id = int(xmlLane.attrib['id'])
        self.type = xmlLane.attrib['type']
        self.width = dict()
        self.roadmark = dict()
        self.material = dict()
        self.speed = dict()

        self.s_vec = list()
        self.x_vec = list()
        self.y_vec = list()
        self.lat_offVec = list()

        for laneChild in xmlLane:
            if(len(self.width) == 0 and "width" in laneChild.tag):
                self.width['sOffset'] = float(laneChild.attrib['sOffset'])
                self.width['a'] = float(laneChild.attrib['a'])
                self.width['b'] = float(laneChild.attrib['b'])
                self.width['c'] = float(laneChild.attrib['c'])
                self.width['d'] = float(laneChild.attrib['d'])
        
            if(len(self.roadmark) == 0 and "roadMark" in laneChild.tag):
                self.roadmark['sOffset'] = float(laneChild.attrib['sOffset'])
                self.roadmark['type'] = laneChild.attrib['type']
                self.roadmark['color'] = laneChild.attrib['color']
                self.roadmark['width'] = float(laneChild.attrib['width'])
                self.roadmark['height'] = float(laneChild.attrib['height'])
            else:
                self.roadmark['sOffset'] = 0
                self.roadmark['type'] = "unknown"
                self.roadmark['color'] = "unknown"
                self.roadmark['width'] = 0
                self.roadmark['height'] = 0               
            if(len(self.material) == 0 and "material" in laneChild.tag):        
                self.material['sOffset'] = float(laneChild.attrib['sOffset'])
                self.material['friction'] = laneChild.attrib['friction']

            if(len(self.speed) == 0 and "speed" in laneChild.tag):        
                self.speed['sOffset'] = float(laneChild.attrib['sOffset'])
                self.speed['max'] = float(laneChild.attrib['max'])
                self.speed['unit'] = laneChild.attrib['unit']

    def __lt__(self, other):
        """ Overwrite Compare operator to enable sorting of lines elements"""
        return self.id < other.id

    def get_lateral_offset(self, s, offset_inner_lane=0):
        """Returns the lateral offset for a given distance s along the lane

        :param s: Distance along the lane
        :param offset_inner_lane: Since the distance is given from the last lane and not from the reference line. This variables allows to give an constant offset on the lateral distance, defaults to 0

        :return: Lateral offset of lane 

        """
        return (np.sign(self.id) * (self.width['a'] + self.width['b'] * s + self.width['c'] * s * s + self.width['d'] * s * s  * s)) + offset_inner_lane

    def sample_me(self, geo, innerLane = None):
        """ Samples this geometry object """  
        s_vec = copy.copy(geo.s_vec)
        lat_offVec = list()
        x_vec = list()
        y_vec = list()
        for index, s_sample in enumerate(s_vec):
            ds = s_sample - s_vec[0]
            sampleLatOffset =  self.width['a']# + self.width['b'] * ds + self.width['c'] * ds * ds + self.width['d'] * ds * ds  * ds 
            if(not innerLane is None):
                sampleLatOffset += innerLane.lat_offVec[index]

            lat_offVec.append(sampleLatOffset)

            if(index == 0):
                dx = geo.x_vec[index] - geo.x_vec[index + 1]
                dy = geo.y_vec[index] - geo.y_vec[index + 1]
                segmentAngle = math.atan2(dy, dx)                
            else:
                dx = geo.x_vec[index - 1] - geo.x_vec[index]
                dy = geo.y_vec[index - 1] - geo.y_vec[index]
                segmentAngle = math.atan2(dy, dx)

            if self.id > 0:
                theta = (segmentAngle - np.pi/2)
            else:
                theta = (segmentAngle + np.pi/2)

            c, s = np.cos(theta), np.sin(theta)
            R = np.array(((c, -s), (s, c)))

            lineVec = np.matmul(R, np.array([1,0])) * sampleLatOffset

            x_vec.append(geo.x_vec[index] + lineVec[0])
            y_vec.append(geo.y_vec[index] + lineVec[1])

        self.s_vec += list(s_vec)
        self.x_vec += list(x_vec)
        self.y_vec += list(y_vec)
        self.lat_offVec += list(lat_offVec)
        

    def get_lane_marking_dicts(self):
        """
        This functions returns all lane markings corresponding to this static world object.

        Therefore, a list of line samplings, e.g. for plotting is created.

        The format of the return type is:
        [{x_vec: [...], y_vec: [...], type: "borken", color: "white", width: 0.12}, 
        {x_vec: [...], y_vec: [...], type: "solid",  color: "white", width: 0.12},
        .
        .
        .
        {x_vec: [...], y_vec: [...], type: "solid",  color: "white", width: 0.12},
        ]

        Types:
        
        * solid: Solid lane marking
        * dashed: Dashed lane marking
        * center_line: Center line fo the corresponding road element
            
        """              
        if(self.s_vec is None):
            raise Exception("Please call sample_me before activating the plotting")

        return [{"x_vec": self.x_vec, "y_vec": self.y_vec, "type": self.roadmark['type'],  "color": self.roadmark['color'], "width": self.roadmark['width']}]