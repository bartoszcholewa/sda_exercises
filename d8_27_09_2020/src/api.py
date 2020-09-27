class API:
    @classmethod
    def get_data(cls):
        return "00"

def get_only_numbers():
    numbers = []
    for line in API.get_data():
        digits = [x.strip() for x in line.split(',') if x.strip().isdigit()]
        numbers.extend(digits)

    return '|'.join(numbers)
