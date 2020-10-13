def domain_name(url):
    while "https://" in url or "http://" in url or "www." in url:
        url = url.replace("https://", ' ') if "https://" in url else url.replace("http://", ' ') if "http://" in url else url.replace("www.", ' ')
    url = list(url)
    for i in range(len(url)):
        if url[i] == ".":
            return "".join(url[0:i]).strip()
print(domain_name("https://www.codewars.com/kata/514a024011ea4fb54200004b/train/python"))
