from typing import List


class PoligonalModel:
    def __init__(self) -> None:
        self.Poligons = []
        self.Textures = []

class Texture:
    pass

class Poligon:
    def __init__(self) -> None:
        self.Points = []
    
class Point3D:
    def __init__(self) -> None:
        self.Points = []

class Angle3D:
    def __init__(self) -> None:
        self.Angles = []

class Flash:
    def __init__(self) -> None:
        self.Location = []
        self.Angle = []
        self.Color = []
        self.Power = []

    def rotate(self, angle: List[Angle3D]) -> None:
        pass

    def move(self, point: List[Point3D]) -> None:
        pass

class Camera:
    def __init__(self) -> None:
        self.Location = []
        self.Angle = []

    def rotate(self, angle: List[Angle3D]) -> None:
        pass

    def move(self, point: List[Point3D]) -> None:
        pass

class Type:
    pass

class Scene:
    def __init__(self) -> None:
        self.id = []
        self.Models = []
        self.Flashes = []
    
    def method1(self, type: Type) -> Type:
        pass
            
    def notify_change(self, type1: Type, type2: Type) -> Type:
        pass
