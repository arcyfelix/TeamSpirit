from flask_restplus import reqparse

class RequestParser(object):
    def __init__(self):
        self.parser = reqparse.RequestParser()

    def parse_parameters_from_array_all_required(self, parameter_array):
        for parameter in parameter_array:
            self.parser.add_argument(parameter, 
                                     type = str, 
                                     location = 'args',
                                     required = True)
        args = self.parser.parse_args()
        return args