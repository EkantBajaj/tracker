"""Runner for tracker backend.

Usage:
  run_app.py [options]

  -u --username=<user>                   MySQL username [default: root].
  -p --password=<password>               MySQL password [default: password].
  -d --database=<database>               Mysql database [default: LEDGER_ENGINE]
  -h --host=<host>                       Mysql host [default: localhost]
  -r --use-reloader                      Reload server on code change.
  -P --port=<port>                       Server bind port [default: 8080].
"""

from tracker.db.sql import create_engine,URL,db_session
from docopt import docopt
from tracker.web import create_app
import logging
logging.basicConfig(level=logging.DEBUG)


def run_web_server(port,use_reloader):
    app = create_app()
    logging.info("Server Ready.")
    app.run(use_reloader=use_reloader,port=port,host='0.0.0.0',debug=True)



if __name__ == '__main__':
    arguments = docopt(__doc__)
    db_session.remove()
    engine = create_engine(URL('mysql', arguments["--username"], host=arguments["--host"],
                               password=arguments["--password"],database=arguments["--database"]))
    db_session.configure(bind=engine)

    run_web_server(port=int(arguments["--port"]),
                   use_reloader=arguments["--use-reloader"])