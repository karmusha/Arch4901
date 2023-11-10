from typing import List

from Editor3D.service import Angle3D, Point3D

class Type:
    pass

class Scene:
    def __init__(self, identificator, models, flashes, cameras) -> None:
        self.identificator = identificator
        if len(models) > 0:
            self.models = models
        else:
            raise Exception('Должна быть одна модель')
        self.flashes = flashes
        if len(cameras) > 0:
            self.cameras = cameras
        else:
            raise Exception('Должна быть одна камера')
        
    def method1(self, type: Type) -> Type:
        return None
            
    def notify_change(self, type1: Type, type2: Type) -> Type:
        return None

class Texture:
    pass

class Poligon:
    def __init__(self, point) -> None:
        self.points = [point]

class PoligonalModel:
    def __init__(self, textures) -> None:
        self.poligons = []
        self.textures = textures
        self.poligons.append(Poligon(Point3D()))

class Flash:
    def __init__(self) -> None:
        self.location = None
        self.angle = None
        self.color = None
        self.power = None

    def rotate(self, angleAction: Angle3D) -> None:
        pass

    def move(self, pointAction: Point3D) -> None:
        pass

class Camera:
    def __init__(self) -> None:
        self.location = None
        self.angle = None

    def rotate(self, angleAction: Angle3D) -> None:
        pass

    def move(self, pointAction: Point3D) -> None:
        pass
