"""Schemas for different models are written here"""
from typing import Optional, List

from pydantic import BaseModel

from app.v1.domain.models import ActivityStatus


class Language(BaseModel):
    language_id: Optional[int] | None = None
    language: str


class Key(BaseModel):
    key_id: Optional[int] | None = None
    key: str
    status: ActivityStatus = "PUBLISHED"


class LanguageTranslation(Language):
    translation: str


class Translate(Key):
    translation_id: Optional[int] | None = None
    translations: List[LanguageTranslation]
