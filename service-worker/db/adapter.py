from psycopg2.extras import  DictRow

from db.models import ClassInfo, CleanData, Eo, LocationInfo, Person, Test


class DataCleaner:

    def parse_row(self, row: DictRow) -> CleanData:
        person = self.__create_person_model(
            row=row
        )
        tests = self.__create_test_models(row=row)
        e_o = self.__create_e_o_model(row=row)
        return CleanData(
            tests=tests,
            person=person,
            e_o=e_o
        )

    def __create_e_o_model(
        self,
        row: DictRow
    ) -> Eo | None:
        return Eo(
            name=row["eoname"],
            type_name=row["eotypename"],
            parent=row["eoparent"],
            location_info=LocationInfo(
                reg_name=row["eoregname"],
                area_name=row["eoareaname"],
                ter_name=row["eotername"]
            ) if row["eoregname"] or row["eoareaname"] or row["eotername"] else None
        ) if row["eoname"] or row["eotypename"] or row["eoparent"] else None

    def __create_person_model(
        self,
        row: DictRow
    ) -> Person:
        return Person(
            outid=row["outid"],
            birth=row["birth"],
            sex_type=row["sextypename"],
            location_info=LocationInfo(
                reg_name=row["regname"],
                area_name=row["areaname"],
                ter_name=row["tername"]
            ),
            class_info=ClassInfo(
                profile_name=row["classprofilename"],
                lang_name=row["classlangname"]
            )
        )


    def __create_test_models(
        self,
        row: DictRow
    ) -> list[Test]:
        tests = []
        if row.get("ukrtest"):
            tests.append(self.__create_ukr_test(row=row))
        if row.get("histtest"):
            tests.append(self.__create_hist_test(row=row))
        if row.get("mathtest"):
            tests.append(self.__create_math_test(row=row))
        if row.get("phystest"):
            tests.append(self.__create_phys_test(row=row))
        if row.get("chemtest"):
            tests.append(self.__create_chem_test(row=row))
        if row.get("biotest"):
            tests.append(self.__create_bio_test(row=row))
        if row.get("geotest"):
            tests.append(self.__create_geo_test(row=row))
        if row.get("engtest"):
            tests.append(self.__create_eng_test(row=row))
        if row.get("fratest"):
            tests.append(self.__create_fra_test(row=row))
        if row.get("deutest"):
            tests.append(self.__create_deu_test(row=row))
        if row.get("spatest"):
            tests.append(self.__create_spa_test(row=row))
        return tests


    
    def __create_ukr_test(
        self,
        row: DictRow
    ) -> Test:
        return Test(
            status=row["ukrteststatus"],
            ball_100=row["ukrball100"],
            ball_12=row["ukrball12"],
            ball=row["ukrball"],
            name=row["ukrtest"],
            adapt_scale=row["ukradaptscale"],
            dpa_level=None,
            location_info=LocationInfo(
                reg_name=row["ukrptregname"],
                area_name=row["ukrptareaname"],
                ter_name=row["ukrpttername"]
            )
        )

    def __create_hist_test(
        self,
        row: DictRow
    ) -> Test:
        return Test(
            status=row["histteststatus"],
            ball_100=row["histball100"],
            ball_12=row["histball12"],
            ball=row["histball"],
            name=row["histtest"],
            adapt_scale=None,
            dpa_level=None,
            location_info=LocationInfo(
                reg_name=row["histptregname"],
                area_name=row["histptareaname"],
                ter_name=row["histpttername"]
            )
        )

    def __create_math_test(
        self,
        row: DictRow
    ) -> Test:
        return Test(
            status=row["mathteststatus"],
            ball_100=row["mathball100"],
            ball_12=row["mathball12"],
            ball=row["mathball"],
            name=row["mathtest"],
            adapt_scale=None,
            dpa_level=None,
            location_info=LocationInfo(
                reg_name=row["mathptregname"],
                area_name=row["mathptareaname"],
                ter_name=row["mathpttername"]
            )
        )

    def __create_phys_test(
        self,
        row: DictRow
    ) -> Test:
        return Test(
            status=row["physteststatus"],
            ball_100=row["physball100"],
            ball_12=row["physball12"],
            ball=row["physball"],
            name=row["phystest"],
            adapt_scale=None,
            dpa_level=None,
            location_info=LocationInfo(
                reg_name=row["physptregname"],
                area_name=row["physptareaname"],
                ter_name=row["physpttername"]
            )
        )

    def __create_chem_test(
        self,
        row: DictRow
    ) -> Test:
        return Test(
            status=row["chemteststatus"],
            ball_100=row["chemball100"],
            ball_12=row["chemball12"],
            ball=row["chemball"],
            name=row["chemtest"],
            adapt_scale=None,
            dpa_level=None,
            location_info=LocationInfo(
                reg_name=row["chemptregname"],
                area_name=row["chemptareaname"],
                ter_name=row["chempttername"]
            )
        )

    def __create_bio_test(
        self,
        row: DictRow
    ) -> Test:
        return Test(
            status=row["bioteststatus"],
            ball_100=row["bioball100"],
            ball_12=row["bioball12"],
            ball=row["bioball"],
            name=row["biotest"],
            adapt_scale=None,
            dpa_level=None,
            location_info=LocationInfo(
                reg_name=row["bioptregname"],
                area_name=row["bioptareaname"],
                ter_name=row["biopttername"]
            )
        )

    def __create_geo_test(
        self,
        row: DictRow
    ) -> Test:
        return Test(
            status=row["geoteststatus"],
            ball_100=row["geoball100"],
            ball_12=row["geoball12"],
            ball=row["geoball"],
            name=row["geotest"],
            adapt_scale=None,
            dpa_level=None,
            location_info=LocationInfo(
                reg_name=row["geoptregname"],
                area_name=row["geoptareaname"],
                ter_name=row["geopttername"]
            )
        )

    def __create_eng_test(
        self,
        row: DictRow
    ) -> Test:
        return Test(
            status=row["engteststatus"],
            ball_100=row["engball100"],
            ball_12=row["engball12"],
            ball=row["engball"],
            name=row["engtest"],
            adapt_scale=None,
            dpa_level=None,
            location_info=LocationInfo(
                reg_name=row["engptregname"],
                area_name=row["engptareaname"],
                ter_name=row["engpttername"]
            )
        )

    def __create_fra_test(
        self,
        row: DictRow
    ) -> Test:
        return Test(
            status=row["frateststatus"],
            ball_100=row["fraball100"],
            ball_12=row["fraball12"],
            ball=row["fraball"],
            name=row["fratest"],
            adapt_scale=None,
            dpa_level=row["fradpalevel"],
            location_info=LocationInfo(
                reg_name=row["fraptregname"],
                area_name=row["fraptareaname"],
                ter_name=row["frapttername"]
            )
        )

    def __create_deu_test(
        self,
        row: DictRow
    ) -> Test:
        return Test(
            status=row["deuteststatus"],
            ball_100=row["deuball100"],
            ball_12=row["deuball12"],
            ball=row["deuball"],
            name=row["deutest"],
            adapt_scale=None,
            dpa_level=row["deudpalevel"],
            location_info=LocationInfo(
                reg_name=row["deuptregname"],
                area_name=row["deuptareaname"],
                ter_name=row["deupttername"]
            )
        )

    def __create_spa_test(
        self,
        row: DictRow
    ) -> Test:
        return Test(
            status=row["spateststatus"],
            ball_100=row["spaball100"],
            ball_12=row["spaball12"],
            ball=row["spaball"],
            name=row["spatest"],
            adapt_scale=None,
            dpa_level=row["spadpalevel"],
            location_info=LocationInfo(
                reg_name=row["spaptregname"],
                area_name=row["spaptareaname"],
                ter_name=row["spapttername"]
            )
        )
