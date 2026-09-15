# ⚡ Smart Electricity Monitor

A Django-based web application for monitoring electricity consumption,
calculating appliance-wise energy usage, and estimating electricity bills.

## 🎯 Project Overview

Smart Electricity Monitor helps users understand their electricity
consumption by allowing them to add appliances, enter their power usage
and operating hours, and calculate estimated energy consumption and
electricity costs.

## ✨ Features

- 🔌 Add and manage electrical appliances
- ⚡ Calculate appliance-wise energy consumption
- 🕒 Track daily appliance usage
- 📊 Estimate monthly electricity consumption
- 💰 Calculate estimated electricity bills
- 🧮 Simple electricity usage and bill calculator
- 🖥️ User-friendly web interface

## 🛠️ Technologies Used

- **Backend:** Python, Django
- **Frontend:** HTML, CSS, JavaScript
- **Database:** SQLite
- **Development Tool:** Visual Studio Code

## 📂 Project Structure

```text
Smart_Electricity_Monitor/
├── smartelectricitymonitor/
│   ├── accounts/
│   ├── appliances/
│   ├── billing/
│   ├── dashboard/
│   ├── smartelectricitymonitor/
│   └── manage.py
├── static/
├── templates/
├── .gitignore
└── README.md


## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/rauzatul-jannah/SmartElectricityMonitor.git
cd SmartElectricityMonitor
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

**Windows:**

```bash
.venv\Scripts\activate
```

### 4. Install Django

```bash
pip install django
```

### 5. Run database migrations

```bash
cd smartelectricitymonitor
python manage.py migrate
```

### 6. Start the development server

```bash
python manage.py runserver
```

Open your browser and visit:

```text
http://127.0.0.1:8000/
```

## ✨ Features

- 🔌 Add and manage household appliances
- ⚡ Calculate appliance-wise electricity consumption
- 🧮 Estimate monthly electricity usage
- 💰 Calculate estimated electricity bills
- 📊 Monitor electricity consumption
- 🏠 Simple and user-friendly interface
- 🗄️ SQLite database integration
- 🔐 Django-based application structure

  ## 🛠️ Technologies Used

| Category | Technologies |
|----------|--------------|
| **Backend** | Python, Django |
| **Frontend** | HTML, CSS, JavaScript |
| **Database** | SQLite |
| **Development Tool** | Visual Studio Code |
| **Version Control** | Git, GitHub |

## 📸 Screenshots

### Home Page

_Add a screenshot of the home page here._

### Appliance Management

_Add a screenshot showing the appliance list or add appliance page here._

### Bill Calculator

_Add a screenshot showing the electricity bill calculator here._
