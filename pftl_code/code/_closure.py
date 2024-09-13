def avg():
    values = []
    def calculate_avg(num):
        values.append(num)
        return sum(values) / len(values)
    return calculate_avg


if __name__ == '__main__':
    a = avg()
    print(a(10))
    print(a(20))
    print(a(20))