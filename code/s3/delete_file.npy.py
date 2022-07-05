from braingeneers.utils.s3wrangler import delete_objects

path = "s3://braingeneers/ephys/2022-06-30-e-UCSB-200123-2950-control/derived/kilosort/spike_times.csv"
delete_objects(path)


