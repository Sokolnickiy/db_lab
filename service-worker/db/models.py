from pydantic import BaseModel


class ClassInfo(BaseModel):
    profile_name: str | None
    lang_name: str | None


class LocationInfo(BaseModel):
    reg_name: str 
    area_name: str 
    ter_name: str 


class Test(BaseModel):
    ball: float | None
    ball_100: float | None
    ball_12: float | None
    status: str
    name: str
    dpa_level: str | None
    adapt_scale: int | None
    location_info: LocationInfo


class Eo(BaseModel):
    name: str | None
    type_name: str | None
    parent: str | None
    location_info: LocationInfo  | None


class Person(BaseModel):
    outid: str
    birth: int
    sex_type: str
    location_info: LocationInfo
    class_info: ClassInfo


class CleanData(BaseModel):
    tests: list[Test]
    person: Person
    e_o: Eo | None
