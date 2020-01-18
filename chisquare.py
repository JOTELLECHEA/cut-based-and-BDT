mydict = {0: 'A',1: 'B',2: 'C',3: 'D',4: 'E',5: 'F'}

for i in xrange(0,6):
	for j in xrange(1,6):
		for k in xrange(2,6):
			for l in xrange(3,6):
				if i == j == k == l :continue
				if i > j > k > l :continue
				if j > k > l :continue
				if k > l :continue
				if i > j :continue
				if j > k  :continue
				if i == j == k :continue
				if i == j :continue
				if i == k :continue
				if i == l :continue
				if j == k == l:continue
				if j == k :continue
				if j == l :continue
				if k == l :continue
				print mydict[i],mydict[j],mydict[k],mydict[l]