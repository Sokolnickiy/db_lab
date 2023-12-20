insert_query = """
INSERT INTO god_table (
    OUTID, Birth, SEXTYPENAME, REGNAME, AREANAME, TERNAME,
    REGTYPENAME, TerTypeName, ClassProfileNAME, ClassLangName,
    EONAME, EOTYPENAME, EORegName, EOAreaName, EOTerName, EOParent,
    UkrTest, UkrTestStatus, UkrBall100, UkrBall12, UkrBall, UkrAdaptScale,
    UkrPTName, UkrPTRegName, UkrPTAreaName, UkrPTTerName,
    histTest, HistLang, histTestStatus, histBall100, histBall12, histBall,
    histPTName, histPTRegName, histPTAreaName, histPTTerName,
    mathTest, mathLang, mathTestStatus, mathBall100, mathBall12, mathBall,
    mathPTName, mathPTRegName, mathPTAreaName, mathPTTerName,
    physTest, physLang, physTestStatus, physBall100, physBall12, physBall,
    physPTName, physPTRegName, physPTAreaName, physPTTerName,
    chemTest, chemLang, chemTestStatus, chemBall100, chemBall12, chemBall,
    chemPTName, chemPTRegName, chemPTAreaName, chemPTTerName,
    bioTest, bioLang, bioTestStatus, bioBall100, bioBall12, bioBall,
    bioPTName, bioPTRegName, bioPTAreaName, bioPTTerName,
    geoTest, geoLang, geoTestStatus, geoBall100, geoBall12, geoBall,
    geoPTName, geoPTRegName, geoPTAreaName, geoPTTerName,
    engTest, engTestStatus, engBall100, engBall12, engDPALevel, engBall,
    engPTName, engPTRegName, engPTAreaName, engPTTerName,
    fraTest, fraTestStatus, fraBall100, fraBall12, fraDPALevel, fraBall,
    fraPTName, fraPTRegName, fraPTAreaName, fraPTTerName,
    deuTest, deuTestStatus, deuBall100, deuBall12, deuDPALevel, deuBall,
    deuPTName, deuPTRegName, deuPTAreaName, deuPTTerName,
    spaTest, spaTestStatus, spaBall100, spaBall12, spaDPALevel, spaBall,
    spaPTName, spaPTRegName, spaPTAreaName, spaPTTerName
) VALUES (
    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
    %s, %s, %s, %s, %s, %s
);
"""
