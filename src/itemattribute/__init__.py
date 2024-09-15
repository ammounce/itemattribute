from .item_attribute import ItemAttribute
import json
import  os

dir = os.path.dirname(os.path.abspath(__file__))

with open(dir + '/version.json') as file:
    __version__ = json.load(file)
