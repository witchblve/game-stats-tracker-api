from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import models
import schemas
from database import get_db

# Вот эта строчка обязана быть в файле players.py и matches.py!
router = APIRouter(prefix="/players", tags=["Players"])

@router.post("/", response_model=schemas.PlayerResponse)
def create_player(player: schemas.PlayerCreate, db: Session = Depends(get_db)):
    db_player = models.Player(username=player.username, game=player.game, rank=player.rank)
    db.add(db_player)
    db.commit()
    db.refresh(db_player)
    return db_player

@router.get("/", response_model=list[schemas.PlayerResponse])
def get_players(db: Session = Depends(get_db)):
    return db.query(models.Player).all()

@router.put("/{player_id}", response_model=schemas.PlayerResponse)
def update_player(player_id: int, player_data: schemas.PlayerUpdate, db: Session = Depends(get_db)):
    player = db.query(models.Player).filter(models.Player.id == player_id).first()
    if not player:
        raise HTTPException(status_code=404, detail="player not found")
    
    player.username = player_data.username  
    player.game = player_data.game
    player.rank = player_data.rank
    
    db.commit()
    db.refresh(player)
    return player

@router.delete("/{player_id}")
def delete_player(player_id: int, db: Session = Depends(get_db)):
    player = db.query(models.Player).filter(models.Player.id == player_id).first()
    if not player:
        raise HTTPException(status_code=404, detail="данный игрок не найден")

    db.delete(player)
    db.commit()
    return {"message": f"player {player.username} success deleted"}