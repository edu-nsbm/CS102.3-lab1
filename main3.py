def get_inputs() -> tuple[float, float]:
    var1: float = float(input("Enter number 1: "))
    var2: float = float(input("Enter number 2: "))

    return (var1, var2)


def print_calculations(inputs: tuple[float, float]) -> None:
    print(f"{inputs[0]} + {inputs[1]} is: {inputs[0] + inputs[1]}")
    print(f"{inputs[0]} - {inputs[1]} is: {inputs[0] - inputs[1]}")
    print(f"{inputs[0]} * {inputs[1]} is: {inputs[0] * inputs[1]}")
    print(f"{inputs[0]} / {inputs[1]} is: {inputs[0] / inputs[1]}")


def main() -> None:
    inputs: tuple[float, float] = get_inputs()
    print_calculations(inputs)


if __name__ == "__main__":
    main()
