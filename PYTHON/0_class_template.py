#!/usr/bin/python3

import json

class Object:
	def __init__(self, attr: str) -> None:
		self._attr = attr
	
	@property
	def getter(self) -> str:
		return self._attr
	
	@getter.setter
	def setter(self, attr: str) -> None:
		self._attributes = attr

	def __str__(self) -> str:
		return f"These are the attributes {self._attr}"
	def __repr__(self) -> str:
		#return f"Object(atrr={self._attr})"
		return str(self.__dict__)
		#return self.toJSON()
	def toJSON(self) -> str:
		return json.dumps(self.__dict__, indent=4)

o = Object("Pedro")
o._attr = "Juan"
print(f"getting and setting: {o._attr}")
print("----------str")
print("usando metodo externo: " + str(o))
print("usando metodo interno: " + o.__str__())
print("----------repr")
print("usando metodo externo: " + repr(o))
print("usando metodo interno: " + o.__repr__())
print("json:\n" + o.toJSON())

