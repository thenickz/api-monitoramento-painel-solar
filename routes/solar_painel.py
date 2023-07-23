from fastapi import APIRouter
from models.Solar_Panel_Data import Solar_Panel_Data, dt_moment


router = APIRouter()


###### GET METHODS ######
@router.get('/solar-painel/start-id={start_id}-end-id={end_id}')
def teste(start_id: int, end_id: int):
    return {'id': (start_id, end_id)}


###### POST METHODS ######
@router.post('/solar-painel/send/{new_current}/{new_irradiance}')
def teste(new_current=float, new_irradiance=float):
    dados = Solar_Panel_Data(datetime=dt_moment(),current=new_current, irradiance=new_irradiance)
    dados.insert()
    return {'Criado': ':D'}
