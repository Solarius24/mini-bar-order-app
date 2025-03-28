from pathlib import Path
import csv


def create_csv(path, drinks, total_cost, tip, grand_total):
    with path.open("w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(["Drink name", "Cost"])
        writer.writerows(drinks)
        writer.writerow(['Total', total_cost])
        writer.writerow(['Tip', tip])
        writer.writerow(['Grand Total', grand_total])

        print(f"The bar tab has been saved to {path}")


def calcualte_totals(drinks):
    total_cost = 0
    for name, cost in drinks:
        total_cost += cost
    tip = total_cost * 0.20
    grand_total = total_cost + tip

    return total_cost, tip, grand_total


def serve_user():
    drinks = []
    while True:
        name = input("Drink name(or type 'f' to finish): ")
        if name.lower() == "f":
            break
        try:
            cost = float(input(f"{name} price: "))
        except ValueError:
            print("The prcice must be a nimber :")
            continue

        drinks.append((name, cost))
    return drinks


def main():
    # get table number from user
    try:
        table_no = int(input("Table number: "))
        print(f"Starting a tab for table {table_no}")
    except:
        print("Not a valid table number. Exiting program.")
        return

    # create file path using table number
    path = Path(__file__).parent / f"table_{table_no}.csv"
    print(path)

    # get items from user (drink name and price)

    drinks = serve_user()
    print(drinks)

    if not drinks:
        print("No drink added existing the programm")
        return

    # calculate the totals (total, tip, grand_total)
    total_cost, tip, grand_total = calcualte_totals(drinks)
    print(total_cost, tip, grand_total)
    # create the csv
    create_csv(path, drinks, total_cost, tip, grand_total)


if __name__ == "__main__":
    main()
