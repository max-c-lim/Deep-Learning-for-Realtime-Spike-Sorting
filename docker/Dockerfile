FROM surygeng/kilosort_docker:latest

RUN apt-get update && apt-get install -y --no-install-recommends \
        wget \
        python-is-python3

RUN python -m pip install git+https://github.com/braingeneers/braingeneerspy.git#egg=braingeneerspy[iot,ml,data,analysis]

COPY code /project/code
