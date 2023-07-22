from src.models.parameter import Parameter

class ParameterManager:
    def __init__(self):
        self.parameters = {}  # Key: parameter ID, value: Parameter instance

    def create_parameter(self, id: int, name: str, definition: str = ""):
        parameter = Parameter(id, name, definition)
        self.parameters[id] = parameter
        return parameter

    def get_parameter(self, id: int):
        return self.parameters.get(id)

    def update_parameter(self, id: int, name: str = None, definition: str = None):
        parameter = self.get_parameter(id)
        if parameter is None:
            return None  # No parameter with this ID exists

        if name is not None:
            parameter.name = name
        if definition is not None:
            parameter.definition = definition

        return parameter

    def delete_parameter(self, id: int):
        return self.parameters.pop(id, None)