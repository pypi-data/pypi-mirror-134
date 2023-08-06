FROM pytorch/pytorch
RUN apt update -y && \
    apt install -y libglib2.0-0 libsm6 libxrender1 libxext6 libgl1-mesa-glx build-essential wget git
RUN mkdir -p /sap_cv/data
RUN mkdir -p /sap_cv/module
RUN mkdir -p /tmp/model
WORKDIR /sap_cv
ENV HOME=/sap_cv
RUN python -m pip install --upgrade pip
COPY requirements.txt /sap_cv/requirements.txt
RUN pip install detectron2 -f https://dl.fbaipublicfiles.com/detectron2/wheels/cu113/torch1.10/index.html
RUN pip install metaflow-argo awscli \
    --index-url=http://nexus.wdf.sap.corp:8081/nexus/content/groups/build.milestones.pypi/simple/ \
    --trusted-host nexus.wdf.sap.corp
COPY sap_computer_vision /sap_cv/module/sap_computer_vision
ENV PYTHONPATH="/sap_cv/module:${PYTHONPATH}"
RUN python -m pip install -r /sap_cv/requirements.txt
RUN chgrp -R nogroup /sap_cv && \
    chmod -R 777 /sap_cv
RUN chgrp -R nogroup /tmp && \
    chmod -R 777 /tmp
