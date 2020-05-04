class UserName:
    def __init__(self, name):
        if not (4 <= len(name) <= 20):
            raise ValueError(f'{name}は文字数のルール違反！やで')

        self.name = name

    def screen_name(self):
        return self.name.upper()


# UserNameクラスのインスタンス化
hibiki = UserName(name='hibiki')

# print(hibiki)
# print(type(hibiki))
# print(hibiki.name)

# sho = UserName('sho')
# print(sho.name)
print(hibiki.screen_name())
