from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import json

app = FastAPI()

# 配置CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 挂载静态文件
app.mount("/static", StaticFiles(directory="../"), name="static")

# 读取学生名单
def read_students():
    try:
        with open('students.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        return {"students": "离丁真,王大锤,芜湖,起说飞,利达挠,圣埃蒂安,的撒旦,是多少,仨打算,突然和"}

# 保存学生名单
def save_students(students_str):
    with open('students.json', 'w', encoding='utf-8') as f:
        json.dump({"students": students_str}, f, ensure_ascii=False)

# 获取学生名单
@app.get("/api/students")
async def get_students():
    return read_students()

# 更新学生名单
@app.post("/api/students")
async def update_students(students: dict):
    save_students(students["students"])
    return {"message": "更新成功"} 