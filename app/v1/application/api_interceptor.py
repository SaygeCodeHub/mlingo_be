"""Apis are intercepted in this file"""

from fastapi import APIRouter
from fastapi import Depends

from app.infrastructure.database import engine, get_db
from app.v1.application.dto.dto_classes import ResponseDTO
from app.v1.application.service.language_service import add_translation, fetch_language_keys, \
    fetch_all_translation
from app.v1.domain import models, schema

router = APIRouter()
models.Base.metadata.create_all(bind=engine)

"""----------------------------------------------Language Related APIs-------------------------------------------------------------------"""


@router.post("/v1/addTranslation")
def new_translation(addTranslation: schema.Translate, db=Depends(get_db)):
    try:
        return add_translation(addTranslation, db)
    except Exception as e:
        ResponseDTO(204, f"{str(e)}", {})


@router.get("/v1/getAllTranslations")
def get_all_translations(db=Depends(get_db)):
    try:
        return fetch_all_translation(db)
    except Exception as e:
        return ResponseDTO(204, f"{str(e)}", [])


@router.get("/v1/getLanguageKeys")
def get_language_keys(languageId: int, db=Depends(get_db)):
    try:
        return fetch_language_keys(languageId, db)
    except Exception as e:
        return ResponseDTO(204, f"{str(e)}", [])


@router.get("/v1/getAllLanguage")
def get_all_language(db=Depends(get_db)):
    try:
        languages = db.query(models.Language).all()
        return ResponseDTO(200, "Languages fetched successfully", languages)
    except Exception as e:
        return ResponseDTO(204, f"{str(e)}", [])
