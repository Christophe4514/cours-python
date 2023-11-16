from crm import User
import pytest
from tinydb import TinyDB, table
from tinydb.storages import MemoryStorage


@pytest.fixture()
def setup_db():
    User.DB = TinyDB(storage=MemoryStorage)


@pytest.fixture()
def user(setup_db):
    u = User(first_name="Don",
             last_name="Makila",
             adress="limete kin",
             phone_number="812435265")
    u.save()
    return u


def test_first_name(user):
    assert user.first_name == "Don"


def test_full_name(user):
    assert user.full_name == "Don Makila"


def test_exists(user):
    assert user.exists() is True


def test_no_exists():
    u = User(first_name="Don",
             last_name="Makila",
             adress="limete kin",
             phone_number="812435265")
    assert u.exists() is False


def test_db_instance(user):
    assert isinstance(user.db_instance, table.Document)
    assert user.db_instance["first_name"] == "Don"
    assert user.db_instance["last_name"] == "Makila"
    assert user.db_instance["adress"] == "limete kin"
    assert user.db_instance["phone_number"] == "812435265"


# def test_not_db_instance(setup_db):
#     u = User(first_name="Don",
#              last_name="Makila",
#              adress="limete kin",
#              phone_number="812435265")
#     assert u.db_instance() is None


def test__check_phone_number(setup_db):
    user_good = User(first_name="Don",
                     last_name="Makila",
                     adress="limete kin",
                     phone_number="812435265")
    user_bad = User(first_name="Don",
                    last_name="Makila",
                    adress="limete kin",
                    phone_number="etrd")

    with pytest.raises(ValueError) as err:
        user_bad._check_phone_number()

    assert "invalide" in str(err.value)

    user_good.save(validate_data=True)
    assert user_good.exists() is True


def test__check_name_empty(setup_db):
    user_bad = User(first_name="",
                    last_name="",
                    adress="limete kin",
                    phone_number="812435265")

    with pytest.raises(ValueError) as err:
        user_bad._check_name()

    assert "le prénom et le nom de famille ne peuvent pas etre vides" in str(err.value)


def test__check_name_invalid_char(setup_db):
    user_bad = User(first_name="Patr@",
                    last_name="Wi~#",
                    adress="limete kin",
                    phone_number="812435265")

    with pytest.raises(ValueError) as err:
        user_bad._check_name()

    assert "Nom invalide" in str(err.value)


def test_delete(setup_db):
    user_test = User(first_name="Don",
                     last_name="Makila",
                     adress="limete kin",
                     phone_number="812435265")
    user_test.save()
    first = user_test.delete()
    second = user_test.delete()
    assert len(first) > 0
    assert isinstance(first, list)
    assert len(second) == 0
    assert isinstance(second, list)


def test_save(setup_db):
    user_test = User(first_name="Don",
                     last_name="Makila",
                     adress="limete kin",
                     phone_number="812435265")
    user_test_dup = User(first_name="Don",
                         last_name="Makila",
                         adress="limete kin",
                         phone_number="812435265")

    first = user_test.save()
    second = user_test_dup.save()
    assert isinstance(first, int)
    assert isinstance(second, int)

    assert first > 0
    assert second == -1
