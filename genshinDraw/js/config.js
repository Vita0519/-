// 名字用 ,(英文的逗号 ,) 分开

// 从后端获取学生名单
let studentsList = '离丁真，王大锤，芜湖，起说飞，利达挠，圣埃蒂安，的撒旦，是多少，仨打算，突然和'

// 添加一个获取学生列表的函数
async function getStudentsList() {
    try {
        // 将 localhost:8000 改为你的域名
        const response = await fetch('改为你的域名'); 
        const data = await response.json();
        studentsList = data.students;
        // 分割并清理名单
        return studentsList
            .split(/[,，]/)
            .map(name => name.trim())
            .filter(name => name)
            .map(name => name.replace(/\s+/g, ''));
    } catch (error) {
        console.error('获取学生名单失败:', error);
        return studentsList
            .split(/[,，]/)
            .map(name => name.trim())
            .filter(name => name)
            .map(name => name.replace(/\s+/g, ''));
    }
}

