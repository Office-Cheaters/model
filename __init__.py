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

    def request(self, data_file_names, prompt):
                
        input = self.file_to_df(data_file_names)

        # pandas_ai (data, prompt) 형태로 요청
        result = self.pandas_ai(input, prompt)
        
        return result
    
    
    # file들을 df로 변환
    def file_to_df(self, data_file_names):
        
        multiple: bool = isinstance(data_file_names, list)
        
        # 여기는 다양한 format file 처리할 수 있는 함수 만들 예정
        
        if multiple :
            df_list = []
            
            for file in data_file_names :
                # multilple
                df = from_excel(file)
                df_list.append(df)
                
            return df_list
            
            
        else :
            df = from_excel(data_file_names)
            
            return df