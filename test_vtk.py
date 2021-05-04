# simple test of vtk tool
# requires files/dump.damp.*
# creates tmp*.vtk

d = dump("post/dump*.damper")
v = vtk(d)
v.one()
v.many()
#v.single(0,"tmp.single")

print "all done ... type CTRL-D to exit Pizza.py"
