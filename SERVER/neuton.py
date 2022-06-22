import requests
import json


def send_request(url, file_path):
    upload_file = requests.post(
        url + "/v2/predict/file", files={"file": open(file_path, "r")}
    )
    uuid = json.loads(upload_file.text)["data"]
    print("Request has been sent.")

    _is_processed = True
    while _is_processed:
        check_status = requests.get(url + "/v2/predict/status/{}".format(uuid))
        _is_processed = is_processed_file(check_status.text)
    print("Request was processed")

    get_result = requests.get(url + "/v2/predict/result/{}".format(uuid))
    file_name = "result.csv"  # "result_{}.csv".format(uuid)
    with open(file_name, "w") as file:
        data = json.loads(get_result.text)["data"]
        file.writelines(data.split("\n "))
    print("Result saved in file: {}".format(file_name))


def is_processed_file(response) -> bool:
    _status = json.loads(response)["data"]
    return "SUCCESS" != _status and "ERROR" != _status


if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument("--url", dest="url", required=True, help="Ready solution URL")
    parser.add_argument(
        "--file_path",
        dest="file_path",
        required=True,
        help="Path to file for prediction",
    )
    args = parser.parse_args()
    send_request(args.url, args.file_path)
