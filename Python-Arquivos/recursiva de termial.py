>>> def tr(n):
	if n == 0: return 0
	return tr(n - 1) + n

>>> tr(2)
3
>>> tr(50)
1275
>>> 