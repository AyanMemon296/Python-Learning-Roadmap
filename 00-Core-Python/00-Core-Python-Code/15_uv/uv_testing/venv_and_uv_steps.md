# Python Virtual Environments and `uv` Setup Guide

This guide explains step-by-step how to **install**, **create**, and **set up** Python environments using both **`venv`** (built-in) and **`uv`** (fast modern tool).  
After setup, you can install packages and run your projects in an isolated environment.

---

## 1. Prerequisites
- **Python 3.10+** installed on your system.
- **PowerShell (Windows)** or **Terminal (Mac/Linux)**.
- Ensure Python is added to your system PATH.

---

## 2. Setting Up `venv`

### **2.1 Create a Virtual Environment**
Navigate to your project folder:
```powershell
cd D:\Projects\MyApp
python -m venv .venv
````

This creates a folder named `.venv` containing the environment.

---

### **2.2 Activate the Environment**

```powershell
.\.venv\Scripts\activate
```

If you see **“running scripts is disabled”**, fix it with:

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned -Force
```

Then run activate again.

---

### **2.3 Install Packages**

```powershell
pip install requests flask
```

To save dependencies:

```powershell
pip freeze > requirements.txt
```

---

### **2.4 Deactivate**

```powershell
deactivate
```

---

## 3. Setting Up `uv`

`uv` is a modern, fast package and environment manager for Python.

---

### **3.1 Install `uv`**

```powershell
pip install uv
```

(You can also install via `pipx install uv` if you have pipx.)

---

### **3.2 Create a New Project**

```powershell
uv init myapp
cd myapp
```

This sets up a project and creates an environment automatically.

---

### **3.3 Add Packages**

```powershell
uv add flask requests
```

---

### **3.4 Run Python Scripts**

```powershell
uv run app.py
```

`uv` automatically uses the right virtual environment.

---

### **3.5 Sync Dependencies**

```powershell
uv sync
```

This installs all dependencies listed in `uv.lock`.

---

## 4. Which Should You Use?

* Use **`venv`** if you want the built-in, classic method.
* Use **`uv`** for **speed**, **automatic environment handling**, and modern features.

---

## 5. Next Steps

After creating your environment (via `venv` or `uv`):

* Create your Python scripts (`app.py`).
* Install required libraries.
* Run your project using the isolated environment.

---

**Happy Coding!**
