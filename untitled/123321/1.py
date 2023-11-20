love = '\n'.join([''.join([('love'[(x-y) % len('Love')] if ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3 <= 0 else ' ') for x in
 range(-30, 30)]) for y in range(30, -30, -1)])
print("\033[5;31;40m%s\033[0m" % love)