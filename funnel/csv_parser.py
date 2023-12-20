import pandas as pd
import numpy as np  
from time import sleep
from loguru import logger


DATA_HEADER = [
    "OUTID", "Birth", "SEXTYPENAME", "REGNAME", "AREANAME", "TERNAME",
    "REGTYPENAME", "TerTypeName", "ClassProfileNAME", "ClassLangName",
    "EONAME", "EOTYPENAME", "EORegName", "EOAreaName", "EOTerName", "EOParent", 
    "UkrTest", "UkrTestStatus", "UkrBall100", "UkrBall12", "UkrBall", "UkrAdaptScale", "UkrPTName", "UkrPTRegName", "UkrPTAreaName", "UkrPTTerName", 
    "histTest", "HistLang", "histTestStatus", "histBall100", "histBall12", "histBall", "histPTName", "histPTRegName", "histPTAreaName", "histPTTerName", 
    "mathTest", "mathLang", "mathTestStatus", "mathBall100", "mathBall12", "mathBall", "mathPTName", "mathPTRegName", "mathPTAreaName", "mathPTTerName", 
    "physTest", "physLang", "physTestStatus", "physBall100", "physBall12", "physBall", "physPTName", "physPTRegName", "physPTAreaName", "physPTTerName", 
    "chemTest", "chemLang", "chemTestStatus", "chemBall100", "chemBall12", "chemBall", "chemPTName", "chemPTRegName", "chemPTAreaName", "chemPTTerName", 
    "bioTest", "bioLang", "bioTestStatus", "bioBall100", "bioBall12", "bioBall", "bioPTName", "bioPTRegName", "bioPTAreaName", "bioPTTerName",
    "geoTest", "geoLang", "geoTestStatus", "geoBall100", "geoBall12", "geoBall", "geoPTName", "geoPTRegName", "geoPTAreaName", "geoPTTerName", 
    "engTest", "engTestStatus", "engBall100", "engBall12", "engDPALevel", "engBall", "engPTName", "engPTRegName", "engPTAreaName", "engPTTerName", 
    "fraTest", "fraTestStatus", "fraBall100", "fraBall12", "fraDPALevel", "fraBall", "fraPTName", "fraPTRegName", "fraPTAreaName", "fraPTTerName", 
    "deuTest", "deuTestStatus", "deuBall100", "deuBall12", "deuDPALevel", "deuBall", "deuPTName", "deuPTRegName", "deuPTAreaName", "deuPTTerName", 
    "spaTest", "spaTestStatus", "spaBall100", "spaBall12", "spaDPALevel", "spaBall", "spaPTName", "spaPTRegName", "spaPTAreaName", "spaPTTerName"
]
HEADER_MAPPING = {string: index for index, string in enumerate(DATA_HEADER)}


class CsvParser:

    def __init__(self, csv_file: str = "U8D2019.csv") -> None:
        self.__csv_file = csv_file

    def parse_to_dict(self) -> None:
        self.df = pd.read_csv(self.__csv_file, encoding="utf-8", delimiter=";", header=None)
        header = self.df.iloc[0].tolist()
        if header == DATA_HEADER:
            self._parse_to_float()
            logger.debug("Parsing successful")
        else:
            logger.info("Wrong csv format")
    
    def _parse_to_float(self) -> None:
        for header_value in DATA_HEADER:
            if header_value.endswith("100") or header_value.endswith("12") or header_value.endswith("Ball") or header_value.endswith("Scale"):
                self.df[HEADER_MAPPING[header_value]] = self.df[HEADER_MAPPING[header_value]].str.replace(',', '.', regex=False)
                self.df[HEADER_MAPPING[header_value]] = pd.to_numeric(self.df[HEADER_MAPPING[header_value]].dropna(), errors='coerce')
                self.df.replace({np.nan: None}, inplace=True)
                
