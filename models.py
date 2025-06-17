from pydantic import BaseModel, HttpUrl
from typing import List, Optional
from datetime import datetime

class Objects(BaseModel):
    total: int
    objectIDs: Optional[List[int]]

class Constituent(BaseModel):
    constituentID: int
    role: str
    name: str
    constituentULAN_URL: HttpUrl
    constituentWikidata_URL: HttpUrl
    gender: Optional[str]  # в Api указано, что может быть пустым

class Measurement(BaseModel):
    elementName: str
    elementDescription: str
    elementMeasurements: dict

class Tag(BaseModel):
    term: str
    AAT_URL: str
    Wikidata_URL: str

class Object(BaseModel):
    objectID: int
    isHighlight: bool
    accessionNumber: str
    accessionYear: str
    isPublicDomain: bool
    primaryImage: str
    primaryImageSmall: str
    additionalImages: Optional[List[str]]
    constituents: Optional[List[Constituent]]  # Constituent описан выше
    department: str
    objectName: str
    title: str
    culture: str
    period: str
    dynasty: str
    reign: str
    portfolio: str
    artistRole: str
    artistPrefix: str
    artistDisplayName: str
    artistDisplayBio: str
    artistSuffix: str
    artistAlphaSort: str
    artistNationality: str
    artistBeginDate: str
    artistEndDate: str
    artistGender: str
    artistWikidata_URL: str
    artistULAN_URL: str
    objectDate: str
    objectBeginDate: int
    objectEndDate: int
    medium: str
    dimensions: str
    #dimensionsParsed: float # его нет в ответе, но есть в описании API
    measurements: Optional[List[Measurement]]  # описан выше
    creditLine: str
    geographyType: str
    city: str
    state: str
    county: str
    country: str
    region: str
    subregion: str
    locale: str
    locus: str
    excavation: str
    river: str
    classification: str
    rightsAndReproduction: str
    linkResource: str
    metadataDate: datetime
    repository: str
    objectURL: str
    tags: Optional[List[Tag]]
    objectWikidata_URL: str
    isTimelineWork: bool
    GalleryNumber: str

class SearchResponse(BaseModel):
    total: int
    objectIDs: Optional[List[int]]


class Departament(BaseModel):
    departmentId: int
    displayName: str

class Departments(BaseModel):
    departments: Optional[List[Departament]]  # описан выше



