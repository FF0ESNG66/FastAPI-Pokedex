import models
from config import engine, SessionLocal
from fastapi import FastAPI, HTTPException, Depends, Path
from sqlalchemy.orm import Session
from typing import Annotated, Optional
from schemas import PokedexBase, UpdatePokedexBase
from sqlalchemy import func


app = FastAPI()
models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]



@app.get("/")
async def pokedex(db: db_dependency):
    result = db.query(models.Pokedex).all()
    if not result:
        raise HTTPException(status_code=404, detail="There is not pokemon information in the pokedex right now, try again later.")
    
    return result



@app.get("/pokemon-name/{pokemon_name}")
async def pokedex_query_name(pokemon_name: str, db: db_dependency):
    pokemon_name = pokemon_name.capitalize()
    result = db.query(models.Pokedex).filter(models.Pokedex.name == pokemon_name).first()
    if not result:
        raise HTTPException(status_code=404, detail="This pokemon is not registered in the pokedex yet.")
    
    return result



@app.get("/pokedex-index/{pokemon_num}")
async def pokedex_query_pokemon_num(pokemon_num: int, db: db_dependency):
    result = db.query(models.Pokedex).filter(models.Pokedex.pokedex_num == pokemon_num).first()
    if not result:
        raise HTTPException(status_code=404, detail="This pokemon is not registered in the pokedex yet.")
    
    return result
    


# @app.get("/type/{type}")
# async def pokedex_query_pokemon_type(type: str, db: db_dependency):
#     result = db.query(models.Pokedex).filter(models.Pokedex.types.any(func.lower(type))).all()

#     if not result:
#         raise HTTPException(status_code=404, detail=f"No Pokémon found with type: {type}")

#     return result



@app.get("/ability/{ability}")
async def pokedex_query_pokemon_abillity(ability: str, db: db_dependency):
    result = db.query(models.Pokedex).filter(models.Pokedex.abilities.any(func.lower(ability))).all()
    if not result:
        raise HTTPException(status_code=404, detail=f"No Pokémon found with ability: {ability}")
    
    return result
    


################################################################################################

### Getting pokemon but with query params ###

@app.get("/type")
async def pokedex_query_pokemon_type(type: Optional[str], db: db_dependency):
    result = db.query(models.Pokedex).filter(models.Pokedex.types.any(func.lower(type))).all()
    if not result:
        return HTTPException(status_code=404, detail=f"There are no pokemons with type: {type}")
    
    return result
    
################################################################################################



@app.post("/create-pokemon/")
async def post_pokemon(pokemon: PokedexBase, db: db_dependency):
    new_pokemon =  models.Pokedex(
        pokedex_num=pokemon.pokedex_num,
        name=pokemon.name.lower(),
        description=pokemon.description,
        types=pokemon.types,
        abilities=pokemon.abilities,
        location=pokemon.location)
    db.add(new_pokemon)
    db.commit()
    return {"Message": "Pokemon uploaded successfully!"}



@app.delete("/delete/{pokemon_name}")
async def delete_pokemon(pokemon_name: str, db: db_dependency):
    pokemon_name_low = pokemon_name.lower()
    result = db.query(models.Pokedex).filter(models.Pokedex.name == pokemon_name_low).first()

    if not result:
        raise HTTPException(status_code=404, detail="This pokemon is not registered in the pokedex yet.")
    else:
        db.delete(result)
        db.commit()
        return {"detail": "Pokemon deleted successfully"}
    



@app.put("/update-pokemon")
async def update_pokemon(pokemon: UpdatePokedexBase, db: db_dependency):
    pokemon_object = db.query(models.Pokedex).filter(pokemon.name == models.Pokedex.name).first()
    if not pokemon_object:
        raise HTTPException(status_code=404, detail='This pokemon doesn\'t exist')
    
    if pokemon.name != None:
        pokemon_object.name = pokemon.name
    if pokemon.pokedex_num != None:
        pokemon_object.pokedex_num = pokemon.pokedex_num
    if pokemon.description != None:
        pokemon_object.description = pokemon.description
    if pokemon.types != None:
        pokemon_object.types = pokemon.types
    if pokemon.abilities != None:
        pokemon_object.abilities = pokemon.abilities
    if pokemon.location != None:
        pokemon_object.location = pokemon.location
    db.commit()
    return {'Message': 'Pokemon updated successfully'}
        