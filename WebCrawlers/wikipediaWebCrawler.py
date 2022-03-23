import requests


def getData(title, founded):
    unfounded = []
    url = "https://en.wikipedia.org/w/api.php"
    index = 0
    s = requests.Session()

    params = {
        'action': "parse",
        'page': title,
        'prop': 'sections',
        'format': "json"
    }
    r = s.get(url=url, params=params)
    data = r.json()

    for errorkey in data.keys():
        if "error" != errorkey:
            for x in range(0, len(data["parse"]["sections"])):
                if data["parse"]["sections"][x]["line"] == "See also":
                    index = data["parse"]["sections"][x]["index"]

        if index == 0:
            founded.append(title + " : See also not founded!")
            return

        params = {
            'action': "parse",
            'page': title,
            'prop': 'links',
            'section': index,
            'format': "json"
        }

        r = s.get(url=url, params=params)
        data = r.json()
        for i in range(0, len(data["parse"]["links"])):
            if data["parse"]["links"][i]["*"] not in founded:
                founded.append(data["parse"]["links"][i]["*"])
                unfounded.append(data["parse"]["links"][i]["*"].replace(" ", "_"))
        return unfounded
    else:
        print("Wrong Input")


def findAll(title, founded, i):
    if i == 0:
        return
    else:
        founded.append("\n-----------------" + title + "-----------------")
        unfounded = getData(title, founded)
        if unfounded:
            for x in unfounded:
                findAll(x, founded, i - 1)


def writeToFile(founded, i):
    name = "results" + str(i) + ".txt"
    f = open(name, "w", encoding="utf-8")
    for x in founded:
        f.write(x + '\n')
    f.close()


def printOnScreen(founded):
    for x in founded:
        print(x)


if __name__ == '__main__':
    i = 1
    while True:
        print("Co chcesz wyszukać?")
        title = input().replace(" ", "_")
        founded = []
        print("Jak głęboko? (rekomendowane 2)")
        level = int(input())

        findAll(title, founded, level)
        writeToFile(founded, i)
        i += 1
        printOnScreen(founded)