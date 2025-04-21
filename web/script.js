async function startConversion() {
    const templateInput = document.getElementById("templateFile");
    const planInput = document.getElementById("planFile");
    const saveDirInput = document.getElementById("saveDir");
    const status = document.getElementById("status");

    if (!templateInput.files[0] || !planInput.files[0] || !saveDirInput.files[0]) {
        status.textContent = "❗ Пожалуйста, выберите все файлы и папку.";
        return;
    }

    const templatePath = templateInput.files[0].path;
    const planPath = planInput.files[0].path;
    const saveDir = saveDirInput.files[0].path; // Это будет путь к файлу внутри папки

    // Получаем только директорию
    const saveFolder = saveDir.substring(0, saveDir.lastIndexOf("\\") || saveDir.lastIndexOf("/"));

    const result = await eel.start_conversion(templatePath, planPath, saveFolder)();
    status.textContent = result;
}
