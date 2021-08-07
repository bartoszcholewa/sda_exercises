import re
def domain_name(url):
    pattern = re.compile(r'((https?://)?(www\.)?)([a-zA-Z0-9-]+)(\.\w+)')
    subbed_urls = pattern.sub(r'\4', url)
    print(subbed_urls)
    # matches = pattern.finditer(url)
    # for match in matches:
    #     print(match.group(4))

    #subbed_urls = pattern.sub(r'\4', url)
    #print(subbed_urls)

urls = (
    "http://google.com",
    "http://google.co.jp",
    "www.xakep.ru",
    "https://youtube.com",
    "https://hyphen-site.org",
)
results = map(domain_name, urls)
for result in results:
    if result:
        print(result)