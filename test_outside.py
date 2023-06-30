from model import Model

# Model Class 선언
model = Model()

# data랑 prompt 넣고 함수 호출
output = model.request("model/data/Loan payments data.xlsx", '이 사람들의 학력을 그래프로 만들어줘')