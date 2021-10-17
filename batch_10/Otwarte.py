import argparse


class TextAnalyzer:
    def __init__(self, file_name):
        self.file_name = file_name

        self.lines = None
        self.line_count = 0

        self.words = []
        self.word_count = 0

        self.signs = []
        self.sign_count = 0
        self.lower_count = 0
        self.upper_count = 0
        self.non_alpha_count = 0

        self.get_lines()
        self.get_words()
        self.get_signs()
        self.upper_lower()
        self.analyze()

    def get_lines(self):
        with open(self.file_name, "r") as file_handle:
            self.lines = file_handle.readlines()

        for i in range(len(self.lines)):
            self.lines[i] = self.lines[i][:-1]
        self.line_count = len(self.lines)

    def get_words(self):
        for i in self.lines:
            words = i.split()
            self.words += words
        self.word_count = len(self.words)

    def get_signs(self):
        for i in self.words:
            for j in range(len(i)):
                self.signs.append(i[j])
        self.sign_count = len(self.signs)

    def upper_lower(self):
        for i in self.signs:
            if i.isalpha():
                if i == i.upper():
                    self.upper_count += 1
                else:
                    self.lower_count += 1
            else:
                self.non_alpha_count += 1

    def analyze(self):
        analysis = ""
        analysis += "Text analysis:\n"
        analysis += f"         text name: {self.file_name}\n"
        analysis += f"         line count: {str(self.line_count)}\n"
        analysis += f"         word count: {self.word_count}\n"
        analysis += f"         sign count: {self.sign_count}\n"
        analysis += f"         uppercase letter count: {self.upper_count}\n"
        analysis += f"         lowercase letter count: {self.lower_count}\n"
        analysis += f"         non-letter count: {self.non_alpha_count}\n"

        print(analysis)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--file_name", type=str, required=True, help="The name of the .txt file to analyze.")
    name = parser.parse_args().file_name
    analyzer = TextAnalyzer(name)
