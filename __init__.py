from .pandasai import PandasAI
import os
import uuid

import pandas as pd

class Model:
    def __init__(self, private = False):
        
        # 보안을 위해 api_key.txt는 따로 보관
        api_key_file = os.path.join(os.path.dirname(__file__), "api_key.txt")
        
        with open(api_key_file, 'r') as file:
            api_token = file.read()

        # Instantiate a LLM
        from pandasai.llm.openai import OpenAI

        self.llm = OpenAI(api_token = api_token)

        # Load llm to PandasAI
        self.pandas_ai = PandasAI(self.llm, save_charts=True, verbose=True, enforce_privacy = private)

    def request(self, data_file_names, prompt, output_format=None):
                
        input = self.files_to_input(data_file_names)

        # pandas_ai (data, prompt) 형태로 요청
        result = self.pandas_ai(input, prompt, output_format=output_format)
        
        return result
    
    
    # file들을 df로 변환
    def files_to_input(self, data_file_names):
        
        multiple: bool = isinstance(data_file_names, list)
        
        # 여기는 다양한 format file 처리할 수 있는 함수 만들 예정
        
        if multiple :
            df_list = []
            
            for file in data_file_names :
                # multilple
                df = self.file_to_df(file)
                df_list.append(df)
                
            return df_list
            
            
        else :
            df = self.file_to_df(data_file_names)
            
            return df
        
    def file_to_df(self, file_name):
        
        ext = os.path.splitext(file_name)[1]
        # ('data_name', '.xlsx')

        file_format = {
            ".csv": pd.read_csv,
            ".xls": pd.read_excel,
            ".xlsx": pd.read_excel,
            ".xlsm": pd.read_excel,
            ".xlsb": pd.read_excel,
            ".json": pd.read_json,
            ".html": pd.read_html,
            ".sql": pd.read_sql,
            ".feather": pd.read_feather,
            ".parquet": pd.read_parquet,
            ".dta": pd.read_stata,
            ".sas7bdat": pd.read_sas,
            ".h5": pd.read_hdf,
            ".hdf5": pd.read_hdf,
            ".pkl": pd.read_pickle,
            ".pickle": pd.read_pickle,
            ".gbq": pd.read_gbq,
            ".orc": pd.read_orc,
            ".xpt": pd.read_sas,
            ".sav": pd.read_spss,
            ".gz": pd.read_csv,
            ".zip": pd.read_csv,
            ".bz2": pd.read_csv,
            ".xz": pd.read_csv,
            ".txt": pd.read_csv,
            ".xml": pd.read_xml,
        }
        
        assert ext in file_format, "Unsupported file format."
        
        df = file_format[ext](file_name)
        return df