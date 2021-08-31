import pymongo
from connect_db import get_database_connection

DB_NAME = "contracts"
COLLECTION = "contracts"


def delete_data_from_db():
    """
    Delete selected data from database.
    Note that pymongo doesn't support sql scripts.

    execute the given sql statement to remove
    the extra data
    """

    sql_query = ''' DELETE FROM authors WHERE (author='Smith, Jackson' AND pages=400); '''

    db = get_database_connection()
    contracts = db[COLLECTION]

    res = contracts.delete_many({"author": "Smith, Jackson", "pages": "400"})
    print(res.deleted_count, "documents deleted.")


def update_data():
    """ Update the selected data.

    execute the given sql statement to
    correct the due date of the entry
    """
    sql_query = ''' UPDATE authors SET due_date='2020-10-31' WHERE author='Smith, Jackson'; '''

    db = get_database_connection()

    contracts = db[COLLECTION]

    res = contracts.update_many({"author": "Smith, Jackson"}, {"$set": {"due_date": "2020-10-31"}})
    print(res.modified_count, "documents updated.")


def test_delete_data():
    sql_query = ''' SELECT count(author) FROM authors WHERE author='Smith, Jackson'; '''

    # make connection to db
    db = get_database_connection()

    contracts = db[COLLECTION]
    results = list()

    # find all documents with "Smith, Jackson" as the author
    for contract in contracts.find({"author": "Smith, Jackson"}):
            results.append(contract)
    assert len(results) == 1, "the number of Smith Jackson rows is incorrect"


def test_update_data():
    sql_query = ''' SELECT due_date FROM authors WHERE author='Smith, Jackson'; '''

    # make connection to db
    db = get_database_connection()

    contracts = db[COLLECTION]
    results = list()

    # find all documents with "Smith, Jackson" as the author
    for contract in contracts.find({"author": "Smith, Jackson"}):
            results.append(contract)

    assert results[0]["due_date"] == "2020-10-31", "due date not updated correctly"


def main():
    delete_data_from_db()
    test_delete_data()
    update_data()
    test_update_data()


if __name__ == "__main__":
    main()