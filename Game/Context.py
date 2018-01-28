
class Context:
    def __init__(self, camera_x=6, camera_y=87):

        self._tileSize = 64
        self._cameraPosition = (camera_x, camera_y)

    def getCameraPosition(self):
        return self._cameraPosition

    def getCameraRenderPosition(self):
        camera_x, camera_y = self._cameraPosition
        return camera_x * -64, camera_y * -64

    def getTileSize(self):
        return self._tileSize

    def setCameraPosition(self, position):
        self._cameraPosition = position




