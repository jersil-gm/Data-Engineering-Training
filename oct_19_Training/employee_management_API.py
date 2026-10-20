from fastapi import FastAPI, HTTPException, Body

app = FastAPI()

employees = []

@app.post("/employees")
def create_employee(emp: dict = Body(...)):
    employees.append(emp)
    return emp

@app.get("/employees")
def get_all_employees():
    return employees

@app.get("/employees/{employee_id}")
def get_employee_by_id(employee_id: int):
    for emp in employees:
        if emp.get("id") == employee_id:
            return emp
    raise HTTPException(status_code=404, detail="Employee not found")

@app.put("/employees/{employee_id}")
def update_employee(employee_id: int, updated_emp: dict = Body(...)):
    for index, emp in enumerate(employees):
        if emp.get("id") == employee_id:
            employees[index] = updated_emp
            return updated_emp
    raise HTTPException(status_code=404, detail="Employee not found")

@app.delete("/employees/{employee_id}")
def delete_employee(employee_id: int):
    for index, emp in enumerate(employees):
        if emp.get("id") == employee_id:
            employees.pop(index)
            return {"message": f"Employee {employee_id} deleted successfully"}
    raise HTTPException(status_code=404, detail="Employee not found")