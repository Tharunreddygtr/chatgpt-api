import gpt_api
import traceback
import sys
import inspect


# fix errors which caught in the raise exception

def main(error, filename, function, line_no):
    with open(filename, 'r', encoding='utf-8') as f:
        code = f.read()
    start_index = code.index(f'def {function}(')
    end_index = code.index('\n', start_index) + 1
    indent_level = len(code[start_index:end_index]) - len(code[start_index:end_index].lstrip())
    end_index = start_index
    while True:
        try:
            next_line_start = end_index + 1
            end_index = code.index('\n', next_line_start) + 1
        except ValueError:
            break
        next_line = code[next_line_start:end_index].lstrip()
        if next_line == '' or len(next_line) - len(next_line.lstrip()) < indent_level:
            break

    extracted_function = code[start_index:end_index]
    changed_code = gpt_api.main(code, error, function, str(line_no))

    try:
        exec(changed_code)
        code = code[:start_index] + changed_code.replace("\n\n\n", '') + '\n'*3 + code[end_index:]
        with open(filename, 'w') as f:
            f.write(code)
    except Exception as er:
        print(str(er))
        # main(str(er), filename, function)


try:
    import image

except Exception as e:
    tb = traceback.extract_tb(sys.exc_info()[2])
    file_name, line_number, function_name, text = tb[-1]
    if file_name != inspect.getframeinfo(inspect.currentframe()).filename:
        main(str(e), file_name, function_name, line_number)
