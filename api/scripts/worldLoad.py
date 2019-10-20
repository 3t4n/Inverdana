from django.contrib.gis.utils import LayerMapping
from api.models import WorldBorder
from django.conf import settings
#BASE_DIR

world_mapping = {
    'fips' : 'FIPS',
    'iso2' : 'ISO2',
    'iso3' : 'ISO3',
    'un' : 'UN',
    'name' : 'NAME',
    'area' : 'AREA',
    'region' : 'REGION',
    'subregion' : 'SUBREGION',
    'mpoly' : 'MULTIPOLYGON',
}

world_shp = settings.BASE_DIR+"/data/TM_WORLD_BORDERS-0.3.shp"
#We need to tranform WGS84 to 3857
def run(verbose=True):
    lm = LayerMapping(WorldBorder.WorldBorder, world_shp, world_mapping, transform=True)
    lm.save(strict=True, verbose=True)
