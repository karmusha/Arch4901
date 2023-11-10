from typing import List

from model_store import Flash, Camera, Scene, PoligonalModel

class IModelChangedObserver:
    def applyUpdateModel(self):
        pass

class IModelChanger:
    def notifyChange(self, sender):
        pass
    
class ModelStore(IModelChanger):
    def __init__(self, changeObserver: List[IModelChangedObserver]) -> None:
        # super().__init__()
        self.models = []
        self.scenes = []
        self.flashes = []
        self.cameras = []
        self.changeObservers = changeObserver

        textures = []
        self.models.append(PoligonalModel(textures))
        self.cameras.append(Camera())
        self.flashes.append(Flash())
        self.scenes.append(Scene(0, self.models, self.flashes, self.cameras))
    
    def get_scene(self, id):
        for scene in self.scenes:
            if scene.id == id:
                return scene
            
    def notify_change(self, sender: IModelChanger):
        pass