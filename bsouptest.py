import urllib.robotparser
rp = urllib.robotparser.RobotFileParser()
rp.set_url("https://facebook.com/robots.txt")
rp.read()
print(rp.can_fetch("*", "https://www.facebook.com"))
