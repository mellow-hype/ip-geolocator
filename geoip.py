### IP to geolocation module
import sys, getopt
import geoip2.database


def main(argv):
    database = ''
    target = ''
    try:
        opts, args = getopt.getopt(argv,"hi:t:",["database=","target_ip="])
    except getopt.GetoptError:
        print('geoip.py -i </path/to/database> -t <target_ip>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('geoip.py -i <database> -t <target_IP>')
            sys.exit()
        elif opt in ("-i", "--database"):
            database = arg
            reader = geoip2.database.Reader(database)
        elif opt in ("-t", "--target_ip"):
            target = arg
            response = reader.city(target)

            print("IP: " + target + "\nCity: " + response.city.name +\
                    "\nCountry: " + response.country.name + "\n")
                
            reader.close()
        
if __name__ == "__main__":
   main(sys.argv[1:])
