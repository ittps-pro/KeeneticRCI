from requests import Session
from hashlib  import md5, sha256

class router:
    def __init__(self, user:str="admin", password:str="1234", ip:str="192.168.1.1"):
        self.__session = Session()
        self.__guiURL = f"http://{ip}"
        self.__authURL = f"{self.__guiURL}/auth"
        self.__rciURL = f"{self.__guiURL}/rci"

        self._auth   = self.__authenticate(user, password)
        if not self._auth:
            assert False, "Unauthorized access."

    def __authenticate(self, user:str, password:str) -> bool:
        r = self.__session.get(self.__authURL)
        if r.status_code == 200:
            return True

        device = r.headers["X-NDM-Realm"]
        token = r.headers["X-NDM-Challenge"]

        __password = f"{user}:{device}:{password}"
        __password = md5(__password.encode("utf-8")).hexdigest()
        __password = f"{token}{__password}"
        __password = sha256(__password.encode("utf-8")).hexdigest()

        r = self.__session.post(
            url  = self.__authURL,
            json = {"login":user, "password":__password}
        )

        return r.status_code == 200

    command = "show ip neighbour"

    def run(self, command:str="show version"):
        # Parse command and create URL path
        urlPath = ""
        for argument in command.split(" "):
            urlPath = urlPath + "/" + argument

        return self.__session.get(self.__rciURL + urlPath).json()