from fastapi import APIRouter


router = APIRouter()


###### GET METHODS ######
@router.get('/')
def status():
    return {'STATUS': 'ONLINE'}
