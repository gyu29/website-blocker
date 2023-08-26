# Python script to block specified websites by modifying the hosts file
website_to_block = "your-website.com"
redirect_ip = "127.0.0.1"

with open('/etc/hosts', 'a') as hosts_file:
    hosts_file.write(f"\n{redirect_ip} {website_to_block}\n")
