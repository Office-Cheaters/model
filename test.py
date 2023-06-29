from pandasai import PandasAI

# 보안을 위해 api_key.txt는 따로 보관
with open('api_key.txt', 'r') as file:
    api_token = file.read()

# Instantiate a LLM
from pandasai.llm.openai import OpenAI

llm = OpenAI(api_token = api_token)

# Load llm to PandasAI
pandas_ai = PandasAI(llm)



# input data가 .xlsx로 끝나면 from_excel 함수 사용 (그 이외 format도 계속 추가해나갈 예정)
from pandasai.helpers.from_excel import from_excel

df = from_excel("data/Loan payments data.xlsx")

# pandas_ai (data, prompt) 형태로 요청
result = pandas_ai(df, prompt='이 사람들의 학력을 정리해서 표로 만들어줘')

# Print result and type
print("Result : \n", result, "\n")
print("Type : \n", type(result), "\n")