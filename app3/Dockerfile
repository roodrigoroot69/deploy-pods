# Use the official PostgreSQL image from the Docker Hub
FROM postgres:13

# Set environment variables for PostgreSQL
ENV POSTGRES_DB=mydatabase
ENV POSTGRES_USER=myuser
ENV POSTGRES_PASSWORD=mypassword

# Expose the default PostgreSQL port
EXPOSE 5432

# Optional: Add SQL script to initialize the database
COPY init.sql /docker-entrypoint-initdb.d/

# Optional: Add custom configuration files
# COPY custom-postgresql.conf /etc/postgresql/postgresql.conf
# RUN echo "include '/etc/postgresql/postgresql.conf'" >> /usr/share/postgresql/postgresql.conf.sample
