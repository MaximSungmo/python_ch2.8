# class point

class Point:

    count_of_instance = 0

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y= y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def show(self):
        print(f'점[{self.x}, {self.y}] 를 그렸습니다.')

# 어노테이션을 통해서 호출 방식이 변경됨
    @classmethod
    def class_method(cls):
        return cls.count_of_instance

# 어노테이션을 통해 스태틱 함수를 정의함
    @staticmethod
    def static_method():
        print('static method called')

