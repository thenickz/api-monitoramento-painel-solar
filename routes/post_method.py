from fastapi import APIRouter
from models import db_class


router = APIRouter()


@router.post('/solar_painel/send/{new_current}/{new_irradiance}')
def teste(new_current=float, new_irradiance=float):
    dados = db_class.Painel_Solar_Data(datetime=db_class.dt_moment(),current=new_current, irradiance=new_irradiance)
    dados.insert()
    return {'Criado': 1}
