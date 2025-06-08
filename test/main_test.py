from fastapi.testclient import TestClient
import datetime


def test_can_add_new_class(client: TestClient):
    """Test adding a new fitness class to the database"""
    # add zumba class
    zumba_class_time = datetime.datetime.now(datetime.UTC) + datetime.timedelta(weeks=1)
    zumba_response = client.post(
        "/classes/", json={"name": "zumba class", "class_time": f"{zumba_class_time}", "instructor": "zumba instructor", "total_slot": 2}
    )
    zumba_data = zumba_response.json()
    assert zumba_response.status_code == 200

    # validate zumba class
    assert zumba_data["name"] == "zumba class"
    # assert data["class_time"] == zumba_class_time  # TODO
    assert zumba_data["instructor"] == "zumba instructor"
    assert zumba_data["total_slot"] == 2

    # add yoga class
    yoga_class_time = datetime.datetime.now(datetime.UTC) + datetime.timedelta(weeks=2)
    yoga_response = client.post(
        "/classes/", json={"name": "yoga class", "class_time": f"{yoga_class_time}", "instructor": "yoga instructor", "total_slot": 3}
    )

    yoga_data = yoga_response.json()
    assert yoga_response.status_code == 200

    # validate yoga class
    assert yoga_data["name"] == "yoga class"
    # assert data["class_time"] == yoga_class_time   # TODO
    assert yoga_data["instructor"] == "yoga instructor"
    assert yoga_data["total_slot"] == 3



def test_get_list_of_all_classes(client: TestClient):
    """Adds two classes then retrives all classes"""
    #------------------------------------setup---------------------------------
    zumba_class_time = datetime.datetime.now(datetime.UTC) + datetime.timedelta(weeks=1)
    client.post(
        "/classes/", json={"name": "zumba class", "class_time": f"{zumba_class_time}", "instructor": "zumba instructor", "total_slot": 2}
    )
    yoga_class_time = datetime.datetime.now(datetime.UTC) + datetime.timedelta(weeks=2)
    client.post(
        "/classes/", json={"name": "yoga class", "class_time": f"{yoga_class_time}", "instructor": "yoga instructor", "total_slot": 3}
    )
    #------------------------------------setup---------------------------------

    get_response = client.get("/classes")
    get_data = get_response.json()
    assert get_response.status_code == 200
    # validate return data is a list type
    assert isinstance(get_data, list)
    assert get_data[0]["name"] == "zumba class"
    assert get_data[1]["name"] == "yoga class"


def test_book_a_class(client: TestClient):
    """Test if a client can book a class"""
    #------------------------------------setup---------------------------------
    yoga_class_time = datetime.datetime.now(datetime.UTC) + datetime.timedelta(weeks=2)
    client.post(
        "/classes/", json={"name": "yoga class", "class_time": f"{yoga_class_time}", "instructor": "yoga instructor", "total_slot": 3}
    )
    #------------------------------------setup---------------------------------


    book_response = client.post("/book/", json={"client_name": "client 1", "client_email": "client1@example.com", "class_id": 1})

    book_data = book_response.json()
    assert book_response.status_code == 200
    assert book_data["client_name"] == "client 1"
    assert book_data["client_email"] == "client1@example.com"
    assert book_data["class_id"] == 1


def test_get_all_booking_by_email(client: TestClient):
    """Test retriving all booking made by a specific email address"""

    #------------------------------------setup---------------------------------
    yoga_class_time = datetime.datetime.now(datetime.UTC) + datetime.timedelta(weeks=2)
    client.post(
        "/classes/", json={"name": "yoga class", "class_time": f"{yoga_class_time}", "instructor": "yoga instructor", "total_slot": 3}
    )
    client.post(
        "/classes/", json={"name": "zumba class", "class_time": f"{yoga_class_time}", "instructor": "zumba instructor", "total_slot": 3}
    )
    
    # book three classes
    client.post("/book/", json={"client_name": "client 1", "client_email": "client1@example.com", "class_id": 1})
    client.post("/book/", json={"client_name": "client 1", "client_email": "client1@example.com", "class_id": 1})
    client.post("/book/", json={"client_name": "client 1", "client_email": "client1@example.com", "class_id": 2})
    #------------------------------------setup---------------------------------


    # retrive all bookings
    get_response = client.get("/booking", params={
                                  "client_email": "client1@example.com"
                              } )
    get_data = get_response.json()
    assert get_response.status_code == 200
    assert len(get_data) == 3
   
def test_overbooking_error(client: TestClient):
    """Test server throughs error when is there is no slot available"""
    yoga_class_time = datetime.datetime.now(datetime.UTC) + datetime.timedelta(weeks=2)
    client.post(
        "/classes/", json={"name": "yoga class", "class_time": f"{yoga_class_time}", "instructor": "yoga instructor", "total_slot": 2}
    )
    
    # try to book three classes
    response = client.post("/book/", json={"client_name": "client 1", "client_email": "client1@example.com", "class_id": 1})
    assert response.status_code == 200
    response = client.post("/book/", json={"client_name": "client 1", "client_email": "client1@example.com", "class_id": 1})
    assert response.status_code == 200
    response = client.post("/book/", json={"client_name": "client 1", "client_email": "client1@example.com", "class_id": 1})
    assert response.status_code == 409
