import requests
file="domains.txt"
fh=open(file,"r")
websites = []
for each in fh.readlines():
    websites.append(each.strip("\n"))
print "<---------------Checking for Subdomain and Cloudfront Takeovers--------------->"
for i in websites:
    r=requests.get(i)
    if "NoSuchBucket" in r.content:
        print "Subdomain takeover possible:"+" "+i
    elif "Generated by cloudfront" in r.content:
        print "CloudFront takeover possible:"+" "+i
    else:
        print "Access Denied:"+" "+i
fh.close()
