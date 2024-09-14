
SQL_QUERY = """
SELECT e1.employee_name, e2.employee_name 
FROM employee e1 
JOIN sample_data d ON e1.department_id = d.department_id;
"""

SQ = SQL_QUERY.upper().strip().replace(";","").split()

KEYWORD_LIST = ['FROM','JOIN']


for KW in SQ:
    if KW in KEYWORD_LIST:
        # index = SQ.index(KW)
        # print(index)
        TABLE_NAME_INDEX = SQ.index(KW)+1
        # print(SQ[TABLE_NAME_INDEX])
        SQ[TABLE_NAME_INDEX] = SQ[TABLE_NAME_INDEX] + "YYYYYYY"
    # else:
    #     # print(KEYWORD_LIST.index(KW))
    #     # index = SQ.index(KW)
    #     # print(index)
    #     print('no')

print(SQ)