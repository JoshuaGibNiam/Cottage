from paper import Paper
from sig_function import intinput
import json
import os
class Tree:
    """tree handles the back-end of this program."""
    papers = []
    algebra_subsets = {
        "Elementary Algebra": [],
        "Linear Algebra": [],
        "Abstract Algebra": [],
        "Boolean Algebra": [],
        "Group Theory": [],
        "Ring Theory": [],
        "Field Theory": []
    }

    geometry_subsets = {
        "Euclidean Geometry": [],
        "Non-Euclidean Geometry": [],
        "Analytic Geometry": [],
        "Differential Geometry": [],
        "Topology": [],
        "Projective Geometry": [],
        "Computational Geometry": []
    }

    calculus_subsets = {
        "Differential Calculus": [],
        "Integral Calculus": [],
        "Multivariable Calculus": [],
        "Vector Calculus": [],
        "Real Analysis": [],
        "Complex Analysis": [],
        "Functional Analysis": []
    }

    statistics_subsets = {
        "Descriptive Statistics": [],
        "Inferential Statistics": [],
        "Bayesian Statistics": [],
        "Probability Theory": [],
        "Regression Analysis": [],
        "Multivariate Statistics": []
    }

    number_theory_subsets = {
        "Elementary Number Theory": [],
        "Analytic Number Theory": [],
        "Algebraic Number Theory": [],
        "Computational Number Theory": [],
        "Diophantine Equations": [],
        "Cryptographic Number Theory": []
    }

    # Science subsets as dictionaries with empty lists
    physics_subsets = {
        "Classical Mechanics": [],
        "Quantum Mechanics": [],
        "Thermodynamics": [],
        "Electromagnetism": [],
        "Relativity": [],
        "Optics": [],
        "Nuclear Physics": [],
        "Astrophysics": []
    }

    chemistry_subsets = {
        "Organic Chemistry": [],
        "Inorganic Chemistry": [],
        "Physical Chemistry": [],
        "Analytical Chemistry": [],
        "Biochemistry": [],
        "Theoretical Chemistry": []
    }

    biology_subsets = {
        "Botany": [],
        "Zoology": [],
        "Genetics": [],
        "Microbiology": [],
        "Ecology": [],
        "Evolutionary Biology": [],
        "Molecular Biology": [],
        "Neuroscience": []
    }
        # Dictionary referencing the lists
    math_twigs = {
            "Algebra": algebra_subsets,
            "Geometry": geometry_subsets,
            "Calculus": calculus_subsets,
            "Statistics": statistics_subsets,
            "Number Theory": number_theory_subsets
        }

    science_twigs = {
            "Physics": physics_subsets,
            "Chemistry": chemistry_subsets,
            "Biology": biology_subsets
        }

    branches = {"math": math_twigs, "science": science_twigs}

    def update(self):
        #add all existing papers into a list
        #TODO: add a kwarg to specify the paper that you want to update
        for x in Tree.branches.values():
            for y in x.values():
                for z in y.values():
                    for a in z:
                        Tree.papers.append(a)


    def __init__(self):
        pass

    def initialize(self):
        print(list(Tree.branches.keys()))
        c1 = intinput("What type of paper are you publishing/adding (1: math, 2: science)?"
                      ":", 2)

        if c1 == "1":
            c1 = "math"
            print("\n")
            for index, key in enumerate(Tree.math_twigs.keys(), start=1):
                print(f"{index}. {key}")
            c2 = intinput("What type of paper are you publishing (enter index)?",
                          len(Tree.math_twigs.keys()))
            for k, x in enumerate(Tree.math_twigs.keys(), start=1):
                if k == int(c2):
                    c2name = x
                    break
            for index, value in enumerate(Tree.math_twigs.values(), start=1):
                if index == int(c2):
                    c2 = value
                    break
            for index, key in enumerate(c2,start=1):
                print(f"{index}. {key}")
            #c stands for choice
            c3 = intinput("What type of paper are you publishing (enter index)?",
                          len(c2.keys()))
            for x, y in enumerate(c2.keys()):
                if x == int(c3):
                    c3name = y
                    break
            for index, key in enumerate(c2.keys(), start=1):
                if index == int(c3):
                    c3 = key
                    break


            title = input("What is the title of the paper you are publishing/adding?: ")
            author = input("What is the author of the paper you are publishing/adding?: ")
            date = input("When was the paper completed? (DD/MM/YYYY): ")

            c2[c3].append(Paper(author, title, date, c1, c2name, c3name))
            print("Paper has been successfully published/initialized.")
            self.update()



        elif c1 == "2":
            c1 = "science"
            print("\n")
            for index, key in enumerate(Tree.science_twigs.keys(), start=1):
                print(f"{index}. {key}")
            c2 = intinput("What type of paper are you publishing (enter index)?",
                          len(Tree.math_twigs.keys()))
            for k, x in enumerate(Tree.science_twigs.keys(), start=1):
                if k == int(c2):
                    c2name = x
                    break
            for index, value in enumerate(Tree.science_twigs.values(), start=1):
                if index == int(c2):
                    c2 = value
                    break
            for index, key in enumerate(c2, start=1):
                print(f"{index}. {key}")
            c3 = intinput("What type of paper are you publishing (enter index)?",
                          len(c2.keys()))
            for x, y in enumerate(c2.keys(), start=1):
                if x == int(c3):
                    c3name = y
                    break
            for index, key in enumerate(c2.keys(), start=1):
                if index == int(c3):
                    c3 = key
                    break

            title = input("What is the title of the paper you are publishing/adding?: ")
            author = input("What is the author of the paper you are publishing/adding?: ")
            date = input("When was the paper completed? (DD/MM/YYYY): ")

            c2[c3].append(Paper(author, title, date, c1, c2name, c3name))
            print("Paper has been successfully published/initialized.")
            self.update()


    def write(self, paper : Paper) -> bool:
        """adds the content to the initialized paper"""
        path = input(r"Enter file path (e.g. 'Papers\relativity.txt): ")
        if not paper.extract(path):
            return False
        else:
            self.update()
            return True
    def search_by_structure(self):
        """Search the paper by the structure, returns paper obj if exists else false"""
        for index, key in enumerate(Tree.branches, start=1):
            print(f"{index}. {key}")
        c1 = intinput("What type of paper are you searching for (enter index)?",
                      2)
        if c1 == "1":
            c1 = "math"
            print("\n")
            for index, key in enumerate(Tree.math_twigs.keys(), start=1):
                print(f"{index}. {key}")
            c2 = intinput("What type of paper are you searching for (enter index)?",
                          len(Tree.math_twigs.keys()))
            for k, x in enumerate(Tree.math_twigs.keys(), start=1):
                if k == int(c2):
                    c2 = Tree.math_twigs[x]
                    break

            for index, key in enumerate(c2, start=1):
                print(f"{index}. {key}")
            c3 = int(intinput("What type of paper are you searching for (enter index)?",
                          len(c2.keys())))
            for index, key in enumerate(c2.keys(), start=1):
                if index == c3:
                    c3 = key

            if len(c2[c3]) == 0:
                print(f"There are no papers in {c3}!")
                return False
            else:
                for x, y in enumerate(c2[c3], start=1):
                    print(f"{x}. {y}")
                c4 = int(intinput("What type of paper are you searching for (enter index)?",
                        len(c2[c3])))
                print(c2[c3][c4-1])
                return c2[c3][c4-1]

        if c1 == "2":
            c2 = "science"
            print("\n")
            for index, key in enumerate(Tree.science_twigs.keys(), start=1):
                print(f"{index}. {key}")
            c2 = intinput("What type of paper are you searching for (enter index)?",
                          len(Tree.science_twigs.keys()))
            for k, x in enumerate(Tree.science_twigs.keys(), start=1):
                if k == int(c2):
                    c2 = Tree.science_twigs[x]
                    break

            for index, key in enumerate(c2, start=1):
                print(f"{index}. {key}")
            c3 = int(intinput("What type of paper are you searching for (enter index)?",
                              len(c2.keys())))
            for index, key in enumerate(c2.keys(), start=1):
                if index == c3:
                    c3 = key

            if len(c2[c3]) == 0:
                print(f"There are no papers in {c3}!")
                return False
            else:
                for x, y in enumerate(c2[c3], start=1):
                    print(f"{x}. {y}")
                c4 = int(intinput("What type of paper are you searching for (enter index)?",
                        len(c2[c3])))
                print(c2[c3][c4-1])
                return c2[c3][c4-1]

    def save(self):
        print("Saving data....")
        for x in Tree.branches:
            for y in Tree.branches[x]:
                for z in Tree.branches[x][y]:
                    for a in Tree.branches[x][y][z]:
                        Tree.branches[x][y][z][Tree.branches[x][y][z].index(a)] = {
                            "author": a.author,
                            "title": a.title,
                            "date": a.date,
                            "branch": a.branch,
                            "twig": a.twig,
                            "subset": a.subset,
                            "path": a.path
                        }

        path = "papers.json"
        if os.path.exists(path):
            with open(path, "w") as file:
                json.dump(Tree.branches, file, indent=4)
                print("Successfully saved data!")
        else:
            raise FileNotFoundError("Initialize file first!")


    def load(self):
        path = "papers.json"
        print("Loading data...")

        if os.path.exists(path):
            with open(path, "r") as file:
                loaded_data = json.load(file)


            t.branches["math"] = t.math_twigs
            t.branches["science"] = t.science_twigs


            for category in ["math", "science"]:
                if category in loaded_data:
                    for twig, subsets in loaded_data[category].items():
                        if twig in t.branches[category]:
                            for subset, papers in subsets.items():
                                if subset in t.branches[category][twig]:
                                    t.branches[category][twig][subset] = [
                                        Paper(
                                                author=item["author"],
                                                title=item["title"],
                                                date=item["date"],
                                                branch=item["branch"],
                                                twig=item["twig"],
                                                subset=item["subset"],
                                                path=item["path"]
                                            ) for item in papers
                                        ]
            t.update()
            print("Successfully loaded file!")

        else:
            print("File not found. Initializing new data...")
            with open(path, "w") as file:
                json.dump(t.branches, file, indent=4)

    def search_by_title(self):
        """Searches a paper by its title, returns False if nothing found."""
        title = input("What is the title of the paper you want to search? ")
        for x in Tree.papers:
            if x.title == title:
                if x.title != "":
                    print(f"{x}")
                else:
                    print("null")
                affirm = input("Is this the paper you want(y/n)? ")
                if affirm == "y":
                    return x
                elif affirm == "n":
                    continue
                else:
                    print('invalid input taken as yes.')
                    return x

        else:
            for i in range(15):
                try:
                    title_list = title.split(" ")
                    for x in Tree.papers:
                        if x.title.split(" ")[i] == title_list[i]:
                            print(f"{x}")
                            affirm = input("Is this the paper you want(y/n)? ")
                            if affirm == "y":
                                return x
                            elif affirm == "n":
                                continue
                            else:
                                print('invalid input taken as yes.')
                                return x
                except IndexError:
                    continue
            else:
                print("No papers found!")
                return False

    def search_by_author(self):
        author = input("What is the author of the paper you want to search? ")
        for x in Tree.papers:
            if x.author.lower() == author.lower():
                print(f"{x}")
                affirm = input("Is this the paper you want(y/n)? ")
                if affirm == "y":
                    return x
                elif affirm == "n":
                    continue
                else:
                    print('invalid input taken as yes.')
                    return x
        for i in range(15):
            for x in Tree.papers:
                try:
                    if x.author.lower().split(" ")[i] == author.lower().split(" ")[i]:
                        print(f"{x}")
                        affirm = input("Is this the paper you want(y/n)? ")
                        if affirm == "y":
                            return x
                        elif affirm == "n":
                            continue
                        else:
                            print('invalid input taken as yes.')
                            return x
                except IndexError:
                    continue

        print("No papers found!")
        return False



if __name__ == "__main__":

    t = Tree()
    t.load()
    t.initialize()
    t.write(t.search_by_author())
    t.save()



