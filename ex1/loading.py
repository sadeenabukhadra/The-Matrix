import importlib
from typing import Any


def check_dependencies() -> dict[str, Any]:
    modules: dict[str, Any] = {}
    libs = ["pandas", "numpy", "matplotlib"]
    print("Checking dependencies:")
    for lib in libs:
        try:
            module = importlib.import_module(lib)
            modules[lib] = module
            print(f"[OK] {lib} ({module.__version__})")
        except ImportError:
            print(f"[MISSING] {lib}")
            print("\nPlease install the required dependencies:")
            print("Using pip:")
            print("    pip install -r requirements.txt")
            print("\nOr using Poetry:")
            print("    poetry install")
    return modules


def compare_package_managers() -> None:
    print("PIP VS POETRY COMPARISON :")
    print(" - pip : tool ->  ")
    print("default simple package installer")
    print("Installs libraries from PyPI")
    print("Manage simple dependencies via requirements.txt")
    print("No built-in dependency resolution lock file \
    (reproducibility is manual")
    print("Doesn’t manage virtual environments by itself")
    print("No strong project structure management")
    print("________________________________________________")
    print(" - poetry : system ->")
    print("A tool that manages dependencies + \
    virtual environments + packaging")
    print("Handles dependencies automatically")
    print("Creates and manages virtual environments")
    print("Uses a lock file for reproducibility (poetry.lock)")
    print("Manages project metadata (pyproject.toml)")
    print("Builds and publishes packages")


def analyze_data(modules: dict[str, Any]) -> None:
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt

    data = np.random.rand(1000)
    df = pd.DataFrame(data, columns=["values"])
    print("\n Statistical Summary :")
    print(df.describe())
    plt.plot(df["values"])
    plt.title("Matrix Analysis")
    plt.savefig("matrix_analysis.png")
    plt.close()
    print("Graph saved as matrix_analysis.png")


def main():
    print("LOADING STATUS: Loading programs...")

    modules = check_dependencies()

    analyze_data(modules)

    compare_package_managers()


if __name__ == "__main__":
    main()
