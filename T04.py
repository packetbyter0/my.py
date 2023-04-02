# Auther: Quintin Schroeer
# Date: 02.04.2023

# Aufgabe T04
share_database = []


def create_share(symbol: str, name: str) -> None:
    global share_database
    share_database.append({"symbol": symbol, "name": name, "date": "", "time": "", "share_price": "", "traded_volume": ""})


def list_all_share_information() -> str:
    global share_database
    print_line = "-"*58
    if not share_database:
        return ""
    else:
        first_element = share_database[0]
        output = f"{first_element['symbol']:7} - {first_element['name']}\n" f"{print_line}\n" f"| {'Date':10} | {'Time':5} | {'Price $':15} | {'Traded Volume':15} |\n" + print_line
        for element in share_database:
            output += f"\n| {element['date']:10} | {element['time']:5} | {element['share_price']:15} | {element['traded_volume']:15} |"
        return output



def add_share_data(symbol: str, date: str, time: str, share_price: float, traded_volume: int = 0) -> None:
    global share_database
    for i, element in enumerate(share_database):
        if element["date"] == date and element["time"] == time:
            share_database[i] = {"symbol": symbol, "name": element['name'],  "date": date, "time": time, "share_price": share_price, "traded_volume": traded_volume}
            break
    else:
        share_database.append({"symbol": symbol, "name": "", "date": date, "time": time, "share_price": share_price, "traded_volume": traded_volume})



def add_trade(symbol : str, date : str, time : str, share_price : float, traded_volume : int) -> None:
    global share_database
    for i, element in enumerate(share_database):
        if element["date"] == date and element["time"] == time:
            share_database[i] = {"symbol": symbol, "name": element['name'],  "date": date, "time": time, "share_price": share_price, "traded_volume": traded_volume}
            break
    else:
        share_database.append({"symbol": symbol, "name": "", "date": date, "time": time, "share_price": share_price, "traded_volume": traded_volume})



create_share("AAPL", "Apple Inc.")
add_share_data("AAPL", "2021-10-15", "08:30", 142.12)
add_share_data("AAPL", "2021-10-15", "08:45", 142.33)
add_share_data("AAPL", "2021-10-15", "09:15", 141.95)
add_trade     ("AAPL", "2021-10-15", "09:17", 141.93, 500)
add_share_data("AAPL", "2021-10-15", "09:33", 143.12)
add_trade     ("AAPL", "2021-10-15", "09:58", 143.01, -100)
print(list_all_share_information())
