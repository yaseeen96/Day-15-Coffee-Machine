from data import resources


def get_report():
    print("\n\n---------REPORT START----------\n\n")
    for resource in resources:
        print(f"{resource}: {resources[resource]}")
    print("\n\n---------REPORT END----------\n\n")
