# https://aws-data-wrangler.readthedocs.io/en/2.4.0-docs/api.html#amazon-s3
# To use any of the functions in the doc above
# import braingeneers.utils.s3wrangler as s3wrangler
# s3wrangler.function
# ex) s3wrangler.list_directories

import braingeneers.utils.s3wrangler as wr

# get all UUIDs from s3://braingeneers/ephys/
objects = wr.list_objects('s3://braingeneers/ephys/2022-06-30-e-UCSB-200123-2950-control')
for o in objects:
    print(o)
