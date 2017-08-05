
import telnetlib
import time

USER = 'pyclass'
PASS = '88newclass'
IP_ADDR = 'cisco1.twb-tech.com'

TELNET_PORT = 23
TELNET_TIMEOUT = 5

def main():
    remote_conn = telnetlib.Telnet(IP_ADDR, TELNET_PORT, TELNET_TIMEOUT)

    output = remote_conn.read_until( 'rname', TELNET_TIMEOUT)
    print output
    remote_conn.write(USER + '\n')
    output = remote_conn.read_until('sword', TELNET_TIMEOUT)
    print output
    remote_conn.write(PASS + '\n')


    remote_conn.write( 'show ip int br' + '\n')
    time.sleep(1)
    output = remote_conn.read_very_eager()
    print output
    remote_conn.close()



if __name__ == '__main__':
    main()