# BemEstar-Back
Este é o backend do projeto BemEstar, utilizando Django e PostgreSQL no Docker.

### Requisitos
Docker e Docker Compose instalados em sua máquina.

##Passo a Passo
### 1. Clonar o repositório
Clone o repositório para a sua máquina local:

```
git clone https://github.com/seu_usuario/BemEstar-Back.git
cd BemEstar-Back
```

### 2. Construir e subir os contêineres
Com o Docker e Docker Compose instalados, execute o comando abaixo para construir e iniciar os contêineres:

```
docker-compose up --build
```

Este comando irá:

* Construir as imagens (se necessário).
* Subir o banco de dados PostgreSQL.
* Subir o servidor Django.
* Rodar as migrações automaticamente.

### 3. Criar um superusuário (caso necessário)
Se você precisar criar um superusuário para acessar o Django Admin, execute o comando abaixo:

```
docker-compose exec web python manage.py createsuperuser
```

Siga as instruções para definir um nome de usuário, e-mail e senha.

### 4. Acessar a aplicação
Após a inicialização, a aplicação estará disponível no seguinte endereço:

Django Admin: http://localhost:8000/admin/

API: http://localhost:8000/

Você pode acessar a aplicação no seu navegador ou fazer requisições à API.

### 5. Parar os contêineres
Quando terminar de usar a aplicação, você pode parar os contêineres com:

```
docker-compose down
```

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
  "new_password": "test2",
  "confirm_password": "test2"
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
