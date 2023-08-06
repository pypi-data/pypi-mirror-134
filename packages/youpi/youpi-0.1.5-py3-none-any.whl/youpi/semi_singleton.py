 #  한 YouTube객체에서 생성된 Stream 객체가 공유하는 유사 싱글톤 클래스
class SemiSingleton:
    def __init__(self, title: str):
        self.title = title