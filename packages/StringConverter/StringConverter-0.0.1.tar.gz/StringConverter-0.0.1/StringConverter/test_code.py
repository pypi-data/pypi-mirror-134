from StringConverter import intStringConverter


def run_test_0():
    # - 10 - +10
    Test_case_0 = [-5, -3, - 1, 0, 1, 4, 5, 7, 8, 9]
    expected_out0 = ["negative five.", "negative three.", "negative one.", "zero.", "one.", "four.", "five.", "seven.", "eight.",
                     "nine."]
    output = []
    for num_input, expected_0 in zip(Test_case_0, expected_out0):
        curr_out = intStringConverter.intConverter(num_input).lower()
        assert curr_out == expected_0.lower(), f"Failed at Test 0 - expected {expected_0}, got {curr_out}"


def run_test_1():
    # -1000 - + 1000
    Test_case_1 = [-978, -777, - 525, -300, -78, 56, 120, 303, 450, 981]
    expected_out1 = ["negative nine hundred and seventy eight.", "negative seven hundred and seventy seven.",
                     "negative five hundred and twenty five.",
                     "negative three hundred.", "negative seventy eight.", "fifty six.", "One hundred and twenty.",
                     "Three hundred and three.",
                     "four hundred and fifty.", "nine hundred and eighty one."]
    for num_input, expected_1 in zip(Test_case_1, expected_out1):
        curr_out = intStringConverter.intConverter(num_input).lower()
        assert curr_out == expected_1.lower(), f"Failed at Test 1 - expected {expected_1}, got {curr_out}"


def run_test_2():
    # large numbers with zeros
    Test_case_2 = [1000000, 20000000, 20050000, 4823000000, 12000000000000, 210948040000]
    expected_out2 = ["One Million.", "Twenty Million.", "Twenty Million and Fifty Thousand.",
                     "four billion and eight hundred and twenty three million.", "twelve trillion.",
                     "two hundred and ten billion, nine hundred and forty eight million and forty thousand."]
    output = []
    for num_input, expected_2 in zip(Test_case_2, expected_out2):
        curr_out = intStringConverter.intConverter(num_input).lower()
        assert curr_out == expected_2.lower(), f"Failed at Test 2 - expected {expected_2} , got {curr_out}"


if __name__ == "__main__":
    run_test_0()
    run_test_1()
    run_test_2()
    print("Finished All Tests")
