from src.inference import BaseInference
from src.message import BaseMessage,AIMessage

class LLMSwitcher(BaseInference):
    def __init__(self, llms:list[BaseInference]=[],max_retries:int=3):
        self.llms = llms
        self.current_llm_index = 0
        self.max_retries = max_retries

    def switch_llm(self):
        self.current_llm_index = (self.current_llm_index + 1) % len(self.llms)
    
    @property
    def current_llm(self):
        return self.llms[self.current_llm_index]

    def invoke(self, messages:list[BaseMessage],json:bool=False)->AIMessage|RuntimeError:
        retries=0
        while retries<self.max_retries:
            current_llm = self.current_llm
            try:
                return current_llm.invoke(messages=messages,json=json)
            except Exception as e:
                print(f"Error with {current_llm.__class__.__name__}: {e}")
                self.switch_llm()
                retries+=1
        raise RuntimeError("All LLM's failed after maximum retries")
    
    def stream(self, messages:list[BaseMessage],json:bool=False):
        retries=0
        while retries<self.max_retries:
            current_llm = self.current_llm
            try:
                return current_llm.stream(messages=messages,json=json)
            except Exception as e:
                print(f"Error with {current_llm.name}: {e}")
                self.switch_llm()
                retries+=1
        raise RuntimeError("All LLM's failed after maximum retries")
