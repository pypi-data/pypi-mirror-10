#!/usr/bin/python
#
# Copyright 2015 Michael Sparks
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

def get_statements(AST):
    statements = []
    if AST[0] == "program":
        assert AST[1][0] == "statements"
        statements = AST[1][1]
    else:
        print AST[0]
    return statements

def todo(*args):
    print "TODO", " ".join([repr(x) for x in args])

def find_variables(AST):
    variables = {}
    statements = get_statements(AST)
    for statement in statements:
        tag, rest = statement[0], statement[1:]
        if tag == "assignment_statement":
            lvalue, assigntype, rvalue = rest
            if assigntype[1] != "=":
                todo("assignment where the assigntype is not '='")
                continue # Skip
            if lvalue[1] != "IDENTIFIER":
                todo("assignment where the lvalue is not an identifier")
                continue # Skip
            if rvalue[0] != "value_literal":
                todo("assignment where the rvalue is not a value_literal")
                continue # Skip

            identifer = lvalue[0]
            v_type = rvalue[2]
            if identifer in variables:
                todo("we could check that the identifier doesn't change type")
                continue # Skip
            variables[identifer] = v_type

    return variables

class UnknownType(Exception):
    pass

class CannotConvert(Exception):
    pass

def python_type_to_c_type(ptype):
    if ptype == "STRING":  return "string"
    if ptype == "NUMBER":  return "int"
    if ptype == "BOOLEAN": return "bool"
    if ptype == "FLOAT":   return "double"
    if ptype == "CHARACTER": return "char"
    raise UnknownType("Cannot identify C Type for %s" % ptype)

def includes_for_ctype(ctype):
    if ctype == "string":  return "<string>"

def includes_for_cstatement(cstatement):
    if cstatement[0] == "print_statement": return "<iostream>"

def crepr_literal(pyliteral):
    assert pyliteral[0] == "value_literal"
    ctype = pyliteral[2]
    if ctype == "STRING":
        return '"' + pyliteral[1] + '"'

    if ctype == "CHARACTER":
        char = pyliteral[1]
        char = char.replace("'","\\'")
        return "'" + char + "'"

    if ctype == "NUMBER":
        return repr(pyliteral[1])
    raise ValueError("Do not not know how to create crepr_literal for " + repr(pyliteral))

def crepr_op(py_op):
    assert py_op[0] == "operator_function"
    func = py_op[1]

    if func == "plus":
        return ["op", "plus"]
    if func == "minus":
        return ["op", "minus"]
    if func == "times":
        return ["op", "times"]
    if func == "divide":
        return ["op", "divide"]
    else:
        todo("Cannot yet convert operators functions other than plus...")
        raise CannotConvert("Cannot yet convert operators functions other than plus...:" + repr(py_op))



def convert_assignment(assignment):
    lvalue, assigntype, rvalue = assignment

    if assigntype[1] != "=":
        todo("Convert Assignment where assigntype is not '='")
        raise CannotConvert("Cannot convert assignment where assigntype is not '='")
    if lvalue[1] != "IDENTIFIER":
        todo("assignment where the lvalue is not an identifier")
        raise CannotConvert("Cannot convert assignment where the lvalue is not an identifier")
    if rvalue[0] != "value_literal":
        todo("assignment where the rvalue is not a value_literal")
        raise CannotConvert("Cannot convert assignment where the rvalue is not a value_literal")

    print rvalue
    lvalue = lvalue[0]
    rvalue = crepr_literal(rvalue)
    return ["assignment", lvalue, "=", rvalue ]

def convert_value_literal(arg):
    print repr(arg), arg
    stype = None
    try:
        tag, value, vtype, line = arg
    except ValueError:
        tag, value, vtype, stype, line = arg
    if vtype == "STRING":
        return ["string",  value]
    if vtype == "NUMBER":
        return ["integer",  value]
    if vtype == "FLOAT":
        return ["double",  value]
    if vtype == "IDENTIFIER":
        return ["identifier",  value]
    if vtype == "BOOLEAN":
        print "VALUE", repr(value), value
        if value == True:
            value = "true"
        else:
            value = "false"
        return ["boolean",  value]

    todo("Cannot handle other value literals")
    raise CannotConvert("Cannot convert value-literal of type" + repr(arg))


def convert_operator_function(arg):
    print "CONVERT - convert_operator_function", repr(arg)
    assert arg[0] == "operator_function"


    func = arg[1]
    arg1 = arg[2]
    arg2 = arg[3]

    crepr_arg1 = convert_arg(arg1)
    crepr_arg2 = convert_arg(arg2)
    print "crepr_arg1", repr(crepr_arg1)
    print "crepr_arg2", repr(crepr_arg2)

    result = crepr_op(arg) + [crepr_arg1, crepr_arg2]
    print repr(result)
    return result

    #todo("Cannot yet convert operator functions")
    #raise CannotConvert("Cannot convert operator function :" + repr(arg))


