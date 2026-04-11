# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  loading.py                                        :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: klucchin <klucchin@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/04/11 13:41:03 by klucchin        #+#    #+#               #
#  Updated: 2026/04/11 15:07:51 by klucchin        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import importlib
import sys


REQUIRED_PACKAGES = ["pandas", "numpy", "matplotlib"]


def check_dependencies():
    print("LOADING STATUS: Loading programs...")
    print("Checking dependencies:")

    installed = {}
    missing = []

    for pkg in REQUIRED_PACKAGES:
        try:
            module = importlib.import_module(pkg)
            version = getattr(module, "__version__", "unknown")
            print(f"[OK] {pkg} ({version}) - ready")
            installed[pkg] = module
        except ImportError:
            print(f"[MISSING] {pkg} - not installed")
            missing.append(pkg)

    return installed, missing


def show_install_instructions(missing):
    print("\nMissing dependencies detected!\n")

    print("Install with pip:")
    print("pip install " + " ".join(missing))

    print("\nOr using requirements.txt:")
    print("pip install -r requirements.txt")

    print("\nOr with Poetry:")
    print("poetry add " + " ".join(missing))

    print("\nThen run:")
    print("python loading.py")


def generate_data(np):
    print("\nAnalyzing Matrix data...")

    data = np.random.normal(loc=50, scale=15, size=1000)
    return data


def analyze_data(pd, np, data):
    print(f"Processing {len(data)} data points...")
    return pd.DataFrame({"signal_strength": data})


def visualize(matplotlib, df):
    print("Generating visualization...")

    plt = matplotlib.pyplot

    plt.figure()
    df["signal_strength"].hist(bins=50)
    plt.title("Matrix Signal Distribution")
    plt.xlabel("Signal Strength")
    plt.ylabel("Frequency")

    plt.savefig("matrix_analysis.png")


def main():
    installed, missing = check_dependencies()

    if missing:
        show_install_instructions(missing)
        sys.exit(1)

    pd = installed["pandas"]
    np = installed["numpy"]
    matplotlib = installed["matplotlib"]

    import matplotlib.pyplot

    data = generate_data(np)
    df = analyze_data(pd, np, data)

    visualize(matplotlib, df)

    print("\nAnalysis complete!")
    print("Results saved to: matrix_analysis.png")


if __name__ == "__main__":
    main()
