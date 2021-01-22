import dataset
import mvc_exceptions as mvc_exc
from sqlalchemy.exc import IntegrityError, NoSuchTableError

DB_NAME = 'test_db'

def create_table(conn, table_name):
    """Load a table or create it if it doesn't exist yet.


    Parameters
    ----------
    table_name : str
    conn : dataset.persistence.database.Database
    """
    try:
        conn.load_table(table_name)
    except NoSuchTableError as e:
        print('Table {} does not exist. It will be created now'.format(e))
        conn.get_table(table_name, primary_id='id', primary_type='int')
        print('Created table {} on database {}'.format(table_name, DB_NAME))

def insert_many(conn, items, table_name):
    """Insert all items in a table.

    Parameters
    ----------
    items : list
        list of dictionaries
    table_name : str
    conn : dataset.persistence.database.Database
    """
    table = conn.load_table(table_name)
    try:
        table.insert("CREATE TABLE currency_exchange_new(dt text, from_currency text, from_amount text, to_currency text, to_amount text, rate text);")
    except IntegrityError as e:
        print('At least one in {} was already stored in table "{}".\nOriginal '
              'Exception raised: {}'
              .format([x['dt'] for x in items], table.table.name, e))



def insert_many(conn, items, table_name):
    """Insert all items in a table.

    Parameters
    ----------
    items : list
        list of dictionaries
    table_name : str
    conn : dataset.persistence.database.Database
    """
    # TODO: check what happens if 1+ records can be inserted but 1 fails
    table = conn.load_table(table_name)
    try:
        for x in items:
            table.insert(dict(
                dt=x['dt'], from_currency=x['from_currency'], from_amount=x['from_amount'], to_currency=x['to_currency'], rate=x['rate']))
    except IntegrityError as e:
        print('At least one in {} was already stored in table "{}".\nOriginal '
              'Exception raised: {}'
              .format([x['dt'] for x in items], table.table.name, e))


def select_one(conn, name, table_name):
    """Select a single item in a table.

    The dataset library returns a result as an OrderedDict.

    Parameters
    ----------
    name : str
        name of the record to look for in the table
    table_name : str
    conn : dataset.persistence.database.Database

    Raises
    ------
    mvc_exc.ItemNotStored: if the record is not stored in the table.
    """
    table = conn.load_table(table_name)
    row = table.find_one(name=name)
    if row is not None:
        return dict(row)
    else:
        raise mvc_exc.ItemNotStored(
            'Can\'t read "{}" because it\'s not stored in table "{}"'.format(name, table.table.name))

#Read
def select_all(conn, table_name):
    """Select all items in a table.

    The dataset library returns results as OrderedDicts.

    Parameters
    ----------
    table_name : str
    conn : dataset.persistence.database.Database

    Returns
    -------
    list
        list of dictionaries. Each dict is a record.
    """
    table = conn.load_table(table_name)
    rows = table.all()
    return list(map(lambda x: dict(x), rows))

class UnsupportedDatabaseEngine(Exception):
    pass


def connect_to_db(db_name=None, db_engine='postgres'):
    """Connect to a database. Create the database if there isn't one yet.

    The database is PostgreSQL DB. In order to connect to a PostgreSQL DB you have first to create a database, create a user, and finally grant him all necessary privileges on that database and tables.
    'postgresql://<username>:<password>@localhost:<PostgreSQL port>/<db name>'
    Parameters
    ----------
    db_name : str or None
        database name
    db_engine : str
        database engine ('postgres')

    Returns
    -------
    dataset.persistence.database.Database
        connection to a database
    """

    if db_engine == 'postgres':
            db_string = \
                'postgresql://test_user:test_password@localhost:5432/{}'.format(DB_NAME)
            print('New connection to PostgreSQL DB...')
    else:
            raise UnsupportedDatabaseEngine(
                'No database engine with this name. '
                'Choose one of the following: {}'.format(db_engine))

    return dataset.connect(db_string)



def main():

    conn = connect_to_db(db_name='test_db', db_engine='postgres')
    table_name = 'currency_exchange_'
    create_table(conn, table_name)

    # CREATE
    my_items = [
        {'dt': '2012021', 'from_currency': 'USD', 'from_amount': '2', 'to_currency': 'EUR', 'to_amount': '5',
         'rate': '1 usd = 0.9 eurr'},
        {'dt': '1912021', 'from_currency': 'USD', 'from_amount': '2', 'to_currency': 'EUR', 'to_amount': '5',
         'rate': '1 usd = 0.9 eurr'},
        {'dt': '2112021', 'from_currency': 'USD', 'from_amount': '2', 'to_currency': 'EUR', 'to_amount': '5',
         'rate': '1 usd = 0.9 eurr'},
    ]

    insert_many(conn, items=my_items, table_name=table_name)
    # if we try to insert an object already stored we get an ItemAlreadyStored exception

    # READ
    print('SELECT all')
    print(select_all(conn, table_name=table_name))


if __name__ == '__main__':
    main()