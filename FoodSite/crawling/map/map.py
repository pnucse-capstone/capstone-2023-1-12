from pyproj import Transformer

proj = Transformer.from_crs('epsg:2097', 'epsg:4326')

dot = (389840.487043521, 194422.456329212)
# dot = (389969.699906310, 194245.391458314)

dot2 = proj.transform(*(dot[::-1]))
print(dot2)
