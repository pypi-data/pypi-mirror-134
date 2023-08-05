from pydantic import BaseModel, Field
from typing import Optional, List
from decimal import Decimal
from datetime import datetime as dt


def camel_case(string: str) -> str:
    return ''.join(word.capitalize() if i > 0 else word for i, word in enumerate(string.split('_')))


class LayerModel(BaseModel):
    name: str
    title: str
    cmap: Optional[str]
    bands: Optional[dict]
    layer_permissions: Optional[set]
    background_layer: Optional[str]
    product_unit: Optional[str]

    class Config:
        alias_generator = camel_case


class Region(BaseModel):
    id: int
    name: str


class WqLayerModel(LayerModel):
    product: str
    client: str
    country: str
    temporal_resolution: str
    region: Region

    @property
    def name(self):
        return f"{self.client}_{self.country}_{self.region.name}_{self.product}"

    @property
    def s3_file_dir(self):
        return f"{self.client}/{self.country}/{self.region.name}/{self.product}/"


class StepModel(BaseModel):
    datetime: str
    resolution: int
    sensor: str
    temporal_resolution: str
    filename: str = None
    filedir: str = None
    cog_filepath: str = None

    class Config:
        alias_generator = camel_case


class LayerPermissionModel(BaseModel):
    layers: set


class ColorMap(BaseModel):
    name: str
    levels: List[Decimal]
    colors: List[List[Decimal]]
