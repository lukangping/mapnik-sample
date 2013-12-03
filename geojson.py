import mapnik

stylesheet = 'geojson.xml'
image = 'geojson.png'
m = mapnik.Map(600, 300)
mapnik.load_map(m, stylesheet)
m.zoom_all() 
mapnik.render_to_file(m, image)
print "rendered image to '%s'" % image
