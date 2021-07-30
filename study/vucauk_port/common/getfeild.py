import requests


def get_field(base_url, data):
    return requests.post(url=base_url+"/code/getFileId", files={"file": data})


if __name__ == '__main__':
    response = get_field("http://rdt.vucauk.com", "../data/companymoment.html")
    print(response.text)
