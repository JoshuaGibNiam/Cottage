from paper import Paper

class Interface:

        # Mathematics subsets
    algebra_subsets = [
            "Elementary Algebra",
            "Linear Algebra",
            "Abstract Algebra",
            "Boolean Algebra",
            "Group Theory",
            "Ring Theory",
            "Field Theory"
        ]

    geometry_subsets = [
            "Euclidean Geometry",
            "Non-Euclidean Geometry",
            "Analytic Geometry",
            "Differential Geometry",
            "Topology",
            "Projective Geometry",
            "Computational Geometry"
        ]

    calculus_subsets = [
            "Differential Calculus",
            "Integral Calculus",
            "Multivariable Calculus",
            "Vector Calculus",
            "Real Analysis",
            "Complex Analysis",
            "Functional Analysis"
        ]

    statistics_subsets = [
            "Descriptive Statistics",
            "Inferential Statistics",
            "Bayesian Statistics",
            "Probability Theory",
            "Regression Analysis",
            "Multivariate Statistics"
        ]

    number_theory_subsets = [
            "Elementary Number Theory",
            "Analytic Number Theory",
            "Algebraic Number Theory",
            "Computational Number Theory",
            "Diophantine Equations",
            "Cryptographic Number Theory"
        ]

        # Science subsets
    physics_subsets = [
            "Classical Mechanics",
            "Quantum Mechanics",
            "Thermodynamics",
            "Electromagnetism",
            "Relativity",
            "Optics",
            "Nuclear Physics",
            "Astrophysics"
        ]

    chemistry_subsets = [
            "Organic Chemistry",
            "Inorganic Chemistry",
            "Physical Chemistry",
            "Analytical Chemistry",
            "Biochemistry",
            "Theoretical Chemistry"
        ]

    biology_subsets = [
            "Botany",
            "Zoology",
            "Genetics",
            "Microbiology",
            "Ecology",
            "Evolutionary Biology",
            "Molecular Biology",
            "Neuroscience"
        ]

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



