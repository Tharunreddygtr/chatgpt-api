import openai
import re


def main(input_data=None, error_message=None, function_name=None, error_line=None):
    # Set the API key
    openai.api_key = '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'

    # Define the prompt
    if input_data is not None:
        prompt = input_data + "  " + error_message + "at " + error_line + " function " + function_name + \
                 " fix those errors provide the code after changes "
    else:
        prompt = input('Enter search ')

    # Generate text
    completion = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Get the generated text
    text = completion.choices[0].text
    # lines = text.split("\n")
    # code = ["#" + line if line.startswith(' ') else line for line in lines]
    # code = "\n".join(code)
    code = []
    in_function = False
    in_class = False
    is_variable = False
    # for line in lines:
    #     # check if line starts a function or class definition
    #     if re.match(r"^\s*def\s+", line) or re.match(r"^\s*class\s+", line):
    #         in_function = True
    #         in_class = True
    #     # check if line ends a function or class definition
    #     if re.match(r":\s*$", line):
    #         in_function = False
    #         in_class = False
    #     # check if line is a variable assignment
    #     if re.match(r"^\s*\w+\s*=\s*", line):
    #         in_function = False
    #         in_class = False
    #         is_variable = True
    #     # if not in function or class and not a variable assignment, comment out the line
    #     if not in_function and not in_class and not is_variable:
    #         line = "# " + line
    #     code.append(line)
    # # code = "\n".join(code)
    return text
