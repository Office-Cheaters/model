from model import Model

# Model Class 선언
model = Model()

# data랑 prompt 넣고 함수 호출
output = model.request("model/data/예제모음.xlsx", '생일이 빠른순으로 정렬해줘')

# # multiple files는 list로
# output = model.request(["model/data/예제모음.xlsx", "model/data/Loan payments data.xlsx"], '각각 엑셀파일에서 생일이 빠른순으로 정렬해줘')

print(output)