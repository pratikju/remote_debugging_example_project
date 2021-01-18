def test_sample(app):
    with app.test_client() as client:
        resp = client.post("/api/v1/test")

        assert resp.status_code == 200
