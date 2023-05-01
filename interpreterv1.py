from intbase import InterpreterBase
from bparser import BParser


class Interpreter(InterpreterBase):
    def __init__(self, console_output=True, inp=None, trace_output=False):
        super().__init__(console_output, inp)   # call InterpreterBase’s constructor

    def run(self, program):
        result, parsed_program = BParser.parse(program)
        if result == False:
            return  # error
        for class_def in parsed_program:
            class_name = class_def[1]
            class_methods = []
            class_fields = []
            for item in class_def[2:]:
                if item[0] == 'field':
                    field_name, initial_value = [item[1:]]
                    class_fields.append(FieldDefinition(
                        field_name, initial_value))
                elif item[0] == 'method':
                    method_name = item[1]
                    params = item[2]
                    statements = item[3]
                    class_methods.append(MethodDefinition(
                        method_name, params, statements))
        new_class_def = ClassDefinition(
            class_name, class_methods, class_fields)
        obj_def = new_class_def.instantiate_object()
        obj_def.call_method("main", [])
        # self.__discover_all_classes_and_track_them(parsed_program)
        # class_def = self.__find_definition_for_class("main")
        # obj = class_def.instantiate_object()
        # obj.run_method("main")


class FieldDefinition:
    def __init__(self, field_name, initial_value):
        self.field_name = field_name
        self.initial_value = initial_value


class MethodDefinition:
    def __init__(self, method_name, params, statements):
        self.method_name = method_name
        self.params = params
        self.statements = statements

    def get_top_level_statement(self):
        return self.statements


class ClassDefinition:
    def __init__(self, name, methods, fields):
        self.name = name
        self.methods = methods
        self.fields = fields

    def add_method(self, method_def):
        self.methods.append(method_def)

    def add_field(self, field_def):
        self.fields = field_def

    def instantiate_object(self):
        obj = ObjectDefinition()
        for method in self.methods:
            obj.add_method(method)
        for field in self.fields:
            obj.add_field(field)
        return obj

    #        obj.add_filed(field.name(), filed.initial_value())


class ObjectDefinition:
    def __init__(self):
        self.methods = {}
        self.fields = {}

    def add_field(self, field_name, initial_value):
        self.fields[field_name] = initial_value

    def add_method(self, method):
        self.methods[method.method_name] = method

    def call_method(self, method_name, parameters):
        method = self.methods[method_name]
        statement = method.get_top_level_statement()
        result = self.__run_statement(statement, parameters)
        return result

    def __run_statement(self, statement, parameters):
        result = None
        if statement[0] == 'print':
            result = self.__execute_print_statement(statement, parameters)
        return result

    def __execute_print_statement(self, statement, parameters=None):
        expression = Expression(statement[1])
        value = expression.evaluate_expression(parameters)
        print(value)
        return value


# class PrintDefinition:
 #   def __init__(self, expression):
  #      self.expression = expression

   # def evaluate_expression(self):
    #    return self.expression.evaluate()


class Expression:
    def __init__(self, value):
        self.value = value

    def evaluate_expression(self, parameters):
        try:
            return int(self.value)
        except ValueError:
            if self.value in parameters:
                return parameters[self.value]
            else:
                return str(self.value)


'''
class PrintDefinition:
    def __init__(self, expr):
        self.expr = expr

    def execute(self):
        print(self.expr.evaluate())


class Expr:
    def __init__(self, value):
        self.value = value

    def evaluate(self):
        try:
            return int(self.value)
        except ValueError:
            return str(self.value)


a = Expr("A")
b = PrintDefinition(a)
b.execute()


'''


print_src = ['(class main',
             ' (method main ()',
             ' (print "hello world!")',
             ' ) # end of method',
             ') # end of class']

test = Interpreter()
test.run(print_src)
