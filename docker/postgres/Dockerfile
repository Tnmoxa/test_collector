FROM postgres:17

ARG POSTGRESQL_DB
ENV POSTGRES_DB ${POSTGRESQL_DB:-stat_collection}

ARG POSTGRESQL_USER
ENV POSTGRES_USER ${POSTGRESQL_USER:-postgres}
RUN echo  ${POSTGRES_USER}

ARG POSTGRESQL_PASSWORD
ENV POSTGRES_PASSWORD ${POSTGRESQL_PASSWORD}
RUN echo ${POSTGRES_PASSWORD}