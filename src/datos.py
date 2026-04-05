def limpiar_datos(students):
    students_limpio = {}

    for alumno in students:


        name = alumno.get("name")
        if not name or not name.strip():
            continue

        
        grade_limpio = alumno.get("grade")
        if not grade_limpio or not str(grade_limpio).strip().isdigit():
            continue

        grade = int(grade_limpio)

        
        name_normalizado = name.strip().title()
        status_normalizado = alumno.get("status", "").strip().title()

       
        if name_normalizado not in students_limpio or grade > students_limpio[name_normalizado]["grade"]:
            students_limpio[name_normalizado] = {"grade": grade, "status": status_normalizado}


    resultado = sorted(
        [
            {"name": k, "grade": v["grade"], "status": v["status"]}
            for k, v in students_limpio.items()
        ],
        key=lambda x: x["name"]
    )
    return resultado