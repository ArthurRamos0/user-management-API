import uuid

# ---------------------------
# TESTES COMPLETOS DE CRUD
# ---------------------------

def test_create_user(client):
    email = f"user_{uuid.uuid4().hex}@email.com"
    payload = {"name": "Teste", "email": email, "password": "senha123"}
    response = client.post("/users/", json=payload)
    print("CREATE:", response.json())  # opcional para debug
    assert response.status_code == 201
    data = response.json()
    assert "id" in data
    assert data["name"] == "Teste"
    assert data["email"] == email

def test_get_user(client):
    email = f"user_{uuid.uuid4().hex}@email.com"
    payload = {"name": "User2", "email": email, "password": "123456"}
    response_post = client.post("/users/", json=payload)
    user_id = response_post.json()["id"]

    response_get = client.get(f"/users/{user_id}")
    print("GET:", response_get.json())
    assert response_get.status_code == 200
    data = response_get.json()
    assert data["id"] == user_id
    assert data["name"] == "User2"
    assert data["email"] == email

def test_update_user(client):
    email = f"user_{uuid.uuid4().hex}@email.com"
    payload = {"name": "User3", "email": email, "password": "abcdef"}
    response_post = client.post("/users/", json=payload)
    user_id = response_post.json()["id"]

    update_email = f"user_{uuid.uuid4().hex}@email.com"
    update_payload = {"name": "User3Updated", "email": update_email}
    response_put = client.put(f"/users/{user_id}", json=update_payload)
    print("UPDATE:", response_put.json())
    assert response_put.status_code == 200
    data = response_put.json()
    assert data["id"] == user_id
    assert data["name"] == "User3Updated"
    assert data["email"] == update_email

def test_delete_user(client):
    email = f"user_{uuid.uuid4().hex}@email.com"
    payload = {"name": "User4", "email": email, "password": "123456"}
    response_post = client.post("/users/", json=payload)
    user_id = response_post.json()["id"]

    response_delete = client.delete(f"/users/{user_id}")
    assert response_delete.status_code == 204

    response_get = client.get(f"/users/{user_id}")
    assert response_get.status_code == 404

# ---------------------------
# TESTES DE VALIDAÇÃO
# ---------------------------

def test_create_user_invalid_email(client):
    payload = {"name": "Bad", "email": "invalido", "password": "123456"}
    response = client.post("/users/", json=payload)
    assert response.status_code == 422

def test_create_user_short_password(client):
    payload = {"name": "ShortPass", "email": f"user_{uuid.uuid4().hex}@email.com", "password": "123"}
    response = client.post("/users/", json=payload)
    assert response.status_code == 422

# ---------------------------
# TESTES DE USUÁRIO INEXISTENTE
# ---------------------------

def test_get_nonexistent_user(client):
    response = client.get("/users/99999")
    assert response.status_code == 404

def test_update_nonexistent_user(client):
    update_payload = {"name": "NoUser", "email": f"user_{uuid.uuid4().hex}@email.com"}
    response = client.put("/users/99999", json=update_payload)
    assert response.status_code == 404

def test_delete_nonexistent_user(client):
    response = client.delete("/users/99999")
    assert response.status_code == 404
