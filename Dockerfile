# Use the official PHP image as the base image
FROM php:8.0-apache

# Set the working directory in the container
WORKDIR /var/www/html

# Install PHP extensions and dependencies
RUN apt-get update && \
    apt-get install -y \
        libzip-dev \
        zip && \
    docker-php-ext-install zip && \
    docker-php-ext-install pdo_mysql mysqli pdo

 # Copy the source code to the container
COPY ./rams-v2/www /var/www/html

COPY custom-apache.conf /etc/apache2/conf-available/custom-apache.conf

RUN a2enconf custom-apache

# Expose port 80
EXPOSE 80 

# Start the Apache server
CMD ["apache2-foreground"]