class Post:
    # 게시글 클래스
    def __init__(self, date, content):
        # 게시글은 속성으로 작성 날짜와 내용을 갖는다
        self.date = date
        self.content = content

    def __str__(self):
        # 게시글의 정보를 문자열로 리턴하는 메소드
        return "작성 날짜: {}\n내용: {}".format(self.date, self.content)
    
    
class BlogUser:
    # 블로그 유저 클래스
    def __init__(self, name):
        self.name = name
        self.posts = []

    def add_post(self, date, content):
        new_post = Post(date, content)
        self.posts.append(new_post)

    def show_all_posts(self):
        for post in self.posts:
            print(post)

    def __str__(self):
        return f"안녕하세요 {self.name}입니다.\n"

blog_user_1 = BlogUser("성태호")

print(blog_user_1)

blog_user_1.add_post("2019년 8월 30일", """
오늘은 내 생일이였다.
많은 사람들이 축하해줬다.
행복했다.
""")

blog_user_1.add_post("2019년 8월 31일", """
재밌는 코딩 교육 사이트를 찾았다.
코드잇이란 곳인데 최고다.
같이 공부하실 분들은 www.codeit.kr로 오세요!
""")

# 블로그 유저의 모든 게시글 출력
blog_user_1.show_all_posts()