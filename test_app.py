from fastapi.testclient import TestClient

from app import app

client = TestClient(app)


def test_get_github():
    url = "https://github.com/NOTfedos"
    response = client.post("/content/parse", json={"url": url}, timeout=20)
    assert response.status_code == 200
    assert response.json() == {
        "title": "NOTfedos - Overview",
        "description": "NOTfedos has 20 repositories available. Follow their code on GitHub.",
        "imageUrl": "https://avatars.githubusercontent.com/u/32240844?v=4?s=400"
    }


def test_get_instagram():
    url = "https://instagram.com/st.lowwer"
    response = client.post("/content/parse", json={"url": url}, timeout=20)
    assert response.status_code == 400
    assert response.json() == {
        "error": {
            "message": "Connection to instagram.com timed out. (connect timeout=5)"
        }
    }


def test_get_404_github():
    url = "https://github.com/pasjgsjkn"
    response = client.post("/content/parse", json={"url": url}, timeout=20)
    assert response.status_code == 400
    assert response.json() == {
        "error": {
            "message": "404 Client Error: Not Found for url: https://github.com/pasjgsjkn"
        }
    }


def test_get_403_ozon():
    url = "https://www.ozon.ru/product/toster-tefal-s-poddonom-i-shchiptsami-includeo-tt533811-chernyy-324415005/?campaignId=226&sh=zx9AarFd2g"
    response = client.post("/content/parse", json={"url": url}, timeout=20)
    assert response.status_code == 400
    assert response.json() == {
        "error": {
            "message": "403 Client Error: Forbidden for url: https://www.ozon.ru/product/toster-tefal-s-poddonom-i-shchiptsami-includeo-tt533811-chernyy-324415005/?campaignId=226&sh=zx9AarFd2g"
        }
    }


def test_get_vk():
    url = "https://vk.com/konchenny_krab"
    response = client.post("/content/parse", json={"url": url}, timeout=20)
    assert response.status_code == 200
    assert response.json() == {
        "title": "Grigory Klientov | VK",
        "imageUrl": "https://vk.com//top-fwz1.mail.ru/counter?id=2579437;js=na"
    }
