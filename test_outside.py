from model import Model

# Model Class 선언
model = Model()

# data랑 prompt 넣고 함수 호출
output = model.request("model/data/Loan payments data.xlsx", '나이 분포를 histogram 그래프로 나타내줘')

print(output)