FROM tensorflow/tensorflow:2.11.0-gpu

ARG work_dir="/work"

WORKDIR ${work_dir}

COPY requirements.txt ./

RUN pip install --upgrade pip && pip install -r requirements.txt
