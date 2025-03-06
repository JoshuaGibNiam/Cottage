from paper import Paper
from sig_function import intinput
class Tree:
    """tree handles the back-end of this program."""
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

    def intiialize(self):
        '''Creates a paper'''
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

    def write(self, paper : Paper):
        path = input(r"Enter file path (e.g. 'Papers\relativity.txt): ")
        if not paper.extract(path):
            return False
        else:
            return True

if __name__ == "__main__":
    paper1 = Paper("Joshua", "JoshuaNIam", "11/2/2025", "math", "Algebra"
                   , "Elementary algebra")
    t = Tree()
    t.write(paper1)

