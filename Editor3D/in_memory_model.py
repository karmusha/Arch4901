from typing import List


class IModelChangedObserver:
    def applyUpdateModel(self):
        pass

class IModelChanger:
    def notifyChange(self, sender: IModelChanger):
        pass
    
class ModelStore(IModelChanger):
    def __init__(self, changeObserver: List[IModelChangedObserver]) -> None:
        # super().__init__()
        self.Models = []
        self.Scenes = []
        self.Flashes = []
        self.Cameras = []
        self.ChangeObservers = changeObserver
    
    def get_scene(self, id):
        for scene in self.Scenes:
            if scene.id == id:
                return scene
            
    def notify_change(self, sender: IModelChanger):
        pass