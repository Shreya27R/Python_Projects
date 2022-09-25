import datetime


end_time = datatime.datetime(2022,09,26)   #function
site_block = ["www.facebook.com","www.instagram.com"]
host_path = "C:\Windows\System32\drivers\etc"
redirect = "127.0.0.1" #change the slash as forward slach

while True:
    if datetime.datetime.now()< end_time:
        print("start Blocking")
        with open(host_path,"r+") as host_file:
            content = host_file.read()
            for website in site_block:
                if website not in content:
                    host_file.write(redirect + " "+ website+."\n")
                else :
                    pass
    eles:
        with open(host_path, "r+") as host_file:
            content =host_file.readlines()
            host_file.seek(0)
            for lines in content:
                if not any(website in lines for website in site_block):
                    host_file.write(lines)
            host_file.truncate
        time.sleep(5)
