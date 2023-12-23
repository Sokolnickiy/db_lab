GET_NUMBER_OF_ROWS = """
    SELECT count(id) from "god_table"
"""

GET_GOD_TABLE_ROW = """
    SELECT * FROM "god_table" WHERE id = %(id)s;
"""

CREATE_LOCATION_INFO = """
    INSERT INTO "location_info" (
        reg_name,
        area_name,
        ter_name
    ) VALUES (
        %(reg_name)s,
        %(area_name)s,
        %(ter_name)s
    ) RETURNING id;
"""

CREATE_E_O = """
    INSERT INTO "e_o" (
        name,
        type_name,
        parent,
        location_info_id
    ) VALUES (
        %(name)s,
        %(type_name)s,
        %(parent)s,
        %(location_info_id)s
    ) RETURNING id;
"""

CREATE_CLASS_INFO = """
    INSERT INTO "class_info" (
        lang_name,
        profile_name
    ) VALUES (
        %(lang_name)s,
        %(profile_name)s
    ) RETURNING id;
"""

CREATE_PERSON = """
    INSERT INTO "person" (
        outid,
        birth,
        sex_type,
        location_info_id,
        e_o_id,
        class_info_id
    ) VALUES (
        %(outid)s,
        %(birth)s,
        %(sex_type)s,
        %(location_info_id)s,
        %(e_o_id)s,
        %(class_info_id)s
    ) RETURNING id;
"""

CREATE_TEST = """
    INSERT INTO "test" (
        ball,
        ball12,
        ball100,
        status,
        name,
        dpa_level,
        adapt_scale,
        location_info_id
    ) VALUES (
        %(ball)s,
        %(ball12)s,
        %(ball100)s,
        %(status)s,
        %(name)s,
        %(dpa_level)s,
        %(adapt_scale)s,
        %(location_info_id)s
    ) RETURNING id;
"""

CREATE_PERSON_TEST = """
    INSERT INTO "person_test" (
        test_id,
        person_id
    ) VALUES (
        %(test_id)s,
        %(person_id)s
    ) RETURNING id;
"""

GET_LOCATION_ID = """
    SELECT id FROM "location_info"
    WHERE 
        reg_name = %(reg_name)s 
        AND area_name = %(area_name)s
        AND ter_name = %(ter_name)s;
"""

GET_E_O = """
    SELECT id FROM "e_o"
    WHERE
        name = %(name)s
        AND type_name = %(type_name)s
        AND parent = %(parent)s
        AND location_info_id = %(location_info_id)s;
"""

GET_CLASS_INFO = """
    SELECT id FROM "class_info" 
    WHERE
        lang_name = %(lang_name)s
        AND profile_name = %(profile_name)s;
"""
