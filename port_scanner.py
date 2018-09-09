# Python implementation of a port scanner
import optparse

def pScan(host, ports):
    # Implement actual scanning process
    print(host)
    for p in ports:
        print(p)


def main():
    # Instantiate parser object with two parameters: tgtHost and tgtPort
    parser = optparse.OptionParser(('usage %prog -H <target> -p <port(s) separated by a space>'))
    parser.add_option("-H", dest="tgtHost", type="string", help="specify target Host")
    parser.add_option("-p", dest="tgtPort", type="string", help="specify target port(s) separated by a space")

    # Receive user parameters and store them as tuple
    (options,args) = parser.parse_args()

    # Check for improper user inputs
    if (not options.tgtHost) | (not options.tgtPort):
        print(parser.usage)
        exit(0)

    # Clean user input by stripping white space
    tgtHost = str(options.tgtHost).strip()
    # Strip white spaces and store ports in list
    tgtPorts = [s.strip() for s in str(options.tgtPort).split(' ')]

    pScan(tgtHost, tgtPorts)

if __name__=="__main__":
    main()
