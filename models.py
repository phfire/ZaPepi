from geojson import Feature

class MapPoly():
    pixel_feature: list[list[float]] = None

    def __init__(self, feature: Feature, id_color: int, id_background: int, id_pattern: int) -> None:
        self.feature = feature
        self.id_color = id_color
        self.id_background = id_background
        self.id_pattern = id_pattern