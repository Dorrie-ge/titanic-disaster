
FROM rocker/tidyverse:4.3.1
WORKDIR /app
COPY . /app
RUN Rscript -e "install.packages('caret', repos='https://cloud.r-project.org')"
CMD ["Rscript", "main.R"]
