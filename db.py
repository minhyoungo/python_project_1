# SingleTone
# ㄴ내부에서 제어 불가능 외부에서 가능

class Person:
    name = ""
    secret_code = ""
    chulcheck = False

    def data_setter(self, p1, p2, p3):
        self.name = p1
        self.secret_code = p2
        self.chul_check = p3

    def c_data_setter(self, c1):
        self.chul_check = c1

    def __str__(self):

        return f"{self.name} | {self.secret_code} | {self.chulcheck}"


class Admin:
    admin_name = ""
    admin_secret_code = ""

    def data_setter(self, p1, p2):
        self.admin_name = p1
        self.admin_secret_code = p2

    def __str__(self):
        return f"{self.admin_name} | {self.admin_secret_code}"
