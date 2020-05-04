"""
class(成人の)bim
関連しそうな属性：
-身長
-体重
-bmiという値そのもの
ルール：
-10以上40以下（常識的な範囲）
-表示する時は、小数点第2位まで
できること：
？？？？
"""


# クラス名はUpperCamaelCaseが普通
class BMI:
    def __init__(self, height, weight):
        self.value = weight / (height ** 2)

        if not (10 <= self.value <= 40):
            raise ValueError('BMIが正常値の範囲を超えています。')

    def __str__(self):
        return f'{self.value:.2f}'


# BMIクラスのインスタンス(実体)化
hibiki_bmi = BMI(height=1.80, weight=67.0)
noriya_bmi = BMI(height=1.78, weight=75.0)

print('hibiki')
print(hibiki_bmi)
