__author__ = 'teemu kanstren'

import pypro.snmp.config as config
from pypro.snmp.oid import OID
import pypro.snmp.main as main

config.ES_NW_ENABLED = False
config.ES_FILE_ENABLED = False
config.CSV_ENABLED = True
config.KAFKA_ENABLED = False
config.KAFKA_TOPIC = "asus"
config.KAFKA_SERVER = "192.168.2.153"
config.PRINT_CONSOLE = True
#raw user space cpu time
config.SNMP_OIDS.append(OID('1.3.6.1.4.1.2021.11.50.0', 'user cpu time', 'public', '192.168.2.1', 161, 'router', True))
#percentage of user space cpu time
config.SNMP_OIDS.append(OID('.1.3.6.1.4.1.2021.11.9.0', 'percentage user cpu time', 'public', '192.168.2.1', 161, 'router', True))
#raw system cpu time
config.SNMP_OIDS.append(OID('1.3.6.1.4.1.2021.11.52.0', 'system cpu time', 'public', '192.168.2.1', 161, 'router', True))
#percentage of system time
config.SNMP_OIDS.append(OID('1.3.6.1.4.1.2021.11.10.0', 'percentage system cpu time', 'public', '192.168.2.1', 161, 'router', True))
#raw idle cpu time
config.SNMP_OIDS.append(OID('.1.3.6.1.4.1.2021.11.53.0', 'idle cpu time', 'public', '192.168.2.1', 161, 'router', True))
#percentage of idle time
config.SNMP_OIDS.append(OID('.1.3.6.1.4.1.2021.11.11.0', 'percentage idle cpu time', 'public', '192.168.2.1', 161, 'router', True))
#total ram used
config.SNMP_OIDS.append(OID('.1.3.6.1.4.1.2021.4.6.0', 'total RAM used', 'public', '192.168.2.1', 161, 'router', True))
#total ram free
config.SNMP_OIDS.append(OID('.1.3.6.1.4.1.2021.4.11.0', 'total RAM free', 'public', '192.168.2.1', 161, 'router', True))
#available disk space, requires modifying snmp config on host
config.SNMP_OIDS.append(OID('.1.3.6.1.4.1.2021.9.1.7.1', 'available disk space', 'public', '192.168.2.1', 161, 'router', True))
#used disk space, requires modifying snmp.config on host
config.SNMP_OIDS.append(OID('.1.3.6.1.4.1.2021.9.1.8.1', 'used disk space', 'public', '192.168.2.1', 161, 'router', True))
#bytes in (network interface 1, the last number..)
config.SNMP_OIDS.append(OID('.1.3.6.1.2.1.2.2.1.10.1', 'nw bytes in if 1', 'public', '192.168.2.1', 161, 'router', True))
#bytes out (network interface 1, the last number..)
config.SNMP_OIDS.append(OID('.1.3.6.1.2.1.2.2.1.16.1', 'nw bytes out if 1', 'public', '192.168.2.1', 161, 'router', True))

main.run_poller()
