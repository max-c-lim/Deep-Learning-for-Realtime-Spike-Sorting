import braingeneers.utils.s3wrangler as wr

# get all UUIDs from s3://braingeneers/ephys/
objects = wr.list_objects('s3://braingeneers/ephys/2022-06-30-e-UCSB-200123-2950-control')
for o in objects:
    print(o)
