from collections import UserDict, UserString
from datetime import date

from numpy import double

from ProyectoPOO.Clases.Administrador import Administrador


class User():
  userid:str
  pasword: str
  registerDate:date
  name:str
  adress: str

class customer(User):
    customerld:str
    acountBalance:float


class order():
    orderld:str
    customerName:str
    date:date
    def __init__(self,custo):
        customer=custo


class orderDetails():
    orderlds:str
    productld:str
    productName:str
    quantity:int
    unitCoat:float
    total:float
    def __init__(self,detal):
        order=detal
        





    