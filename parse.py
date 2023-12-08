def parse_args(args, argc):
    port_num = ""
    origin_server = ""
    cdn = ""
    user = ""
    key = ""
    for i in range(0, argc-1):
        if args[i] == '-p':
            port_num = args[i+1]
        elif args[i] == '-o':
            origin_server = args[i+1]
        elif args[i] == '-n':
            cdn = args[i+1]
        elif args[i] == '-u':
            user = args[i+1]
        elif args[i] == '-i':
            key = args[i+1]

    if port_num == "" or origin_server == "" or cdn == "" or user == "" or key == "":
        print("Usage: ./[deploy][run][stop]CDN -p <port> -o <origin> -n <name> -u <username> -i <keyfile>")
        exit(1)

    return port_num, origin_server, cdn, user, key

