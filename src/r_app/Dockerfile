FROM rocker/tidyverse:latest

WORKDIR /app
COPY . /app
RUN Rscript -e "install.packages('caret', repos='https://cloud.r-project.org')"
CMD ["Rscript", "main.R"]
