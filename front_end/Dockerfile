# Use the Nginx image from Docker Hub as the base image
FROM nginx:alpine

# Install openssl
RUN apk add --no-cache openssl

# Create a directory for the keys
RUN mkdir -p /etc/nginx/ssl

# Generate a self-signed SSL certificate and key
RUN openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/nginx/ssl/nginx.key -out /etc/nginx/ssl/nginx.crt -subj "/C=US/ST=Denial/L=Springfield/O=Dis/CN=www.example.com"

# Remove the default Nginx configuration file
RUN rm /etc/nginx/conf.d/default.conf

# Copy the HTML file to the Nginx document root
COPY *.html /usr/share/nginx/html

# Copy the CSS file to the Nginx document root
COPY styles.css /usr/share/nginx/html

# Copy a configuration file from the current directory
COPY nginx.conf /etc/nginx/conf.d

# Expose ports 80 and 443
EXPOSE 80 443

# Start Nginx when the container has provisioned
CMD ["nginx", "-g", "daemon off;"]