# tests/test_main.py

import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock


@pytest.fixture(autouse=True)
@patch.dict("os.environ", {
    "DATABASE_URL": "postgresql://your_user:your_password@postgres/your_dbname",
    "JWT_SECRET": "mocked_jwt_secret"
})
@patch("src.managers.database_manager.DatabaseManager", autospec=True)
def mock_database_manager(mocked_database_manager):
    mocked_database_manager.return_value = MagicMock()
    yield mocked_database_manager.return_value


@pytest.fixture
def test_app():
    # Use the app instance from the main module
    from src.main import app
    client = TestClient(app)
    yield client


def test_read_health(test_app):
    response = test_app.get("/health")
    assert response.status_code == 200
    assert response.json() == {}
