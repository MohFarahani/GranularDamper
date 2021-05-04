# simple test of log tool
# requires log.liggghts
# creates tmp.log and tmp.log.two

lg = log("log.liggghts")

print "# of vectors =",lg.nvec
print "length of vectors =",lg.nlen
print "names of vectors =",lg.names

time,KE = lg.get("Step","KinEng")
print KE
lg.write("KE.log")
lg.write("KE.log.two","Step","KinEng")

print "all done ... type CTRL-D to exit Pizza.py"
