for a in range(47):
	for b in range(47):
		for c in range(47):
			s = '0' + a*'1' + b*'2' + c*'3'
			while ('01' in s) or ('02' in s) or ('03' in s):
				s = s.replace('01', '30', 1)
				s = s.replace('02', '3103', 1)
				s = s.replace('03', '1201', 1)
			if s.count('1') == 31 and s.count('2') == 24 and s.count('3') == 46 :
				print(c)
				print(s.count('0'))



                