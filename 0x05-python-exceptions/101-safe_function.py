#!/usr/bin/python3
def safe_function(fct, *args):
	try:
		f = fct(*args)
		return f
	except Exception as err:
		print(f"Exception: {err}")
		return None
