'''
Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

domain_name("http://github.com/carbonfive/raygun") == "github" 
domain_name("http://www.zombie-bites.com") == "zombie-bites"
domain_name("https://www.cnet.com") == "cnet"
'''


def domain_name(url:str):
    startList = ('https://www.','http://www.','http://','https://','www.',"")
    # if url.startswith(startList):
    for item in startList:
        if url.startswith(item):
            temp = url[len(item):]
            b = temp.find('.')
            # print(temp[:b])
            return temp[:b]
        
a = "https://www.google.com"
domain_name(a)
# print(a.find('.'))