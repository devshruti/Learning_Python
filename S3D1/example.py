def allocate_projects(employees,projects):
    assign_pro =[]

    for employee in employees:
        if employee["current_project"] is not None:
            continue

    for project in projects:
        if project not in assign_pro:
            if all(skill in employee["skills"] for skill in project["required_skills"]):
                employee["current_project"] = project["name"]
                break

    pro_assign = [{"employee":employee["name"], "project": employee["current_project"]} for employee in employees]
    return pro_assign
        

employees = [ 
    {"name":"John", "skills":["Python", "Database"], "current_project": None},
    {"name":"Emma", "skills":["Java", "Testing"], "current_project": None},
    {"name":"Kelly", "skills":["Python", "Java"], "current_project": None}
]

projects = [
    {"name":"Project A", "required_skills":["Python", "Database"]},
    {"name":"Project B", "required_skills":["Java", "Testing"]},
    {"name":"Project C", "required_skills":["Python", "Java"]}
]

res = allocate_projects(employees,projects)
print(res)