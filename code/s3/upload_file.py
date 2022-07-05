from braingeneers.utils.s3wrangler import upload

LOCAL_FILE_PATH = "spike_times.npy"

S3_ROOT = "s3://braingeneers/ephys"
BATCH_UUID = "2022-06-30-e-UCSB-200123-2950-control"
BATCH_SUBPATH = "derived/kilosort/spike_times.npy"
s3_path = f"{S3_ROOT}/{BATCH_UUID}/{BATCH_SUBPATH}"

upload(LOCAL_FILE_PATH, s3_path)

