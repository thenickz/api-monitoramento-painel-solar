from fastapi import APIRouter
router = APIRouter()



@router.get('/')
def status():
    return {'STATUS': 'ONLINE'}

@router.get('/solar_painel/start_id={start_id}-end_id={end_id}')
def teste(id: int):
    return {'id': id}


