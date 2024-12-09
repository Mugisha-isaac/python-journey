import pandas as pd
import requests
from time import sleep


def process_excel_data(file_path, api_url, batch_size=100, delay=1):
    try:
        df = pd.read_excel(file_path)
        print(f"Successfully loaded {len(df)} records from Excel")

        records = df.to_dict(orient="records")

        results = {
            "total_records": len(records),
            "successful": 0,
            "failed": 0,
            "failed_records": [],
        }

        for i in range(0, len(records), batch_size):
            batch = records[i : i + batch_size]
            try:
                response = requests.post(
                    api_endpoint,
                    json={"data": batch},
                    headers={"Content-Type": "application/json"},
                )

                if response.status_code == 200:
                    results["successful"] += len(batch)
                    print(f"Successfully processed batch {i//batch_size + 1}")

                else:
                    results["failed"] += len(batch)
                    results["failed_records"].extend(batch)
                    print(f"Failed to process batch {i//batch_size + 1}")

                sleep(delay)

            except Exception as e:
                print(f"Error processing batch {i//batch_size + 1}: {e}")
                results["failed"] += len(batch)
                results["failed_records"].extend(batch)

        return results

    except Exception as e:
        print(f"Error processing Excel data: {e}")
        return None


if __name__ == "__main__":
    file_path = "data.xlsx"
    api_endpoint = "https://jsonplaceholder.typicode.com/posts"
    results = process_excel_data(file_path, api_endpoint)

    if results:
        print(f"Total records: {results['total_records']}")
        print(f"Successful: {results['successful']}")
        print(f"Failed: {results['failed']}")
        print(f"Failed records: {results['failed_records']}")
    else:
        print("Failed to process Excel data")
