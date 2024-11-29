from fastapi import FastAPI,HTTPException,APIRouter

crud_router = APIRouter()
user = {}
# @crud_router.get('/test')
# async def testing_crud():
#     return {"message":"For Testing Purpose"}

@crud_router.post('/create_user')
async def create_new_user(user_id : int, name:str):
    if user_id in user:
        raise HTTPException(status_code=400,detail='Already Present ')
    user[user_id] = {name:name}
    return user[user_id]

@crud_router.get('/user/{user_id}')
async def get_user_id(user_id :int):
    if user_id  not in user:
        raise HTTPException(status_code=404,detail="User not found")
    return user[user_id]

@crud_router.get('/user')
async def get_user():
    return user


@crud_router.put('/user/{user_id}')
async def user_update(user_id:int,name:str):
    if user_id not in user:
        raise HTTPException(status_code=404,detail="User Not Found")
    
    user[user_id][name] =  name
    return {"Updated User":user[user_id][name]}

@crud_router.delete('/delete/{user_id}')
async def user_Delete(user_id:int):
    if user_id not in user:
        raise HTTPException(status_code=404,detail="User not found ")
    del user[user_id]
    return {"message":"User Deleted Successfully"}