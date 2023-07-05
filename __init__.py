from .pandasai import PandasAI
import os

# input data가 .xlsx로 끝나면 from_excel 함수 사용 (그 이외 format도 계속 추가해나갈 예정)
from pandasai.helpers.from_excel import from_excel

class Model:
    def __init__(self):
        
        # 보안을 위해 api_key.txt는 따로 보관
        api_key_file = os.path.join(os.path.dirname(__file__), "api_key.txt")
        
        with open(api_key_file, 'r') as file:
            api_token = file.read()

        # Instantiate a LLM
        from pandasai.llm.openai import OpenAI

        self.llm = OpenAI(api_token = api_token)

        # Load llm to PandasAI
        self.pandas_ai = PandasAI(self.llm, save_charts=True, verbose=True)

    def request(self, data_file_name, prompt):
        
        # 여기는 다양한 format file 처리할 수 있는 함수 만들 예정
        df = from_excel(data_file_name)

        # pandas_ai (data, prompt) 형태로 요청
        result = self.pandas_ai(df, prompt)

        # Print result and type
        print("Result : \n", result, "\n")
        print("Type : \n", type(result), "\n")
        
        return result