def convert_arg(arg):
    if arg[0] == "value_literal":
        return convert_value_literal(arg)
    if arg[0] == "operator_function":
        return convert_operator_function(arg)
    else:
        todo("Handle print for non-value-literals")
        raise CannotConvert("Cannot convert print for non-value-literals")

def convert_print(arg_spec):
    print "convert_print(arg_spec)", repr(arg_spec[0]), len(arg_spec[0])
    arg_spec = arg_spec[0]
    cstatement = []
    cargs = []
    print "arg_spec",arg_spec[0]
    for arg in arg_spec:
        print arg[0]
        print "We need to convert the arg", arg
        crepr = convert_arg(arg)
        carg = crepr
        cargs.append(carg)
    return ["print_statement"] + cargs


def convert_statements(AST):
    cstatements = []
    statements = get_statements(AST)
    for statement in statements:
        tag, rest = statement[0], statement[1:]
        try:
            if tag == "assignment_statement":
                cstatement = convert_assignment(rest)
                print cstatement
                cstatements.append(cstatement)
            if tag == "print_statement":
                cstatement = convert_print(rest)
                cstatements.append(cstatement)

        except CannotConvert:
            pass
    return cstatements

def ast_to_cst(program_name, AST):
    cst = {}

    # Extract and handle variables
    pvariables = find_variables(AST)
    cvariables = []
    ctypes = {}
    includes = []
    for name in pvariables:
        ctype = python_type_to_c_type(pvariables[name])
        identifier = [ "identifier", ctype, name ]
        cvariables.append(identifier)
        ctypes[ctype] = True

    cstatements = convert_statements(AST)
    print cstatements

    # Based on variables, update includes
    for ctype in ctypes:
        inc = includes_for_ctype(ctype)
        if inc:
            includes.append(inc)

    # Based on statements, update includes
    for cstatement in cstatements:
        inc = includes_for_cstatement(cstatement)
        if inc:
            includes.append(inc)

    program = {}
    program["name"] = program_name
    program["includes"] = sorted(includes)
    program["main"] = {}
    program["main"]["c_frame"] = {}
    program["main"]["c_frame"]["identifiers"] = cvariables
    program["main"]["c_frame"]["statements"] = cstatements

    return { "PROGRAM" : program }


if __name__ == "__main__":
    AST =   ['program',
             ['statements',
              [['assignment_statement',
                ['first', 'IDENTIFIER', 1],
                ['ASSIGN', '='],
                ['value_literal', 1, 'NUMBER', 'INT', 1]],
               ['assignment_statement',
                ['second', 'IDENTIFIER', 2],
                ['ASSIGN', '='],
                ['value_literal', 2, 'NUMBER', 'INT', 2]],
               ['assignment_statement',
                ['third', 'IDENTIFIER', 3],
                ['ASSIGN', '='],
                ['value_literal', 3, 'NUMBER', 'INT', 3]],
               ['print_statement',
                [['value_literal', 'first', 'IDENTIFIER', 5],
                 ['value_literal', 'second', 'IDENTIFIER', 5],
                 ['value_literal', 'third', 'IDENTIFIER', 5]]],
               ['print_statement',
                [['value_literal', 1, 'NUMBER', 'INT', 6],
                 ['value_literal', 2, 'NUMBER', 'INT', 6],
                 ['value_literal', 'hello', 'STRING', 6]]]]]]

    expect = {
        'PROGRAM': {'includes': ['<iostream>', '<iostream>'],
             'main': {'c_frame': {'identifiers': [['identifier', 'int', 'second'],
                                                  ['identifier', 'int', 'third'],
                                                  ['identifier', 'int', 'first']],
                                  'statements': [['assignment', 'first', '=', '1'],
                                                 ['assignment', 'second', '=', '2'],
                                                 ['assignment', 'third', '=', '3'],
                                                 ['print_statement',
                                                      ['identifier', 'first'],
                                                      ['identifier', 'second'],
                                                      ['identifier', 'third']],
                                                 ['print_statement',
                                                      ["integer", 1],
                                                      ["integer", 2],
                                                      ["string", 'hello']]]}},
             'name': 'hello_world_mixed'}}

    AST = ['program',
           ['statements',
            [['print_statement',
              [['operator_function',
                'plus',
                ['value_literal', 1, 'NUMBER', 'INT', 1],
                ['value_literal', 1, 'NUMBER', 'INT', 1]]]]]]]

    expect = {
        'PROGRAM': {'includes': ['<iostream>'],
             'main': {'c_frame': {'identifiers': [],
                                  'statements': [['print_statement', ['op', 'plus', 
                                                                            ["integer", 1],
                                                                            ["integer", 1]]]
,
                                                ] }},
             'name': 'hello_operators'}}


    actual = ast_to_cst("hello_operators", AST)

    print "actual == expect --->", actual == expect

    import json
    import pprint
    # print json.dumps(actual, indent=4)
    pprint.pprint(actual)
    pprint.pprint(expect)

