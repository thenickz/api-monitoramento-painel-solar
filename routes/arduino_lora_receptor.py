from fastapi import APIRouter


router = APIRouter()


###### GET METHODS ######
@router.get('/arduino-lora-receptor/status')
def status():
    # create logic to check all this
    return {'STATUS': 'ONLINE',
            'SITUATION': 'NORMAL',
            'Data Sent': {
                'Last Data': 123,
                'Last Time': 'dd/mm/yy 12:34:56',
                'Time until next data': 12
                },
            'Data Receveid': {
                'Last Data': 123,
                'Last Time': 'dd/mm/yy 12:34:56',
                'Time until next data': 12
                }
            }

            
