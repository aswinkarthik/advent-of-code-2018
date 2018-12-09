import fileinput

TWO = 2
THREE = 3


class Line:
    line = ""
    dict = {}

    def __init__(self, line):
        self.line = line
        map_dict = {}
        for c in line:
            if c in map_dict:
                map_dict[c] += 1
            else:
                map_dict[c] = 1
        self.dict = map_dict

    def __getitem__(self, index):
        return self.line[index]

    def __setitem__(self, index, value):
        self.line[index] = value

    def __len__(self):
        return len(self.line)

    def __str__(self):
        return self.line

    def find_twos_and_threes(self):
        twos = 0
        threes = 0
        for _, v in self.dict.items():
            if v == TWO:
                twos = 1
            if v == THREE:
                threes = 1

        return twos, threes

    def equals(self, another):
        return self.line == another.line

    def distance(self, another_line):
        size_of_line = len(self)
        size_of_another_line = len(another_line)

        min_of_two_lines = min(size_of_line, size_of_another_line)
        max_of_two_lines = max(size_of_line, size_of_another_line)

        distance = max_of_two_lines - min_of_two_lines

        for i in range(min_of_two_lines):
            if self[i] != another_line[i]:
                distance += 1

        return distance

    def intersect(self, another_line):
        result = ""
        length_of_another_line = len(another_line)

        for i in range(len(self)):
            if i < length_of_another_line and self[i] == another_line[i]:
                result += self[i]

        return result


def main():
    twos = 0
    threes = 0
    lines = []
    for line_from_stdin in fileinput.input():
        line = Line(line_from_stdin.strip())
        twos_in_line, threes_in_line = line.find_twos_and_threes()
        twos += twos_in_line
        threes += threes_in_line
        lines.append(line)

    print('Problem 1')
    print(twos * threes)

    print('Problem 2')
    for i in range(len(lines)):
        line = lines[i]
        j = i + 1
        while j < len(lines):
            next_line = lines[j]
            if not line.equals(next_line):
                if line.distance(next_line) == 1:
                    print(line.intersect(next_line))
            j += 1


if __name__ == '__main__':
    main()
