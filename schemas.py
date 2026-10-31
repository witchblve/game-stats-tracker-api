#классы 
from pydantic import BaseModel, ConfigDict


class PlayerCreate(BaseModel):
    username: str
    game: str
    rank: str


class PlayerUpdate(BaseModel):
    username: str
    game: str
    rank: str


class PlayerResponse(BaseModel):
    id: int
    username: str
    game: str
    rank: str
    model_config = ConfigDict(from_attributes=True)


class MatchCreate(BaseModel):
    player_id: int
    result: str
    kills: int
    deaths: int

class MatchResponse(BaseModel):
    id: int
    player_id: int
    result: str
    kills: int
    deaths: int

    # Правильный синтаксис конфигурации в Pydantic v2 (обрати внимание на model_config и две 't' в attributes)
    model_config = {"from_attributes": True}
#когда ты делаешь запрос в базу данных через SQLAlchemy, она возвращает тебе не обычный словарь с данными (вроде {"id": 1, "username": "Alex"}), а специальный объект класса модели
#благодаря этой строке програма может читать данные которые приходят из таблиц
