FROM abpzzareg.azurecr.io/viya-4-x64_oci_linux_2-docker/sas-decisions-runtime-base:1.54.15-20230614.1686753305803
LABEL model container image
USER root
RUN chown sas:sas /modules
USER sas
ENV SAS_SCR_APP_PATH=/loanapplicationproject
COPY --chown=sas:sas unzipped/ /modules/
COPY --chown=sas:sas manifest/ /manifest/
USER root
COPY Dockerfile-requirements.txt /tmp/Dockerfile-requirements.txt
RUN pip3 install -r /tmp/Dockerfile-requirements.txt
USER sas
ENV LD_LIBRARY_PATH=/opt/scr/viya/home/SASFoundation/utilities/bin:/opt/scr/viya/home/SASFoundation/sasexe
