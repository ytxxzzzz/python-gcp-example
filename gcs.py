from google.cloud import storage as gcs
import os

PROJECT_NAME = os.environ['GCP_PROJECT']
GCS_BUCKET = os.environ['GCS_BACKET']
GCS_PATH = os.environ['GCS_PATH']

#プロジェクト名を指定してclientを作成
client = gcs.Client(PROJECT_NAME)

def write_to_gcs(bucket_name: str, path: str, data: str):
    #バケットオブジェクトを取得
    bucket = client.get_bucket(bucket_name)
    # 書き込み先のファイルオブジェクト(BLOB)を取得
    # BLOBとは　http://e-words.jp/w/BLOB.html
    blob = gcs.Blob(path, bucket)
    # BLOBオブジェクトに文字列形式でアップロード
    blob.upload_from_string(data)


def read_from_gcs(bucket_name: str, path: str) -> str:
    #バケットオブジェクトを取得
    bucket = client.get_bucket(bucket_name)
    #Blobを作成
    blob = gcs.Blob(path, bucket)
    return blob.download_as_string()


if __name__ == '__main__':
    write_to_gcs(GCS_BUCKET, GCS_PATH, "aaabbbccc")
    read_data = read_from_gcs(GCS_BUCKET, GCS_PATH)
    print(f"読み出しデータ＝{read_data}")
