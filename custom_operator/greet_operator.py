from airflow.models.baseoperator import BaseOperator

class GreetOperator(BaseOperator):
    def __init__(self, msg: str, **kwargs) -> None:
        super().__init__(**kwargs)
        self.msg = msg

    def execute(self, context):
        message = f"Greetings: {self.msg}"
        print(message)
        return message