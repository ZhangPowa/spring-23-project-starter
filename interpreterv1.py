from intbase import InterpreterBase
from bparser import BParser


class Interpreter(InterpreterBase):
    def __init__(self, console_output=True, inp=None, trace_output=False):
        super().__init__(console_output, inp)   # call InterpreterBase’s constructor

    def run(self, program):
        result, parsed_program = BParser.parse(program_source)
        if result == False:
            return  # error
        self.__discover_all_classes_and_track_them(parsed_program)
        class_def = self.__find_definition_for_class("main")
        obj = class_def.instantiate_object()
        obj.run_method("main")


class ClassDefinition:
    def __init__(self, ...):

    def instantiate_object(self):
        obj = ObjectDefinition()
        for method in self.my_methods:
            obj.add_method(method)
        for field in self.my_fields:
            obj.add_filed(field.name(), filed.initial_value())
        return obj


class ObjectDefinition:
    def __init__(self, ...):

    def call_method(self, method_name, parameters):
        method = self.__find__method(method_name)
        statement = method.get_top_level_statement()
        result = self.__run_statement(statement)
        return result

    def __run_statement(self, statement):
    if is_a_print_statement(statement):
        result = self.__execute_print_statement(statement)
    elif is_an_input_statement(statement):
        result = self.__execute_input_statement(statement)
    elif is_a_call_statement(statement):
        result = self.__execute_call_statement(statement)
    elif is_a_while_statement(statement):
        result = self.__execute_while_statement(statement)
    elif is_an_if_statement(statement):
        result = self.__execute_if_statement(statement)
    elif is_a_return_statement(statement):
        result = self.__execute_return_statement(statement)
    elif is_a_begin_statement(statement):
        result = self.__execute_all_sub_statements_of_begin_statement(
            statement)
   …
   return result
