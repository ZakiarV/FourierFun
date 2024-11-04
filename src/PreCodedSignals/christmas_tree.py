from src.complex_number import ComplexNumber


def calculate_christmas_tree_signal():
    __dumb_list = []
    for i in range(36):
        __dumb_list.append(ComplexNumber(i * 2, (i * 2) - 292.5))
    for i in range(36):
        __dumb_list.append(ComplexNumber((90 * 2) - (i * 1.5), (90 * 2) - 292.5))
    for i in range(36):
        __dumb_list.append(ComplexNumber((90 * 0.5) + (i * 1.5), (90 * 2) + (i * 1.5) - 292.5))
    for i in range(36):
        __dumb_list.append(ComplexNumber((90 * 2) - (i * 1.5), (90 * 3.5) - 292.5))
    for i in range(36):
        __dumb_list.append(ComplexNumber((90 * 0.5), (90 * 3.5) + (i * 1.5) - 292.5))
    for i in range(36):
        __dumb_list.append(ComplexNumber((90 * 0.5) - i, (90 * 5) - 292.5))
    for i in range(36):
        __dumb_list.append(ComplexNumber((90 * -0.5), (90 * 5) - (i * 1.5) - 292.5))
    for i in range(36):
        __dumb_list.append(ComplexNumber((90 * -0.5) - (i * 1.5), (90 * 3.5) - 292.5))
    for i in range(36):
        __dumb_list.append(ComplexNumber((90 * -2) + (i * 1.5), (90 * 3.5) - (i * 1.5) - 292.5))
    for i in range(36):
        __dumb_list.append(ComplexNumber((90 * -0.5) - (i * 1.5), (90 * 2) - 292.5))
    for i in range(36):
        __dumb_list.append(ComplexNumber((90 * -2) + (i * 2), (90 * 2) - (i * 2) - 292.5))
    return __dumb_list


CHRISTMAS_TREE_SIGNAL = calculate_christmas_tree_signal()
