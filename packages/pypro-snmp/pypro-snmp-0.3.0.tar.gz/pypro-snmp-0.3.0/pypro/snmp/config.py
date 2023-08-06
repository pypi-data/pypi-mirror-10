__author__ = 'teemu kanstren'

#log into mysql? you can use create_db.sql file to create the schema
MYSQL_ENABLED = False
#log directly into elasticsearch (over the network)
ES_NW_ENABLED = False
#log to file using elasticsearch bulk format
ES_FILE_ENABLED = False
#log into a file using CSV format
CSV_ENABLED = True
#print log data to console (CSV/ES only)
PRINT_CONSOLE = False
KAFKA_ENABLED = True

#elasticsearch server host address
ES_HOST = "localhost"
#elasticsearch host server port
ES_PORT = 9200

#name of the data collection session
SESSION_NAME = "session"
SESSION_ID = 1
#name of the elasticsearch index to write logs into
DB_NAME = "my_database"

KAFKA_SERVER = "localhost:9092"
KAFKA_TOPIC = "pypro"
#target of measurement identifier
TOM = "host1"

#polling interval. this is the time the poller sleeps between reading and writing values.
INTERVAL = 1

SNMP_OIDS = []
SNMP_AUTH = False
SNMP_USER = 'my_user'
SNMP_PASS = 'my_pass'
SNMP_PRIVKEY = 'my_priv_key'
SNMP_AUTH_PROTO = 'SHA'
SNMP_PRIV_PROTO = 'AES'