import csv

TABLE_PATHS = {
    "store": "database/store.csv",
    "product": "database/product.csv",
    "transaction": "database/transaction.csv",
}

TABLE_INDEX = {
    "1": "store",
    "2": "product",
    "3": "transaction",
}


# Util
def get_path(table):
    return TABLE_PATHS[table]


def load_csv(file_path):
    data = []
    with open(file_path, "r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            data.append(row)
    return data


def save_csv(file_path, data_dict):
    field_names = data_dict[0].keys()

    try:
        with open(file_path, "w", newline="") as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=field_names)
            csv_writer.writeheader()
            csv_writer.writerows(data_dict)
        print("Data saved to CSV successfully.")
    except Exception as e:
        print(f"Error saving data to CSV: {e}")


def convert_to_json(data):
    # json_data = json.loads(data)
    return data


def print_table(data):
    # data = json.loads(json_data)

    if not isinstance(data, list):
        print("Invalid JSON format. Expected a list of dictionaries.")
        return

    if not data:
        print("No data to display.")
        return

    headers = data[0].keys()
    header_format = " | ".join(["{:<15s}" for _ in headers])
    header_line = header_format.format(*headers)
    print("-" * len(header_line))
    print(header_line)
    print("-" * len(header_line))

    for item in data:
        row = [str(item[key])[:15] for key in headers]
        row_format = " | ".join(["{:<15s}" for _ in row])
        row_line = row_format.format(*row)
        print(row_line)

    print("-" * len(header_line))


# CRUD
def get_data(table):
    csv_file_path = get_path(table)

    csv_data = load_csv(csv_file_path)
    json_data = convert_to_json(csv_data)

    return json_data


def insert_data(table, data_dict):
    csv_file_path = get_path(table)

    csv_data = load_csv(csv_file_path)
    json_data = convert_to_json(csv_data)

    json_data.append(data_dict)

    save_csv(csv_file_path, json_data)


def update_data(table, data_dict):
    csv_file_path = get_path(table)

    csv_data = load_csv(csv_file_path)
    json_data = convert_to_json(csv_data)

    data_id = data_dict.get("id")
    data_dict_updated = [row for row in json_data if row.get("id") != data_id]
    data_dict_updated.append(data_dict)
    save_csv(csv_file_path, data_dict_updated)


def delete_data(table, data_dict):
    csv_file_path = get_path(table)

    csv_data = load_csv(csv_file_path)
    json_data = convert_to_json(csv_data)

    data_id = data_dict.get("id")
    data_dict_updated = [row for row in json_data if row.get("id") != data_id]
    save_csv(csv_file_path, data_dict_updated)


def validate_data(table, data_dict):
    csv_file_path = get_path(table)

    csv_data = load_csv(csv_file_path)
    json_data = convert_to_json(csv_data)

    data_id = data_dict.get("id")
    return data_id in [row.get("id") for row in json_data]
