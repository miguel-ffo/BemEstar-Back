# BemEstar-Back


Este repositório contém a API de saúde do projeto BemEstar, que visa fornecer funcionalidades para registrar e consultar dados de saúde diários, incluindo glicemia, pressão arterial e controle hídrico para usuários autenticados. A API também oferece funcionalidades de registro de usuários, login, alteração de senha e gerenciamento de treinos.


## Estrutura do Projeto

### 1. Modelos

**User:**
Modelo para gerenciar os usuários (com autenticação via JWT).

**DailyRecordModel:**
Modelo principal para armazenar o registro diário de saúde, incluindo glicemia e pressão arterial.

**GlycemiaModel:**
 Modelo para armazenar os dados de glicemia (pré e pós-treino).

**BloodPressureModel:**
 Modelo para armazenar os dados de pressão arterial (pré e pós-treino).

**Workout:** Modelo para armazenar os dados de treino diário.

### 2. Views

**RegisterPersonalView, RegisterUserView, LoginView, ChangePasswordView, ListAlunosView:**
 Views para registrar, login, alteração de senha e listar usuários.

**WaterConsumeView, AnamnesisCreateView, DailyRecordCreateView, DailyRecordGetView** Views para registrar consumo de agua, registrar anamnese e registrar e visualizar ficha diária de saúde.

**RegisterWorkoutView, ListWorkoutView:** View para registrar e listar o treino diário de um usuário.

### 3. Serializers

**PersonalRegisterSerializer, UserRegisterserializer, LoginSerializer, ChangePasswordSerializer:**

 Serializer para registrar, login e alteração de senha de usuários e personal.

**WaterConsumeSerializer, AnamnesisSerializer, GlycemiaSerializer, BloodPressureSerializer, DailyRecordSerializer, DailyRecordGetSerializer :** Serializer para registrar consumo de água, anamnese, glicemia, pressão sanguínea , registrar e listar registros diários de saúde.

**WorkoutSerializer, WorkoutListSerializer:** Serializer para registrar e listar os treinos diários.

## Instruções de Uso
Pré-requisitos
Python 3.8+
Django 3.2+
Django REST Framework
JWT (JSON Web Tokens) para autenticação

## Instalação

### Clone o repositório:


```
git clone https://github.com/miguel-ffo/BemEstar-Back.git
```
### Crie e ative uma venv:
```
python -m venv venv
venv/Scripts/activate
```

### Instale as dependências:

```
cd BemEstar-Back
pip install -r requirements.txt
cd core
```
### Execute as migrações para criar as tabelas no banco de dados:

```
python manage.py migrate
```

### Crie um superusuário para acessar a API:

```
python manage.py createsuperuser
```

### Inicie o servidor Django:

```
python manage.py runserver
```

Agora a API estará disponível em  http://127.0.0.1:800
Para acessar o painel Swagger é so acesar a url: /api/docs

# Endpoints


## Authentication

### Register Personal User


**POST** `/auth/personal/register/`

#### Headers:
- `Content-Type`: `application/json`
- `User-Agent`: `insomnia/10.3.0`

#### Body:
```json
{
  "username": "test1",
  "password": "test1password",
  "email": "test1@test.com",
  "role": "personal",
  "phone": "123456789"
}
```

### Register User

**POST** `/auth/users/register/`

#### Headers:
- `Authorization`: Bearer token
- `Content-Type`: `application/json`
- `User-Agent`: `insomnia/10.3.1`

#### Body:
```json
{
  "username": "test4",
  "password": "test4password",
  "email": "test4@test.com",
  "role": "usuario",
  "phone": "123456789"
}
```

### Login
**POST** `/auth/login/`

#### Headers:
- `Content-Type`: `application/json`
- `User-Agent`: `insomnia/10.3.1`

#### Body:
```json
{
  "email": "user@example.com",
  "password": "usuario1"
}
```

### Change Password
**POST** `/auth/change-password/`

#### Headers:
- `Authorization`: Bearer token
- `Content-Type`: `application/json`
- `User-Agent`: `insomnia/10.3.1`

#### Body:
```json
{
  "old_password": "test2password",
  "new_password": "test2"
}
```

### List Personal Users
**GET** `/auth/personal/users/`

#### Headers:
- `Authorization`: Bearer token
- `User-Agent`: `insomnia/10.3.1`

### Register Workout
**POST** `/workouts/register/`

#### Headers:
- `Authorization`: Bearer token
- `Content-Type`: `application/json`
- `User-Agent`: `insomnia/10.3.1`

#### Body:
```json
{
  "date": "2025-03-01",
  "status": "done",
  "description": "muito facil"
}
```

### List Workouts
**GET** `/workouts/list/?id=2`

#### Headers:
- `Authorization`: Bearer token
- `User-Agent`: `insomnia/10.3.1`

### Water Intake
**POST** `/health/water-intake/`

#### Headers:
- `Authorization`: Bearer 
- `Content-Type`: `application/json`
- `User-Agent`: `insomnia/10.3.1`

#### Body:
```json
{
  "user_id": 2,
  "date": "2025-03-09",
  "water_goal": 2000,
  "water_consumed": 1750
}
```

### Anamnesis
**POST** `/health/anamnesis/`

#### Headers:
- `Authorization`: Bearer
- `Content-Type`: `application/json`
- `User-Agent`: `insomnia/10.3.1`

#### Body:
```json
{
  "weight": 61,
  "height": 1.70,
  "medical_conditions": "null",
  "medications": "null",
  "exercise_frequency": "5 days at week",
  "goals": "70 kg"
}
```

### Daily Record
**POST** `/health/daily-record/`

#### Headers:
- `Authorization`: Bearer 
- `Content-Type`: `application/json`
- `User-Agent`: `insomnia/10.3.1`

#### Body:
```json
{
  "date": "2025-03-09",
  "glycemia": {
    "pre_workout": 100,
    "post_workout": 140
  },
  "blood_pressure": {
    "pre_workout_systolic": 100,
    "pre_workout_diastolic": 100,
    "post_workout_systolic": 200,
    "post_workout_diastolic": 240
  }
}
```

### Daily Record View
**GET** `/health/daily-record-view/?date=2025-03-09`

#### Headers:
- `Authorization`: Bearer 
- `User-Agent`: `insomnia/10.3.1`
